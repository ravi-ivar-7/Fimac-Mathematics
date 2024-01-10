from core.theory_core import sub
from sympy import *

r = round
accuracy = 5
(x, y, z) = symbols('x y z')

def newtons_raphson_function(result, **kwargs):
    f=kwargs['fun']
    accuracy=kwargs['accuracy']
    iterations=kwargs['iterations']
    initial_x=kwargs['initial_x']

    decimal_accuracy = 1 / 10**accuracy
    all_row = []
    all_step = []

    f_diff = f.diff(x)
    this_step = [f"Given function is: {f} and initial guess is {initial_x}"]
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
                all_step.append([f"Hence, x={r(x_n, accuracy)} is the required solution for our function f(x)={f}"])
                all_step.append(["Thank you. Happy Learning!"])
                break

            initial_x = x_n
            count += 1
            iterations -= 1

            if iterations == 0:
                all_step.append(["It seems you need to increase iterations as the function does not converge to its solution yet."])

        return result.extend([all_row, all_step])
    
    except Exception as e:
        return result.extend([-1, f"An error occurred: {str(e)}"])

def secant_function(result,**kwargs):
    try:
        f=kwargs['fun']
        accuracy=kwargs['accuracy']
        iterations=kwargs['iterations']
        x_n=kwargs['initial_x']
        x_x_1=kwargs['final_x']

        f_value=f.subs(x,x_n)
        
        all_row=[]
        this_step=[f"Given function is : {f} with first guess(x{sub('0')})= {x_n} and second guess(x{sub('1')})= {x_n_1}"]
        all_step=[]
        all_step.append(this_step)
        this_step=[f"Formula we are going to use is: x{sub('n+2')}=x{sub('n+1')}-f(x{sub('n+1')})(x{sub('n+1')}-x{sub('n')})/(f(x{sub('n+1')})-f(x{sub('n')})) -------------eq(1)"]
        all_step.append(this_step)
        decimal_accuracy=1/(10**accuracy)
        count=0
        while(iterations):
            x_n_2=r(x_n_1-(f.subs(x,x_n_1)*((x_n_1-x_n))/(f.subs(x,x_n_1)-f.subs(x,x_n))),accuracy)
            f_value=r(f.subs(x,x_n_2),accuracy)
            this_step=[f"For iteration= {count+1} and n={count},  x{sub(str(count+1))}={r(x_n_1,accuracy)}, x{sub(str(count))}={r(x_n,accuracy)} , f(x{sub(str(count))})= {r(f.subs(x,x_n),accuracy)} and f(x{sub(str(count+1))})= {r(f.subs(x,x_n_1),accuracy)}. Putting all these values in eq(1), we get x{sub(str(count+2))}={r((x_n_2),accuracy)} and f(x{sub(str(count+2))})= {r((f_value),accuracy)}. Absolute difference i.e. |x{sub(str(count+2))}-x{sub(str(count+1))}| is {r(abs(x_n_2-x_n_1),accuracy)}"]
            all_step.append(this_step)
            this_row=[r(x_n,accuracy),r(x_n_1,accuracy),r(x_n_2,accuracy),r(f_value,accuracy),r(abs(x_n_2-x_n_1),accuracy)]
            x_n=x_n_1     
            all_row.append(this_row)
            iterations-=1
            if(abs(x_n_2-x_n_1)<decimal_accuracy):
                this_step=[f"Now, in iteration={count+1} and n={count}, we get x{sub(str(count+2))}={r(x_n_1,accuracy)} and f(x{sub(str(count+2))})={f_value} ≅ {r((f_value),accuracy)} , and |x{sub(str(count+2))}-x{sub(str(count+1))}| ≅ {r((x_n_2-x_n),accuracy)}"]
                all_step.append(this_step)
                this_step=[f"Hence, x={r(x_n_2,accuracy)} is the required solution for our function f(x)={f}"]
                all_step.append(this_step)
                this_step=[f"Thank you. Happy Learning!"]
                all_step.append(this_step)
                break
            else:
                x_n_1=x_n_2
            if iterations==0:
                this_step=[f"It seems you need to increase iterations as the function does not converges to it's solution yet."]
                all_step.append(this_step)
            count+=1
   
        return result.extend([all_row, all_step])
    except Exception as e:
        return result.extend([-1,str(e)])

def bisection_function(result, **kwargs):
    try:
        f=kwargs['fun']
        accuracy=kwargs['accuracy']
        iterations=kwargs['iterations']
        a=kwargs['initial_x']
        b=kwargs['final_x']

        decimal_accuracy = 1 / (10 ** accuracy)
        all_row = []
        all_step = []

        this_step = [f"Let m=(a+b)/2 "]
        all_step.append(this_step)

        for i in range(iterations):
            m = r((a + b) / 2, accuracy)
            this_row = [a, m, b, r(abs(b - a), accuracy), r(f.subs(x, a), accuracy), r(f.subs(x, m), accuracy),
                        r(f.subs(x, b), accuracy)]
            all_row.append(this_row)

            if f.subs(x, a) * f.subs(x, m) < 0:
                this_step = [f"In iteration {i + 1}, we have a={a}, b={b}, m={m}, and f(a).f(m) < 0. |a-b| > accuracy. So put b = m."]
                all_step.append(this_step)
                b = m

            if f.subs(x, m) * f.subs(x, b) < 0:
                this_step = [f"In iteration {i + 1}, we have a={a}, b={b}, m={m}, and f(m).f(b) < 0. |a-b| > accuracy. So put a = m."]
                all_step.append(this_step)
                a = m

            if abs(b - a) <= decimal_accuracy:
                this_step = [
                    f"In the previous iteration, we get a={a}, b={b}, and |a-b| = {r(N(abs(b-a), accuracy))} < accuracy. "
                    f"So, the root of the given function is {a}"
                ]
                all_step.append(this_step)
                break

            if i == iterations - 1:
                this_step = [f"It seems you need to increase iterations as the function does not converge to its solution yet."]
                all_step.append(this_step)
                
        return result.extend([all_row, all_step])

    except Exception as e:
        return result.extend([-1,str(e)])

    
