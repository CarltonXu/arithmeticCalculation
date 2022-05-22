import sys

def arithmetic_arranger(countlist, flag=False):
    one = ""
    two = ""
    three = ""
    four = ""
    checkListType(countlist)
    checkGiveParamNum(countlist)
    checkParamType(countlist)
    checkOperator(countlist)
    checkParamNumLength(countlist)
    formatParam(countlist)
    mathresult = formatParam(countlist)
    for ma in mathresult:
        if mathresult.index(ma) == 0:
            one += ma.split("\n")[0]
            two += ma.split("\n")[1] 
            three += ma.split("\n")[2]
            four += ma.split("\n")[3]
        else:
            one += " " * 4 + ma.split("\n")[0]
            two += " " * 4 + ma.split("\n")[1] 
            three += " " * 4 + ma.split("\n")[2]
            four += " " * 4 + ma.split("\n")[3]
            
    print(one)
    print(two)
    print(three)
    if flag:
        print(four)
    
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

def formatParam(param):
    flist = []
    for p in param:
        firstnum = p.split()[0]
        mathSymbols = p.split()[1]
        secondnum = p.split()[2]
        if len(firstnum) > len(secondnum):
            lengthnum = len(firstnum)
        else:
            lengthnum = len(secondnum)
        lengthnum += 2
        if len(firstnum) < lengthnum:
            fone = " " * (lengthnum - len(firstnum)) + firstnum
        else:
            fone = firstnum
        if len(secondnum) < lengthnum:
            ftwo = mathSymbols + " " * (lengthnum - len(secondnum) -1) + secondnum
        else:
            ftwo = mathSymbols + " " + secondnum
        if mathSymbols == "+":
            mathresultnum = int(firstnum) + int(secondnum)
        else:
            mathresultnum = int(firstnum) - int(secondnum)
        fthree = fone + "\n" + ftwo + "\n" + ((lengthnum) * "-") + "\n" + (" " * (lengthnum - len(str(mathresultnum))) + str(mathresultnum))
        flist.append(fthree)
    return flist
            

if __name__ == "__main__":
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)