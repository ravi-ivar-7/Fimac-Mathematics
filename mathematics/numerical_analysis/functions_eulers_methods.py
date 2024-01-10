from sympy import *

r=round
timeout=20
accuracy=5
custom_config = {'displaylogo':False}
(x, y, z) = symbols('x y z')

from core.theory_core import super ,sub


import time
def picards_function(result, **kwargs):
    try:
        function = kwargs['function']
        initial_x = kwargs['initial_x']
        initial_y = kwargs['initial_y']
        final_x = kwargs['final_x']
        iterations = kwargs['iterations']

        all_steps = []

        all_steps.append([f"Given IVP is {function} with initial condition as y({initial_x})={initial_y}"])
        this_step=[f"Now using the picard's formula for n{super('th')} approximation y{sub('n+1')}= y{sub('0')} +  ∫f(x,y{sub('n')})dx with limits from a to x."]

        y_0 = initial_y
        y_n_minus_1 = initial_y

        for n in range(iterations):
            fun = function.subs(y, y_n_minus_1)
            integral_value = integrate(fun, (x, initial_x, x))

            all_steps.extend([
                [f"f(x,y{sub(str(n))}) is {fun} and   "],
                [f"∫f(x,y{sub(str(n))}) from limit ({initial_x} to x) is  {integral_value}"],
                [f"Approximation - {n+1} of function is {y_0 + integral_value}"]
            ])

            y_n_minus_1 = y_0 + integral_value

        result.extend(all_steps)
        return result
    except Exception as e:
        result.extend([-1, str(e)])
        return result
    
def eulers_forward_function(result, **kwargs):
    try:
        accuracy = kwargs['accuracy']
        f = kwargs['function']
        y_n = kwargs['initial_y']
        final_x = kwargs['final_x']
        step_size = kwargs['step_size']
        x_n = kwargs['initial_x']
        iterations = int((final_x - x_n) / step_size)

        all_steps = []
        all_rows = []

        all_steps.append([f"Given IVP is {kwargs['function']} with initial condition as y({x_n})={y_n}"])
        all_steps.append([f"Using Euler's forward method,  y{sub('i+1')}=y{sub('i')}+hf(x{sub('i')},y(x{sub('i')})) -------eq(1)"])

        for i in range(iterations):
            f_value = r(f.subs([(x, x_n), (y, y_n)]), accuracy)
            y_n_1=r((y_n + step_size * f_value), accuracy)

            all_steps.extend([
                [f"for x={x_n}, y{sub(str(i))}={y_n} and value of f({x_n},{y_n}) is {f_value}"],
                [f"Putting above values in eq(1), we get y{sub(str(i+1))} = y({r(x_n+step_size,accuracy)}) = {y_n_1}"]
            ])

            x_n = r((x_n + step_size), accuracy)
            y_n = y_n_1
            all_rows.append([x_n, y_n])

        result.extend([all_rows, all_steps])

    except Exception as e:
        result.extend([-1, str(e)])

    return result

def eulers_cauchy_function(result, **kwargs):
    try:
        accuracy = kwargs['accuracy']
        f = kwargs['function']
        y_n = kwargs['initial_y']
        final_x = kwargs['final_x']
        step_size = kwargs['step_size']
        x_n = kwargs['initial_x']
        iterations = int((final_x - x_n) / step_size)

        all_steps = []
        all_rows = []

        all_steps.extend([
            [f"Given IVP is {f} with initial condition as y({x_n})={y_n}"],
            [f"Using Euler's Cauchy method,  y{sub('i+1')}=y{sub('i')}+(h/2)[f(x{sub('i')},y(x{sub('i')}))+f(x{sub('i+1')},y(x{sub('i+1')}))] and  y{sub('i+1')} is found using Euler forward method i.e. y{sub('i+1')}=y{sub('i')}+hf(x{sub('i')},y(x{sub('i')})) -------eq(1)"]
        ])

        for i in range(iterations):
            f_i_value = r(f.subs([(x, x_n), (y, y_n)]), accuracy)
            f_i1_value = r(f.subs([(x, x_n + step_size), (y, y_n + step_size * f_i_value)]), accuracy)

            all_steps.extend([
                [f"for x{sub(str(i))}={x_n}, y{sub(str(i))}={y_n}. Value of f(x{sub(str(i))},y{sub(str(i))}) is {f_i_value} and f(x{sub(str(i+1))},y{sub(str(i+1))}) using Euler forward method is {f_i1_value}"],
                [f"Putting above values in eq(1), we get y{sub(str(i+1))} = y({r((x_n + step_size), accuracy)}) = {r((y_n + (step_size / 2) * (f_i_value + f_i1_value)), accuracy)}"]
            ])

            x_n = r((x_n + step_size), accuracy)
            y_n = r((y_n + (step_size / 2) * (f_i_value + f_i1_value)), accuracy)
            all_rows.append([x_n, y_n])

        result.extend([all_rows, all_steps])

    except Exception as e:
        result.extend([-1, str(e)])

    return result


#not working yet
def taylors_function(**kwargs):
    fun = kwargs['function']
    y_n=kwargs['initial_y']
    x_n=kwargs['initial_x']
    step_size = kwargs['step_size']
    iterations=kwargs['iterations']
    terms=kwargs['terms']
    this_row=[]
    all_row=[]
    while(iterations):
        f=series(fun,x,x_n,terms)
        f=lambdify([x ,y], f)
        y_n_1=f(x_n,y_n)
        x_n=x_n+step_size
        this_row=[round(x_n,4),y_n_1]
        print('this row',this_row)
        all_row.append(this_row)
        iterations-=1

    return all_row