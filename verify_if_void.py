def verify_if_void(function_path :str) -> bool:
    """
    Check if a function is Void or not.
    :param function_path: Function to check.
    :out: Returns True if the function returns a void value or not.
    """

    function_path = function_path.replace("\\", "/")

    # Boolean to check if a multiline comment is opened.
    open_Comment: bool = False

    # Boolean which is the return value.
    is_void: bool = False

    # Function name. We keep the last part after /, and then the name without .c
    function_name:str = function_path.strip("/")[-1][0:-2]
    

    with open(function_path, 'r') as file:
    
        # Reading all line
        for line in file:
            # We must ignore the comment on many line.
            if "/*" in line and "*/" not in line:
                open_Comment = True
            
            if open_Comment == True and "*/" in line:
                open_Comment = False
            
            if not open_Comment:
                if function_name in line:
                    if line.strip().startswith("void"):
                        is_void = True
    
    return is_void

if __name__ == "__main__":
    pass