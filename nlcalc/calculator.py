from botify import Botify
from nlcalc.context import *
from nlcalc.utils import is_numeric, convert_to_numeric, text2int


class NLCalculator:
    def __init__(self):
        self._parser = Botify(is_token_data_callback=is_numeric,
                              clean_data_callback=convert_to_numeric)
        self._init_tasks()
        self._init_modifiers()

    def _init_tasks(self):
        # Addition
        self._parser.add_task(keywords=('sum', 'summation', 'add', 'additon', 'total'),
                              context=CONTEXT_SUM, rule=(1, 2))
        self._parser.add_task(keywords=('added',), context=CONTEXT_SUM, rule=(-2, -1))
        self._parser.add_task(keywords=('plus', '+'), context=CONTEXT_SUM, rule=(-1, 1))

        # Subtraction
        self._parser.add_task(keywords=('difference', 'subtract', 'subtraction'),
                              context=CONTEXT_DIFF, rule=(1, 2))
        self._parser.add_task(keywords=('subtracted',), context=CONTEXT_DIFF, rule=(-2, -1))
        self._parser.add_task(keywords=('minus', '-'), context=CONTEXT_DIFF, rule=(-1, 1))

        # Multiplication
        self._parser.add_task(keywords=('product', 'multiply', 'multiplication'),
                              context=CONTEXT_MUL, rule=(1, 2))
        self._parser.add_task(keywords=('into', 'times', '*'), context=CONTEXT_MUL,
                              rule=(-1, 1))
        self._parser.add_task(keywords=('multiplied',), context=CONTEXT_MUL, rule=(-2, -1))

        # Division
        self._parser.add_task(keywords=('divide', 'division'),
                              context=CONTEXT_DIV, rule=(1, 2))
        self._parser.add_task(keywords=('divided', 'over', '/'),
                              context=CONTEXT_DIV, rule=(-1, 1))

        # Factorial
        self._parser.add_task(keywords=('factorial',), context=CONTEXT_FACT, rule=(-1,))

        # Exponent
        self._parser.add_task(keywords=('power', '^', '**'), context=CONTEXT_POW,
                              rule=(-1, 1))

        # Square
        self._parser.add_task(keywords=('square', 'squared'), context=CONTEXT_SQR,
                              rule=(-1,))

        # Cube
        self._parser.add_task(keywords=('cube', 'cubed'), context=CONTEXT_CUBE,
                              rule=(-1,))

        # Root
        self._parser.add_task(keywords=('root',), context=CONTEXT_SQRT, rule=(1,))

        # Special Constants
        self._parser.add_task(keywords=('pi',), context=CONTEXT_PI, rule=())   # pi
        self._parser.add_task(keywords=('e',), context=CONTEXT_E, rule=())     # e

    def _init_modifiers(self):
        self._parser.add_modifier(modifier='to',
                                  keywords=('added', 'multiplied'),
                                  relative_pos=-1,
                                  action=Botify.ACTION_UPDATE_RULE,
                                  parameter=(-1, 1))
        self._parser.add_modifier(modifier='with',
                                  keywords=('added', 'multiplied'),
                                  relative_pos=-1,
                                  action=Botify.ACTION_UPDATE_RULE,
                                  parameter=(-1, 1))
        self._parser.add_modifier(modifier='of',
                                  keywords=('factorial', 'square', 'cube'),
                                  relative_pos=-1,
                                  action=Botify.ACTION_UPDATE_RULE,
                                  parameter=(1,))
        self._parser.add_modifier(modifier='by',
                                  keywords=('divide', 'divided', 'multiply', 'multiplied'),
                                  relative_pos=-1,
                                  action=Botify.ACTION_UPDATE_RULE,
                                  parameter=(-1, 1))
        self._parser.add_modifier(modifier='from',
                                  keywords=('subtract',),
                                  relative_pos=-2,
                                  action=Botify.ACTION_UPDATE_RULE,
                                  parameter=(2, 1))
        self._parser.add_modifier(modifier='from',
                                  keywords=('subtracted',),
                                  relative_pos=-2,
                                  action=Botify.ACTION_UPDATE_RULE,
                                  parameter=(1, -1))
        self._parser.add_modifier(modifier='root',
                                  keywords=('square', 'cube'),
                                  relative_pos=-2,
                                  action=Botify.ACTION_UPDATE_RULE,
                                  parameter=(1,))

        self._parser.add_modifier(modifier='root',
                                  keywords=('square',),
                                  relative_pos=-2,
                                  action=Botify.ACTION_UPDATE_CONTEXT,
                                  parameter=CONTEXT_SQRT)
        self._parser.add_modifier(modifier='root',
                                  keywords=('cube',),
                                  relative_pos=-2,
                                  action=Botify.ACTION_UPDATE_CONTEXT,
                                  parameter=CONTEXT_CUBE_ROOT)

        self._parser.add_modifier(modifier='root',
                                  keywords=('square', 'cube'),
                                  relative_pos=-2,
                                  action=Botify.ACTION_DELETE)

    def calculate(self, text):
        res = self._parser.parse(text2int(text))
        if len(res) == 1:
            return res[0]
        else:
            raise ValueError("Unable to Parse")


def main():
    m = NLCalculator()
    while True:
        print(m.calculate(input("---> ")))

if __name__ == '__main__':
    main()
