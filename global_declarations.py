from dataclasses import dataclass, field

@dataclass
class function_analyse:
    function_name: str
    returned_values: list[str]
    has_been_searched: bool = False # Not used. Could be usefull to avoid searching many times for the same function, by using recursivity.
    list_files_problems: list[str] = field(default_factory=list)

# To replace the pointer ASP_ServiceConfig[DSDP_u8_ServiceIndex].FP_MainProcessPtr

list_changing_values_ServiceIndex: list[str] = []


# To replace the pointer ASP_ServiceConfig[u8_ServiceIdIxSupported].FP_MainProcessPtr

list_changing_values_ServiceSupported: list[str] = []