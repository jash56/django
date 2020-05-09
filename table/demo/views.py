from django.shortcuts import render
from django.http import HttpResponse
from django import template

register = template.Library()


def home(request):
    return render(request, 'hello.html', {'name':'JASH'})

def tab(request):
    val = int(request.GET['even'])
    ans =  list()
    col = list()

    for i in range(0, (val - 1)):
            ans.append(i)
    
    '''ans =  list()
    ans1 = list()
    ans2 = list()
    c = 1

    for i in range(1, (val-1)):
        if (i % 2 == 0):
            ans.append(i)

    for i in ans:
        ans1.append(i)
        if (c % 13 == 0):
            ans2.append(ans1)
            ans1 = []  
        c = c + 1
    ans2.append(ans1)

    return render(request, 'result.html', {'val': ans2})'''
    return render(request, 'result.html', {'ans': ans, 'col' : 6})