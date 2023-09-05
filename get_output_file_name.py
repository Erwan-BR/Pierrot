import os

def get_output_file_name(output_file_path: str = None) -> str :
    """
    This function search for the output file name. If you use it in debug mode, you may let None 
    :param output_file_path: Path of the output file. If you use it in debug mode, you may let None. In this case, the folder is created if needed.
    :return: The output file name, including all the path.
    """
    # output_file_path should not be None, but it may be the case if you are debugging.
    if output_file_path is None:
        output_folder_path = "output"
        current_output_path = os.path.join(os.getcwd(), output_folder_path)
        index_output_file_name = 0
        output_file_name = "output.xlsx"

        while os.path.isfile(os.path.join(current_output_path, output_file_name)):
            index_output_file_name += 1
            output_file_name = f"output_{index_output_file_name}.xlsx"
        
        output_file_name = os.path.join(current_output_path, output_file_name)
    else:
        # We get the last part after the last /
        output_file_name = output_file_path
    
    return output_file_name

if __name__ == "__main__":
    pass