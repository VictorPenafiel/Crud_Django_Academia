from django.shortcuts import render
from web.models import *
from web.forms import MainForm
from django.http import JsonResponse

# Create your views here.


def index(request): 
    estudiante_datos = Estudiante.objects.all()
    if request.method == 'POST': # Preguntamos si el formulario fue enviado
        forma = MainForm(request.POST)
        region_buscado = request.POST.get('region_selector')
        curso_buscado = request.POST.get('curso_selector')
        print(region_buscado, curso_buscado)

        if curso_buscado != '':
            estudiante_datos = estudiante_datos.filter(codigo_curso = curso_buscado)

    else:
        forma = MainForm()
        estudiante_datos = []
    return render(request, 'form.html', {'estudiantes': estudiante_datos, 'form': forma})


def getregion(request):
    if request.method == "POST":
        codigo_region = request.POST['codigo_region']
        data = {}
        try:
            region = Region.objects.filter(codigo_region=codigo_region)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(curso.values('codigo_curso', 'title')), safe=False)


def detalle(request):
    codigo_curso = request.POST.get('detalle_id')
    print(codigo_curso)
    query = f"""
        select "codigo_curso" = {codigo_curso};
    """
    datos = Curso.objects.raw(query)

    return render(request, 'detalle.html', {'datos': datos[0]})
