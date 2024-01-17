from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.

def index(request):
    items = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'items':items,
    }
    # return HttpResponse(template.render(context, request))
    return render(request,'food/index.html',context)

  
def item(request):
      
    return HttpResponse('this is item view')



def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context ={
        "item":item
    }

    return render(request,'food/detail.html',context)

    # return HttpResponse("this is item Number is : %s" %item_id)