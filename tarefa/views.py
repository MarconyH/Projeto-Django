from django.shortcuts import render
from tarefa.models import Tarefa

#se a função for para urls se usa request
def home(request):
    tarefas = Tarefa.objects.all()
    
    context = {'tarefas' : tarefas}
    
    return render(request, 'index.html', context)
