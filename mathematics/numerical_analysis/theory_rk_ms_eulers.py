from core.theory_core import super, sub

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

def decide_step_size_rk_euler():
    theory=[f"In any initial value problem, we require solution for x > x0 and usually up to a point x = b. The step length h for application of any numerical method for the initial value problem must be properly chosen. The computations contain mainly two types of errors: truncation error and round-off error. Truncation error is in the hand of the user. It can be controlled by choosing higher order methods. Round-off errors are not in the hands of the user. They can grow and finally destroy the true solution. In such case, we say that the method is numerically unstable. This happens when the step length is chosen larger than the allowed limiting value. All explicit methods have restrictions on the step length that can be used. Many implicit methods have no restriction on the step length that can be used. Such methods are called unconditionally stable methods."]
    theory=theory+[f"The behaviour of the solution of the given initial value problem is studied by considering the linearized form of the differential equation y' = f (x, y). The linearized form of the initial value problem is given by y' = λ y, λ < 0, y(x=x{sub('0')})=y{sub('0')}. The single step methods are applied to this differential equation to obtain the difference equation y{sub('i+1')} = E(λh)y{sub('i')}, where E(λh) is called the amplification factor. If | E(λh) | < 1, then all the errors (round-off and other errors) decay and the method gives convergent solutions. We say that the method is stable. This condition gives a bound on the step length h that can be used in the computations. We have the following conditions for stability of the single step methods : "]
    theory=theory+[f"1. Euler method: -2 < λh < 0"]
    theory=theory+[f"2. Runge-Kutta method of second order: -2 < λh < 0."]
    theory=theory+[f"3. Classical Runge-Kutta method of fourth order: -2.78 < λh < 0."]
    theory=theory+[f"4. Backward Euler method: Stable for all h, that is, -∞ < λh < 0. (Unconditionally stable method)."]
    theory=theory+[f"Thus, we conclude that a numerical method can not be applied as we like to a given initial value problem. The choice of the step length is very important and it is governed by the stability condition."]
    theory=theory+[f"For example, if we are solving the initial value problem y' = -100y, y(x=x{sub('0')})=y{sub('0')}, by Euler method, then the step length should satisfy the condition -2 < λh < 0 or -2 < -100h < 0, or h < 0.02."]
    return theory

def source_of_info():
    theory=[f"Source: Numerical methods by S.R.K Lyenger,R.K Jain"]

    return theory

def picards_theory():
    theory=[f" Picard method is an iterative method. An iterative method gives a sequence of approximations y1(x), y2(x), …,yk(x),…to the solution of differential equations such that the nth approximation is obtained from one or more prevoius approximations. The integration of differential equation (i.e given IVP) yields , y(t)= y{sub('0')}+ ∫f(x,y(x))dx with limits form t{sub('0')} to t "]
    return theory

def euler_forward_theory():
    theory=[f"Euler forward method for IVP dy/dx=f(x,y) , is y{sub('i+1')}=y{sub('i')}+hf(x{sub('i')},y(x{sub('i')})) "]
    theory=theory+[f"This method is of 1{super('st')} order."]
    return theory

def euler_cauchy_theory():
    theory=[f"This method is called euler cauchy method, euler improved method, or runge-kutta method of second order."]
    theory=theory+[f"It's formula is given as :y{sub('i+1')}=y{sub('i')}+(h/2)[f(x{sub('i')},y(x{sub('i')}))+f(x{sub('i+1')},y(x{sub('i+1')}))] and  y{sub('i+1')} is found using euler forward method i.e. y{sub('i+1')}=y{sub('i')}+hf(x{sub('i')},y(x{sub('i')}))"]
    theory=theory+[f"It is of second order."]
    return theory

def rk_theory():
    theory=[f"Given IVP: dy/dx=f(x,y), with initial condition as : y(x=x{sub('0')})=y{sub('0')}"]
    theory=theory+[f"(1) Euler forward method for IVP dy/dx=f(x,y) , is y{sub('i+1')}=y{sub('i')}+hf(x{sub('i')},y(x{sub('i')})). This method is of 1{super('st')} order."]
    theory=theory+[f"(2) Euler cauchy method, euler improved method, or runge-kutta method of second order.It is of second order."]
    theory=theory+[f"It's formula is given as :y{sub('i+1')}=y{sub('i')}+(h/2)[f(x{sub('i')},y(x{sub('i')}))+f(x{sub('i+1')},y(x{sub('i+1')}))] and  y{sub('i+1')} is found using euler forward method i.e. y{sub('i+1')}=y{sub('i')}+hf(x{sub('i')},y(x{sub('i')}))"]
    theory=theory+[f"(3) 'Classic Runge-Kutta method' or simply as 'the Runge-Kutta method' is a fourth-order method, meaning that the local truncation error is of the order of O(h{super('5')}) while the total accumulated error is on the order of O(h{super('4')}) its formula is given as:"]
    theory=theory+[{'link':"https://wikimedia.org/api/rest_v1/media/math/render/svg/2883d610363b37ad92665f906a06240d1b3299bb"}]
    theory=theory+[{'link':"https://wikimedia.org/api/rest_v1/media/math/render/svg/4b038c70313036aabe58cdc5d6ec6ecb098dbb70"}]
    theory=theory+[f"(4) Gill's 4th Order Method is a fourth-order method, meaning that the local truncation error is of the order O(h{super('5')}) and given as :"]
    theory=theory+[{'link':'/static/theory_images/gills_k_values.jpeg'}]
    theory=theory+[f"(5) The Runge-Kutta-Fehlberg method (denoted RKF45) is of order 4 and given as:"]
    theory=theory+[{'link':'/static/theory_images/felberg.jpeg'}]
    theory=theory+[f"Each step requires the use of the following six values:"]
    theory=theory+[{'link':"/static/theory_images/felberg_k_values.jpeg"}]
    theory=theory+[f"(6) A better value for the solution is determined using a Runge-Kutta method of order 5(lets call it improved-fehlberg) given as:"]
    theory=theory+[{'link':"/static/theory_images/felberg_improved.jpeg"}]
    
    return theory

def adams_bashforth_theory():
    theory=[f"All Adams-Bashforth (predictor) methods are explicit methods. These methods are derived as follows:"]
    theory=theory+[{'link':'/static/theory_images/adams_bashforth_derivation.jpg'}]
    theory=theory+[f"Truncation error is of order O(h{super('k+1')}). Therefore, a k-step Adams-Bashforth method is of order k. Truncation Error is given as :"]
    theory=theory+[{'link':'/static/theory_images/te_adams_bashforth.jpeg'}]
    theory=theory+[f"First order Adams-Bashforth method:"]
    theory=theory+[{'link':'/static/theory_images/adams_bashforth_1_order.jpeg'}]
    theory=theory+[f"Second order Adams-Bashforth method:"]
    theory=theory+[{'link':'/static/theory_images/adams_bashforth_2_order.jpg'}]
    theory=theory+[f"Third order Adams-Bashforth method:"]
    theory=theory+[{'link':'/static/theory_images/adams_bashforth_3_order.jpeg'}]
    theory=theory+[f"Forth order Adams-Bashforth method:"]
    theory=theory+[{'link':'/static/theory_images/adams_bashforth_4_order.jpeg'}]
    theory=theory+[f"The required starting values for the application of the Adams-Bashforth methods are obtained by using any single step method like Euler's method, Taylor series method or Runge-Kutta methods."]
    return theory

def adams_moulton_theory():
    theory=[f"All Adams-Moulton (corrector) methods are implicit methods. Adams moulton methods are derived as:"]
    theory=theory+[{'link':'/static/theory_images/adams_moultan_drivation.jpg'}]
    theory=theory+[f"Truncation error is of order O(h{super('k+2')}). Therefore, a k-step Adams-Moulton method is of order k + 1. Traunction error is drived as:"]
    theory=theory+[{'link':'/static/theory_images/te_adams_moulton.jpg'}]
    theory=theory+[f"First order Adams-Moulton Method:"]
    theory=theory+[{'link':'/static/theory_images/adams_moulton_1_order.jpeg'}]
    theory=theory+[f"Second order Adams-Moulton Method:"]
    theory=theory+[{'link':'/static/theory_images/adams_moulton_2_order.jpeg'}]
    theory=theory+[f"Third order Adams-Moulton Method:"]
    theory=theory+[{'link':'/static/theory_images/adams_moulton_3_order.jpg'}]
    theory=theory+[f"Forth order Adams-Moulton Method:"]
    theory=theory+[{'link':'/static/theory_images/adams_moulton_4_order.jpeg'}]
    return theory

def milne_theory():
    theory=[f"Derivation of Milne-methods:"]
    theory=theory+[{'link':'/static/theory_images/milne_derivation.jpg'}]
    theory=theory+[f"Milne-Simpson Method of order 4 is as follows:"]
    theory=theory+[{'link':'/static/theory_images/milne_simpson_4_order.jpeg'}]
    return theory

def milne_adams_theory():
    theory=[f"Adams-Bashforth(predictor) method of fourth order which is commonly used with milne simpson in predictor-corrector is :"]
    theory=theory+[{'link':'/static/theory_images/adams_milne_4_order.jpeg'}]
    theory=theory+[f"It's derivation is as follows:"]
    theory=theory+[{'link':'/static/theory_images/adams_milne_derivation.jpeg'}]
    theory=theory+[f"Truncation Error is given as:"]
    theory=theory+[{'link':'/static/theory_images/te_adams_milne.jpeg'}]
    return theory