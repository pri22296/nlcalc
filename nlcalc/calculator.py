from botify import NLParser
from nlcalc.context import *
from nlcalc.utils import is_numeric, convert_to_numeric, text2int
    
class NLCalculator:
    def __init__(self):
        self._parser = NLParser(is_token_data_callback=is_numeric,
                                clean_data_callback=convert_to_numeric)
        self._init_tasks()
        self._init_rule_modifiers()
        self._init_context_modifiers()
        self._init_custom_modifiers()

    def _init_tasks(self):
        # Addition
        self._parser.add_task(keywords=('sum', 'summation', 'add', 'additon', 'total'),
                     context=CONTEXT_SUM, rule=(1,2))
        self._parser.add_task(keywords=('added',), context=CONTEXT_SUM, rule=(-2,-1))
        self._parser.add_task(keywords=('plus', '+'), context=CONTEXT_SUM, rule=(-1,1))

        # Subtraction
        self._parser.add_task(keywords=('difference', 'subtract', 'subtraction'),
                     context=CONTEXT_DIFF, rule=(1,2))
        self._parser.add_task(keywords=('subtracted',), context=CONTEXT_DIFF, rule=(-2,-1))
        self._parser.add_task(keywords=('minus', '-'), context=CONTEXT_DIFF, rule=(-1,1))

        # Multiplication
        self._parser.add_task(keywords=('product', 'multiply', 'multiplication'),
                     context=CONTEXT_MUL, rule=(1,2))
        self._parser.add_task(keywords=('into', 'times', '*'), context=CONTEXT_MUL,
                     rule=(-1,1))
        self._parser.add_task(keywords=('multiplied',), context=CONTEXT_MUL, rule=(-2,-1))

        # Division
        self._parser.add_task(keywords=('divide', 'division'),
                     context=CONTEXT_DIV, rule=(1,2))
        self._parser.add_task(keywords=('divided', 'over', '/'),
                     context=CONTEXT_DIV, rule=(-1,1))

        # Factorial
        self._parser.add_task(keywords=('factorial',), context=CONTEXT_FACT, rule=(-1,))

        # Exponent
        self._parser.add_task(keywords=('power', '^', '**'), context=CONTEXT_POW,
                     rule=(-1,1))

        # Square
        self._parser.add_task(keywords=('square', 'squared'), context=CONTEXT_SQR,
                     rule=(-1,))

        # Cube
        self._parser.add_task(keywords=('cube', 'cubed'), context=CONTEXT_CUBE,
                     rule=(-1,))

        # Root
        self._parser.add_task(keywords=('root',), context=CONTEXT_SQRT, rule=(1,))

        # Special Constants

        self._parser.add_task(keywords=('pi',), context=CONTEXT_PI, rule=()) # pi
        self._parser.add_task(keywords=('e',), context=CONTEXT_E, rule=()) # e

    def _init_rule_modifiers(self):
        self._parser.add_rule_modifier(modifier='to', keywords=('added', 'multiplied'),
                             rule=(-1,1), relative_pos=-1)
        self._parser.add_rule_modifier(modifier='with', keywords=('added', 'multiplied'),
                             rule=(-1,1), relative_pos=-1)
        self._parser.add_rule_modifier(modifier='of',
                             keywords=('factorial', 'square', 'cube'),
                             rule=(1,), relative_pos=-1)
        self._parser.add_rule_modifier(modifier='by', keywords=('divide', 'divided', 'multiply', 'multiplied'),
                             rule=(-1,1), relative_pos=-1)
        self._parser.add_rule_modifier(modifier='from', keywords=('subtract',),
                             rule=(2,1), relative_pos=-2)
        self._parser.add_rule_modifier(modifier='from', keywords=('subtracted',),
                             rule=(1,-1), relative_pos=-2)
        self._parser.add_rule_modifier(modifier='root', keywords=('square', 'cube'),
                             rule=(1,), relative_pos=-2)

    def _init_context_modifiers(self):
        self._parser.add_context_modifier(modifier='root', keywords=('square',),
                                context=CONTEXT_SQRT, relative_pos=-2)
        self._parser.add_context_modifier(modifier='root', keywords=('cube',),
                                context=CONTEXT_CUBE_ROOT, relative_pos=-2)

    def _init_custom_modifiers(self):
        self._parser.add_custom_modifier(modifier='root', keywords=('square', 'cube'),
                               action='delete', params=(-2,), relative_pos=-2)

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

if __name__ == '__main__': main()
