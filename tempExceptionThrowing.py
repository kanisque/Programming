#Exception handling
def hitIt():
    try:
        print(5/0)
        return(1)
    except Exception as ex:
        print("Error in hitIt",ex)
        raise Exception("not applicable")