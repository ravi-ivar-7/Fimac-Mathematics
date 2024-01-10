to_sup = str.maketrans("0123456789abcdefghijklmnopqrstuvwxyz+-", "⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖˤʳˢᵗᵘᵛʷˣʸᶻ⁺⁻")
to_sub = str.maketrans("0123456789aehijklmnoprstuvx+-", "₀₁₂₃₄₅₆₇₈₉ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ₊₋")
import sympy
def super(text):
    return text.translate(to_sup)
def sub(text):
    return text.translate(to_sub)

def how_to_input():
    input=[f"Make sure that input is given correct to avoid any error. Avoid copy-pasting function."]
    input=input+[f"If e is present in output, like 23e-4 which means 23x10{super('-4')}"]
    input=input+[f"If E is present in output, then it is euler number (E=2.71828)"]
    input=input+[f"If I is present in output, then it is imaginary unit, I{super('2')}=-1"]
    input=input+[f"Be careful while use square root or similar root, might get error if root-value becomes negative or divide by some invalid number."]
    input=input+[f"For multiplication: use * ; for division: use / ; for power : use: ** ; Eulers Number(e) : use exp(),eg: e{super('x')} as exp(x)"]
    input=input+[f"For sinx : use sin(x) and same for other trignometric functions"]
    input=input+[f"For  pi (π), you can use pi word or 3.141592653589793 "]
    input=input+[f"For sin{super('-1')}(x) : use asin(x) and same for other trignometric functions"]
    input=input+[f"For natural base log (i.e ln(function)) : use log(function) "]
    input=input+[f"For log with given base : use log(function,base) or log(function)/log(base)"]
    input=input+[f"Here are some examples to show how to give input:"]
    input=input+[f"(1) If a two variable function is f(x,y)=x{super('2')} + y{super('9')} + 3x + xy +sinx + e{super('-2x')} + log(x{super('4')}) => input as : x**2+y**9+3*x+x*y+sin(x)+exp(-2*x) +log(x**4)"]
    input=input+[f"(2) If a one variable function is f(t) = 2000log{sub('10')}[140000/(140000-2100t)]-9.8t => input as : 2000*log(140000/(140000-2100*x),10)-9.8*x"]
    return input