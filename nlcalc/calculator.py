from botify import Botify
from nlcalc.context import *
from nlcalc.utils import is_numeric, convert_to_numeric, text2int


class NLCalculator:
    """Natural Language Mathematical Calculator.

    This class can be used to parse mathematical statements in natural
    language.

    Example
    -------
    >>> from nlcalc import NLCalculator
    >>> my_calc = NLCalculator()
    >>> result = my_calc.calculate("what is two plus twenty five")
    >>> print(result)
    27
    >>> result = my_calc.calculate("3 square plus four square")
    >>> print(result)
    25

    Attributes
    ----------
    strict_mode_enabled
    """
    def __init__(self):
        self._parser = Botify(is_token_data_callback=is_numeric,
                              clean_data_callback=convert_to_numeric)
        self._init_tasks()
        self._init_modifiers()

    @property
    def strict_mode_enabled(self):
        """Whether strict mode is enabled for the calculator instance."""
        return self._parser.strict_mode_enabled

    @strict_mode_enabled.setter
    def strict_mode_enabled(self, value):
        self._parser.strict_mode_enabled = value
        

    def _init_tasks(self):
        # Addition
        self._parser.add_task(keywords=('sum', 'summation', 'add',
                                        'additon', 'total'),
                              context=CONTEXT_SUM,
                              rule=(1, 2))
        self._parser.add_task(keywords=('added',),
                              context=CONTEXT_SUM,
                              rule=(-2, -1))
        self._parser.add_task(keywords=('plus', '+'),
                              context=CONTEXT_SUM,
                              rule=(-1, 1))

        # Subtraction
        self._parser.add_task(keywords=('difference', 'subtract', 'subtraction'),
                              context=CONTEXT_DIFF,
                              rule=(1, 2))
        self._parser.add_task(keywords=('subtracted',),
                              context=CONTEXT_DIFF,
                              rule=(-2, -1))
        self._parser.add_task(keywords=('minus', '-'),
                              context=CONTEXT_DIFF,
                              rule=(-1, 1))

        # Multiplication
        self._parser.add_task(keywords=('product', 'multiply', 'multiplication'),
                              context=CONTEXT_MUL,
                              rule=(1, 2))
        self._parser.add_task(keywords=('into', 'times', '*'),
                              context=CONTEXT_MUL,
                              rule=(-1, 1))
        self._parser.add_task(keywords=('multiplied',),
                              context=CONTEXT_MUL,
                              rule=(-2, -1))

        # Division
        self._parser.add_task(keywords=('divide', 'division'),
                              context=CONTEXT_DIV,
                              rule=(1, 2))
        self._parser.add_task(keywords=('divided', 'over', '/'),
                              context=CONTEXT_DIV,
                              rule=(-1, 1))

        # Factorial
        self._parser.add_task(keywords=('factorial',),
                              context=CONTEXT_FACT,
                              rule=(-1,))

        # Exponent
        self._parser.add_task(keywords=('power', '^', '**'),
                              context=CONTEXT_POW,
                              rule=(-1, 1))

        # Square
        self._parser.add_task(keywords=('square', 'squared'),
                              context=CONTEXT_SQR,
                              rule=(-1,))

        # Cube
        self._parser.add_task(keywords=('cube', 'cubed'),
                              context=CONTEXT_CUBE,
                              rule=(-1,))

        # Root
        self._parser.add_task(keywords=('root',),
                              context=CONTEXT_SQRT,
                              rule=(1,))

        # Special Constants
        self._parser.add_task(keywords=('pi',),     # pi
                              context=CONTEXT_PI,
                              rule=())
        self._parser.add_task(keywords=('e',),      # e
                              context=CONTEXT_E,
                              rule=())

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
                                  action=Botify.ACTION_DELETE,
                                  parameter=1)

    def calculate(self, text):
        """Calculate the output after parsing input.

        Parameters
        ----------
        text : str
            A string value which should be parsed

        Returns
        -------
        int or float:
            The final result

        Raises
        ------
        ValueError
            If the text cannot be succesfully parsed and evaluated to get
            a result.
        """
        res = self._parser.parse(text2int(text))
        if len(res) == 1:
            return res[0]
        else:
            raise ValueError("Unable to Parse")


def main():
    m = NLCalculator()
    while True:
        print(m.calculate(input("---> ")))
        print(m._parser._get_report())

if __name__ == '__main__':
    main()
