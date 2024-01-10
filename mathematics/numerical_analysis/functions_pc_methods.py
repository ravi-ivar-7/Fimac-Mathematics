
from sympy import *
from numpy import pi

from core.theory_core import sub,super

from numerical_analysis.functions_rk_methods import runge_kutta_helper_function

r=round
(x, y, z) = symbols('x y z')


def adams_bashforth_pc_function(result,**kwargs):
    try:
        accuracy=kwargs['accuracy']
        decimal_accuracy=1/(10**accuracy)
        f=kwargs['function']
        initial_y=kwargs['initial_y']
        final_x = kwargs['final_x']
        step_size = kwargs['step_size']
        initial_x = kwargs['initial_x']
        method=kwargs['method']
        iterations=int((final_x-initial_x)/step_size)
        this_step=[f"Given IVP is {kwargs['function']} with initial condition as y({initial_x})={initial_y}"]
        all_step=[]
        all_step.append(this_step)
        this_step=[f"Using the formula of Adams-Bashforth Pridictor-Corrector given below. Let Adams-Bashforth-Predictior -----------eq(P) and Adams-Moulton-Corrector-----------eq(Q)."]
        all_step.append(this_step)
        this_step=[{'link':'/static/theory_images/adam_bashforht_moulton_pc_4_order.jpeg'}]
        all_step.append(this_step)

        if method=='user_input':  #inputed by user
            initial_data=kwargs['user_input']
            this_row=[]
            all_row=initial_data.copy()
            this_step=[f"Initial values [x,y]  provided by you are: {initial_data}"]
            all_step.append(this_step)
        else: #find initial values using one of already present methods
            kwargs['final_x']=3*step_size+initial_x #needs only three iteration

            initial_data=runge_kutta_helper_function(**kwargs)

            if initial_data[0]==-1:
                return [-1,initial_data[1]]
            else:
                initial_data=initial_data[0]
            this_row=[initial_x,initial_y]
            all_row=[]
            all_row=[this_row]+initial_data
            this_step=[f"Initial values [x,y] from the method you selected are as follows : {all_row}"]
            all_step.append(this_step)
        count=1
        for i in range(iterations-3):
            y_j_3=all_row[-1][1]
            y_j_2=all_row[-2][1]
            y_j_1=all_row[-3][1]
            y_j_0=all_row[-4][1]

            x_j_3=all_row[-1][0]
            x_j_2=all_row[-2][0]
            x_j_1=all_row[-3][0]
            x_j_0=all_row[-4][0]

            #predicted value
            y_j_4_p=r(y_j_3+(step_size/24)*(55*(f.subs([(x,x_j_3),(y,y_j_3)]))-59*(f.subs([(x,x_j_2),(y,y_j_2)]))+37*(f.subs([(x,x_j_1),(y,y_j_1)]))-9*(f.subs([(x,x_j_0),(y,y_j_0)]))),accuracy)
            this_step=[f"_________________________________________________________________________________________________"]
            all_step.append(this_step)

            this_step=[f"Now, We will calculate predicted value at x= {r(x_j_3+step_size,accuracy)} , using formula (P). Putting required values of f{sub(str(i))} =  f{r(x_j_0,accuracy),r(y_j_0,accuracy)} = {r(f.subs([(x,x_j_0),(y,y_j_0)]),accuracy)}; f{sub(str(i+1))}= f{r(x_j_1,accuracy),r(y_j_1,accuracy)}= {r(f.subs([(x,x_j_1),(y,y_j_1)]),accuracy)}; f{sub(str(i+2))} = f{r(x_j_2,accuracy),r(y_j_2,accuracy)} = {r(f.subs([(x,x_j_2),(y,y_j_2)]),accuracy)}; f{sub(str(i+3))} = f{r(x_j_3,accuracy),r(y_j_3,accuracy)} = {r(f.subs([(x,x_j_3),(y,y_j_3)]),accuracy)} in (P), we get predicted value y{super('p')}(x = {r(x_j_3+step_size,accuracy)}) = {y_j_4_p}"]
            all_step.append(this_step)
            #corrector
            y_j_4_c=r(y_j_3+(step_size/24)*(9*(f.subs([(x,x_j_3+step_size),(y,y_j_4_p)]))+ 19*(f.subs([(x,x_j_3),(y,y_j_3)]))-5*(f.subs([(x,x_j_2),(y,y_j_2)]))+(f.subs([(x,x_j_1),(y,y_j_1)]))),accuracy)

            this_step=[f"For iteration {count} of corrector , we will be using above predicted value in corrector (C), we get required vaules as f{sub(str(i+1))}= f{r(x_j_1,accuracy),r(y_j_1,accuracy)} = {r(f.subs([(x,x_j_1),(y,y_j_1)]),accuracy)}; f{sub(str(i+2))} = f{r(x_j_2,accuracy),r(y_j_2,accuracy)} = {r(f.subs([(x,x_j_2),(y,y_j_2)]),accuracy)}; f{sub(str(i+3))} = f{r(x_j_3,accuracy),r(y_j_3,accuracy)} = {r(f.subs([(x,x_j_3),(y,y_j_3)]),accuracy)}; f{sub(str(i+4))} = f{r(x_j_3+step_size,accuracy),r(y_j_4_p,accuracy)} = {r(f.subs([(x,x_j_3+step_size),(y,y_j_4_p)]),accuracy)}  and value of first iteration of corrector y{super('c')}(x = {r(x_j_3+step_size,accuracy)}) = y{sub(str(i+4))} = {y_j_4_c}"]
            all_step.append(this_step)

            while abs(y_j_4_p-y_j_4_c)>decimal_accuracy:
                this_step=[f"Since in iteration {count} for corrector at x= {r(x_j_3+step_size,accuracy)} , absolute difference between two successive corrected value i.e. {y_j_4_c} and {y_j_4_p} = {abs(y_j_4_p-y_j_4_c)} > {decimal_accuracy} . So we repeat for same value of x= {r(x_j_3+step_size,accuracy)} but using new corrected value for f{sub(str(i+4))}= f({r(x_j_3+step_size,accuracy),r(y_j_4_c,accuracy)}) = {r(f.subs([(x,x_j_3+step_size),(y,y_j_4_p)]),accuracy)} in formula (C) , while values of other requied f(x,y) remains same."]
                all_step.append(this_step)
                y_j_4_p=y_j_4_c
                #new corrector value
                y_j_4_c=r(y_j_3+(step_size/24)*(9*(f.subs([(x,x_j_3+step_size),(y,y_j_4_p)]))+ 19*(f.subs([(x,x_j_3),(y,y_j_3)]))-5*(f.subs([(x,x_j_2),(y,y_j_2)]))+(f.subs([(x,x_j_1),(y,y_j_1)]))),accuracy)
                count=count+1
                this_step=[f"In iteration {count} , we get new corrected value y{super('c')}(x = {r(x_j_3+step_size,accuracy)}) =    y{sub(str(i+4))} = {y_j_4_c} ."]
                all_step.append(this_step)


            if abs(y_j_4_p-y_j_4_c)<=decimal_accuracy:
                this_row=[r((x_j_3+step_size),accuracy),r(y_j_4_c,accuracy)]
                all_row.append(this_row)
                this_step=[f"Now, in iteration {count} for corrector at x= {r(x_j_3+step_size,accuracy)} , we get absolute difference between {y_j_4_c} and {y_j_4_p} = {abs(y_j_4_p-y_j_4_c)} <= {decimal_accuracy} . So, finally we have value of y{sub(str(i+4))} = y({r(x_j_3+step_size,accuracy)}) = {y_j_4_c}"]
                all_step.append(this_step)
                count=1
        this_step=[f"Above are some steps which are involved during solving Adams-Bashforth P-C methods."]
        all_step.append(this_step)
       
        return result.extend([all_row, all_step]) 
    except Exception as e:
        return result.extend([-1,str(e)])

def milve_adams_pc_function(result, **kwargs):
    try:
        accuracy=kwargs['accuracy']
        decimal_accuracy=1/(10**accuracy)
        f=kwargs['function']
        initial_y=kwargs['initial_y']
        final_x = kwargs['final_x']
        step_size = kwargs['step_size']
        initial_x = kwargs['initial_x']
        method=kwargs['method']
        iterations=int((final_x-initial_x)/step_size)
        this_step=[f"Given IVP is {kwargs['function']} with initial condition as y({initial_x})={initial_y}"]
        all_step=[]
        all_step.append(this_step)
        this_step=[f"Using the formula of Adams-Milve Pridictor-Corrector given below. Let Adams-Bashforth-Predictior -----------eq(P) and Adams-Milve-Corrector-----------eq(Q)."]
        all_step.append(this_step)
        this_step=[{'link':'/static/theory_images/milve_adams_pc_4_order.jpeg'}]
        all_step.append(this_step)
        if method=='user_input':  #inputed by user
            initial_data=kwargs['user_input']
            this_row=[]
            all_row=initial_data.copy()
            this_step=[f"Initial values [x,y]  provided by you are: {initial_data}"]
            all_step.append(this_step)
        else: #find initial values using one of already present methods
            kwargs['final_x']=3*step_size+initial_x #needs only three iteration
            initial_data=runge_kutta_helper_function(**kwargs)
            if initial_data[0]==-1:
                return [-1,initial_data[1]]
            else:
                initial_data=initial_data[0]
            this_row=[initial_x,initial_y]
            all_row=[]
            all_row=[this_row]+initial_data
            this_step=[f"Initial values [x,y] from the method you selected are as follows : {all_row}"]
            all_step.append(this_step)
        count=1
        for i in range(iterations-3):
            y_j_3=all_row[-1][1]
            y_j_2=all_row[-2][1]
            y_j_1=all_row[-3][1]
            y_j_0=all_row[-4][1]
            x_j_3=all_row[-1][0]
            x_j_2=all_row[-2][0]
            x_j_1=all_row[-3][0]
            x_j_0=all_row[-4][0]
            #predicted value
            y_j_4_p=r(y_j_0+((4*step_size)/3)*(2*(f.subs([(x,x_j_3),(y,y_j_3)]))-(f.subs([(x,x_j_2),(y,y_j_2)]))+2*(f.subs([(x,x_j_1),(y,y_j_1)]))),accuracy)
            this_step=[f"_________________________________________________________________________________________________"]
            all_step.append(this_step)
            this_step=[f"Now, We will calculate predicted value at x= {r(x_j_3+step_size,accuracy)} , using formula (P). Putting required values of f{sub(str(i+1))}= f{r(x_j_1,accuracy),r(y_j_1,accuracy)}= {r(f.subs([(x,x_j_1),(y,y_j_1)]),accuracy)}; f{sub(str(i+2))} = f{r(x_j_2,accuracy),r(y_j_2,accuracy)} = {r(f.subs([(x,x_j_2),(y,y_j_2)]),accuracy)}; f{sub(str(i+3))} = f{r(x_j_3,accuracy),r(y_j_3,accuracy)} = {r(f.subs([(x,x_j_3),(y,y_j_3)]),accuracy)} in (P), we get predicted value y{super('p')}(x = {r(x_j_3+step_size,accuracy)}) = {y_j_4_p}"]
            all_step.append(this_step)
            #corrector
            y_j_4_c=r(y_j_2+(step_size/3)*((f.subs([(x,x_j_3+step_size),(y,y_j_4_p)]))+4*(f.subs([(x,x_j_3),(y,y_j_3)]))+(f.subs([(x,x_j_2),(y,y_j_2)]))),accuracy)
            this_step=[f"For iteration {count} of corrector , we will be using above predicted value in corrector (C), we get required vaules as f{sub(str(i+2))} = f{r(x_j_2,accuracy),r(y_j_2,accuracy)} = {r(f.subs([(x,x_j_2),(y,y_j_2)]),accuracy)}; f{sub(str(i+3))} = f{r(x_j_3,accuracy),r(y_j_3,accuracy)} = {r(f.subs([(x,x_j_3),(y,y_j_3)]),accuracy)}; f{sub(str(i+4))} = f{r(x_j_3+step_size,accuracy),r(y_j_4_p,accuracy)} = {r(f.subs([(x,x_j_3+step_size),(y,y_j_4_p)]),accuracy)}  and value of first iteration of corrector y{super('c')}(x = {r(x_j_3+step_size,accuracy)}) = y{sub(str(i+4))} = {y_j_4_c}"]
            all_step.append(this_step)
            while abs(y_j_4_p-y_j_4_c)>decimal_accuracy:
                this_step=[f"Since in iteration {count} for corrector at x= {r(x_j_3+step_size,accuracy)} , absolute difference between two successive corrected value i.e. {y_j_4_c} and {y_j_4_p} = {abs(y_j_4_p-y_j_4_c)} > {decimal_accuracy} . So we repeat for same value of x= {r(x_j_3+step_size,accuracy)} but using new corrected value for f{sub(str(i+4))}= f({r(x_j_3+step_size,accuracy),r(y_j_4_c,accuracy)}) = {r(f.subs([(x,x_j_3+step_size),(y,y_j_4_p)]),accuracy)} in formula (C) , while values of other requied f(x,y) remains same."]
                all_step.append(this_step)
                y_j_4_p=y_j_4_c
                #new corrector value
                y_j_4_c=r(y_j_2+(step_size/3)*((f.subs([(x,x_j_3+step_size),(y,y_j_4_p)]))+4*(f.subs([(x,x_j_3),(y,y_j_3)]))+(f.subs([(x,x_j_2),(y,y_j_2)]))),accuracy)
                count=count+1
                this_step=[f"In iteration {count} , we get new corrected value y{super('c')}(x = {r(x_j_3+step_size,accuracy)}) =    y{sub(str(i+4))} = {y_j_4_c} ."]
                all_step.append(this_step)
            if abs(y_j_4_p-y_j_4_c)<=decimal_accuracy:
                this_row=[r((x_j_3+step_size),accuracy),r(y_j_4_c,accuracy)]
                all_row.append(this_row)
                this_step=[f"Now, in iteration {count} of corrector at x= {r(x_j_3+step_size,accuracy)} , we get absolute difference between {y_j_4_c} and {y_j_4_p} = {abs(y_j_4_p-y_j_4_c)} <= {decimal_accuracy} . So, finally we have value of y{sub(str(i+4))} = y({r(x_j_3+step_size,accuracy)}) = {y_j_4_c}"]
                all_step.append(this_step)
                count=1
        this_step=[f"Above are some steps which are involved during solving Adams-Bashforth P-C methods."]
        all_step.append(this_step)

        return result.extend([all_row, all_step]) 
    except Exception as e:
        return result.extend([-1,str(e)])
