from core.theory_core import sub,super


def source_of_info():
    theory=[f"Source: Wikipedia,Numerical methods by S.R.K Lyenger,R.K Jain"]
    return theory

def trapezoidal_theory():
    theory=[f"The trapezoidal rule is based on the Newton-Cotes formula that if one approximates the integrand by an  nth order polynomial, then the integral of the function is approximated by the integral of that  nth order polynomial"]
    theory=theory +[f"The formula used is : I(integral)=h/2[f(x{sub('0')})+2Σ(i=1 to n-1)f(x{sub('i')})+f(x{sub('n')})] , where h is step size"]
    theory=theory+[f"Error is calculate using formula:|((b-a)h{super('2')}(d{super('2')}f(x)/dx{super('2')})/12|{sub('max')}, where a and b are initial and final point of integral."]
    theory=theory+[f"Example, if the given integral is : ∫5xe{super('-2x')} dx with limits from 0.1 to 1.3. Then input function is as follows: 5*x*exp(-2*x)"]
    return theory

def simpson_3_theory():
    theory=[f"Formula used for simpson 1/3 rule is : Integral (I)=∫f(x)=h([f(x{sub('0')})+4Σ(i=odd integer)f(x{sub('i')})+2Σ(i=even interger)f(x{sub('i')})+f(x{sub('n')}))/3 where h is step size:(x{sub('n')}-{sub('0')})/n and n is no. of segment(n should be even integer) ]"]
    theory=theory+[f"Formula used for error is : |((x{sub('n')}-x{sub('0')})/180)x(h{super('4')}d{super('4')}f/dx{super('4')})|{sub('max')} where h is step size (final limit-initial limit)/no. of division"]
    theory=theory+[f"Simpson's 1/3rd rule is an extension of the trapezoidal rule in which the integrand is approximated by a second-order polynomial. Simpson rule can be derived from the various way using Newton's divided difference polynomial,  Lagrange polynomial and the method of coefficients."]
    theory=theory+[f"Example 1: 1/(2x+3) with limits form 0 to 1 => input function is: 1/(2*x+3)"]
    theory=theory+[f"Example 2 : x{super('2')}+2sin(x)+cosx with limits from 0 to 1 and no. of division(n)=10 => Input function is: cos(x)+2*sin(x)+x**2 "]
    return theory