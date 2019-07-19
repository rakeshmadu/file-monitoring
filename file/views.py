from django.shortcuts import render,redirect
from .models import Register,Display,Fir_Details
from .forms import RegForm,Loginform,FirForm
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def reg(request):
    form = RegForm()
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(login)
    return render(request,'reg.html',{"form":form})

def login(request):
    form = Loginform()
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                dbuser = Register.objects.get(username = username,password = password)
                if dbuser:
                    if dbuser.designation == 'SI':
                        return render(request,"index.html")
                    elif dbuser.designation == 'DSP':
                        return render(request,"index.html")
                    elif dbuser.designation == 'DIGP':
                        return render(request,"index.html")
                    else:
                        return HttpResponse("No access")
            except Register.DoesNotExist:
                return render(request, 'login.html',{"msg":"UserName and Password Does Not Match"})
    return render(request,'login.html',{'form':form})

def home(request):
    form = Display.objects.all()
    return render(request,'home.html',{'form':form})

def fir(request):
    form = FirForm()
    if request.method == 'POST':
        form = FirForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'reg1.html',{"msg":"fir details successfully submited"})
    return render(request,'reg1.html',{'form':form})

# @login_required
def display_view(request):
    employee = Fir_Details.objects.all()
    return render(request,"result.html",{'form':employee})

def delete_view(request,id):
    employee = Fir_Details.objects.get(id=id)
    employee.delete()
    return redirect('/display')

def update_view(request, id):
    form = Fir_Details.objects.get(id = id)
    if request.method == "POST":
        form = FirForm(request.POST, instance = form)
        if form.is_valid():
            form.save()
        return redirect("/display")  
    return render(request, 'update.html', {'employee':form})

def search_view(request):
    query = request.POST['q']
    object_list = Fir_Details.objects.filter(Q(fir_number__iexact = query) | Q(police_station_code__iexact = query))
    return render(request, 'search.html',{'form':object_list})

def search2_view(request):
    query = request.POST['x']
    object_list = Display.objects.filter(Q(number_id__iexact = query))
    return render(request, 'search2.html',{'form':object_list})