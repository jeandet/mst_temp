#include <stdint.h>

typedef void (*vector_table_entry_t)(void);

typedef struct {
	uint32_t *initial_sp_value; /**< Initial stack pointer value. */
	vector_table_entry_t reset;
	vector_table_entry_t nmi;
	vector_table_entry_t hard_fault;
	vector_table_entry_t memory_manage_fault; /* not in CM0 */
	vector_table_entry_t bus_fault;           /* not in CM0 */
	vector_table_entry_t usage_fault;         /* not in CM0 */
	vector_table_entry_t reserved_x001c[4];
	vector_table_entry_t sv_call;
	vector_table_entry_t debug_monitor;       /* not in CM0 */
	vector_table_entry_t reserved_x0034;
	vector_table_entry_t pend_sv;
	vector_table_entry_t systick;
} common_vector_table_t;

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

__attribute__ ((section(".common_interrupt_vector_table"))) common_vector_table_t common_interrupt_vector_table = {
	.initial_sp_value = &_stack,
	.reset = __mst__reset_handler,
	.nmi = __mst__nmi_handler,
	.hard_fault = __mst__hard_fault_handler,

	.memory_manage_fault = __mst__mem_manage_handler,
	.bus_fault = __mst__bus_fault_handler,
	.usage_fault = __mst__usage_fault_handler,
	.debug_monitor = __mst__debug_monitor_handler,

	.sv_call = __mst__sv_call_handler,
	.pend_sv = __mst__pend_sv_handler,
	.systick = __mst__sys_tick_handler
};

