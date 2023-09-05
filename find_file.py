import os

def find_file(folder: str, file: str) -> str:
    """
    Find the location of a file.
    :param folder: Name of the folder where we search the file. Must be a raw string.
    :param file: Name of the file that we search.
    :out: Full path of the searched file.
    """

    return_Path = None
    
    if folder is None :
        return return_Path
    
    # Replace the backslash to avoid an error
    folder = folder.replace("\\", "/")

    for current_Folder, _, inner_Files in os.walk(folder):   
        if file in inner_Files:
            return_Path = os.path.join(current_Folder, file)
            if return_Path is not None :
                return return_Path.replace("\\", "/")

if __name__ == "__main__":
    pass