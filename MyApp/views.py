from django.shortcuts import render

# Create your views here.
def Homepage(request):
    return render(request,'Homepage.html')

def Cadastro(request):
    return render(request,'Cadastro.html')