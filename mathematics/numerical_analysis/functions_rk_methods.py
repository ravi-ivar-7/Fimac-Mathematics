from sympy import *

r=round
timeout=20
accuracy=5
custom_config = {'displaylogo':False}
(x, y, z) = symbols('x y z')

from core.theory_core import sub

def individual_runge_kutta_function(result,**kwargs): #this function is for all  runge kutta types individually
    try:
        accuracy=kwargs['accuracy']
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
        x_j=initial_x #will be same for all methods
        this_row=[]
        all_row=[]

        if(method=='euler'): #eulers forward method
            e_y_j=initial_y
            this_step=[f"Using eulers forward method,  y{sub('i+1')}=y{sub('i')}+hf(x{sub('i')},y(x{sub('i')})) -------eq(1)"]
            all_step.append(this_step)

            for i in range(iterations):
                this_step=[f"for x= {x_j}, y{sub(str(i))}= {e_y_j} and value of f({x_j,e_y_j}) is {r(f.subs([(x,x_j),(y,e_y_j)]),accuracy)} "]
                all_step.append(this_step)
                e_y_j_1=r((e_y_j+step_size*(f.subs([(x,x_j),(y,e_y_j)]))),accuracy)
                x_j=r((x_j+step_size),accuracy)
                this_step=[f"Putting above values in eq(1), we get y{sub(str(i+1))} = y({x_j}) = {e_y_j_1}"]
                all_step.append(this_step)
                this_row=[x_j,e_y_j_1]
                all_row.append(this_row) 
                e_y_j=e_y_j_1

        if(method=='cauchy'): #euler cauchy or rk 2nd order method
            ec_y_j=initial_y
            this_step=[f"Using eulers cauchy method,  y{sub('i+1')}=y{sub('i')}+(h/2)[f(x{sub('i')},y(x{sub('i')}))+f(x{sub('i+1')},y(x{sub('i+1')}))] and  y{sub('i+1')} is found using euler forward method i.e. y{sub('i+1')}=y{sub('i')}+hf(x{sub('i')},y(x{sub('i')})) -------eq(1)"]
            
            for i in range(iterations):
                this_step=[f"for x{sub(str(i))}= {x_j}, y{sub(str(i))}= {ec_y_j}. Value of f(x{sub(str(i))},y{sub(str(i))}) is {r(f.subs([(x,x_j),(y,ec_y_j)]),accuracy)} and f(x{sub(str(i+1))},y{sub(str(i+1))}) using euler forward method is {r(f.subs([(x,x_j+step_size),(y,ec_y_j+step_size*(f.subs([(x,x_j),(y,ec_y_j)])))]),accuracy)}"]
                all_step.append(this_step)
                ec_y_j_1=r((ec_y_j+(step_size/2)*(f.subs([(x,x_j),(y,ec_y_j)])+f.subs([(x,x_j+step_size),(y,ec_y_j+step_size*(f.subs([(x,x_j),(y,ec_y_j)])))]))),accuracy)
                x_j=r((x_j+step_size),accuracy)
                ec_y_j=ec_y_j_1
                this_step=[f"Putting above values in eq(1), we get y{sub(str(i+1))}= y({x_j})= {ec_y_j_1}"]
                all_step.append(this_step)
                this_row=[x_j,ec_y_j_1]
                all_row.append(this_row) 

        if(method=='classical'):#Runge Kutta Classical 4 th order Method
            c_y_j=initial_y
            this_step=[f"Using Runge Kutta Classical 4{sub('th')} order Method, -------eq(1), [formula for this method is given above in 'Theory Realted To Method'.]"]
            all_step.append(this_step)

            for i in range(iterations):
                c_k1=step_size*f.subs([(x,x_j),(y,c_y_j)])  
                c_k2=step_size*f.subs([(x,x_j+step_size/2),(y,c_y_j+c_k1/2)])
                c_k3=step_size*f.subs([(x,x_j+step_size/2),(y,c_y_j+c_k2/2)])
                c_k4=step_size*f.subs([(x,x_j+step_size),(y,c_y_j+c_k3)])
                this_step=[f"For x{sub(str(i))}={x_j} and y{sub(str(i))} = {c_y_j}, we get values of k{sub('1')}= {r(c_k1,accuracy)}, k{sub('2')}= {r(c_k2,accuracy)}, k{sub('3')}= {r(c_k3,accuracy)} ,k{sub('4')}= {r(c_k4,accuracy)}"]
                all_step.append(this_step)                
                c_y_j_one=r((c_y_j+(1/6)*(c_k1+2*c_k2+2*c_k3+c_k4)),accuracy)
                x_j=r((x_j+step_size),accuracy)
                this_step=[f"Putting values of k{sub('1')}, k{sub('2')}, k{sub('3')}, k{sub('4')}, we get value of y({x_j})= y{sub(str(i+1))} = {c_y_j_one}"]
                all_step.append(this_step)
                c_y_j=c_y_j_one                
                this_row=[x_j,c_y_j_one]
                all_row.append(this_row)

        if(method=='gills'):#Runge Kutta Gill Method
            g_y_j=initial_y
            this_step=[f"Using Runge Kutta Gills 4{sub('th')} order Method, -------eq(1), [formula for this method is given above in 'Theory Realted To Method'.]"]
            all_step.append(this_step)

            for i in range(iterations):
                g_k1=step_size*f.subs([(x,x_j),(y,g_y_j)])       
                g_k2=step_size*f.subs([(x,x_j+step_size/2),(y,g_y_j+g_k1/2)])
                g_k3=step_size*f.subs([(x,x_j+step_size/2),(y,g_y_j+((2-2**0.5)/2)*g_k2+((2**0.5-1)/2)*g_k1)])
                g_k4=step_size*f.subs([(x,x_j+step_size),(y,g_y_j+((-2**0.5)/2)*g_k2+((2**0.5+2)/2)*g_k3)])
                g_y_j_one=r((g_y_j+(1/6)*(g_k1+(2-2**0.5)*g_k2+(2+2**0.5)*g_k3+g_k4)),accuracy)
                this_step=[f"For x{sub(str(i))}={x_j} and y{sub(str(i))} ={g_y_j}, we get values of k{sub('1')}= {r(g_k1,accuracy)}, k{sub('2')}= {r(g_k2,accuracy)}, k{sub('3')}= {r(g_k3,accuracy)} ,k{sub('4')}= {r(g_k4,accuracy)}"]
                all_step.append(this_step)
                x_j=r((x_j+step_size),accuracy)
                this_step=[f"Putting values of k{sub('1')}, k{sub('2')}, k{sub('3')}, k{sub('4')}, we get value of y({x_j})= y{sub(str(i+1))} = {g_y_j_one}"]
                all_step.append(this_step)
                g_y_j=g_y_j_one                
                this_row=[x_j,g_y_j_one]
                all_row.append(this_row)     

        if(method=='fehlberg'):#Runge Kutta Fehlberg Method
            if_y_j=initial_y
            this_step=[f"Using Runge Kutta Fehlberg  4{sub('th')} order Method, -------eq(1), [formula for this method is given above in 'Theory Realted To Method'.]"]
            all_step.append(this_step)

            for i in range(iterations):
                if_k1=step_size*f.subs([(x,x_j),(y,if_y_j)])                
                if_k2=step_size*f.subs([(x,x_j+step_size/4),(y,if_y_j+if_k1/4)])
                if_k3=step_size*f.subs([(x,x_j+(3/8)*step_size),(y,if_y_j+(9/32)*if_k2+(3/32)*if_k1)])
                if_k4=step_size*f.subs([(x,x_j+(12/13)*step_size),(y,if_y_j+(1932/2197)*if_k1+(-7200/2197)*if_k2+(7296/2197)*if_k3)])
                if_k5=step_size*f.subs([(x,x_j+step_size),(y,if_y_j+(439/216)*if_k1-8*if_k2+(3680/513)*if_k3-(845/4104)*if_k4)]) 
                f_y_j_one=r((if_y_j+(25/216)*if_k1+(1408/2565)*if_k3+(2197/4104)*if_k4+(-1/5)*if_k5),accuracy)
                if_y_j=f_y_j_one              
                this_step=[f"For x{sub(str(i))}={x_j} and y{sub(str(i))}={if_y_j}, we get values of k{sub('1')}= {r(if_k1,accuracy)}, k{sub('2')}= {r(if_k2,accuracy)}, k{sub('3')}= {r(if_k3,accuracy)} ,k{sub('4')}= {r(if_k4,accuracy)}, k{sub('5')}= {r(if_k5,accuracy)}"]
                all_step.append(this_step)               
                this_step=[f"Putting values of k{sub('1')}, k{sub('2')}, k{sub('3')}, k{sub('4')}, and k{sub('5')} in eq(1), we get value of y({r((x_j+step_size),accuracy)})= y{sub(str(i+1))} = {f_y_j_one}"]
                all_step.append(this_step)
                x_j=r((x_j+step_size),accuracy)                   
                this_row=[x_j,f_y_j_one]
                all_row.append(this_row)                   

        result.extend([all_row, all_step])

    except Exception as e:
        result.extend([-1, str(e)])

    return result
    


def all_runge_kutta_function(result, **kwargs):
    try:
        accuracy=kwargs['accuracy']
        f=kwargs['function']
        initial_y=kwargs['initial_y']
        final_x = kwargs['final_x']
        step_size = kwargs['step_size']
        initial_x = kwargs['initial_x']
        iterations=int((final_x-initial_x)/step_size)
        x_j=initial_x
        c_y_j=initial_y
        ec_y_j=initial_y
        g_y_j=initial_y
        f_y_j=initial_y
        if_y_j=initial_y
        this_row=[]
        all_row=[]
        while iterations:
            #Runge Kutta Classical 4 th order Method
            c_k1=step_size*f.subs([(x,x_j),(y,c_y_j)])
            c_k2=step_size*f.subs([(x,x_j+step_size/2),(y,c_y_j+c_k1/2)])
            c_k3=step_size*f.subs([(x,x_j+step_size/2),(y,c_y_j+c_k2/2)])
            c_k4=step_size*f.subs([(x,x_j+step_size),(y,c_y_j+c_k3)])
            c_y_j_one=r((c_y_j+(1/6)*(c_k1+2*c_k2+2*c_k3+c_k4)),accuracy)
            c_y_j=c_y_j_one
            #Runge Kutta Gill Method
            g_k1=step_size*f.subs([(x,x_j),(y,g_y_j)])       
            g_k2=step_size*f.subs([(x,x_j+step_size/2),(y,g_y_j+g_k1/2)])
            g_k3=step_size*f.subs([(x,x_j+step_size/2),(y,g_y_j+((2-2**0.5)/2)*g_k2+((2**0.5-1)/2)*g_k1)])
            g_k4=step_size*f.subs([(x,x_j+step_size),(y,g_y_j+((-2**0.5)/2)*g_k2+((2**0.5+2)/2)*g_k3)])
            g_y_j_one=r((g_y_j+(1/6)*(g_k1+(2-2**0.5)*g_k2+(2+2**0.5)*g_k3+g_k4)),accuracy)
            g_y_j=g_y_j_one
            #Runge Kutta Fehlberg Method and its improved version
            if_k1=step_size*f.subs([(x,x_j),(y,if_y_j)])                
            if_k2=step_size*f.subs([(x,x_j+step_size/4),(y,if_y_j+if_k1/4)])
            if_k3=step_size*f.subs([(x,x_j+(3/8)*step_size),(y,if_y_j+(9/32)*if_k2+(3/32)*if_k1)])
            if_k4=step_size*f.subs([(x,x_j+(12/13)*step_size),(y,if_y_j+(1932/2197)*if_k1+(-7200/2197)*if_k2+(7296/2197)*if_k3)])
            if_k5=step_size*f.subs([(x,x_j+step_size),(y,if_y_j+(439/216)*if_k1-8*if_k2+(3680/513)*if_k3-(845/4104)*if_k4)])         
            #k6 is for its improved version doubtful
            k6=step_size*f.subs([(x,x_j+step_size/2),(y,if_y_j-(8/27)*if_k1+2*if_k2+(-3544/2565)*if_k3+(1859/4104)*if_k4+(-11/40)*if_k5)])
            if_y_j_one=r((if_y_j+(16/135)*if_k1+(6656/12825)*if_k3+(2856/56430)*if_k4+(-9/50)*if_k5+(2/55)*k6),accuracy)
            if_y_j=if_y_j_one 
            #fehlberg method            
            f_y_j_one=r((f_y_j+(25/216)*if_k1+(1408/2565)*if_k3+(2197/4104)*if_k4+(-1/5)*if_k5),accuracy)
            f_y_j=f_y_j_one  
            #euler cauchy or rk 2nd order method
            ec_y_j_1=r((ec_y_j+(step_size/2)*(f.subs([(x,x_j),(y,ec_y_j)])+f.subs([(x,x_j+step_size),(y,ec_y_j+step_size*(f.subs([(x,x_j),(y,ec_y_j)])))]))),accuracy)
            x_j=r((x_j+step_size),accuracy)
            ec_y_j=ec_y_j_1
            iterations-=1
            this_row=[x_j,ec_y_j,c_y_j,g_y_j,f_y_j]
            all_row.append(this_row)

        return result.extend(all_row)
    
    except Exception as e:
        return result.extend([-1,str(e)])
  


def runge_kutta_helper_function(**kwargs): #this function is for use in multistep and pc methods as a helper functions
    try:
        accuracy=kwargs['accuracy']
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
        x_j=initial_x #will be same for all methods
        this_row=[]
        all_row=[]
        

        if(method=='euler'): #eulers forward method
            e_y_j=initial_y
            this_step=[f"Using eulers forward method,  y{sub('i+1')}=y{sub('i')}+hf(x{sub('i')},y(x{sub('i')})) -------eq(1)"]
            all_step.append(this_step)

            for i in range(iterations):
                this_step=[f"for x= {x_j}, y{sub(str(i))}= {e_y_j} and value of f({x_j,e_y_j}) is {r(f.subs([(x,x_j),(y,e_y_j)]),accuracy)} "]
                all_step.append(this_step)
                e_y_j_1=r((e_y_j+step_size*(f.subs([(x,x_j),(y,e_y_j)]))),accuracy)
                x_j=r((x_j+step_size),accuracy)
                this_step=[f"Putting above values in eq(1), we get y{sub(str(i+1))} = y({x_j}) = {e_y_j_1}"]
                all_step.append(this_step)
                this_row=[x_j,e_y_j_1]
                all_row.append(this_row) 
                e_y_j=e_y_j_1

        if(method=='cauchy'): #euler cauchy or rk 2nd order method
            ec_y_j=initial_y
            this_step=[f"Using eulers cauchy method,  y{sub('i+1')}=y{sub('i')}+(h/2)[f(x{sub('i')},y(x{sub('i')}))+f(x{sub('i+1')},y(x{sub('i+1')}))] and  y{sub('i+1')} is found using euler forward method i.e. y{sub('i+1')}=y{sub('i')}+hf(x{sub('i')},y(x{sub('i')})) -------eq(1)"]
            
            for i in range(iterations):
                this_step=[f"for x{sub(str(i))}= {x_j}, y{sub(str(i))}= {ec_y_j}. Value of f(x{sub(str(i))},y{sub(str(i))}) is {r(f.subs([(x,x_j),(y,ec_y_j)]),accuracy)} and f(x{sub(str(i+1))},y{sub(str(i+1))}) using euler forward method is {r(f.subs([(x,x_j+step_size),(y,ec_y_j+step_size*(f.subs([(x,x_j),(y,ec_y_j)])))]),accuracy)}"]
                all_step.append(this_step)
                ec_y_j_1=r((ec_y_j+(step_size/2)*(f.subs([(x,x_j),(y,ec_y_j)])+f.subs([(x,x_j+step_size),(y,ec_y_j+step_size*(f.subs([(x,x_j),(y,ec_y_j)])))]))),accuracy)
                x_j=r((x_j+step_size),accuracy)
                ec_y_j=ec_y_j_1
                this_step=[f"Putting above values in eq(1), we get y{sub(str(i+1))}= y({x_j})= {ec_y_j_1}"]
                all_step.append(this_step)
                this_row=[x_j,ec_y_j_1]
                all_row.append(this_row) 

        if(method=='classical'):#Runge Kutta Classical 4 th order Method
            c_y_j=initial_y
            this_step=[f"Using Runge Kutta Classical 4{sub('th')} order Method, -------eq(1), [formula for this method is given above in 'Theory Realted To Method'.]"]
            all_step.append(this_step)

            for i in range(iterations):
                c_k1=step_size*f.subs([(x,x_j),(y,c_y_j)])  
                c_k2=step_size*f.subs([(x,x_j+step_size/2),(y,c_y_j+c_k1/2)])
                c_k3=step_size*f.subs([(x,x_j+step_size/2),(y,c_y_j+c_k2/2)])
                c_k4=step_size*f.subs([(x,x_j+step_size),(y,c_y_j+c_k3)])
                this_step=[f"For x{sub(str(i))}={x_j} and y{sub(str(i))} = {c_y_j}, we get values of k{sub('1')}= {r(c_k1,accuracy)}, k{sub('2')}= {r(c_k2,accuracy)}, k{sub('3')}= {r(c_k3,accuracy)} ,k{sub('4')}= {r(c_k4,accuracy)}"]
                all_step.append(this_step)                
                c_y_j_one=r((c_y_j+(1/6)*(c_k1+2*c_k2+2*c_k3+c_k4)),accuracy)
                x_j=r((x_j+step_size),accuracy)
                this_step=[f"Putting values of k{sub('1')}, k{sub('2')}, k{sub('3')}, k{sub('4')}, we get value of y({x_j})= y{sub(str(i+1))} = {c_y_j_one}"]
                all_step.append(this_step)
                c_y_j=c_y_j_one                
                this_row=[x_j,c_y_j_one]
                all_row.append(this_row)

        if(method=='gills'):#Runge Kutta Gill Method
            g_y_j=initial_y
            this_step=[f"Using Runge Kutta Gills 4{sub('th')} order Method, -------eq(1), [formula for this method is given above in 'Theory Realted To Method'.]"]
            all_step.append(this_step)

            for i in range(iterations):
                g_k1=step_size*f.subs([(x,x_j),(y,g_y_j)])       
                g_k2=step_size*f.subs([(x,x_j+step_size/2),(y,g_y_j+g_k1/2)])
                g_k3=step_size*f.subs([(x,x_j+step_size/2),(y,g_y_j+((2-2**0.5)/2)*g_k2+((2**0.5-1)/2)*g_k1)])
                g_k4=step_size*f.subs([(x,x_j+step_size),(y,g_y_j+((-2**0.5)/2)*g_k2+((2**0.5+2)/2)*g_k3)])
                g_y_j_one=r((g_y_j+(1/6)*(g_k1+(2-2**0.5)*g_k2+(2+2**0.5)*g_k3+g_k4)),accuracy)
                this_step=[f"For x{sub(str(i))}={x_j} and y{sub(str(i))} ={g_y_j}, we get values of k{sub('1')}= {r(g_k1,accuracy)}, k{sub('2')}= {r(g_k2,accuracy)}, k{sub('3')}= {r(g_k3,accuracy)} ,k{sub('4')}= {r(g_k4,accuracy)}"]
                all_step.append(this_step)
                x_j=r((x_j+step_size),accuracy)
                this_step=[f"Putting values of k{sub('1')}, k{sub('2')}, k{sub('3')}, k{sub('4')}, we get value of y({x_j})= y{sub(str(i+1))} = {g_y_j_one}"]
                all_step.append(this_step)
                g_y_j=g_y_j_one                
                this_row=[x_j,g_y_j_one]
                all_row.append(this_row)     

        if(method=='fehlberg'):#Runge Kutta Fehlberg Method
            if_y_j=initial_y
            this_step=[f"Using Runge Kutta Fehlberg  4{sub('th')} order Method, -------eq(1), [formula for this method is given above in 'Theory Realted To Method'.]"]
            all_step.append(this_step)

            for i in range(iterations):
                if_k1=step_size*f.subs([(x,x_j),(y,if_y_j)])                
                if_k2=step_size*f.subs([(x,x_j+step_size/4),(y,if_y_j+if_k1/4)])
                if_k3=step_size*f.subs([(x,x_j+(3/8)*step_size),(y,if_y_j+(9/32)*if_k2+(3/32)*if_k1)])
                if_k4=step_size*f.subs([(x,x_j+(12/13)*step_size),(y,if_y_j+(1932/2197)*if_k1+(-7200/2197)*if_k2+(7296/2197)*if_k3)])
                if_k5=step_size*f.subs([(x,x_j+step_size),(y,if_y_j+(439/216)*if_k1-8*if_k2+(3680/513)*if_k3-(845/4104)*if_k4)]) 
                f_y_j_one=r((if_y_j+(25/216)*if_k1+(1408/2565)*if_k3+(2197/4104)*if_k4+(-1/5)*if_k5),accuracy)
                if_y_j=f_y_j_one              
                this_step=[f"For x{sub(str(i))}={x_j} and y{sub(str(i))}={if_y_j}, we get values of k{sub('1')}= {r(if_k1,accuracy)}, k{sub('2')}= {r(if_k2,accuracy)}, k{sub('3')}= {r(if_k3,accuracy)} ,k{sub('4')}= {r(if_k4,accuracy)}, k{sub('5')}= {r(if_k5,accuracy)}"]
                all_step.append(this_step)               
                this_step=[f"Putting values of k{sub('1')}, k{sub('2')}, k{sub('3')}, k{sub('4')}, and k{sub('5')} in eq(1), we get value of y({r((x_j+step_size),accuracy)})= y{sub(str(i+1))} = {f_y_j_one}"]
                all_step.append(this_step)
                x_j=r((x_j+step_size),accuracy)                   
                this_row=[x_j,f_y_j_one]
                all_row.append(this_row)                   

        result= [all_row, all_step]

    except Exception as e:
        result= [-1, str(e)]

    return result