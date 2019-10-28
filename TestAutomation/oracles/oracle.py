def oracle(val1, val2):
    try: val1 = int(val1)
    except:
        try: val1 = float(val1)
        except: pass

    try: val2 = int(val2)
    except:
        try: val2 = float(val2)
        except: pass

    try:
        if(val1==val2):
            return "Pass"
        elif(type(val1)!=type(val2)):
            return "TypeError"
        else:
            return "Fail"
    except Exception as e:
        return "Error:" +str(e)