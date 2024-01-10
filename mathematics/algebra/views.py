from django.shortcuts import render
from sympy import *
from multiprocessing import Process, Manager
import plotly.graph_objects as go

from core.theory_core import how_to_input,super,sub
from algebra.theory_algebra import secant_theory,newton_raphson_theory
from algebra.functions_algebra import newtons_raphson_function, secant_function, bisection_function

custom_config={'displaylogo':False}
r=round
accuracy=5
timeout = 10
timeout_error = f"ERROR: Time-limit exceeded. Current computation time-limit is {timeout} seconds."
(x, y, z) = symbols('x y z')

def home_algebra(request):
    return render(request, 'home_algebra.html')

def bisection_method(request):
    context = {
        'input_info':f"For a function f(x)=0 with x ∈ [a,b] such that f(a).f(b)<0 ",
        'screen_info':'Switch to desktop mode for better plot!',
        'function': 'Enter function f(x) ',
        'initial_x': "Enter inital point of domain (a)",
        'final_x': "Enter final point of domain (b)",
        'iterations': "No. of iterations to terminate in case of non-converging functions(increase if solution exits but not in given iterations)",
        'accuracy':" Accuracy/tolerance (for 5 decimal point i.e. 0.00001, enter 5):",
        'method_theory':None,
        'how_to_input':how_to_input,
        'method_name': 'Bisection Method',
        'topic_name': 'Algebraic and Transcendetal equations',
        'title':'Bisection Method',
    }
    if request.method == 'POST':
        function = request.POST.get('function')
        try:
            fun = simplify(function)
            accuracy = eval(request.POST.get('accuracy'))
            iterations = eval(request.POST.get('iterations'))
            initial_x = eval(request.POST.get('initial_x'))
            final_x = eval(request.POST.get('final_x'))
            
            if fun.subs(x,initial_x)*fun.subs(x,final_x)>0 :
                input_error=f"Cannot find roots as f(a).f(b)>=0 ."
                context_error = {'input_error':input_error,'fun': f"Given function is: {fun}",}
                context={**context,**context_error}
                return render(request, 'input_output_algebra.html', context)
            if fun.subs(x,initial_x)==0 or fun.subs(x,final_x)==0:
                if fun.subs(x,initial_x)==0:
                    info=f"Value of f({initial_x}) = 0"
                if fun.subs(x,final_x)==0:
                    info=f"Value of f{final_x} = 0"     
                context_output = {'info': info ,'fun': f"Given function is: {fun}",}
                context={**context,**context_output}
                return render(request, 'input_output_algebra.html', context)
            
            with Manager() as manager:
                    result = manager.list()
                    process = Process(target=bisection_function, args=(result,), kwargs={'fun': fun, 'initial_x': initial_x, 'accuracy':accuracy,'iterations':iterations,'final_x':final_x})
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
                        x_axis=[float(r(value[1],accuracy)) for value in final_result]
                        y_axis=[float(r(value[5],accuracy)) for value in final_result]
                        fig=go.Figure()
                        fig.update_layout(xaxis_title=f"m{sub('i')}", yaxis_title=f"f(m{sub('i')})", )
                        fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers'))
                        fig=fig.to_html(full_html=False ,config=custom_config)               
                        headings=['a','m=(a+b)/2','b','|b-a|',f"f(a)",'f(m)','f(b)']
                        context_output = {'final_result': final_result,'detail_solution':detail_solution,'fun':f"Your function is: {fun}",'headings':headings , 'plot':fig,'plot_info':'To see how the root of the function converges.'}
                        context={**context_output,**context}
                        return render(request, 'input_output_algebra.html', context)

        except Exception as e: #invalid input
            input_error=f"ERROR:\n{str(e)}. Check function syntax or other input field. Make sure variables is only 'x' "
            context_error = {'input_error':input_error,'fun': f"Given function is: {function}",}
            context={**context,**context_error}

    return render(request, 'input_output_algebra.html', context)

def newton_raphson_method(request):
    context = {
        'input_info':f"For a function f(x)=0 with initial guess (x{sub('0')})",
        'screen_info':'Switch to desktop mode for better plot!',
        'function': 'Enter function f(x) ',
        'initial_x': f"Enter initial guess (x{sub('0')})",
        'iterations': "No. of iterations to terminate in case of non-converging functions(increase if solution exits but not in given iterations)",
        'accuracy':" Accuracy/tolerance (for 5 decimal point i.e. 0.00001, enter 5):",
        'method_theory':newton_raphson_theory,
        'how_to_input':how_to_input,
        'method_name': 'Neton Raphson Method',
        'topic_name': 'Algebraic and Transcendetal equations',
        'title':'Newton Raphson Method',
    }
    if request.method == 'POST':
        function = request.POST.get('function')
        try:
            fun = simplify(function)
            accuracy = eval(request.POST.get('accuracy'))
            iterations = eval(request.POST.get('iterations'))
            initial_x = eval(request.POST.get('initial_x'))

            with Manager() as manager:
                    result = manager.list()
                    process = Process(target=newtons_raphson_function, args=(result,), kwargs={'fun': fun, 'x_i': initial_x, 'accuracy':accuracy,'iterations':iterations})
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
                        fig.update_layout(xaxis_title='x values', yaxis_title='y values', )
                        fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers',name="x values"))
                        fig=fig.to_html(full_html=False ,config=custom_config)               
                        headings=['x values','y values',f"|x{sub('n+1')}-x{sub('n')}|"]
                        context_output = {'final_result': final_result,'detail_solution':detail_solution,'fun':f"Your function is: {fun}",'headings':headings , 'plot':fig,'plot_info':'To see how the root of the function converges.'}
                        context={**context_output,**context}
                    return render(request, 'input_output_algebra.html', context)

        except Exception as e: #invalid input
            input_error=f"ERROR:\n{str(e)}. Check function syntax or other input field. Make sure variables is only 'x' "
            context_error = {'input_error':input_error,'fun': f"Given function is: {function}",}
            context={**context,**context_error}
    
    return render(request, 'input_output_algebra.html', context)

def secant_method(request):
    context = {
        'input_info':f"For a function f(x)=0 with first guess (x{sub('0')}) and second guess (x{sub('1')})",
        'screen_info':'Switch to desktop mode for better plot!',
        'function': 'Enter function f(x) ',
        'initial_x': f"Enter first guess (x{sub('0')})",
        'final_x':f"Enter second guess (x{sub('1')})",
        'iterations': "No. of iterations to terminate in case of non-converging functions(increase if solution exits but not in given iterations)",
        'accuracy':" Accuracy/tolerance (for 5 decimal point i.e. 0.00001, enter 5):",
        'method_theory':secant_theory,
        'how_to_input':how_to_input,
        'method_name': 'Secant Method',
        'topic_name': 'Non-liner and Transcendetal equations',
        'title':'Secant Method',
    }
    if request.method == 'POST':
        function = request.POST.get('function')
        try:
            fun = simplify(function)
            accuracy = eval(request.POST.get('accuracy'))
            iterations = eval(request.POST.get('iterations'))
            initial_x = eval(request.POST.get('initial_x'))#x_n_minus_1
            final_x = eval(request.POST.get('final_x')) #x_n

            with Manager() as manager:
                    result = manager.list()
                    process = Process(target=secant_function, args=(result,), kwargs={'fun': fun, 'initial_x': initial_x, 'accuracy':accuracy,'iterations':iterations,'final_x':final_x})
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
                        fig.update_layout(xaxis_title='x values', yaxis_title='y values', )
                        fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode='lines+markers',name="x values"))
                        fig=fig.to_html(full_html=False ,config=custom_config)
                        headings=[f'x{sub("n")}',f'x{sub("n+1")}',f'x{sub("n+2")}',f'f(x{sub("n+2")})',f'|x{sub("n+2")}-x{sub("n+1")}|']
                        context_output = {'final_result': final_result,'detail_solution':detail_solution,'fun':f"Given function is: {fun}",'headings':headings , 'plot':fig,'plot_info':'To see how the root of the function converges.'}
                        context={**context_output,**context}
                    return render(request, 'input_output_algebra.html', context)

        except Exception as e: #invalid input
            input_error=f"ERROR:\n{str(e)}. Check function syntax or other input field. Make sure variables is only 'x'"
            context_e = {'input_error':input_error,'fun': f"Given function is: {function}",}
            context={**context,**context_e}
    return render(request, 'input_output_algebra.html', context)
                        
