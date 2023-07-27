from django.shortcuts import render
from .models import Transacao
from django.http import HttpResponse
import datetime

def home(request):
    data = {}
    data['transacao'] = ['t1', 't2', 't3']
    data ['now'] = datetime.datetime.now()
    #html = "<html><body> It is now %s.</body></html>" % now
    #return HttpResponse(html)
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = 
    return render(request, 'contas/listagem.html')