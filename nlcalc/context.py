from nlcalc import operations

CONTEXT_SUM = (operations.add,0)
CONTEXT_DIFF = (operations.subtract,0)
CONTEXT_MUL = (operations.multiply,1)
CONTEXT_DIV = (operations.divide,1)
CONTEXT_POW = (operations.power,2)
CONTEXT_FACT = (operations.factorial,3)
CONTEXT_SQR = (operations.square,3)
CONTEXT_SQRT = (operations.sqrt,3)
CONTEXT_CUBE = (operations.cube,3)
CONTEXT_CUBE_ROOT = (operations.cube_root,3)
CONTEXT_PI = (operations.pi,10)
CONTEXT_E = (operations.e,10)
