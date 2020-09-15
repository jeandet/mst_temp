#include <stdint.h>

typedef void (*vector_table_entry_t)(void);

extern uint32_t _stack;
extern void __mst__reset_handler();
extern void __mst__nmi_handler();
extern void __mst__hard_fault_handler();
extern void __mst__mem_manage_handler();
extern void __mst__bus_fault_handler();
extern void __mst__usage_fault_handler();
extern void __mst__debug_monitor_handler();
extern void __mst__sv_call_handler();
extern void __mst__pend_sv_handler();
extern void __mst__sys_tick_handler();

__attribute__ ((section(".common_interrupt_vector_table"))) uint32_t *initial_sp_value=&_stack; /**< Initial stack pointer value. */

__attribute__ ((section(".common_interrupt_vector_table"))) vector_table_entry_t common_interrupt_vector_table[15] = {
	[0] __mst__reset_handler,
  [1]__mst__nmi_handler,
  [2] __mst__hard_fault_handler,

	[3] __mst__mem_manage_handler,
	[4]  __mst__bus_fault_handler,
	[5] __mst__usage_fault_handler,

  [10] __mst__sv_call_handler,
	[11] __mst__debug_monitor_handler,


	[13] __mst__pend_sv_handler,
	[14] __mst__sys_tick_handler
};


