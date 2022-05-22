import pytest


def arithmetic_arranger(problems, flag=False):
    one = ""
    two = ""
    three = ""
    four = ""
    mathresult = []
    # check problems numbers params.
    if len(problems) > 5:
        return "Error: Too many problems."

    for p in problems:
        num1 = p.split()[0]
        sign = p.split()[1]
        num2 = p.split()[2]

        if sign not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if len(num1) > len(num2):
            lengthnum = len(num1)
        else:
            lengthnum = len(num2)

        lengthnum += 2

        if len(num1) < lengthnum:
            fnum1 = " " * (lengthnum - len(num1)) + num1
        else:
            fnum1 = num1

        if len(num2) < lengthnum:
            fnum2 = sign + " " * (lengthnum - len(num2) - 1) + num2
        else:
            fnum2 = sign + " " + num2

        if sign == "+":
            mathresultnum = int(num1) + int(num2)
        else:
            mathresultnum = int(num1) - int(num2)

        fproblem = fnum1 + "\n" + fnum2 + "\n" + ((lengthnum) * "-") + "\n" + (
            " " * (lengthnum - len(str(mathresultnum))) + str(mathresultnum))
        mathresult.append(fproblem)

    for mas in mathresult:
        if mathresult.index(mas) == 0:
            one += mas.split("\n")[0]
            two += mas.split("\n")[1]
            three += mas.split("\n")[2]
            four += mas.split("\n")[3]
        else:
            one += " " * 4 + mas.split("\n")[0]
            two += " " * 4 + mas.split("\n")[1]
            three += " " * 4 + mas.split("\n")[2]
            four += " " * 4 + mas.split("\n")[3]
    if flag:
        result = one + "\n" + two + "\n" + three + "\n" + four
    else:
        result = one + "\n" + two + "\n" + three
    print(result)
    return result


if __name__ == "__main__":
    arithmetic_arranger(
        ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "13 - 34"], True)
    pytest.main()
