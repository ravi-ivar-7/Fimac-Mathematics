from sympy import *
from numpy import pi

from core.theory_core import sub,super

r=round
(x, y, z) = symbols('x y z')


def trapezoidal_function(result,**kwargs):
    try:
        f=kwargs['f']
        x_i=kwargs['x_i']
        x_n=kwargs['x_n']
        accuracy=kwargs['accuracy']
        no_of_segment=kwargs['no_of_segment']

        step_size = r((abs(x_n-x_i)/no_of_segment),accuracy)
        f_0=r(f.subs(x,x_i),accuracy)
        f_n=r(f.subs(x,x_n),accuracy)
        this_step=[f"Given function is {f} with initial limit(a) = {x_i} and final limit(b)= {x_n}"]
        all_step=[]
        all_step.append(this_step)
        this_step=[f"Value of f(a)={f_0} and f(b)= {f_n}"]
        all_step.append(this_step)
        this_step=[f"Now, we will be using the trapezoidal formula as ∫f(x)= I =h/2[f(a)+2Σ(i=1 to n-1)f(x{sub('i')})+f(b)] , where h is step size and is equal to {step_size}"]
        all_step.append(this_step)
        f_i_sum=0
        step_row=[]
        this_row=[x_i,f_0]
        all_row=[]
        all_row.append(this_row)
        for i in range(1, no_of_segment):
            x_i=r((step_size+x_i),accuracy)
            f_i=r(f.subs(x,x_i),accuracy)
            this_row=[x_i,f_i]
            all_row.append(this_row)
            this_step_row=[f"Value of f({x_i}) = {f_i}"]
            step_row.append(this_step_row)
            f_i_sum=f_i+f_i_sum
        this_row=[x_n,f_n]
        all_row.append(this_row)     
        if no_of_segment>1:
            this_step=[f"Values of function from x= {r(x_i+step_size,accuracy)} to x={r(x_n-step_size,accuracy)} is :"]
            all_step.append(this_step)
            all_step.append(step_row)
            this_step=[f"and sum of above terms is {r(f_i_sum,accuracy)}"]
            all_step.append(this_step)
        this_step=[f"Using above formula, we get I= {step_size}/2[{f_0} + 2x{r(f_i_sum,accuracy)}+ {f_n}]"]
        all_step.append(this_step)
        I=r((step_size/2)*(f_0 + 2*f_i_sum+ f_n),accuracy)
        this_step=[f"which gives value of integral equal to {(I)}"]
        all_step.append(this_step)
        #finding maximum bounded error
        this_step=[f"Now we will try to find maximum bounded error in trapezoidal rule using the formula |((b-a)h{super('2')}(d{super('2')}f(x)/dx{super('2')})/12|{sub('max')}"]
        all_step.append(this_step)
        d2_f=diff(f,x,2)
        this_step=[f"2{super('nd')} derivative of f(x) is {d2_f}"]
        all_step.append(this_step)
        d2_f_max=maximum(d2_f,x)
        d2_f=simplify(d2_f)
        if d2_f_max==oo: #if infinity, then finding maxima on boundary points
            d2_f_max=Max(d2_f.subs(x,x_i),d2_f.subs(x,x_n))
            this_step=[f"It seems maximum values of 2{super('nd')} derivative of function is on boundary points and is equal to {r(d2_f_max,accuracy)}"]
            all_step.append(this_step)
        else:
            this_step=[f"Maximum values of 2{super('nd')} derivative of  f(x) is  equal to {r(d2_f_max,accuracy)}"]
            all_step.append(this_step)
        error_bound=r(abs(((x_n-x_i)/12)*(step_size**2)*d2_f_max),accuracy)
        this_step=[f"Maximum error bound is {error_bound}"]
        all_step.append(this_step)

        result.extend([[['value of ∫f(x) is :',I],['Maximum-bounded error* is :',r(error_bound,accuracy)]],all_step,all_row])
        return result
    
    except Exception as e:
        return result.extend([-1,str(e)])
    

def simpson_3_function(result, **kwargs):

    try:
        f=kwargs['f']
        x_i=kwargs['x_i']
        x_n=kwargs['x_n']
        accuracy=kwargs['accuracy']
        no_of_segment=kwargs['no_of_segment']

        step_size = r((abs(x_n-x_i)/no_of_segment),accuracy)
        f_0=r(f.subs(x,x_i),accuracy)
        f_n=r(f.subs(x,x_n),accuracy)
        this_step=[f"Given function is {f} with initial limit(a) = {x_i} and final limit(b)= {x_n}"]
        all_step=[]
        all_step.append(this_step)
        this_step=[f"Value of f(a)={f_0} and f(b)= {f_n}"]
        all_step.append(this_step)
        this_step=[f"Now, we will be using the Simpson's 1/3 method as ∫f(x)= I = h([f(x{sub('0')})+4Σ(i=odd integer)f(x{sub('i')})+2Σ(i=even interger)f(x{sub('i')})+f(x{sub('n')}))/3 where h is step size:(x{sub('n')}-x{sub('0')})/n ={step_size} and n is no. of segment (n should be even integer)"]
        all_step.append(this_step)   
        this_row=[x_i,f_0]    
        all_row=[]
        all_row.append(this_row)
        step_row=[]
        f_i_sum_even=0
        f_i_sum_odd=0
        for i in range(1,no_of_segment):
            if i%2!=0:#i is odd
                x_i=r(x_i+step_size,accuracy)
                f_i=r(f.subs(x,x_i),accuracy)
                f_i_sum_odd+=f_i
            else:
                x_i=r(x_i+step_size,accuracy)
                f_i=r(f.subs(x,x_i),accuracy)
                f_i_sum_even+=f_i
            this_row=[x_i,f_i]
            all_row.append(this_row)
            this_step_row=[f"Value of f({x_i}) = {f_i}"]
            step_row.append(this_step_row)
        all_step.append(step_row)
        this_step=[f"Value of f(x{sub('i')}) when i odd is {r(f_i_sum_odd,accuracy)} and when i is even is {r(f_i_sum_even,accuracy)}"]   
        all_step.append(this_step)
        I=r((step_size*(f_0+4*f_i_sum_odd+2*f_i_sum_even+f_n)/3),accuracy)
        this_step=[f"Value of integral is  {step_size}/3[{f_0}+4x{r(f_i_sum_odd,accuracy)}+2x{r(f_i_sum_even,accuracy)} +{f_n}]"]
        all_step.append(this_step)
        this_step=[f"which comes out to be {I}"]
        all_step.append(this_step)
        #finding maximum bounded error in simpson rule
        this_step=[f"Now we will try to find maximum bounded error in simpson's 1/3 rule using the formula |((b-a)h{super('4')}(d{super('4')}f(x)/dx{super('4')})/180|{sub('max')}"]
        all_step.append(this_step)

        d4_f=diff(f,x,4)
        d4_f_max=maximum(d4_f,x)
        this_step=[f"Fourth derivative of f(x) is {d4_f}"]
        all_step.append(this_step)       
        d4_f=simplify(d4_f)
        if d4_f_max==oo: #if infinity, then finding maxima on boundary points
            d4_f_max=Max(d4_f.subs(x,x_i),d4_f.subs(x,x_n))
            this_step=[f"Maximum value of 4{super('th')} derivative comes on boundary point and is equal to {r(d4_f_max,accuracy)}"]
            all_step.append(this_step)
        else:
            this_step=[f"Maximum values of 4{super('th')} derivative of  f(x) is  equal to {r(d4_f_max,accuracy)}"]
            all_step.append(this_step)       
        error_bound=r(abs(((x_n-x_i)/180)*(step_size**4)*d4_f_max),accuracy)
        this_step=[f"Maximum error bound is {error_bound}"]
        all_step.append(this_step)

        result.extend([[['value of ∫f(x) is :',I],['Maximum-bounded error* is :',error_bound]],all_step,all_row])
        return result
    
    except Exception as e:
        return result.extend([-1,str(e)])
    

    