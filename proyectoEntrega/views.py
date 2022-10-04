from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template
def persona(request):
    return HttpResponse("<h1>Buenas</h1>")

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_y_hora}')

def mi_template(request):
    cargar_archivo = open(r'C:\Users\Nicolas\OneDrive\Documentos\cursos\python\proyectoclases\templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context() 
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)