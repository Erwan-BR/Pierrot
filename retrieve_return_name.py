def retrieve_return_name(path_file: str) -> str:
    """
    Retrieve the name of parameter which is the return value of a function.
    :param path_file: File that contains the function. Must be a raw string.
    :out: Name of the return parameter of this function.
    """
    # Boolean to check if a multiline comment is opened.
    open_Comment: bool = False

    # Name of the return value of the function.
    return_Name = None

    if path_file is None:
        return return_Name

    # Replace the backslash to avoid an error. Must be a raw string to avoid any error.
    path_file = path_file.replace("\\", "/")

    # Parsing the file to find the name of the return value
    with open(path_file, 'r') as file:
        for line in file:
            # We must ignore the comment on many line.
            if "/*" in line and "*/" not in line:
                open_Comment = True
            
            if open_Comment == True and "*/" in line:
                open_Comment = False
            
            current_Line = line.strip()

            if current_Line.startswith("return"):
                oppening_parenthesis = current_Line.find("(")
                closing_parenthesis = current_Line.find(")")

                if oppening_parenthesis !=-1 and closing_parenthesis != -1:
                    
                    return_Name = current_Line[oppening_parenthesis+1:closing_parenthesis].strip()
                
                # Sometime, there is no parenthesis in the return line.
                else:
                    return_Word = current_Line.find("return")
                    ending_Line = current_Line.find(";")

                    if return_Word !=-1 and ending_Line != -1:
                        
                        return_Name = current_Line[return_Word + 1 + len("return"):ending_Line].strip()
    
    return return_Name


if __name__ == "__main__":
    pass