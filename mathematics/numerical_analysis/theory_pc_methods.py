from core.theory_core import sub

def source_of_info():
    theory=[f"Source: Wikipedia,Numerical methods by S.R.K Lyenger,R.K Jain"]
    return theory

def decide_step_size_multistep():
    theory=[f"In any initial value problem, we require solution for x > x0 and usually up to a point x = b. The step length h for application of any numerical method for the initial value problem must be properly chosen. The computations contain mainly two types of errors: truncation error and round-off error. Truncation error is in the hand of the user. It can be controlled by choosing higher order methods. Round-off errors are not in the hands of the user. They can grow and finally destroy the true solution. In such case, we say that the method is numerically unstable. This happens when the step length is chosen larger than the allowed limiting value. All explicit methods have restrictions on the step length that can be used. Many implicit methods have no restriction on the step length that can be used. Such methods are called unconditionally stable methods."]
    theory=theory+[f"The behaviour of the solution of the given initial value problem is studied by considering the linearized form of the differential equation y' = f (x, y). The linearized form of the initial value problem is given by y' = λ y, λ < 0, y(x=x{sub('0')})=y{sub('0')}. The single step methods are applied to this differential equation to obtain the difference equation y{sub('i+1')} = E(λh)y{sub('i')}, where E(λh) is called the amplification factor. If | E(λh) | < 1, then all the errors (round-off and other errors) decay and the method gives convergent solutions. We say that the method is stable. This condition gives a bound on the step length h that can be used in the computations. We have the following conditions for stability of the single step methods : "]
    theory=theory+[f"1. Euler method: -2 < λh < 0"]
    theory=theory+[f"2. Backward Euler method: Stable for all h, that is, -∞ < λh < 0. (Unconditionally stable method)."]
    theory=theory+[f"3. Stability intervals (condition on h) for the multi step methods ( λ<0) is given in below table:"]
    theory=theory+[{'link':'/static/theory_images/stability_multistep.jpeg'}]
    theory=theory+[f"Thus, we conclude that a numerical method can not be applied as we like to a given initial value problem. The choice of the step length is very important and it is governed by the stability condition."]
    theory=theory+[f"For example, if we are solving the initial value problem y' = -100y, y(x=x{sub('0')})=y{sub('0')}, by Euler method, then the step length should satisfy the condition -2 < λh < 0 or -2 < -100h < 0, or h < 0.02."]
    return theory

def source_of_info():
    theory=[f"Source: Numerical methods by S.R.K Lyenger,R.K Jain"]
    return theory

def adams_bashforth_moulton_pc_theory():
    theory=[f"we combine the explicit methods (which have weak stability properties) and implicit methods (which have strong stability properties) to obtain P-C methods"]
    theory=theory+[f"Adams-Bashforth-Moulton predictor-corrector method. Both the predictor and corrector methods are of fourth order and given as:"]
    theory=theory+[{'link':'/static/theory_images/adam_bashforht_moulton_pc_4_order.jpeg'}]
    theory=theory+[{'link':'/static/theory_images/eg_adams_bashforth_pc.jpeg'}]
    theory=theory+[f"For the above example, Input function is => 1/x**2-y/x ."]
    theory=theory+[f"Input x and y values as => x-values: 1,1.1,1.2,1.3 and y-values : 1,0.996,0.986,0.972 "]
    return theory

def milve_adams_pc_theory():
    theory=[f"Both the predictor and corrector methods are of fourth order and given as:"]
    theory=theory+[{'link':'/static/theory_images/milve_adams_pc_4_order.jpeg'}]
    theory=theory+[{'link':'/static/theory_images/eg_adams_milne_simpson.jpeg'}]
    theory=theory+[f"For the above example, Input function is => x**3+y."]
    theory=theory+[f"Input x and y values as => x-values: 0,0.2,0.4,0.6 and y-values : 2,2.073,2.452,3.023 "]
    return theory