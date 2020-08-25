#pragma once

#include "../spi.hpp"
#include "../utils.hpp"
#include "./spi-regs.hpp"

namespace mst::stm32::spi
{
using namespace mst::spi;

template <typename regs, typename word_size = w8bits>
struct data_reg_t : mst::registers::reg_t<uint8_t, regs::address>
{
    using mst::registers::reg_t<uint8_t, regs::address>::operator=;
    using mst::registers::reg_t<uint8_t, regs::address>::operator|=;
    using mst::registers::reg_t<uint8_t, regs::address>::operator&=;
};

template <typename regs>
struct data_reg_t<regs, w16bits> : mst::registers::reg_t<uint16_t, regs::address>
{
    using mst::registers::reg_t<uint16_t, regs::address>::operator=;
    using mst::registers::reg_t<uint16_t, regs::address>::operator|=;
    using mst::registers::reg_t<uint16_t, regs::address>::operator&=;
};

template <typename regs>
struct data_reg_t<regs, w32bits> : mst::registers::reg_t<uint32_t, regs::address>
{
    using mst::registers::reg_t<uint32_t, regs::address>::operator=;
    using mst::registers::reg_t<uint32_t, regs::address>::operator|=;
    using mst::registers::reg_t<uint32_t, regs::address>::operator&=;
};

template <typename regs, typename word_size = w8bits, typename bit_order = msb_first>
struct SPI
{
    static constexpr data_reg_t<decltype (regs::DR), word_size> data_reg={};

    // TODO make this configurable!
    static constexpr void init()
    {
        static_assert(is_16bits_or_less_v<word_size>, "unsuported word size");
        regs::CR1.SPE = 1;
        regs::CR1 = regs::CR1.BR.shift(3) | regs::CR1.SSM.shift(1) | regs::CR1.SSI.shift(1)
            | regs::CR1.MSTR.shift(1) | regs::CR1.LSBFIRST.shift(is_lsb_first_v<bit_order>);
        if constexpr (is_8bits_v<word_size>)
        {
            regs::CR2 = regs::CR2.DS.shift(7) | regs::CR2.FRXTH.shift(1);
        }
        else if constexpr (is_16bits_v<word_size>)
            regs::CR2 = regs::CR2.DS.shift(0xf);
        regs::CR2.SSOE = 1;
        for (volatile int i = 0; i < 16; i++)
            ;
        regs::CR1.SPE = 1;
    }

    template <typename T>
    static constexpr T p_write(T data)
    {
        constexpr int N = (sizeof(T) * 8) / word_size::size;
        T result = 0;
        for (int i = 0; i < N; i++)
        {
            if constexpr (is_msb_first_v<bit_order>)
                data_reg = data >> (word_size::size * (N - 1 - i));
            else
                data_reg = data >> (word_size::size * N);
            while (regs::SR.RXNE == 0)
                ;
            if constexpr (is_msb_first_v<bit_order>)
                result |= data_reg << (word_size::size * (N - 1 - i));
            else
                result |= data_reg << (word_size::size * N);
        }
        return result;
    }

    template <typename T>
    static constexpr T write(T data)
    {
        static_assert(mst::utils::is_one_of<T, char, uint8_t, uint16_t, uint32_t>::value,
            "write function only accept uint8_t, uint16_t or uint32_t");
        return p_write(data);
    }

    template <typename T>
    static constexpr T read(T data)
    {
        static_assert(mst::utils::is_one_of<T, char, uint8_t, uint16_t, uint32_t>::value,
            "read function only accept uint8_t, uint16_t or uint32_t");
        return write(data);
    }
};
} // namespace mst::stm32::spi
