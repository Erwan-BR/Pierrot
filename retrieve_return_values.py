from retrieve_return_name import retrieve_return_name
from retrieve_default_value import retrieve_default_value
from global_declarations import *
from global_debugging import list_all_function_for_test
from functools import cache


@cache
def retrieve_return_values(path_file: str, list_All_Functions: list = []) -> list[str]:
    """
    Retrieve the different values that a function can return.
    If the return parameter take the return value of another function, the name of this function will appear in this list.
    :param path_file: File that contains the function. Must be a raw string.
    :out: List of all the possible returns values. If a function is called, it will add the function name in the list.
    """

    return_Values = []

    # Local variable
    return_Value = ""

    # Boolean to determine if the current value is a structure or not.
    is_A_Structure: bool = False

    if path_file is None :
        return return_Values
    
    # Replace the backslash to avoid an error
    path_file = path_file.replace("\\", "/")
    return_Name = retrieve_return_name(path_file)

    # if return_Name is None, the function doesn't return anything.
    if return_Name is None :
        return return_Values
    
    default_Return_Value = retrieve_default_value(path_file)

    if default_Return_Value is not None :
        return_Values.append(default_Return_Value)
    
    # return_Name is not None and the path_file is valid.
    with open(path_file, 'r') as file:
        for line in file:
            current_Line = line.strip()

            if current_Line.startswith(return_Name):
                
                # If the current line contains a (, it means that the return value will get assigned a function called.
                if current_Line.find("(") !=-1:
                    
                    # We will keep only what's after the equal sign.
                    beggining_strip = current_Line.find("=")
                    end_strip = current_Line.find("(")

                    # There is two structure that must be replaced by functions. They are in global_decalarations.

                    if current_Line[beggining_strip+1:end_strip].strip() == "ASP_ServiceConfig[u8_ServiceIdIxSupported].FP_MainProcessPtr": 
                        is_A_Structure = True
                        
                        for function_To_Replace in list_changing_values_ServiceSupported:
                            if function_To_Replace not in return_Values:
                                return_Values.append(function_To_Replace)
                    
                    elif current_Line[beggining_strip+1:end_strip].strip() == "ASP_ServiceConfig[DSDP_u8_ServiceIndex].FP_MainProcessPtr":
                        is_A_Structure = True

                        for function_To_Replace in list_changing_values_ServiceIndex:
                                if function_To_Replace not in return_Values:
                                    return_Values.append(function_To_Replace)
                    
                    else:
                        is_A_Structure = False

                        return_Value = current_Line[beggining_strip+1:end_strip].strip() + ".c"
                
                # If the current line doesn't contain a (, then this is just a value.
                else :
                    is_A_Structure = False

                    beggining_strip = current_Line.find("=")
                    end_strip = current_Line.find(";")
                    return_Value = current_Line[beggining_strip+1:end_strip].strip()

                if return_Value not in return_Values and not is_A_Structure:
                    return_Values.append(return_Value)
    
    for value in return_Values:
        if value == ".c":
            return_Values[return_Values.index(value)] = "Attention"

    return return_Values

if __name__ == "__main__":
    pass