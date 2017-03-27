from botify import NLParser
from nlcalc.context import *

class NLCalculator(NLParser):

    def __init__(self):
        super().__init__()
        self._init_tasks()
        self._init_rule_modifiers()
        self._init_context_modifiers()
        self._init_custom_modifiers()

    def _init_tasks(self):
        # Addition
        self.add_task(keywords=('sum', 'summation', 'add', 'additon', 'total'),
                     context=CONTEXT_SUM, rule=(1,2))
        self.add_task(keywords=('added',), context=CONTEXT_SUM, rule=(-2,-1))
        self.add_task(keywords=('plus', '+'), context=CONTEXT_SUM, rule=(-1,1))

        # Subtraction
        self.add_task(keywords=('difference', 'subtract', 'subtraction'),
                     context=CONTEXT_DIFF, rule=(1,2))
        self.add_task(keywords=('subtracted',), context=CONTEXT_DIFF, rule=(-2,-1))
        self.add_task(keywords=('minus', '-'), context=CONTEXT_DIFF, rule=(-1,1))

        # Multiplication
        self.add_task(keywords=('product', 'multiply', 'multiplication'),
                     context=CONTEXT_MUL, rule=(1,2))
        self.add_task(keywords=('into', 'times', '*'), context=CONTEXT_MUL,
                     rule=(-1,1))
        self.add_task(keywords=('multiplied',), context=CONTEXT_MUL, rule=(-2,-1))

        # Division
        self.add_task(keywords=('divide', 'division'),
                     context=CONTEXT_DIV, rule=(1,2))
        self.add_task(keywords=('divided', 'over', '/'),
                     context=CONTEXT_DIV, rule=(-1,1))

        # Factorial
        self.add_task(keywords=('factorial',), context=CONTEXT_FACT, rule=(-1,))

        # Exponent
        self.add_task(keywords=('power', '^', '**'), context=CONTEXT_POW,
                     rule=(-1,1))

        # Square
        self.add_task(keywords=('square', 'squared'), context=CONTEXT_SQR,
                     rule=(-1,))

        # Cube
        self.add_task(keywords=('cube', 'cubed'), context=CONTEXT_CUBE,
                     rule=(-1,))

        # Root
        self.add_task(keywords=('root',), context=CONTEXT_SQRT, rule=(1,))

        # Special Constants

        self.add_task(keywords=('pi',), context=CONTEXT_PI, rule=()) # pi
        self.add_task(keywords=('e',), context=CONTEXT_E, rule=()) # e

    def _init_rule_modifiers(self):
        self.add_rule_modifier(modifier='to', keywords=('added', 'multiplied'),
                             rule=(-1,1), relative_pos=-1)
        self.add_rule_modifier(modifier='with', keywords=('added', 'multiplied'),
                             rule=(-1,1), relative_pos=-1)
        self.add_rule_modifier(modifier='of',
                             keywords=('factorial', 'square', 'cube'),
                             rule=(1,), relative_pos=-1)
        self.add_rule_modifier(modifier='by', keywords=('divided', 'multiplied'),
                             rule=(-1,1), relative_pos=-1)
        self.add_rule_modifier(modifier='from', keywords=('subtract',),
                             rule=(2,1), relative_pos=-2)
        self.add_rule_modifier(modifier='from', keywords=('subtracted',),
                             rule=(1,-1), relative_pos=-2)
        self.add_rule_modifier(modifier='root', keywords=('square', 'cube'),
                             rule=(1,), relative_pos=-2)

    def _init_context_modifiers(self):
        self.add_context_modifier(modifier='root', keywords=('square',),
                                context=CONTEXT_SQRT, relative_pos=-2)
        self.add_context_modifier(modifier='root', keywords=('cube',),
                                context=CONTEXT_CUBE_ROOT, relative_pos=-2)

    def _init_custom_modifiers(self):
        self.add_custom_modifier(modifier='root', keywords=('square', 'cube'),
                               action='delete', params=(-2,), relative_pos=-2)
        

    # Returns True if String can be converted to Numeric Type
    # otherwise return False
    def is_data(self, value):
        try:
            int(value)
            return True
        except (ValueError,TypeError):
            try:
                float(value)
                return True
            except (ValueError, TypeError):
                return False


    # Converts String to Numeric Type
    # Raises Error if not Possible
    # int conversion is tried first so that high precision of
    # int in python can be utilized
    def clean_data(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return float(value)

    def parse(self, text):
        res = super().parse(text)
        if len(res) == 1:
            return res[0]
        else:
            raise ValueError("Unable to Parse")

def main():
    m = NLCalculator()
    while True:
        print(m.parse(input("---> ")))
        print(m.get_report())

if __name__ == '__main__': main()
