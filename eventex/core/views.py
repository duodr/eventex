from django.shortcuts import render

# TODO Teste
def home(request):
    return render(request, 'index.html')