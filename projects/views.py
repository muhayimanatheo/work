from django . shortcuts import render
from django . http import HttpResponse
from.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')
def oders(request):
    if request.method == 'POST':
        fullname=request.POST['name']
        email=request.POST['email']
        selectproduct=request.POST['product']
        size=request.POST['size']
        quantity=request.POST['quantity']
        comment=request.POST['comment']
        InsertData=Project(fullname=fullname,email=email,products=selectproduct,size=size,quantity=quantity,comment=comment)
        InsertData.save()
    return render(request, 'oders.html')
def Health(request):
    return render(request,'Health.html')
