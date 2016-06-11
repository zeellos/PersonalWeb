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
            'experience': u'Experiencia',
            'trabajo3cabecera': u'Grupo de Reconocimiento de Patrones e Inteligencia Artificial - GRPIAA',
            'trabajo3titulo' : u'PUCP - 2014 - Actalidad',
            'trabajo3descripcion' : u'Me desempeño como investigador en métodos para caracterización de imágenes basado en formas, he trabajado con redes complejas, fractales para el reconocimiento de plantas endemicas basadas en el contorno, nervadura y texturas de las hojas.',
            'trabajo2cabecera': u'Desarrollador Aplicaciones Web y Administración de Base de Datos',
            'trabajo2titulo' : u'Engage Software Company, 2013-2014',
            'trabajo2descripcion' : u'Desarrollo de sistema de ventas de tarjetas de crédito en banco BCP del Perú, Financiera CrediQ - El Salvador, utilizando tecnologia .NET, Webservices SOAP, SQL SERVER, Javascript.',
            'trabajo1cabecera': u'Analista de Seguridad, Implementación ISO 27001',
            'trabajo1titulo' : u'Ministerio de Transportes y Comunicaciones, 2012',
            'trabajo1descripcion' : u'Desarrollo de políticas, lineamientos y procesos para Tecnologías de Información, Aseguramiento de la Calidad (QA) y Sistemas de Información (SI)',
            'educacion' : u'Educación',
            'estudio3cabecera': u'Estudiante de Doctorado',
            'estudio3titulo' : u'Texas A&M University 2015 - Actualidad',
            'estudio3descripcion' : u'Mi campo de investigación es la caracterización de imágenes medicas para el diagnóstico temprano de cancer en tejido cerebral (gliomas), utilizando técnicas de relección de imágenes como OCT y FLIM',
            'estudio2cabecera': u'Ingeniero Informático',
            'estudio2titulo' : u'Pontificia Universidad Católica del Perú 2008 - 2013',
            'estudio2descripcion' : u'Durante mi formación como ingeniero adquirí habilidades en desarrollo de software, diseño e implementación de lineamientos de Tecnologías de la Información, así como en Ciencias de la Computación',
#            'estudio1cabecera': u'Ingeniero Informático',
#            'estudio1titulo' : u'Pontificia Universidad Católica del Perú 2008 - 2013',
#            'estudio1descripcion' : u'Durante mi formación como ingeniero adquirí habilidades en desarrollo de software, diseño e implementación de lineamientos de Tecnologías de la Información, así como en Ciencias de la Computación',
            'habilidades': u'Habilidades',
            'habilidades1titulo':u'Desarrollo Web',
            'habilidades1Descripcion':u'Experiencia en .NET, Python Django, PHP.',
            'habilidades2titulo':u'Base de Datos',
            'habilidades2Descripcion':u'Dominio en T-SQL, PL-SQL (Oracle), MySQL, PostgreSQL, MongoDB',
            'habilidades3titulo':u'Computación Científica',
            'habilidades3Descripcion':u'MATLAB, R programming, OpenCV, SVMLib, Weka Tool, Etc',
            'habilidades4titulo':u'Otros',
            'habilidades4Descripcion':u'Sistemas Operativos Windows y Linux (Nivel Adminstrador), ISO 27000 Series',
        })
    )
