import os
from global_declarations import function_analyse

def build_dict_functions(file_path: str) -> tuple:
    """
    Functions that create a dictionnary which contains all the functions that need to be parsed.
    :param file_path: Path of the file_path where the functions needs to be parsed. r string needed.
    :out: A tuple containing two things. A dictionnary which is structured like this :
        {path1: [(func1, return_Values), (func2, return_Values)], ...}. return_values is a list.
        A list of all functions that exists. in the file_path.
    """

    return_Dictionnary = {}
    return_List_Functions = []

    if file_path is None :
        return (return_Dictionnary, return_List_Functions)
    
    # Replace the backslash to avoid an error
    file_path = file_path.replace("\\", "/")
    
    for current_Folder, inner_Folder, inner_Files in os.walk(file_path):

        current_Folder = current_Folder.replace("\\", "/")
        
        for inner_File in inner_Files:
            
            # Check if the file is a function file

            if inner_File[0:4].isupper() and inner_File[4] == "_" and inner_File.lower().endswith(".c"):

                # Check if the folder path is not already in the dictionnary.
                if return_Dictionnary.get(current_Folder) is None:
                    return_Dictionnary[current_Folder] = []
                
                # Now the folder path is in the dictionnary. We add the function to the list.
                return_Dictionnary[current_Folder].append(function_analyse(inner_File, []))
                return_List_Functions.append(inner_File)
    
    return (return_Dictionnary, return_List_Functions)


if __name__ == "__main__":
    pass