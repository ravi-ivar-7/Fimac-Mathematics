import django
django.setup()
from django.shortcuts import render
from core.theory_core import super
from core.models import PiSearch

filepath= 'static/pi_1_million.txt'

def get_pi_digits(filepath):
    with open(filepath, 'r') as file:
        pi_digits=file.read()
    return pi_digits

def pi_search(number):
    try:
        pi_digits=get_pi_digits(filepath)
        occurrences = 0
        indices = []
        for i in range(len(pi_digits) - len(number) + 1):
            if pi_digits[i:i + len(number)] == number:
                occurrences += 1
                i=str(i+1)+'\t'+',' +'\t'
                indices.append(i)
        return_list=[occurrences,[[f"In 3.1415926535........5779458151 , 3. is excluded from search result and  first index is after decimal (i.e. number at index-one is 1) "],[f"{number} occured for the first time at position {indices[0]}",f"Last-time occurrenced  at  {indices[-1]} "],[f"All Position of occurrence of {number} are "],indices]]      
        return return_list
    except:
        return[-1,f"No occurrence of {number} has been found in 1{super('st')} One-Million digits of \u03C0"]

def pi_search_method(request):
    context={
        'number':'Enter the number to search',
        'method_name': f"Search your lucky number in First One-Million digits of \u03C0.",
        'topic_name': 'Pi Search',
        'title':'Pi Search',
    }
    if request.method=='POST':
        number=request.POST.get('number')
        date=request.POST.get('date')
        PiSearch.objects.create(
            number=number,
            date=date,
        )
        all_data=pi_search(number)
        if all_data[0]==-1:
            context_output={'output_info':all_data[1]}
            context={**context_output,**context}
            return render(request, 'fun_maths.html', context)
        else:
            context_output = {'detail_output':all_data[1],'output_info':f"Number of occurence of {number} is {all_data[0]}. First-time occurrence at {all_data[1][-1][0]} and last occurrence at {all_data[1][-1][-1]}"}
            context={**context,**context_output}
            return render(request, 'fun_maths.html', context)
    return render(request,'fun_maths.html',context)


