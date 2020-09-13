typedef void (*vector_table_entry_t)(void);

__attribute__ ((section(".specific_interrupt_vector_table"))) vector_table_entry_t specific_interrupt_vector_table[255-12] =
{

};
