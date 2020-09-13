void blocking_handler(void)
{
	while (1);
}

void null_handler(void)
{
	/* Do nothing. */
}

#pragma weak __mst__nmi_handler = null_handler
#pragma weak __mst__hard_fault_handler = blocking_handler
#pragma weak __mst__sv_call_handler = null_handler
#pragma weak __mst__pend_sv_handler = null_handler
#pragma weak __mst__sys_tick_handler = null_handler
#pragma weak __mst__mem_manage_handler = blocking_handler
#pragma weak __mst__bus_fault_handler = blocking_handler
#pragma weak __mst__usage_fault_handler = blocking_handler
#pragma weak __mst__debug_monitor_handler = null_handler


