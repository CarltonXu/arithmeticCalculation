import main


class Testarithmetic_arranger:
    def test_arithmetic_arranger(self):
        arrays1 = [
            "32 + 698", "3801 - 2", "45 + 43", "123 + 49", "33 + 43", "13 - 34"
        ]
        arrays2 = ["32 * 698", "3801 - 34", "335 + 43", "1233 + 49"]
        arrays3 = ["32 + 698", "3801 - 2", "45 + 43", "12c3 + 49"]
        arrays4 = ["32 + 698", "38001 - 2", "45 + 43", "123 + 49"]

        arrays5 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "33 + 43"]

        ret1 = main.arithmetic_arranger(arrays1, True)
        ret2 = main.arithmetic_arranger(arrays2, True)
        ret3 = main.arithmetic_arranger(arrays3, True)
        ret4 = main.arithmetic_arranger(arrays4, True)
        ret5 = main.arithmetic_arranger(arrays5, True)
        ret6 = main.arithmetic_arranger(arrays5, False)

        assert ret1 == "Error: Too many problems."
        assert ret2 == "Error: Operator must be '+' or '-'."
        assert ret3 == "Error: Numbers must only contain digits."
        assert ret4 == "Error: Numbers cannot be more than four digits."
        assert ret5 == "   32      3801      45      123      33\n+ 698    -    2    + 43    +  49    + 43\n-----    ------    ----    -----    ----\n  730      3799      88      172      76"
        assert ret6 == "   32      3801      45      123      33\n+ 698    -    2    + 43    +  49    + 43\n-----    ------    ----    -----    ----"
