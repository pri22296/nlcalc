from nlcalc import operations
from botify import Context

CONTEXT_SUM = Context(operations.add,0)
CONTEXT_DIFF = Context(operations.subtract,0)
CONTEXT_MUL = Context(operations.multiply,1)
CONTEXT_DIV = Context(operations.divide,1)
CONTEXT_POW = Context(operations.power,2)
CONTEXT_FACT = Context(operations.factorial,3)
CONTEXT_SQR = Context(operations.square,3)
CONTEXT_SQRT = Context(operations.sqrt,3)
CONTEXT_CUBE = Context(operations.cube,3)
CONTEXT_CUBE_ROOT = Context(operations.cube_root,3)
CONTEXT_PI = Context(operations.pi,10)
CONTEXT_E = Context(operations.e,10)
