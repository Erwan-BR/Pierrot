from retrieve_return_name import retrieve_return_name

def retrieve_default_value(path_file: str) -> str:
    """
    Retrieve, if there is one, the default value of a function
    :param path_file: The path of the file where we want to find the default value.
    :out: None if no default value, a string if there is one.
    """
    return_Default = None

    # Replace backslash.
    path_file = path_file.replace("\\", "/")
    
    return_name = retrieve_return_name(path_file)

    # Check if a comment is opened
    open_Comment = False

    # Check if it's the full name (example : E_ReturnStatus and PIE_ReturnStatus)
    isItReturnName = True

    with open(path_file, 'r') as file:
        
        # Reading all line
        for line in file:
            
            # We must ignore the comment on many line.
            if "/*" in line and "*/" not in line:
                open_Comment = True
            
            if open_Comment == True and "*/" in line:
                open_Comment = False

            if not open_Comment:
                # The first time we see the return name, it's in the "local variables" zone.
                if return_name in line :
                    
                    # Check if it's the real return name:
                    index_beggining_return_name = line.find(return_name)

                    # Check if before it's a blanck space :
                    if line[index_beggining_return_name-1].isspace():

                        # Check if there is an equal sign.
                        if "=" in line:
                            index_beginning = line.find("=")
                            index_end = line.find(";")
                            return_Default = line[index_beginning+1:index_end].strip()
                        
                        return return_Default
    
    # Maybe there is no Line that respect that condition.
    return return_Default

if __name__ == "__main__":
    pass