import os

from build_dict_functions import build_dict_functions
from retrieve_deep_values import retrieve_deep_values
from verify_if_void import verify_if_void

def fill_dictionnary_of_return_values(project_folder: str, scope_folder: str, progress_callback = None) -> dict:
    """
    Will run the execution for everything.
    :param project_folder: Folder of the project. It's the folder that contains the function that needs to be digged.
    :param scope_folder: Scope of the project, to find the reference of other functions.
    :param progress_callback: Function to emit a signal for the progress bar.
    :out: Dictionnary that contains all paths for keys, and values are the list of function on those paths. Each item of the list is an object of
            class function_analyse (see global_declarations)
    """

    project_folder = project_folder.replace("\\", "/")
    scope_folder = scope_folder.replace("\\", "/")

    (dict_All_Functions, list_All_Functions) = build_dict_functions(scope_folder)

    number_of_functions = len(dict_All_Functions)
    number_of_functions_already_analysed = 0

    # We iterate on the dictionnary.
    for path, functions_Info in dict_All_Functions.items():
        path = path.replace("\\", "/")
        for function in functions_Info:
            
            # We retrieve the return value only if the function is on the project folder.

            if path.startswith(project_folder):
                function_Path = os.path.join(path, function.function_name)
                
                # If the function returns void, we don't parse it.
                if verify_if_void(function_Path):
                    function.returned_values = ["void"]
                else:
                    function.returned_values = retrieve_deep_values(function_Path, scope_folder, list_All_Functions)
            
            # Else, the function is not analysed.
            else:
                # The "Not analysed." str is just for debugging.
                function.returned_values = ["Not analysed."]
        
        number_of_functions_already_analysed += 1

        # For debugging, we do not give the progress_callback argument.
        if progress_callback is not None:
            progress_callback(int((number_of_functions_already_analysed + 1) * 100 / number_of_functions))
    return dict_All_Functions

if __name__ == "__main__":
    pass