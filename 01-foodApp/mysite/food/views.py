from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemFrom

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


def createItem(request):
    form = ItemFrom(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,"food/item-form.html",{'form':form})


def update_item(request,id):
    item = Item.objects.get(id=id)
    form=ItemFrom(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,"food/item-form.html",{'form':form,'item':item})


def delete_item(request,id):
    item = Item.objects.get(id=id)

    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})