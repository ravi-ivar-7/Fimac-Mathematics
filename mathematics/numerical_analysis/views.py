from django.shortcuts import render
from sympy import *
import plotly.graph_objects as go
from multiprocessing import Process, Manager
import re
from core.theory_core import how_to_input,sub,super

# functions
from numerical_analysis.functions_numerical_integration import trapezoidal_function, simpson_3_function
from numerical_analysis.functions_eulers_methods import picards_function, eulers_cauchy_function,eulers_forward_function, picards_function
from numerical_analysis.functions_rk_methods import all_runge_kutta_function, individual_runge_kutta_function
from numerical_analysis.functions_multistep_methods import adams_moulton_function,adams_bashforth_function,milve_adams_function,milve_simpson_function
from numerical_analysis.functions_pc_methods import adams_bashforth_pc_function,milve_adams_pc_function

#theory
from numerical_analysis.theory_numerical_integration import trapezoidal_theory, simpson_3_theory
from numerical_analysis.theory_rk_ms_eulers import picards_theory,euler_cauchy_theory,euler_forward_theory,decide_step_size_rk_euler,source_of_info,rk_theory, adams_bashforth_theory, adams_moulton_theory,milne_adams_theory,milne_theory
from numerical_analysis.theory_pc_methods import source_of_info, adams_bashforth_moulton_pc_theory, decide_step_size_multistep, milve_adams_pc_theory

custom_config={'displaylogo':False}
r=round
accuracy=5
timeout = 20
timeout_error = f"ERROR: Time-limit exceeded. Current computation time-limit is {timeout} seconds."
(x, y, z) = symbols('x y z')

def home_numerical_differentiation(request):
    return render(request, 'home_numerical_differentiation.html')

def home_numerical_integration(request):
    return render(request, 'home_numerical_integration.html')


# numerical integration

def trapezoidal_method(request):
    context = {
                    'input_info':"For  ∫f(x) with lower limit(a) and upper limit(b) such that b > a " ,
                    'function': "Enter function f(x)",
                    'initial_x': "Enter lower limit (a)",
                    'final_x': "Enter upper limit (b)",
                    'no_of_segment':"No. of segment(n). [For no-segment, n=1] :",
                    'accuracy':'Accurate up-to [for 5 decimal point i.e. 0.00001, enter 5] ',
                    'method_name': "Trapezoidal Rule for numerical integrating",
                    'screen_info':'Switch to desktop mode for better plot!',
                    'topic_name': 'Numerical Integration',
                    'title': "Trapezoidal Rule",
                    'method_theory':trapezoidal_theory,
                    'how_to_input':how_to_input,
            }
    if request.method == 'POST':
            function = request.POST.get('function')
            try:
                no_of_segment=eval(request.POST.get('no_of_segment'))
                fun = simplify(function)
                initial_x = eval(request.POST.get('initial_x'))
                final_x = eval(request.POST.get('final_x'))
                accuracy=eval(request.POST.get('accuracy'))

                if initial_x>=final_x:
                    input_error=f"Make upper limit of integration greater than lower limit."
                    context_e = {'input_error': input_error,'fun': f"Your function is: {function}"}
                    context={**context,**context_e}
                    return render(request, 'input_output_numerical_analysis.html', context)    
                    
                with Manager() as manager:
                    result = manager.list()
                    process = Process(target=trapezoidal_function, args=(result,), kwargs={'f': fun, 'x_i': initial_x, 'accuracy':accuracy,'no_of_segment':no_of_segment,'x_n':final_x})
                    process.start()
                    process.join(timeout)

                    if process.is_alive():
                        process.terminate()
                        context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                        context={**context_timeout,**context}

                    elif result[0]==-1:
                        input_error=f"{result[1]}"
                        context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                        context={**context_error,**context}

                    else:
                        final_result=result[0]
                        final_result=result[0]
                        detail_solution=result[1]
                        x_axis=[float(r(value[0],accuracy)) for value in result[2]]
                        y_axis=[float(r(value[1],accuracy)) for value in result[2]]
                        fig=go.Figure()
                        fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"f(x{sub('i')})")
                        fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers'))
                        fig=fig.to_html(full_html=False, config=custom_config)        
                        context_output = {'final_result': final_result,'final_result_info':'Maximum bound error may vary.', 'detail_solution':detail_solution,'fun': f"Given function is: {fun}",'plot':fig,'plot_info':'Area under below curve gives value of ∫f(x) '}
                        context={**context_output,**context}
                    return render(request, 'input_output_numerical_analysis.html', context)
                   
            except Exception as e: 
                input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.|| Make sure variables are only 'x' or 'y'."
                context_e = {'input_error': input_error,'fun': f"Your function is: {function}"}
                context={**context,**context_e}
            
    return render(request,'input_output_numerical_analysis.html',context)

def simpson_3_method(request):
    context = {
                    'input_info':"For  ∫f(x) with lower limit(a) and upper limit(b) such that b>a " ,
                    'function': "Enter function f(x)",
                    'initial_x': "Enter lower limit (a)",
                    'final_x': "Enter upper limit (b)",
                    'no_of_segment':"No. of segment(n), [n should be even] :",
                    'accuracy':'Accurate up-to [for 5 decimal point i.e. 0.00001, enter 5] ',
                     'screen_info':'Switch to desktop mode for better plot!',
                    'method_name': " Simpson's 1/3 Rule",
                    'topic_name': 'Numerical Integration',
                    'title': "Simpson's 1/3 Rule",
                    'method_theory':simpson_3_theory,
                    'how_to_input':how_to_input,
            }
    if request.method == 'POST':
        function = request.POST.get('function')
        no_of_segment=eval(request.POST.get('no_of_segment'))
        if no_of_segment%2!=0:
            error="For simpson's 1/3 rule, number of segment(n) should be even"
            context_n = {'input_error': str(error),}
            context={**context,**context_n}
            return render(request, 'input_output_numerical_analysis.html', context)
        else:
            try:
                fun = simplify(function)
                initial_x = eval(request.POST.get('initial_x'))
                final_x = eval(request.POST.get('final_x'))
                accuracy=eval(request.POST.get('accuracy'))
                if initial_x>=final_x:
                    error="Make upper limit greater than lower limit."
                    context_n = {'input_error': str(error),}
                    context={**context,**context_n}
                    return render(request, 'input_output_numerical_analysis.html', context)
                
                with Manager() as manager:
                    result = manager.list()
                    process = Process(target=simpson_3_function, args=(result,), kwargs={'f': fun, 'x_i': initial_x,'accuracy':accuracy,'no_of_segment':no_of_segment,'x_n':final_x})
                    process.start()
                    process.join(timeout)

                    if process.is_alive():
                        process.terminate()
                        context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                        context={**context_timeout,**context}

                    elif result[0]==-1:
                        input_error=f"{result[1]}"
                        context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                        context={**context_error,**context}

                    else:
                        
                        final_result=result[0]
                        detail_solution=result[1]
                        x_axis=[float(r(value[0],accuracy)) for value in result[2]]
                        y_axis=[float(r(value[1],accuracy)) for value in result[2]]
                        fig=go.Figure()
                        fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"f(x{sub('i')})")
                        fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers'))
                        fig=fig.to_html(full_html=False, config=custom_config)        

                        context_output = {'final_result': final_result,'final_result_info':'Maximum bound error may vary.','detail_solution':detail_solution,'fun': f"Given function is: {fun}",'plot':fig,'plot_info':'Area under below curve gives value of ∫f(x) '}
                        context={**context_output,**context}
                    return render(request, 'input_output_numerical_analysis.html', context)
            
            except Exception as e:
                input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.|| Make sure variables are only 'x' or 'y'."
                context_e = {'input_error': input_error,'fun': f"Your function is: {function}"}
                context={**context,**context_e}
               
    return render(request,'input_output_numerical_analysis.html',context)

def picards_method(request):
    context = {
        'input_info':f"For IVP, dy/dx=f(x,y) x ∈ [a,b], y'(a)= y{sub('0')}. For n{super('th')} approximation of its solution" ,
        'function_prime': "Enter IVP equation dy/dx ",
        'initial_x': "Enter initial point of domain (a)",
        'final_x': "Enter final point of domain (b)",
        'initial_y': f"Enter y{sub('0')}",
        'iterations':f"Enter value of n for n{super('th')} approximation. ",
        'how_to_input':how_to_input,
        'method_theory':picards_theory,
        'method_name': 'picards method',
        'topic_name': 'numerical differentiation',
        'title':'Picards Method',
    }
    if request.method == 'POST':
        function_prime = request.POST.get('function_prime')
        try:
            fun = simplify(function_prime)
            initial_x = eval(request.POST.get('initial_x'))
            final_x = eval(request.POST.get('final_x'))
            initial_y = eval(request.POST.get('initial_y'))
            iterations = eval(request.POST.get('iterations'))
            if(initial_x>=final_x):
                    input_error=f"Make  (b)> (a)"
                    context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                    context={**context,**context_e}
                    return render(request, 'input_output_numerical_analysis.html', context)
            
            with Manager() as manager:
                result = manager.list()
                process = Process(target=picards_function, args=(result,), kwargs={'final_x': final_x, 'initial_x': initial_x, 'initial_y': initial_y, 'iterations': iterations, 'function': fun})
                process.start()
                process.join(timeout)

                if process.is_alive():
                    process.terminate()
                    context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                    context={**context_timeout,**context}

                elif result[0]==-1:
                    input_error=f"{result[1]}"
                    context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                    context={**context_error,**context}

                else:
                    context_output = {'detail_solution':result,'fun': f"Given function is: {fun}"}
                    context={**context_output,**context}
                return render(request, 'input_output_numerical_analysis.html', context)

        except Exception as e:
            input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.||Make sure variables are only 'x' and/or 'y'."
            context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
            context={**context,**context_e}
        
    return render(request, 'input_output_numerical_analysis.html', context)


# single step methods

def eulers_forward_method(request):
        context = {
            'input_info':f"For IVP, dy/dx=f(x,y) x ∈ [a,b], y'(a)= y{sub('0')} with step-size (h)",
            'screen_info':'Switch to desktop mode for better plot!',
            'function_prime': "Enter IVP equation dy/dx ",
            'initial_x': "Enter initial point of domain (a)",
            'final_x': "Enter final point of domain (b)",
            'initial_y': f"Enter y{sub('0')}",
            'step_size': "Enter step size(h)",
            'accuracy':'Accurate up-to [for 5 decimal point i.e. 0.00001, enter 5] ',
            'how_to_input':how_to_input,
            'method_theory':euler_forward_theory,
            'decide_step_size':decide_step_size_rk_euler,
            'method_name': 'Eulers Forward Method',
            'topic_name': 'numerical differentiation',
            'title':' Eulers Forward Method'
            }
        if request.method == 'POST':
            function_prime=request.POST.get('function_prime')
            try:
                fun = simplify(function_prime)
                initial_x = eval(request.POST.get('initial_x'))
                initial_y = eval(request.POST.get('initial_y'))
                final_x = eval(request.POST.get('final_x'))
                step_size=eval(request.POST.get('step_size'))
                accuracy=eval(request.POST.get('accuracy'))
                if(initial_x>=final_x):
                    input_error=f"Make  (b)> (a)"
                    context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                    context={**context,**context_e}
                    return render(request, 'input_output_numerical_analysis.html', context)
                
                with Manager() as manager:
                    result = manager.list()
                    process = Process(target=eulers_forward_function, args=(result,), kwargs={'initial_x': initial_x, 'initial_y': initial_y, 'step_size': step_size, 'accuracy':accuracy, 'function': fun,'step_size':step_size,'final_x':final_x})
                    process.start()
                    process.join(timeout)

                    if process.is_alive():
                        process.terminate()
                        context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                        context={**context_timeout,**context}

                    elif result[0]==-1:
                        input_error=f"{result[1]}"
                        context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                        context={**context_error,**context}

                    else:
                        final_result=result[0]
                        detail_solution=result[1]
                        x_axis=[float(r(value[0],accuracy)) for value in final_result]
                        y_axis=[float(r(value[1],accuracy)) for value in final_result]
                        fig=go.Figure()
                        fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"y(x{sub('i')})" )
                        fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers',name="x values"))
                        fig=fig.to_html(full_html=False ,config=custom_config)
                        headings=[f"x{sub('i')}", f"y(x{sub('i')})"]    
                        context_output = {'final_result': final_result,'detail_solution':detail_solution,'fun': f"Given function is: {fun}",'headings':headings,'plot':fig}
                        context={**context_output,**context}
                    return render(request, 'input_output_numerical_analysis.html', context)

            except Exception as e: #invalid input
                input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.||Make sure variables are only 'x' and/or 'y'."
                context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                context={**context,**context_e}

        return render(request, 'input_output_numerical_analysis.html', context)

def eulers_cauchy_method(request):
        context = {
            'input_info':f"For IVP, dy/dx=f(x,y) x ∈ [a,b], y'(a)= y{sub('0')} with step-size (h)",
            'screen_info':'Switch to desktop mode for better plot!',
            'function_prime': "Enter IVP equation dy/dx ",
            'initial_x': "Enter initial point of domain (a)",
            'final_x': "Enter final point of domain (b)",
            'initial_y': f"Enter y{sub('0')}",
            'step_size': "Enter step size(h)",
            'accuracy':'Accurate up-to [for 5 decimal point i.e. 0.00001, enter 5] ',
            'how_to_input':how_to_input,
            'method_theory':euler_cauchy_theory,
            'decide_step_size':decide_step_size_rk_euler,
            'method_name': 'Eulers Cauchy Method',
            'topic_name': 'numerical differentiation',
            'title':' Eulers Cauchy Method'
            }
        if request.method == 'POST':
            function_prime=request.POST.get('function_prime')
            try:
                fun = simplify(function_prime)
                initial_x = eval(request.POST.get('initial_x'))
                initial_y = eval(request.POST.get('initial_y'))
                final_x = eval(request.POST.get('final_x'))
                accuracy=eval(request.POST.get('accuracy'))
                step_size=eval(request.POST.get('step_size'))
                if(initial_x>=final_x):
                    input_error=f"Make  (b)> (a)"
                    context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                    context={**context,**context_e}
                    return render(request, 'input_output_numerical_analysis.html', context)
                
                with Manager() as manager:
                    result = manager.list()
                    process = Process(target=eulers_cauchy_function, args=(result,), kwargs={'initial_x': initial_x, 'initial_y': initial_y, 'final_x': final_x,'accuracy':accuracy, 'function': fun,'step_size':step_size})
                    process.start()
                    process.join(timeout)

                    if process.is_alive():
                        process.terminate()
                        context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                        context={**context_timeout,**context}

                    elif result[0]==-1:
                        input_error=f"{result[1]}"
                        context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                        context={**context_error,**context}

                    else:
                        final_result=result[0]
                        detail_solution=result[1]
                        try:
                            x_axis=[float(r(value[0],accuracy)) for value in final_result]
                            y_axis=[float(r(value[1],accuracy)) for value in final_result]
                            fig=go.Figure()
                            fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"y(x{sub('i')})" )
                            fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers',name="x values"))
                            fig=fig.to_html(full_html=False ,config=custom_config)
                        except Exception as e:
                            fig=f"Cannot be plotted!"+str(e)
                        headings=[f"x{sub('i')}", f"y(x{sub('i')})"]
                        context_output = {'final_result': final_result,'detail_solution':detail_solution,'fun': f"Given function is: {fun}",'headings':headings,'plot':fig}
                        context={**context_output,**context}
                        return render(request, 'input_output_numerical_analysis.html', context)
                    
            except Exception as e: 
                input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.||Make sure variables are only 'x' or 'y'."
                context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                context={**context,**context_e}

        return render(request, 'input_output_numerical_analysis.html', context)

def individual_runge_kutta_methods(request):
    context = {
            'input_info':f"For IVP, dy/dx=f(x,y) x ∈ [a,b], y'(a)= y{sub('0')} with step-size (h)",
            'screen_info':'Switch to desktop mode for better plot!',
            'function_prime': "Enter IVP equation dy/dx ",
            'initial_x': "Enter initial point of domain (a)",
            'final_x': "Enter final point of domain (b)",
            'initial_y': f"Enter y{sub('0')}",
            'step_size': "Enter step size(h)",
            'accuracy':'Accurate up-to [for 5 decimal points i.e. 0.00001, enter 5] ',
            'method':'Choose a Runge Kutta method:',
            'method_name': 'Runge-Kutta (explict) Methods',
            'how_to_input':how_to_input,
            'decide_step_size':decide_step_size_rk_euler,
            'method_theory':rk_theory()+euler_forward_theory()+source_of_info(),
            'topic_name': 'numerical differentiation',
            'title':' Runge-Kutta-Explict Methods'
    }
    if request.method == 'POST':
        function_prime=request.POST.get('function_prime')
        try:
            fun = simplify(function_prime)
            initial_x = eval(request.POST.get('initial_x'))
            initial_y = eval(request.POST.get('initial_y'))
            final_x = eval(request.POST.get('final_x'))
            step_size=eval(request.POST.get('step_size'))
            accuracy=eval(request.POST.get('accuracy'))
            method=request.POST.get('method')
   
            if(initial_x>=final_x):
                input_error=f"Make  (b)> (a)"
                context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                context={**context,**context_e}
                return render(request, 'input_output_numerical_analysis.html', context)
            
            with Manager() as manager:
                    result = manager.list()
                    process = Process(target=individual_runge_kutta_function, args=(result,), kwargs={ 'initial_x': initial_x, 'final_x': final_x, 'function': fun,'initial_y':initial_y,'step_size':step_size,'accuracy':accuracy,'method':method})
                    process.start()
                    process.join(timeout)

                    if process.is_alive():
                        process.terminate()
                        context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                        context={**context_timeout,**context}

                    elif result[0]==-1:
                        input_error=f"{result[1]}"
                        context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                        context={**context_error,**context}

                    else:
                        final_result=result[0]
                        detail_solution=result[1]
                        try:
                            x_axis=[float(r(value[0],accuracy)) for value in final_result]
                            y_axis=[float(r(value[1],accuracy)) for value in final_result]
                            fig=go.Figure()
                            fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"y(x{sub('i')})" )
                            fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers'))
                            fig=fig.to_html(full_html=False ,config=custom_config)
                        except Exception as e:
                            fig=f"Cannot be plotted!"+str(e)
                        headings=[f"x{sub('i')}", f"y(x{sub('i')})"]
                        context_output = {'final_result': final_result,'detail_solution':detail_solution,'fun': f"Given function is: {fun}",'headings':headings,'plot':fig}
                        context={**context_output,**context}
                    return render(request, 'input_output_numerical_analysis.html', context)

        except Exception as e:
            input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.||Make sure variables are only 'x' or 'y'."
            context_e = {'input_error':input_error,'fun': f"Your function is: {function_prime}",}
            context={**context,**context_e}

    return render(request, 'input_output_numerical_analysis.html', context)

def all_runge_kutta_methods(request):
    context = {
            'info':"For detailed solution, use 'Runge kutta (solved each method individually step-by-step and plotted)'",
            'input_info':f"For IVP, dy/dx=f(x,y) x ∈ [a,b], y'(a)= y{sub('0')} with step-size (h)",
            'screen_info':'Switch to desktop mode for better plot!',
            'function_prime': "Enter IVP equation dy/dx ",
            'initial_x': "Enter initial point of domain (a)",
            'final_x': "Enter final point of domain (b)",
            'initial_y': f"Enter y{sub('0')}",
            'step_size': "Enter step size(h)",
            'accuracy':'Accurate up-to [for 5 decimal points i.e. 0.00001, enter 5] ',
            'how_to_input':how_to_input,
            'decide_step_size':decide_step_size_rk_euler,
            'method_theory':rk_theory()+source_of_info(),
            'method_name': 'Runge-Kutta all Methods together.',
            'topic_name': 'numerical differentiation',
            'title':' Runge-Kutta all Methods'
    }
    if request.method == 'POST':

        function_prime=request.POST.get('function_prime')
        try:
            fun = simplify(function_prime)
            initial_x = eval(request.POST.get('initial_x'))
            initial_y = eval(request.POST.get('initial_y'))
            final_x = eval(request.POST.get('final_x'))
            step_size=eval(request.POST.get('step_size'))
            accuracy=eval(request.POST.get('accuracy'))
            if(initial_x>=final_x):
                input_error=f"Make  (b)> (a)"
                context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                context={**context,**context_e}
                return render(request, 'input_output_numerical_analysis.html', context)
            
            with Manager() as manager:
                    result = manager.list()
                    process = Process(target=all_runge_kutta_function, args=(result,), kwargs={ 'initial_x': initial_x, 'final_x': final_x,  'function': fun,'initial_y':initial_y,'final_x':final_x,'accuracy':accuracy ,'step_size':step_size,})
                    process.start()
                    process.join(timeout)

                    if process.is_alive():
                        process.terminate()
                        context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                        context={**context_timeout,**context}

                    elif result[0]==-1:
                        input_error=f"{result[1]}"
                        context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                        context={**context_error,**context}

                    else:
                        try:
                            x_axis=[float((value[0])) for value in result]
                            y_second_order=[float((value[1])) for value in result]
                            y_classical=[float((value[2])) for value in result]
                            y_gill=[float((value[3])) for value in result]
                            y_fehlberg=[float((value[4])) for value in result]
                            runge_fig=go.Figure()
                            runge_fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"y(x{sub('i')})" )
                            runge_fig.add_trace(go.Scatter(x=x_axis,y=y_second_order,mode='lines+markers',name='R.K second order'))
                            runge_fig.add_trace(go.Scatter(x=x_axis,y=y_classical,mode='lines+markers',name='Classical Method'))
                            runge_fig.add_trace(go.Scatter(x=x_axis,y=y_gill,mode='lines+markers',name='Gill Method'))
                            runge_fig.add_trace(go.Scatter(x=x_axis,y=y_fehlberg,mode='lines+markers',name='Fehlerg Method'))
                            fig=runge_fig.to_html(full_html=False,config=custom_config)
                        except Exception as e:
                            fig=f"Cannot be plotted!"+str(e)
                        headings=[f"x{sub('i')}", f"R.K. 2{super('nd')} order",f"R.K.Classical 4{super('th')} order",f"R.K.Gill 4{super('th')} order",f"R.K.Fehlberg 4{super('th')} order"]
                        context_output = {'final_result':result,'fun': f"Given function is: {fun}",'headings':headings,'plot':fig}
                        context={**context_output,**context}

                    return render(request, 'input_output_numerical_analysis.html', context)
          

        except Exception as e: #invalid input
            input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.||Make sure variables are only 'x' or 'y'."
            context_e = {'input_error':input_error,'fun': f"Your function is: {function_prime}",}
            context={**context,**context_e}

    return render(request, 'input_output_numerical_analysis.html', context)


# multistep methods

def adams_bashforth_method2(request):
    context = {
            'input_info':f"For IVP, dy/dx=f(x,y) x ∈ [a,b], y'(a)= y{sub('0')} with step-size (h)",
            'screen_info':'Switch to desktop mode for better plot!',
            'function_prime': "Enter IVP equation dy/dx ",
            'initial_x': "Enter initial point of domain (a)",
            'final_x': "Enter final point of domain (b)",
            'initial_y': f"Enter y{sub('0')}",
            'step_size': "Enter step size(h)",
            'accuracy':'Accurate up-to [for 5 decimal points i.e. 0.00001, enter 5] ',  
            'method':'Choose a method to find initial value to start with this methods.',
            'order_of_method':'Choose a order of adams-bashforth method.',   
            'how_to_input':how_to_input,
            'decide_step_size':decide_step_size_multistep,
            'method_theory':adams_bashforth_theory()+source_of_info(),
            'method_name': 'Adams-Bashforth-Explict methods',
            'topic_name': 'numerical differentiation',
            'title':' Adams-Bashforth Methods'
    }
    if request.method == 'POST':
        function_prime=request.POST.get('function_prime')
        try:
            fun = simplify(function_prime)
            initial_x = eval(request.POST.get('initial_x'))
            initial_y = eval(request.POST.get('initial_y'))
            final_x = eval(request.POST.get('final_x'))
            accuracy = eval(request.POST.get('accuracy'))
            step_size=eval(request.POST.get('step_size'))
            method=request.POST.get('method')  #methods to find some initial requied data
            order_of_method=(request.POST.get('order_of_method'))
            if(initial_x>=final_x):
                input_error=f"Make  (b)> (a)"
                context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                context={**context,**context_e}
                return render(request, 'input_output_numerical_analysis.html', context)          
            with Manager() as manager:
                result = manager.list() 
                process = Process(target=adams_bashforth_function, args=(result,), kwargs={ 'initial_x': initial_x,'final_x':final_x, 'function': fun,'initial_y':initial_y,'step_size':step_size,'method':method,'order_of_method':order_of_method,'accuracy':accuracy})
                process.start()
                process.join(timeout)
                print(result)
                if process.is_alive():
                    process.terminate()
                    context_t = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                    context={**context,**context_t}
                else:
                    if result[0]==-1:
                        input_error=f"{result[1]}. Report Question."
                        context_e = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                        context={**context_e,**context}
                        return render(request, 'input_output_numerical_analysis.html', context)
                    else:
                        table_output=result[0]
                        step_output=result[1]
                        try:
                            x_axis=[float(r(value[0],accuracy)) for value in table_output]
                            y_axis=[float(r(value[1],accuracy)) for value in table_output]
                            fig=go.Figure()
                            fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"y(x{sub('i')})" )
                            fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers'))
                            fig=fig.to_html(full_html=False ,config=custom_config)
                        except:
                            fig="Failed To Plot!"
                        headings=[f"x{sub('i')}", f"y(x{sub('i')})"]
                        intermediate_data=table_output[:int(order_of_method)]
                        table_output=table_output[int(order_of_method):]
                        context_o={'table_output':table_output, 'step_output':step_output,'intermediate_data':intermediate_data,'fun':f'Given function is {fun}','headings':headings,'plot':fig,'headings_intermediate_data':headings,} 
                        context={**context,**context_o}
                    return render(request, 'input_output_numerical_analysis.html', context)
        except Exception as e: #invalid input
            input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.||Make sure variables are only 'x' or 'y'."
            context_e = {'input_error':input_error,'fun': f"Your function is: {function_prime}",}
            context={**context,**context_e}
            return render(request, 'input_output_numerical_analysis.html', context)
    return render(request, 'input_output_numerical_analysis.html', context)

# not working
def adams_bashforth_method(request):
    context = {
            'input_info':f"For IVP, dy/dx=f(x,y) x ∈ [a,b], y'(a)= y{sub('0')} with step-size (h)",
            'screen_info':'Switch to desktop mode for better plot!',
            'function_prime': "Enter IVP equation dy/dx ",
            'initial_x': "Enter initial point of domain (a)",
            'final_x': "Enter final point of domain (b)",
            'initial_y': f"Enter y{sub('0')}",
            'step_size': "Enter step size(h)",
            'accuracy':'Accurate up-to [for 5 decimal points i.e. 0.00001, enter 5] ',  
            'method':'Choose a method to find initial value to start with this methods.',
            'order_of_method':'Choose a order of adams-bashforth method.',   
            'how_to_input':how_to_input,
            'decide_step_size':decide_step_size_multistep,
            'method_theory':adams_bashforth_theory()+source_of_info(),
            'method_name': 'Adams-Bashforth-Explict methods',
            'topic_name': 'numerical differentiation',
            'title':' Adams-Bashforth Methods'
    }
    if request.method == 'POST':
        function_prime=request.POST.get('function_prime')
        try:
            fun = simplify(function_prime)
            initial_x = eval(request.POST.get('initial_x'))
            initial_y = eval(request.POST.get('initial_y'))
            final_x = eval(request.POST.get('final_x'))
            accuracy = eval(request.POST.get('accuracy'))
            step_size=eval(request.POST.get('step_size'))
            method=request.POST.get('method')  #methods to find some initial requied data
            order_of_method=(request.POST.get('order_of_method'))
            if(initial_x>=final_x):
                input_error=f"Make  (b)> (a)"
                context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                context={**context,**context_e}
                return render(request, 'input_output_numerical_analysis.html', context)  

            with Manager() as manager:
                result = manager.list()
                process = Process(target=adams_bashforth_function, args=(result,), kwargs={ 'initial_x': initial_x,'final_x':final_x, 'function': fun,'initial_y':initial_y,'step_size':step_size,'method':method,'order_of_method':order_of_method,'accuracy':accuracy})
                process.start()
                process.join(timeout)

                if process.is_alive():
                    process.terminate()
                    context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                    context={**context_timeout,**context}
                elif result[0]==-1:
                    input_error=f"{result[1]}"
                    context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                    context={**context_error,**context}
                else:
                    final_result=result[0]
                    detail_solution=result[1]
                    try:
                        x_axis=[float(r(value[0],accuracy)) for value in final_result]
                        y_axis=[float(r(value[1],accuracy)) for value in final_result]
                        fig=go.Figure()
                        fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"y(x{sub('i')})" )
                        fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers'))
                        fig=fig.to_html(full_html=False ,config=custom_config)
                    except:
                        fig="Failed To Plot!"
                    headings=[f"x{sub('i')}", f"y(x{sub('i')})"]
                    intermediate_result=final_result[:int(order_of_method)]
                    final_result=final_result[int(order_of_method):]
                    context_output={'final_result':final_result, 'detail_solution':detail_solution,'intermediate_result':intermediate_result,'fun':f'Given function is {fun}','headings':headings,'plot':fig,'headings_intermediate_result':headings,} 
                    context={**context_output,**context}

                return render(request, 'input_output_numerical_analysis.html', context)
                 
        except Exception as e: 
            input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.||Make sure variables are only 'x' or 'y'."
            context_e = {'input_error':input_error,'fun': f"Your function is: {function_prime}",}
            context={**context,**context_e}
  
    return render(request, 'input_output_numerical_analysis.html', context)

def milve_adams_method(request):
    context = {
            'input_info':f"For IVP, dy/dx=f(x,y) x ∈ [a,b], y'(a)= y{sub('0')} with step-size (h)",
            'screen_info':'Switch to desktop mode for better plot!',
            'function_prime': "Enter IVP equation dy/dx ",
            'initial_x': "Enter initial point of domain (a)",
            'final_x': "Enter final point of domain (b)",
            'initial_y': f"Enter y{sub('0')}",
            'step_size': "Enter step size(h)",
            'accuracy':'Accurate up-to [for 5 decimal points i.e. 0.00001, enter 5] ',
            'method':'Choose a method to find initial value to start with this methods.',
            'how_to_input':how_to_input,
            'decide_step_size':decide_step_size_multistep,
            'method_theory':milne_adams_theory()+source_of_info(),
            'method_name': f"Milve-Adams-Explict-4{super('th')} order methods",
            'topic_name': 'numerical differentiation',
            'title':' Milve-Adams-Explict Methods'
    }
    if request.method == 'POST':
        function_prime=request.POST.get('function_prime')
        try:
            fun = simplify(function_prime)
            initial_x = eval(request.POST.get('initial_x'))
            initial_y = eval(request.POST.get('initial_y'))
            final_x = eval(request.POST.get('final_x'))
            accuracy = eval(request.POST.get('accuracy'))
            step_size=eval(request.POST.get('step_size'))
            method=request.POST.get('method')  #methods to find some initial requied data    
            if(initial_x>=final_x):
                input_error=f"For x ∈ [a,b], a<b"
                context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                context={**context,**context_e}
                return render(request, 'input_output_numerical_analysis.html', context)  
            
            with Manager() as manager:
                    result = manager.list()
                    process = Process(target=milve_adams_function, args=(result,), kwargs={ 'initial_x': initial_x,'accuracy':accuracy, 'function': fun,'initial_y':initial_y,'step_size':step_size,'method':method,'final_x':final_x})
                    process.start()
                    process.join(timeout)

                    if process.is_alive():
                        process.terminate()
                        context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                        context={**context_timeout,**context}

                    elif result[0]==-1:
                        input_error=f"{result[1]}"
                        context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                        context={**context_error,**context}

                    else:
                        final_result=result[0]
                        detail_solution=result[1]
                        try:
                            x_axis=[float(r(value[0],accuracy)) for value in final_result]
                            y_axis=[float(r(value[1],accuracy)) for value in final_result]
                            fig=go.Figure()
                            fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"y(x{sub('i')})" )
                            fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers'))
                            fig=fig.to_html(full_html=False ,config=custom_config)
                        except:
                            fig="Failed To Plot!"
                        headings=[f"x{sub('i')}", f"y(x{sub('i')})"]
                    
                        intermediate_result=final_result[:4]  #since it is implict method
                        final_result=final_result[4:]
                        context_output={'final_result':final_result, 'detail_solution':detail_solution,'intermediate_result':intermediate_result,'fun':f'Given function is {fun}','headings':headings,'plot':fig,'headings_intermediate_result':headings,} 
                        context={**context_output,**context}

                    return render(request, 'input_output_numerical_analysis.html', context)
            
        except Exception as e: 
            input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.||Make sure variables are only 'x' or 'y'."
            context_e = {'input_error':input_error,'fun': f"Your function is: {function_prime}",}
            context={**context,**context_e}

    return render(request, 'input_output_numerical_analysis.html', context)


# pc methods

def milve_adams_pc_method(request):
    context = {
            'input_info':f"For IVP, dy/dx=f(x,y) x ∈ [a,b], y'(a)= y{sub('0')} with step-size (h)",
            'screen_info':'Switch to desktop mode for better plot!',
            'input_user_data':True,
            'function_prime': "Enter IVP equation dy/dx ",
            'initial_x': "Enter initial point of domain (a)",
            'final_x': "Enter final point of domain (b)",
            'initial_y': f"Enter y{sub('0')}",
            'step_size': "Enter step size(h)",
            'accuracy':'Accurate up-to [for 5 decimal points i.e. 0.00001, enter 5] ',
            'method':'Choose a method to find initial value to start with pc methods (if you have initial required  values, choose first option).',
            'how_to_input':how_to_input,
            'decide_step_size':decide_step_size_multistep,
            'method_theory':milve_adams_pc_theory()+source_of_info(),
            'method_name': 'Milve Adams PC methods',
            'topic_name': 'numerical differentiation',
            'title':' P-C Methods',
    }
    if request.method == 'POST':
        function_prime=request.POST.get('function_prime')
        try:
            fun = simplify(function_prime)
            x_values=False
            y_values=False
            initial_x=False
            initial_y=False
            user_input=False
            try:
                initial_x = eval(request.POST.get('initial_x'))
            except:
                x_values=request.POST.get('x_values')
            try:
                initial_y = eval(request.POST.get('initial_y'))
            except:
                y_values=request.POST.get('y_values')
            if x_values:
                x_values = re.findall(r"[-+]?\d*\.\d+|\d+",x_values)
                x_values = [float(x) for x in x_values]
            if y_values:
                y_values = re.findall(r"[-+]?\d*\.\d+|\d+",y_values)
                y_values = [float(x) for x in y_values]
            if x_values and y_values:
                if len(x_values)!=len(y_values) or len(x_values)!=4:
                    input_error=f"There is some error with input of initial data. Make sure (1) Input is separated by space or comma (2) No. of x-points = No. of y-points = 4 (3) Try again after refreshing page."
                    context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                    context={**context,**context_e}
                    return render(request, 'input_output_numerical_analysis.html', context)
                else:
                    user_input=[[x,y] for x, y in zip(x_values,y_values)]
            final_x = eval(request.POST.get('final_x'))
            accuracy =eval(request.POST.get('accuracy'))
            step_size=eval(request.POST.get('step_size'))
            method=(request.POST.get('method'))  #methods to find some initial requied data
            if initial_x:
                if(initial_x>=final_x):
                    input_error=f"ERROR : For x ∈ [a,b] , make a<b !"
                    context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                    context={**context,**context_e}
                    return render(request, 'input_output_numerical_analysis.html', context)
                
            with Manager() as manager:
                    result = manager.list()
                    process = Process(target=milve_adams_pc_function, args=(result,), kwargs={ 'initial_x': initial_x, 'accuracy': accuracy,'final_x':final_x, 'function': fun,'initial_y':initial_y,'step_size':step_size,'method':method,'user_input':user_input})
                    process.start()
                    process.join(timeout)
                    print(result)

                    if process.is_alive():
                        process.terminate()
                        context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                        context={**context_timeout,**context}

                    elif result[0]==-1:
                        input_error=f"{result[1]}"
                        context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                        context={**context_error,**context}

                    else:
                        final_result=result[0]
                        detail_solution=result[1]
                        try:
                            x_axis=[float(r(value[0],accuracy)) for value in final_result]
                            y_axis=[float(r(value[1],accuracy)) for value in final_result]
                            fig=go.Figure()
                            fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"y(x{sub('i')})" )
                            fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers'))
                            fig=fig.to_html(full_html=False ,config=custom_config)
                        except:
                            fig="Failed To Plot!"
                        headings_intermediate_result=[f"x{sub('i')}", f"y(x{sub('i')})"]
                        headings=[f"x{sub('i')}", f"y(x{sub('i')}) [corrector]"]
                    
                        intermediate_result=final_result[:4] 
                        final_result=final_result[4:]
                        context_output={'final_result':final_result, 'detail_solution':detail_solution,'intermediate_result':intermediate_result,'fun':f'Given function is {fun}','headings':headings,'plot':fig,'headings_intermediate_result':headings_intermediate_result,} 
                        context={**context_output,**context}
                        
                    return render(request, 'input_output_numerical_analysis.html', context)

        except Exception as e:
            input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.||Make sure variables are only 'x' or 'y'."
            context_e = {'input_error':input_error,'fun': f"Your function is: {function_prime}",}
            context={**context,**context_e}
        
    return render(request, 'input_output_numerical_analysis.html', context)

def adams_bashforth_pc_method(request):
    context = {
            'input_info':f"For IVP, dy/dx=f(x,y) x ∈ [a,b], y'(a)= y{sub('0')} with step-size (h)",
            'screen_info':'Switch to desktop mode for better plot!',
            'input_user_data':True,
            'function_prime': "Enter IVP equation dy/dx ",
            'initial_x': "Enter initial point of domain (a)",
            'final_x': "Enter final point of domain (b)",
            'initial_y': f"Enter y{sub('0')}",
            'step_size': "Enter step size(h)",
            'accuracy':'Accurate up-to [for 5 decimal points i.e. 0.00001, enter 5] ',
            'method':'Choose a method to find initial value to start with pc methods (if you have initial required     values, chosse first option).',
            'how_to_input':how_to_input,
            'decide_step_size':decide_step_size_multistep,
            'method_theory':adams_bashforth_moulton_pc_theory()+source_of_info(),
            'method_name': 'Adams-Bashforth PC methods',
            'topic_name': 'numerical differentiation',
            'title':' P-C Methods'
    }
    if request.method == 'POST':
        function_prime=request.POST.get('function_prime')
        try:
            fun = simplify(function_prime)
            x_values=False
            y_values=False
            initial_x=False
            initial_y=False
            user_input=False
            try:
                initial_x = eval(request.POST.get('initial_x'))
            except:
                x_values=request.POST.get('x_values')
            try:
                initial_y = eval(request.POST.get('initial_y'))
            except:
                y_values=request.POST.get('y_values')
            if x_values:
                x_values = re.findall(r"[-+]?\d*\.\d+|\d+",x_values)
                x_values = [float(x) for x in x_values]
            if y_values:
                y_values = re.findall(r"[-+]?\d*\.\d+|\d+",y_values)
                y_values = [float(x) for x in y_values]
            if x_values and y_values:
                if len(x_values)!=len(y_values) or len(x_values)!=4:
                    input_error=f"There is some error with input of initial data. Make sure (1) Input is separated by space or comma (2) No. of x-points = No. of y-points = 4 (3) Try again after refreshing page."
                    context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                    context={**context,**context_e}
                    return render(request, 'input_output_numerical_analysis.html', context)
                else:
                    user_input=[[x,y] for x, y in zip(x_values,y_values)]
            final_x = eval(request.POST.get('final_x'))
            accuracy =eval(request.POST.get('accuracy'))
            step_size=eval(request.POST.get('step_size'))
            method=(request.POST.get('method'))  #methods to find some initial requied data
            if initial_x:
                if(initial_x>=final_x):
                    input_error=f"ERROR : For x ∈ [a,b] , make a<b !"
                    context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                    context={**context,**context_e}
                    return render(request, 'input_output_numerical_analysis.html', context)
                
            with Manager() as manager:
                    result = manager.list()
                    process = Process(target=adams_bashforth_pc_function, args=(result,),kwargs={ 'initial_x': initial_x, 'accuracy': accuracy,'final_x':final_x, 'function': fun,'initial_y':initial_y,'step_size':step_size,'method':method,'user_input':user_input})
                    process.start()
                    process.join(timeout)

                    if process.is_alive():
                        process.terminate()
                        context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                        context={**context_timeout,**context}

                    elif result[0]==-1:
                        input_error=f"{result[1]}"
                        context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                        context={**context_error,**context}

                    else:
                        final_result=result[0]
                        detail_solution=result[1]
                        try:
                            x_axis=[float(r(value[0],accuracy)) for value in final_result]
                            y_axis=[float(r(value[1],accuracy)) for value in final_result]
                            fig=go.Figure()
                            fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"y(x{sub('i')})" )
                            fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers'))
                            fig=fig.to_html(full_html=False ,config=custom_config)
                        except:
                            fig="Failed To Plot!"
                        headings_intermediate_result=[f"x{sub('i')}", f"y(x{sub('i')})"]
                        headings=[f"x{sub('i')}", f"y(x{sub('i')}) [corrector]"]
                    
                        intermediate_result=final_result[:4] 
                        final_result=final_result[4:]
                        context_output={'final_result':final_result, 'detail_solution':detail_solution,'intermediate_result':intermediate_result,'fun':f'Given function is {fun}','headings':headings,'plot':fig,'headings_intermediate_result':headings_intermediate_result,} 
                        context={**context_output,**context}

                    return render(request, 'input_output_numerical_analysis.html', context)
           
        except Exception as e:
            input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.||Make sure variables are only 'x' or 'y'."
            context_e = {'input_error':input_error,'fun': f"Your function is: {function_prime}",}
            context={**context,**context_e}

    return render(request, 'input_output_numerical_analysis.html', context)



# under consideration

def adams_moulton_method(request): #implicit method
    context = {
            'input_info':f"For IVP, dy/dx=f(x,y) x ∈ [a,b], y'(a)= y{sub('0')} with step-size (h)",
            'screen_info':'Switch to desktop mode for better plot!',
            'function_prime': "Enter IVP equation dy/dx ",
            'initial_x': "Enter initial point of domain (a)",
            'final_x': "Enter final point of domain (b)",
            'initial_y': f"Enter y{sub('0')}",
            'step_size': "Enter step size(h)",
            'accuracy':'Accurate up-to [for 5 decimal points i.e. 0.00001, enter 5] ',
            'method':'Choose a method to find initial value to start with this methods.',
            'order_of_method':'Choose a order of adams-moulton method.',
            'how_to_input':how_to_input,
            'decide_step_size':decide_step_size_multistep,
            'method_theory':adams_moulton_theory()+source_of_info(),
            'method_name': 'Adams-Moulton-Implict methods',
            'topic_name': 'numerical differentiation',
            'title':' Adams-Moulton Methods'
    }
    if request.method == 'POST':
        function_prime=request.POST.get('function_prime')
        try:
            fun = simplify(function_prime)
            initial_x = eval(request.POST.get('initial_x'))
            initial_y = eval(request.POST.get('initial_y'))
            final_x = eval(request.POST.get('final_x'))
            accuracy = eval(request.POST.get('accuracy'))
            step_size=eval(request.POST.get('step_size'))
            method=request.POST.get('method')  #methods to find some initial requied data
            order_of_method=(request.POST.get('order_of_method'))
            if(initial_x>=final_x):
                input_error=f"For x ∈ [a,b], a<b"
                context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                context={**context,**context_e}
                return render(request, 'input_output_numerical_analysis.html', context)
            
            with Manager() as manager:
                    result = manager.list()
                    process = Process(target=adams_moulton_function, args=(result,),  kwargs={ 'initial_x': initial_x,'accuracy':accuracy, 'function': fun,'initial_y':initial_y,'step_size':step_size,'method':method,'order_of_method':order_of_method,'final_x':final_x})
                    process.start()
                    process.join(timeout)

                    if process.is_alive():
                        process.terminate()
                        context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                        context={**context_timeout,**context}

                    elif result[0]==-1:
                        input_error=f"{result[1]}"
                        context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                        context={**context_error,**context}

                    else:
                        final_result=result[0]
                        detail_solution=result[1]
                        try:
                            x_axis=[float(r(value[0],accuracy)) for value in final_result]
                            y_axis=[float(r(value[1],accuracy)) for value in final_result]
                            fig=go.Figure()
                            fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"y(x{sub('i')})" )
                            fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers'))
                            fig=fig.to_html(full_html=False ,config=custom_config)
                        except:
                            fig="Failed To Plot!"
                        headings=[f"x{sub('i')}", f"y(x{sub('i')})"]
                    
                        intermediate_result=final_result[:int(order_of_method)+1]  #since it is implict method
                        final_result=final_result[int(order_of_method)+1:]
                        context_output={'final_result':final_result, 'detail_solution':detail_solution,'intermediate_result':intermediate_result,'fun':f'Given function is {fun}','headings':headings,'plot':fig,'headings_intermediate_result':headings,} 
                        context={**context_output,**context}

                    return render(request, 'input_output_numerical_analysis.html', context)

        except Exception as e:
            input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.||Make sure variables are only 'x' or 'y'."
            context_e = {'input_error':input_error,'fun': f"Your function is: {function_prime}",}
            context={**context,**context_e}
       
    return render(request, 'input_output_numerical_analysis.html', context)


def milve_simpson_method(request):
    context = {
            'input_info':f"For IVP, dy/dx=f(x,y) x ∈ [a,b], y'(a)= y{sub('0')} with step-size (h)",
            'screen_info':'Switch to desktop mode for better plot!',
            'function_prime': "Enter IVP equation dy/dx ",
            'initial_x': "Enter initial point of domain (a)",
            'final_x': "Enter final point of domain (b)",
            'initial_y': f"Enter y{sub('0')}",
            'step_size': "Enter step size(h)",
            'accuracy':'Accurate up-to [for 5 decimal points i.e. 0.00001, enter 5] ',
            'method':'Choose a method to find initial value to start with this methods.',
            'how_to_input':how_to_input,
            'decide_step_size':decide_step_size_multistep,
            'method_theory':milne_theory()+source_of_info(),
            'method_name': f"Milve Simpson-Implict 4{super('th')} order method",
            'topic_name': 'numerical differentiation',
            'title':' Milve Simpson Method'
    }
    if request.method == 'POST':
        function_prime=request.POST.get('function_prime')
        try:
            fun = simplify(function_prime)
            
            initial_x = eval(request.POST.get('initial_x'))
            initial_y = eval(request.POST.get('initial_y'))
            final_x = eval(request.POST.get('final_x'))
            accuracy = eval(request.POST.get('accuracy'))
            step_size=eval(request.POST.get('step_size'))
            method=request.POST.get('method')  #methods to find some initial requied data    
            if(initial_x>=final_x):
                input_error=f"For x ∈ [a,b], a<b"
                context_e = {'input_error':input_error,'fun': f"Given function is: {function_prime}",}
                context={**context,**context_e}
                return render(request, 'input_output_numerical_analysis.html', context)  
            
            with Manager() as manager:
                    result = manager.list()
                    process = Process(target=milve_simpson_function, args=(result,), kwargs={ 'initial_x': initial_x,'accuracy':accuracy,'function': fun,'initial_y':initial_y,'step_size':step_size,'method':method,'final_x':final_x})
                    process.start()
                    process.join(timeout)

                    if process.is_alive():
                        process.terminate()
                        context_timeout = {'timeout_error': timeout_error,'fun': f"Given function is: {fun}",}
                        context={**context_timeout,**context}

                    elif result[0]==-1:
                        input_error=f"{result[1]}"
                        context_error = {'input_error':input_error,'fun': f"Given function is: {fun}"}
                        context={**context_error,**context}

                    else:
                        final_result=result[0]
                        detail_solution=result[1]
                        try:
                            x_axis=[float(r(value[0],accuracy)) for value in final_result]
                            y_axis=[float(r(value[1],accuracy)) for value in final_result]
                            fig=go.Figure()
                            fig.update_layout(xaxis_title=f"x{sub('i')}", yaxis_title=f"y(x{sub('i')})" )
                            fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers'))
                            fig=fig.to_html(full_html=False ,config=custom_config)
                        except:
                            fig="Failed To Plot!"
                        headings=[f"x{sub('i')}", f"y(x{sub('i')})"]
                    
                        intermediate_result=final_result[:4] 
                        final_result=final_result[4:]
                        context_output={'final_result':final_result, 'detail_solution':detail_solution,'intermediate_result':intermediate_result,'fun':f'Given function is {fun}','headings':headings,'plot':fig,'headings_intermediate_result':headings,} 
                        context={**context_output,**context}
                        
                    return render(request, 'input_output_numerical_analysis.html', context)
            
        except Exception as e: 
            input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.||Make sure variables are only 'x' or 'y'."
            context_e = {'input_error':input_error,'fun': f"Your function is: {function_prime}",}
            context={**context,**context_e}

    return render(request, 'input_output_numerical_analysis.html', context)
