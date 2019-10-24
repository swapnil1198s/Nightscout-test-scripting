def oracle(value, expected):
    try:
        if(value==expected):
            return "Pass"
        else:
            return "Fail"
    except:
        return "Error"