from retrieve_return_values import retrieve_return_values
from find_file import find_file
import time
from global_debugging import list_all_function_for_test

def retrieve_deep_values(path_file:str, project_folder:str, list_All_Functions: list = None) -> list[str]:
    """
    Retrieve all return values that a function can returns, by scrapping the called functions.
    :param path_file: Path of the function that we want to find the values that may be returned. Must be a raw string.
    :param project_folder: Define the scope of all the function that may be called by the function. Must be a raw string.
    :param list_All_Functions: List of all the functions that exists. Not used for the moment.
    :out: a list of all returns values that can be returned by the function.
    """

    start_time = time.time()
    return_Values = []

    # called_Functions contains all function that may have been called to avoid looping indefinitely.
    called_Functions = []

    if path_file is None or project_folder is None :
        return None

    # Replace the backslash to avoid an error
    path_file = path_file.replace("\\", "/")
    project_folder = project_folder.replace("\\", "/")

    # return_Values = retrieve_return_values(path_file, list_All_Functions)

    return_Values = retrieve_return_values(path_file)
    
    #print(return_Values)

    if return_Values != []:

        # While there is some c file in the return_values list, we have to dig more.
        while any(value.lower().endswith(".c") for value in return_Values):
            #print(return_Values)
            current_time = time.time()
            if (current_time - start_time > 2):
                return return_Values
            
            for current_Value in return_Values:
                if current_Value.lower().endswith(".c"):

                    # If the .c file doesn't exist, we have to keep the name from where it can comes.

                    # If the current value is a c file, we have to stock it in current_Value, find the location of the file and
                    # then add the returns values to our output parameters.
                    called_Functions.append(current_Value)

                    # If the function is not a real function (problem of cast of macro / other), Add Attention for color syntax in Excel.
                    if current_Value not in list_All_Functions :
                        if "Attention" not in return_Values:
                            return_Values.append("Attention")

                        # We delete the .c to avoid looping for nothing.
                        return_Values[return_Values.index(current_Value)] = current_Value[0:-2]
                    
                    path_Called_Function = find_file(project_folder, current_Value)

                    # inner_Return_Values = retrieve_return_values(path_Called_Function, list_All_Functions)
                    inner_Return_Values = retrieve_return_values(path_Called_Function)
                    
                    if inner_Return_Values != [] :
                    # We add only the interesting values in return_Values : those that not in and who are not functions that have been checked.
                        for current_Inner_Value in inner_Return_Values:
                            
                            # We had the value only if it was not in the list / a file already parsed.
                            if ((current_Inner_Value not in called_Functions) and (current_Inner_Value not in return_Values)):
                                    return_Values.append(current_Inner_Value)
                
                    # Delete the name of the function from the return_Values if it was a real function.
                    if current_Value in list_All_Functions:
                        return_Values.pop(return_Values.index(current_Value))
    return sorted(return_Values)

if __name__ == "__main__":
    pass