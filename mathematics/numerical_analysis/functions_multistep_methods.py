from sympy import *

r=round
timeout=20
accuracy=5
custom_config = {'displaylogo':False}
(x, y, z) = symbols('x y z')

from core.theory_core import super ,sub
from numerical_analysis.functions_rk_methods import runge_kutta_helper_function


def adams_bashforth_function(result, **kwargs):
    try:
        accuracy=kwargs['accuracy']
        f=kwargs['function']
        initial_y=kwargs['initial_y']
        final_x = kwargs['final_x']
        step_size = kwargs['step_size']
        initial_x = kwargs['initial_x']
        order_of_method=int(kwargs['order_of_method'])
        iterations=int((final_x-initial_x)/step_size)
        this_step=[f"Given IVP is {kwargs['function']} with initial condition as y({initial_x})={initial_y}"]
        all_step=[]
        all_step.append(this_step)
        this_step=[f"Using the formula of {order_of_method}-order of Adams-Bashforth given above in 'Theory Related To Method' ------eq(1)"]
        all_step.append(this_step)
        kwargs['final_x']=3*step_size+initial_x
        initial_data=runge_kutta_helper_function(**kwargs)

        if initial_data[0]==-1:
            return [-1,initial_data[1]]
        else:
            initial_data=initial_data[0]
        this_row=[initial_x,initial_y]
        all_row=[]
        all_row=[this_row]+initial_data

        if order_of_method==1: #first order , same as euler forward method
            e_y_j=initial_y
            x_j=initial_x
            all_row=all_row[:1]
            for i in range(iterations):
                    e_y_j_1=r((e_y_j+step_size*(f.subs([(x,x_j),(y,e_y_j)]))),accuracy)
                    this_step=[f"Putting values of x{sub(str(i))}={x_j} and y{sub(str(i))}= {e_y_j} in eq(1), we get y({r(x_j+step_size,accuracy)})= y{sub(str(i+1))}= {e_y_j_1} "]
                    all_step.append(this_step)
                    x_j=r((x_j+step_size),accuracy)
                    this_row=[x_j,e_y_j_1]
                
                    all_row.append(this_row) 
                    e_y_j=e_y_j_1

        if order_of_method==2:
            all_row=all_row[:2]
            this_step=[f"Initial values required for 2{super('nd')} order Adams-Bashforth method are x{sub('0')}= {r(all_row[-2][0],accuracy)}, x{sub('1')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-2][1],accuracy)} and y{sub('1')}= {r(all_row[-1][1],accuracy)}. Refer respective method for detail-solution for initial data."]
            all_step.append(this_step)
            for i in range(iterations-1):
                y_j_1=all_row[-1][1]
                y_j_0=all_row[-2][1]
                x_j_1=all_row[-1][0]
                x_j_0=x_j_1-step_size
                y_j_2=r((y_j_1+(step_size/2)*(3*f.subs([(x,x_j_1),(y,y_j_1)])-f.subs([(x,x_j_0),(y,y_j_0)]))),accuracy)
                this_step=[f"Putting vaues of x{sub(str(i))}= {r(all_row[-2][0],accuracy)}, x{sub(str(i+1))}= {r(all_row[-1][0],accuracy)}, y{sub(str(i))}= {r(all_row[-2][1],accuracy)} and y{sub(str(i+1))}= {r(all_row[-1][1],accuracy)} in eq(1), we get y({r(all_row[-1][0]+step_size,accuracy)})= y{sub(str(i+2))} = {y_j_2}"]
                all_step.append(this_step)
                x_j_1=r((x_j_1+step_size),accuracy)
                this_row=[x_j_1,y_j_2]
                all_row.append(this_row)

        if order_of_method==3:
            all_row=all_row[:3]
            this_step=[f"Initial values required for 3{super('rd')} order Adams-Bashforth method are x{sub('0')}= {r(all_row[-3][0],accuracy)}, x{sub('1')}= {r(all_row[-2][0],accuracy)}, x{sub('2')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-3][1],accuracy)}, y{sub('1')}= {r(all_row[-2][1],accuracy)} and y{sub('2')}= {r(all_row[-1][1],accuracy)}. Refer respective method for detail-solution for initial data."]
            all_step.append(this_step)
            for i in range(iterations-2):
                y_j_2=all_row[-1][1]
                y_j_1=all_row[-2][1]
                y_j_0=all_row[-3][1]
                x_j_2=all_row[-1][0]
                x_j_1=x_j_2-step_size
                x_j_0=x_j_1-step_size
                y_j_3=r((y_j_2+(step_size/12)*(23*f.subs([(x,x_j_2),(y,y_j_2)])-16*f.subs([(x,x_j_1),(y,y_j_1)])+5*f.subs([(x,x_j_0),(y,y_j_0)]))),accuracy)
                this_step=[f"Putting vaues of  x{sub(str(i))}= {r(all_row[-3][0],accuracy)}, x{sub(str(i+1))}= {r(all_row[-2][0],accuracy)}, x{sub(str(i+2))}= {r(all_row[-1][0],accuracy)}, y{sub(str(i))}= {r(all_row[-3][1],accuracy)}, y{sub(str(i+1))}= {r(all_row[-2][1],accuracy)} and y{sub(str(i+2))}= {r(all_row[-1][1],accuracy)} in eq(1), we get y({r(all_row[-1][0] +step_size,accuracy)})= y{sub(str(i+3))} = {y_j_3}"]
                all_step.append(this_step)
                x_j_2=r((x_j_2+step_size),accuracy)
                this_row=[x_j_2,y_j_3]
                all_row.append(this_row)

        if order_of_method==4: #forth order method
            this_step=[f"Initial values required for 4{super('th')} order Adams-Bashforth method are x{sub('0')}= {r(all_row[-4][0],accuracy)}, x{sub('1')}= {r(all_row[-3][0],accuracy)}, x{sub('2')}= {r(all_row[-2][0],accuracy)}, x{sub('3')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-4][1],accuracy)}, y{sub('1')}= {r(all_row[-3][1],accuracy)}, y{sub('2')}= {r(all_row[-2][1],accuracy)} and y{sub('3')}= {r(all_row[-1][1],accuracy)}. Refer respective method for detail-solution for initial data."]
            all_step.append(this_step)
            for i in range(iterations-3):
                y_j_0=all_row[-4][1]
                y_j_1=all_row[-3][1]
                y_j_2=all_row[-2][1]
                y_j_3=all_row[-1][1]
                x_j_3=all_row[-1][0]
                x_j_2=x_j_3-step_size
                x_j_1=x_j_2-step_size
                x_j_0=x_j_1-step_size
                y_j_4=r((y_j_3+(step_size/24)*(55*f.subs([(x,x_j_3),(y,y_j_3)])-59*f.subs([(x,x_j_2),(y,y_j_2)])+37*f.subs([(x,x_j_1),(y,y_j_1)])-9*f.subs([(x,x_j_0),(y,y_j_0)]))),accuracy)
                this_step=[f"Putting vaues of  x{sub('0')}= {r(all_row[-4][0],accuracy)}, x{sub('1')}= {r(all_row[-3][0],accuracy)}, x{sub('2')}= {r(all_row[-2][0],accuracy)}, x{sub('3')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-4][1],accuracy)}, y{sub('1')}= {r(all_row[-3][1],accuracy)}, y{sub('2')}= {r(all_row[-2][1],accuracy)} and y{sub('3')}= {r(all_row[-1][1],accuracy)} in eq(1), we get y({r(all_row[-1][0] +step_size,accuracy)})= y{sub(str(i+4))} = {y_j_4}"]
                all_step.append(this_step)
                x_j_3=r((x_j_3+step_size),accuracy)
                this_row=[x_j_3,y_j_4]
                all_row.append(this_row)
        

        return result.extend([all_row, all_step])    
    except Exception as e:
        return result.extend([-1,str(e)])
    


def adams_bashforth_function_(result,**kwargs):
    try:
        accuracy=kwargs['accuracy']
        f=kwargs['function']
        initial_y=kwargs['initial_y']
        final_x = kwargs['final_x']
        step_size = kwargs['step_size']
        initial_x = kwargs['initial_x']
        order_of_method=int(kwargs['order_of_method'])
        iterations=int((final_x-initial_x)/step_size)
        this_step=[f"Given IVP is {kwargs['function']} with initial condition as y({initial_x})={initial_y}"]
        all_step=[]
        all_step.append(this_step)
        this_step=[f"Using the formula of {order_of_method}-order of Adams-Bashforth given above in 'Theory Related To Method' ------eq(1)"]
        all_step.append(this_step)
        kwargs['final_x']=3*step_size+initial_x
        result=[]
        initial_data=runge_kutta_helper_function(**kwargs)
        

        if initial_data[0]==-1:
            return [-1,initial_data[1]]
        else:
            initial_data=initial_data[0]
        this_row=[initial_x,initial_y]
        all_row=[]
        all_row=[this_row]+initial_data
        if order_of_method==1: #first order , same as euler forward method
            e_y_j=initial_y
            x_j=initial_x
            all_row=all_row[:1]
            for i in range(iterations):
                    e_y_j_1=r((e_y_j+step_size*(f.subs([(x,x_j),(y,e_y_j)]))),accuracy)
                    this_step=[f"Putting values of x{sub(str(i))}={x_j} and y{sub(str(i))}= {e_y_j} in eq(1), we get y({r(x_j+step_size,accuracy)})= y{sub(str(i+1))}= {e_y_j_1} "]
                    all_step.append(this_step)
                    x_j=r((x_j+step_size),accuracy)
                    this_row=[x_j,e_y_j_1]
                
                    all_row.append(this_row) 
                    e_y_j=e_y_j_1

        if order_of_method==2:
            all_row=all_row[:2]
            this_step=[f"Initial values required for 2{super('nd')} order Adams-Bashforth method are x{sub('0')}= {r(all_row[-2][0],accuracy)}, x{sub('1')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-2][1],accuracy)} and y{sub('1')}= {r(all_row[-1][1],accuracy)}. Refer respective method for detail-solution for initial data."]
            all_step.append(this_step)
            for i in range(iterations-1):
                y_j_1=all_row[-1][1]
                y_j_0=all_row[-2][1]
                x_j_1=all_row[-1][0]
                x_j_0=x_j_1-step_size
                y_j_2=r((y_j_1+(step_size/2)*(3*f.subs([(x,x_j_1),(y,y_j_1)])-f.subs([(x,x_j_0),(y,y_j_0)]))),accuracy)
                this_step=[f"Putting vaues of x{sub(str(i))}= {r(all_row[-2][0],accuracy)}, x{sub(str(i+1))}= {r(all_row[-1][0],accuracy)}, y{sub(str(i))}= {r(all_row[-2][1],accuracy)} and y{sub(str(i+1))}= {r(all_row[-1][1],accuracy)} in eq(1), we get y({r(all_row[-1][0]+step_size,accuracy)})= y{sub(str(i+2))} = {y_j_2}"]
                all_step.append(this_step)
                x_j_1=r((x_j_1+step_size),accuracy)
                this_row=[x_j_1,y_j_2]
                all_row.append(this_row)

        if order_of_method==3:
            all_row=all_row[:3]
            this_step=[f"Initial values required for 3{super('rd')} order Adams-Bashforth method are x{sub('0')}= {r(all_row[-3][0],accuracy)}, x{sub('1')}= {r(all_row[-2][0],accuracy)}, x{sub('2')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-3][1],accuracy)}, y{sub('1')}= {r(all_row[-2][1],accuracy)} and y{sub('2')}= {r(all_row[-1][1],accuracy)}. Refer respective method for detail-solution for initial data."]
            all_step.append(this_step)
            for i in range(iterations-2):
                y_j_2=all_row[-1][1]
                y_j_1=all_row[-2][1]
                y_j_0=all_row[-3][1]
                x_j_2=all_row[-1][0]
                x_j_1=x_j_2-step_size
                x_j_0=x_j_1-step_size
                y_j_3=r((y_j_2+(step_size/12)*(23*f.subs([(x,x_j_2),(y,y_j_2)])-16*f.subs([(x,x_j_1),(y,y_j_1)])+5*f.subs([(x,x_j_0),(y,y_j_0)]))),accuracy)
                this_step=[f"Putting vaues of  x{sub(str(i))}= {r(all_row[-3][0],accuracy)}, x{sub(str(i+1))}= {r(all_row[-2][0],accuracy)}, x{sub(str(i+2))}= {r(all_row[-1][0],accuracy)}, y{sub(str(i))}= {r(all_row[-3][1],accuracy)}, y{sub(str(i+1))}= {r(all_row[-2][1],accuracy)} and y{sub(str(i+2))}= {r(all_row[-1][1],accuracy)} in eq(1), we get y({r(all_row[-1][0] +step_size,accuracy)})= y{sub(str(i+3))} = {y_j_3}"]
                all_step.append(this_step)
                x_j_2=r((x_j_2+step_size),accuracy)
                this_row=[x_j_2,y_j_3]
                all_row.append(this_row)

        if order_of_method==4: #forth order method
            this_step=[f"Initial values required for 4{super('th')} order Adams-Bashforth method are x{sub('0')}= {r(all_row[-4][0],accuracy)}, x{sub('1')}= {r(all_row[-3][0],accuracy)}, x{sub('2')}= {r(all_row[-2][0],accuracy)}, x{sub('3')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-4][1],accuracy)}, y{sub('1')}= {r(all_row[-3][1],accuracy)}, y{sub('2')}= {r(all_row[-2][1],accuracy)} and y{sub('3')}= {r(all_row[-1][1],accuracy)}. Refer respective method for detail-solution for initial data."]
            all_step.append(this_step)
            for i in range(iterations-3):
                y_j_0=all_row[-4][1]
                y_j_1=all_row[-3][1]
                y_j_2=all_row[-2][1]
                y_j_3=all_row[-1][1]
                x_j_3=all_row[-1][0]
                x_j_2=x_j_3-step_size
                x_j_1=x_j_2-step_size
                x_j_0=x_j_1-step_size
                y_j_4=r((y_j_3+(step_size/24)*(55*f.subs([(x,x_j_3),(y,y_j_3)])-59*f.subs([(x,x_j_2),(y,y_j_2)])+37*f.subs([(x,x_j_1),(y,y_j_1)])-9*f.subs([(x,x_j_0),(y,y_j_0)]))),accuracy)
                this_step=[f"Putting vaues of  x{sub('0')}= {r(all_row[-4][0],accuracy)}, x{sub('1')}= {r(all_row[-3][0],accuracy)}, x{sub('2')}= {r(all_row[-2][0],accuracy)}, x{sub('3')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-4][1],accuracy)}, y{sub('1')}= {r(all_row[-3][1],accuracy)}, y{sub('2')}= {r(all_row[-2][1],accuracy)} and y{sub('3')}= {r(all_row[-1][1],accuracy)} in eq(1), we get y({r(all_row[-1][0] +step_size,accuracy)})= y{sub(str(i+4))} = {y_j_4}"]
                all_step.append(this_step)
                x_j_3=r((x_j_3+step_size),accuracy)
                this_row=[x_j_3,y_j_4]
                all_row.append(this_row)
        
        return result.extend([all_row, all_step]) 
    except Exception as e:
        return result.extend([-1,str(e)])


def milve_adams_function(result, **kwargs): #explict method
    try:
        accuracy=kwargs['accuracy']
        f=kwargs['function']
        initial_y=kwargs['initial_y']
        final_x = kwargs['final_x']
        step_size = kwargs['step_size']
        initial_x = kwargs['initial_x']
        iterations=int((final_x-initial_x)/step_size)
        this_step=[f"Given IVP is {kwargs['function']} with initial condition as y({initial_x})={initial_y}"]
        all_step=[]
        all_step.append(this_step)
        this_step=[f"Using the formula of 4{super('th')}-order of Adams-Milve-Explict method given above in 'Theory Related To Method' ------eq(1)"]
        all_step.append(this_step)
        kwargs['final_x']=3*step_size+initial_x
        initial_data=runge_kutta_helper_function(**kwargs)
        if initial_data[0]==-1:
            return [-1,initial_data[1]]
        else:
            initial_data=initial_data[0]
        this_row=[initial_x,initial_y]
        all_row=[]
        all_row=[this_row]+initial_data

        this_step=[f"Initial values required for 4{super('th')} order Adams-Milve-Implict method are x{sub('1')}= {r(all_row[-3][0],accuracy)}, x{sub('2')}= {r(all_row[-2][0],accuracy)}, x{sub('3')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-4][1],accuracy)}, y{sub('1')}= {r(all_row[-3][1],accuracy)}, y{sub('2')}= {r(all_row[-2][1],accuracy)} and y{sub('3')}= {r(all_row[-1][1],accuracy)}. Refer respective method for detail-solution for initial data."]
        all_step.append(this_step)

        for i in range(iterations-3):
            y_j_0=all_row[-4][1]
            y_j_1=all_row[-3][1]
            y_j_2=all_row[-2][1]
            y_j_3=all_row[-1][1]

            x_j_3=all_row[-1][0]
            x_j_2=x_j_3-step_size
            x_j_1=x_j_2-step_size

            y_j_4=r((y_j_0+((4*step_size)/3)*(2*f.subs([(x,x_j_3),(y,y_j_3)])-f.subs([(x,x_j_2),(y,y_j_2)])+2*f.subs([(x,x_j_1),(y,y_j_1)]))),accuracy)
            this_step=[f"Putting vaues of  x{sub((str(i+1)))}= {r(all_row[-3][0],accuracy)}, x{sub((str(i+2)))}= {r(all_row[-2][0],accuracy)}, x{sub((str(i+3)))}= {r(all_row[-1][0],accuracy)}, y{sub((str(i)))}= {r(all_row[-4][1],accuracy)}, y{sub((str(i+1)))}= {r(all_row[-3][1],accuracy)}, y{sub((str(i+2)))}= {r(all_row[-2][1],accuracy)} and y{sub((str(i+3)))}= {r(all_row[-1][1],accuracy)} in eq(1), we get y({r(all_row[-1][0]+step_size,accuracy)})= y{sub(str(i+4))} = {y_j_4}"]
            all_step.append(this_step)
            this_row=[r(x_j_3+step_size,3),y_j_4]
            all_row.append(this_row)

        return result.extend([all_row, all_step]) 
    except Exception as e:
        return result.extend([-1,str(e)])


#a corrector method

# under consideration
def adams_moulton_function(result ,**kwargs):
    try:
        accuracy=kwargs['accuracy']
        f=kwargs['function']
        initial_y=kwargs['initial_y']
        final_x = kwargs['final_x']
        step_size = kwargs['step_size']
        initial_x = kwargs['initial_x']
        order_of_method=int(kwargs['order_of_method'])
        iterations=int((final_x-initial_x)/step_size)
        this_step=[f"Given IVP is {kwargs['function']} with initial condition as y({initial_x})={initial_y}"]
        all_step=[]
        all_step.append(this_step)
        this_step=[f"Using the formula of {order_of_method}-order of Adams-Moulton method given above in 'Theory Related To Method' ------eq(1)"]
        all_step.append(this_step)
        kwargs['final_x']=3*step_size+initial_x
        initial_data=runge_kutta_helper_function(**kwargs)
        if initial_data[0]==-1:
            return [-1,initial_data[1]]
        else:
            initial_data=initial_data[0]
        
        this_row=[initial_x,initial_y]
        all_row=[]
        all_row=[this_row]+initial_data

        if order_of_method==1:  #this is a backeuler method, output will be different
            all_row=all_row[:2]
            this_step=[f"Initial values required for 1{super('st')} order Adams-Moulton method are  x{sub('1')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-2][1],accuracy)} and y{sub('1')}= {r(all_row[-1][1],accuracy)}. Refer respective method for detail-solution for initial data."]
            all_step.append(this_step)
            for i in range(iterations):
                y_j_1=all_row[-1][1]
                y_j_0=all_row[-2][1]
                x_j_1=all_row[-1][0]
                y_j_1=r((y_j_0+step_size*(f.subs([(x,x_j_1),(y,y_j_1)]))),accuracy)
                this_step=[f"Putting vaues of x{sub(str(i+1))}= {r(all_row[-1][0],accuracy)}, y{sub(str(i))}= {r(all_row[-2][1],accuracy)} and y{sub(str(i+1))}= {r(all_row[-1][1],accuracy)} in eq(1), we get y({r(all_row[-1][0],accuracy)})= y{sub(str(i+1))} = {y_j_1}"]
                all_step.append(this_step)        
                this_row=[r(x_j_1+step_size,accuracy),y_j_1]
                all_row.append(this_row)
      

        if order_of_method==2: #also called trapezium method
            all_row=all_row[:2]
            this_step=[f"Initial values required for 2{super('nd')} order Adams-Moulton method are x{sub('0')}= {r(all_row[-2][0],accuracy)}, x{sub('1')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-2][1],accuracy)} and y{sub('1')}= {r(all_row[-1][1],accuracy)}. Refer respective method for detail-solution for initial data."]
            all_step.append(this_step)
            for i in range(iterations):              
                y_j_1=all_row[-1][1]
                y_j_0=all_row[-2][1]
                x_j_1=all_row[-1][0]
                x_j_0=x_j_1-step_size
                y_j_1=r((y_j_1+(step_size/2)*(f.subs([(x,x_j_1),(y,y_j_1)])+f.subs([(x,x_j_0),(y,y_j_0)]))),accuracy)
                this_step=[f"Putting vaues of x{sub(str(i))}= {r(all_row[-2][0],accuracy)}, x{sub(str(i+1))}= {r(all_row[-1][0],accuracy)}, y{sub(str(i))}= {r(all_row[-2][1],accuracy)} and y{sub(str(i+1))}= {r(all_row[-1][1],accuracy)} in eq(1), we get y({r(all_row[-1][0],accuracy)})= y{sub(str(i+1))} = {y_j_1}"]
                all_step.append(this_step)          
                this_row=[r(x_j_1+step_size,accuracy),y_j_1]
                all_row.append(this_row)
      
        if order_of_method==3:
            all_row=all_row[:3]
            this_step=[f"Initial values required for 3{super('rd')} order Adams-Bashforth method are x{sub('0')}= {r(all_row[-3][0],accuracy)}, x{sub('1')}= {r(all_row[-2][0],accuracy)}, x{sub('2')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-3][1],accuracy)}, y{sub('1')}= {r(all_row[-2][1],accuracy)} and y{sub('2')}= {r(all_row[-1][1],accuracy)}. Refer respective method for detail-solution for initial data."]
            all_step.append(this_step)
            for i in range(iterations):
                y_j_2=all_row[-1][1]
                y_j_1=all_row[-2][1]
                y_j_0=all_row[-3][1]
                x_j_2=all_row[-1][0]
                x_j_1=x_j_2-step_size
                x_j_0=x_j_1-step_size 
                y_j_2=r((y_j_1+(step_size/12)*(5*f.subs([(x,x_j_2),(y,y_j_2)])+8*f.subs([(x,x_j_1),(y,y_j_1)])-f.subs([(x,x_j_0),(y,y_j_0)]))),accuracy)
                this_step=[f"Putting vaues of  x{sub(str(i))}= {r(all_row[-3][0],accuracy)}, x{sub(str(i+1))}= {r(all_row[-2][0],accuracy)}, x{sub(str(i+2))}= {r(all_row[-1][0],accuracy)}, y{sub(str(i))}= {r(all_row[-3][1],accuracy)}, y{sub(str(i+1))}= {r(all_row[-2][1],accuracy)} and y{sub(str(i+2))}= {r(all_row[-1][1],accuracy)} in eq(1), we get y({r(all_row[-1][0],accuracy)})= y{sub(str(i+3))} = {y_j_2}"]
                all_step.append(this_step) 
                this_row=[r(x_j_2+step_size,accuracy),y_j_2]
                all_row.append(this_row)
            
        if order_of_method==4:
            this_step=[f"Initial values required for 4{super('th')} order Adams-Bashforth method are x{sub('0')}= {r(all_row[-4][0],accuracy)}, x{sub('1')}= {r(all_row[-3][0],accuracy)}, x{sub('2')}= {r(all_row[-2][0],accuracy)}, x{sub('3')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-4][1],accuracy)}, y{sub('1')}= {r(all_row[-3][1],accuracy)}, y{sub('2')}= {r(all_row[-2][1],accuracy)} and y{sub('3')}= {r(all_row[-1][1],accuracy)}. Refer respective method for detail-solution for initial data."]
            all_step.append(this_step)
            for i in range(iterations): #4th order 
                y_j_0=all_row[-4][1]
                y_j_1=all_row[-3][1]
                y_j_2=all_row[-2][1]
                y_j_3=all_row[-1][1]
                x_j_3=all_row[-1][0]
                x_j_2=x_j_3-step_size
                x_j_1=x_j_2-step_size
                x_j_0=x_j_1-step_size
                y_j_3=r((y_j_2+(step_size/24)*(9*f.subs([(x,x_j_3),(y,y_j_3)])+ 19*f.subs([(x,x_j_2),(y,y_j_2)])-5*f.subs([(x,x_j_1),(y,y_j_1)])+f.subs([(x,x_j_0),(y,y_j_0)]))),accuracy)
                this_step=[f"Putting vaues of  x{sub(str(i))}= {r(all_row[-4][0],accuracy)}, x{sub((str(i+1)))}= {r(all_row[-3][0],accuracy)}, x{sub((str(i+2)))}= {r(all_row[-2][0],accuracy)}, x{sub((str(i+3)))}= {r(all_row[-1][0],accuracy)}, y{sub((str(i)))}= {r(all_row[-4][1],accuracy)}, y{sub((str(i+1)))}= {r(all_row[-3][1],accuracy)}, y{sub((str(i+2)))}= {r(all_row[-2][1],accuracy)} and y{sub((str(i+3)))}= {r(all_row[-1][1],accuracy)} in eq(1), we get y({r(all_row[-1][0],accuracy)})= y{sub(str(i+3))} = {y_j_3}"]
                all_step.append(this_step)             
                this_row=[r(x_j_3+step_size,accuracy),y_j_3]
                all_row.append(this_row)  
        
        return result.extend([all_row, all_step]) 
    except Exception as e:
        return result.extend([-1,str(e)])

# under consideration
def milve_simpson_function(result,**kwargs): #implict forth order method
    try:
        accuracy=kwargs['accuracy']
        f=kwargs['function']
        initial_y=kwargs['initial_y']
        final_x = kwargs['final_x']
        step_size = kwargs['step_size']
        initial_x = kwargs['initial_x']
        iterations=int((final_x-initial_x)/step_size)
        this_step=[f"Given IVP is {kwargs['function']} with initial condition as y({initial_x})={initial_y}"]
        all_step=[]
        all_step.append(this_step)
        this_step=[f"Using the formula of 4{super('th')}-order of Adams-Milve-Explict method given above in 'Theory Related To Method' ------eq(1)"]
        all_step.append(this_step)
        kwargs['final_x']=3*step_size+initial_x
        initial_data=runge_kutta_helper_function(**kwargs)
        if initial_data[0]==-1:
            return [-1,initial_data[1]]
        else:
            initial_data=initial_data[0]
        this_row=[initial_x,initial_y]
        all_row=[]
        all_row=[this_row]+initial_data
        this_step=[f"Initial values required for 4{super('th')} order Milve-Simpson-Implict method are x{sub('0')}= {r(all_row[-3][0],accuracy)}, x{sub('1')}= {r(all_row[-2][0],accuracy)}, x{sub('2')}= {r(all_row[-1][0],accuracy)}, y{sub('0')}= {r(all_row[-3][1],accuracy)}, y{sub('1')}= {r(all_row[-2][1],accuracy)} and y{sub('2')}= {r(all_row[-1][1],accuracy)}. Refer respective method for detail-solution for initial data."]
        all_step.append(this_step)
        for i in range(iterations):
            y_j_0=all_row[-3][1]
            y_j_1=all_row[-2][1]
            y_j_2=all_row[-1][1]
            x_j_2=all_row[-1][0]
            x_j_1=x_j_2-step_size
            x_j_0=x_j_1-step_size
            y_j_2=r((y_j_0+(step_size/3)*(f.subs([(x,x_j_2),(y,y_j_2)])+4*f.subs([(x,x_j_1),(y,y_j_1)])+f.subs([(x,x_j_0),(y,y_j_0)]))),accuracy)
            this_step=[f"Putting vaues of  x{sub((str(i)))}= {r(all_row[-3][0],accuracy)}, x{sub((str(i+1)))}= {r(all_row[-2][0],accuracy)}, x{sub((str(i+2)))}= {r(all_row[-1][0],accuracy)}, y{sub((str(i)))}= {r(all_row[-3][1],accuracy)}, y{sub((str(i+1)))}= {r(all_row[-2][1],accuracy)} and y{sub((str(i+2)))}= {r(all_row[-1][1],accuracy)} in eq(1), we get y({r(all_row[-1][0],accuracy)})= y{sub(str(i+2))} = {y_j_2}"]
            all_step.append(this_step)
            this_row=[r(x_j_2+step_size,accuracy),y_j_2]
            all_row.append(this_row)
        
        return result.extend([all_row, all_step]) 
    except Exception as e:
        return result.extend([-1,str(e)])
