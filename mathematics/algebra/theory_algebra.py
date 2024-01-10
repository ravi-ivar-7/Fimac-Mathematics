from core.theory_core import sub, super

def source_of_info():
    theory=[f"Source: Wikipedia,Numerical methods by S.R.K Lyenger,R.K Jain"]
    return theory

def newton_raphson_theory():
    theory=[f" Newton's method is very powerful but calculating f' is very computationaly extensive."]
    theory=theory+[f"The (n+1){super('th')} step in newton raphson method is given as: x{sub('n+1')}=x{sub('n')}-f(x{sub('n')})/f'(x{sub('n')}) and we say x{sub('n+1')} is solution of f(x) if |x{sub('n+1')}-x{sub('n')}|<accuracy."]
    theory=theory +[f"This method will fails when f'(x{sub('n')}) becomes zero or there is a cyclic behaviour of function."]
    theory=theory+[f"Example are: cos(x) + 2 sin(x) + x{sub('2')} with initial guess as -0.1. Input function is: cos(x)+2*sin(x)+x**2 , with initial guess as -0.1 ."]
    theory=theory+[f"Input function for x{super('3')} + e{super('x/2')} +log(x{super('4')}) +sin(x) +tan{super('-1')}(x) is : x**3 + exp(x/2) + log(x**4) + sin(x) + atan(x)"]
    sub
    return theory

def secant_theory():
    theory=[f"The (n+1){super('th')} step in Secant method is given as: x{sub('n+2')}=x{sub('n+1')}-f(x{sub('n+1')})(x{sub('n+1')}-x{sub('n')})/(f(x{sub('n+1')})-f(x{sub('n')})) and we say x{sub('n+1')} is solution of f(x) if |x{sub('n+1')}-x{sub('n')}|<accuracy."]
    theory=theory+[f"Example are: cos(x) + 2 sin(x) + x{sub('2')} with initial guess as -0.1 and 0. Input function is: cos(x)+2*sin(x)+x**2 , with first guess as -0.1 and second guess as 0"]
    
    return theory
