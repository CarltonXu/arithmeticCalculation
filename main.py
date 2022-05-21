import sys

def arithmetic_arranger(countlist):
    checkListType(countlist)
    checkGiveParamNum(countlist)
    checkParamType(countlist)
    checkOperator(countlist)
    checkParamNumLength(countlist)
    

def checkListType(param):
    if not type(param):
        print("Give parameter not list type")
        sys.exit()

def checkGiveParamNum(param):
    if len(param) > 4:
        print("Error: Too many problems.")
        sys.exit()

def checkOperator(param):
    for o in param:
        if o.split()[1] not in ["+", "-"]:
            print("Error: Operator must be '+' or '-'.")
            sys.exit()

def checkParamType(param):
    for n in param:
        if not n.split()[0].isdigit() or not n.split()[2].isdigit():
            print("Error: Numbers must only contain digits.")
            sys.exit()

def checkParamNumLength(param): 
    for L in param:
        if len(L.split()[0]) > 4 or len(L.split()[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            sys.exit()

if __name__ == "__main__":
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])