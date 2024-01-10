
from sympy import *
from core.theory_core import sub

# to_sup = str.maketrans("0123456789abcdefghijklmnopqrstuvwxyz+-", "⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖˤʳˢᵗᵘᵛʷˣʸᶻ⁺⁻")
# to_sub = str.maketrans("0123456789aehijklmnoprstuvx+-", "₀₁₂₃₄₅₆₇₈₉ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ₊₋")

# def super(text):
#     return text.translate(to_sup)
# def sub(text):
#     return text.translate(to_sub)

r = round
accuracy = 5
(x, y, z) = symbols('x y z')

# @timeout(10)
def newtons_raphson(function, accuracy, iterations, initial_x):
    decimal_accuracy = 1 / 10**accuracy
    all_row = []
    all_step = []

    f = function
    f_diff = f.diff(x)
    this_step = [f"Given function is: {function} and initial guess is {initial_x}"]
    all_step.append(this_step)
    this_step = [f"The first derivative of f(x) is: {f_diff}"]
    all_step.append(this_step)
    this_step = [f"Formula we will be using is: x{sub('n+1')}=x{sub('n')}-f(x{sub('n')})/f'(x{sub('n')})-------eq(1)"]
    all_step.append(this_step)

    count = 0
    try:
        while iterations:
            x_n = initial_x - f.subs(x, initial_x) / f_diff.subs(x, initial_x)
            f_value = f.subs(x, x_n)
            all_row.append([r(x_n, accuracy), r(f_value, accuracy), r(abs(x_n - initial_x), accuracy)])

            this_step = [
                f"For iteration={count + 1} and n={count}, "
                f"x{sub(str(count))}={r(initial_x, accuracy)}, "
                f"f(x{sub(str(count))})={r(f.subs(x, initial_x), accuracy)}, "
                f"f'(x{sub(str(count))})={r(f_diff.subs(x, initial_x), accuracy)}. "
                f"Putting all these values in eq(1), we get "
                f"x{sub(str(count + 1))}={r(x_n, accuracy)}, "
                f"f(x{sub(str(count + 1))})={r(f_value, accuracy)}. "
                f"Absolute difference i.e. |x{sub(str(count + 1))}-x{sub(str(count))}| is {r(x_n - initial_x, accuracy)}"
            ]
            all_step.append(this_step)

            if abs(x_n - initial_x) < decimal_accuracy:
                this_step = [
                    f"Now, in iteration={count + 1}, for n={count}, we get "
                    f"x{sub(str(count + 1))}={r(x_n, accuracy)} and "
                    f"f(x{sub(str(count + 1))})={r(f_value, accuracy)}. "
                    f"Absolute difference |x{sub(str(count + 1))}-x{sub(str(count))}| is {r(abs(x_n - initial_x), accuracy)}"
                ]
                all_step.append(this_step)
                all_step.append([f"Hence, x={r(x_n, accuracy)} is the required solution for our function f(x)={function}"])
                all_step.append(["Thank you. Happy Learning!"])
                break

            initial_x = x_n
            count += 1
            iterations -= 1

            if iterations == 0:
                all_step.append(["It seems you need to increase iterations as the function does not converge to its solution yet."])

    except TimeoutError:
        all_step.append(["Function execution timed out."])

    return [all_row, all_step]

from concurrent.futures import ThreadPoolExecutor, TimeoutError
with ThreadPoolExecutor() as executor:
    try:
        # Use submit to execute the function with arguments and set a timeout
        future = executor.submit(newtons_raphson, x**2, 5, 5, 2)
        # Get the result with a timeout
        result = future.result(timeout=0.0000001)
        print(result)
    except TimeoutError as e:
        print(f"Function execution timed out.{e}")