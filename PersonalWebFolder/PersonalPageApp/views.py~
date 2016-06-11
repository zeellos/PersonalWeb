# -*- coding: iso-8859-15 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.encoding import smart_text
# Create your views here.

def main_page(request):
    
    return render_to_response(
        'index.html', RequestContext(request,{
            'tituloPagina': u'Ronald Miguel Juarez Chambi - Ronald Juarez - Software Engineer - Ingeniero Informático - Developer ',
            'nombreCompleto': u'Ronald Miguel Juarez Chambi',
            'especialidad': u'Ingeniero Informático, PhD Student',
            'universidad': u'Pontificia Universidad Católica del Perú',
            'tituloPrincipal': u'Conóceme',
            'acercaDeMi': u'En mis (3) primeros años como ingeniero adquirí destreza en Seguridad de la Información, Desarrollo Web, Base de Datos y Administración de Sistemas Operativos. Ahora estoy en una nueva etapa de mi carrera, dedicándome a la investigación en procesamiento de imágenes y reconocimiento de patrones en imágenes médicas.',
            'informacionAdicional': u'Me considero una persóna muy versátil, me adapto fácilmente a cualquier situación. Soy un buen compañero de trabajo con potencial a forjar una gran amistad. En lo personal me gusta mucho la música, cualquier lectura analítica y discutir vanalmente sobre política y deportes. No me gusta la aceituna.',
            'especialidad1': u'Desarrollo de Software',
            'especialidad2': u'Sistemas Operativos',
            'especialidad3': u'Ciencias de la Computación',
            'especialidad4': u'Seguridad de la Información',
            'descargarCV' : u'Descargar CV',
            'trayectoriaProfesional': u'Trayectoria',
            'experience': u'Experiencia'
        })
    )
