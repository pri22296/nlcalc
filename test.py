from nlcalc import NLCalculator
calc = NLCalculator()

query_list = ["9 over 8 plus 4 times 2 divide by 3",
              "1 plus 2",
              "1 plus 2 times 3",
              "9 minus 3 times 7",
              "4 minus 8 plus 6 times 9",
              "7 over 9 plus 1",
              "2 over 4 times 2"]

for query in query_list:
    result = calc.calculate(query)
    print(query, '=', result)
