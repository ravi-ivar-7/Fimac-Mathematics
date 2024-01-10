from sympy import *
import pprint
from numpy import pi

(x, y, z) = symbols('x y z')

def indefinite_integral_function(result, **kwargs):
    try:
        function=kwargs['function']
        target_x=kwargs['target_x']
        integral = integrate(function, x)
        integral_at_x=(integral.subs({x:target_x}))
        integralf =pprint.pformat(integral)
        return  result.extend([['Integral is:'],[integralf],[f"Value of Integral at {target_x} is :"],[f"{integral_at_x}"],[f"which comes out to be {round(N(integral_at_x),5)}"]])
    except Exception as e:
        return result.extend([-1,str(e)])