import pkg_resources

from chainer import function
from chainer import function_set
from chainer.functions import basic_math
from chainer import optimizer
from chainer import parameterized
from chainer import serializer
from chainer import variable


__version__ = pkg_resources.get_distribution('chainer').version

Variable = variable.Variable
Function = function.Function
FunctionSet = function_set.FunctionSet

Optimizer = optimizer.Optimizer
GradientMethod = optimizer.GradientMethod

ParameterizedObject = parameterized.ParameterizedObject
ParameterizedDict = parameterized.ParameterizedDict
ParameterizedList = parameterized.ParameterizedList
Serializer = serializer.Serializer

basic_math.install_variable_arithmetics()
