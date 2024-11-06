from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from map.models import User

def map(request):
   
    template = loader.get_template('first.html')
    details = User.objects.all().values()
    context={
        'details' : details,
        'person1' : details[0],
        'person2' : details[1], 
        'person3' : details[2], 
        'person4' : details[3],  
        'fruits'  : ["apple", "banana", "cherry"],
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'first.html', context)
def map2(request):
   
    template = loader.get_template('second.html')
    
    
    
    return HttpResponse(template.render())
    # return render(request, 'first.html', context) 
