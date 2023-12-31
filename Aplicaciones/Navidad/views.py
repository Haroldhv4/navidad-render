from django.shortcuts import render
from .models import Cliente
# Create your views here.
#Vista principal y las 5 vistas de: Harold
def home(request):
    clientesBdd=Cliente.objects.all()
    return render(request,"index.html",{'clientes':clientesBdd})

def pagina(request):
    contexto={
        'variable': ' Hola desde la vista',
    }
    return render(request,"1.html",contexto)

def texto(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"2.html",contexto)

def libro(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"3.html",contexto)

def cuaderno(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"4.html",contexto)

def libreta(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"5.html",contexto)
#Vistas de: Gary
def vista(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"gary.html",contexto)

def uno(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"gary1.html",contexto)

def dos(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"gary2.html",contexto)

def tres(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"gary3.html",contexto)

def cuatro(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"gary4.html",contexto)

#Vista de: Viviana

def eve(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"eve.html",contexto)

def eve1(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"eve1.html",contexto)

def eve2(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"eve2.html",contexto)

def eve3(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"eve3.html",contexto)

def eve4(request):
    contexto={
        'variable': 'Hola desde la vista',
    }
    return render(request,"eve4.html",contexto)
