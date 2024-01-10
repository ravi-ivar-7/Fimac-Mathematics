from django.shortcuts import render
from sympy import *
from multiprocessing import Process, Manager
import plotly.graph_objects as go

from core.theory_core import how_to_input,super,sub
from calculus.functions_calculus import indefinite_integral_function

custom_config={'displaylogo':False}
r=round
accuracy=5
timeout = 10
timeout_error = f"ERROR: Time-limit exceeded. Current computation time-limit is {timeout} seconds.||Reduce no. of iterations or accuracy.||Avoid using any random function."
(x, y, z) = symbols('x y z')

def home_calculus(request):
    return render(request, 'home_calculus.html')


def indefinite_integral(request):
    context = {
        'input_info':"For  ∫f(x) " ,
        'function': "Enter function f(x) ",
        'target_x': "Find value of integral at x=",
        'how_to_input':how_to_input,
        'method_name': 'Indefinite Integration',
        'topic_name': 'calculus one',
        'title': 'Indefinite Integration',
    }
    if request.method == 'POST':
        function = request.POST.get('function')
        try:
            fun = simplify(function)
            target_x = eval(request.POST.get('target_x'))

            with Manager() as manager:
                    result = manager.list()
                    process = Process(target=indefinite_integral_function, args=(result,), kwargs={'function':fun,'target_x':target_x})
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
                        context_output = {'detail_solution':result ,'fun': f"Given function is: {fun}",}
                        context={**context_output,**context}

                    return render(request, 'input_output_calculus.html', context)
            
        except Exception as e: 
            input_error=f"ERROR:\n{str(e)} ||Check function syntax or other input field.|| Make sure variable are only x and y."
            context_error = {'input_error':input_error,'fun': f"Given function is: {function}"}
            context={**context_error,**context}

    return render(request, 'input_output_calculus.html', context)