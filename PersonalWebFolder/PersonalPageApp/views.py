# -*- coding: iso-8859-15 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.encoding import smart_text
# Create your views here.

def main_page(request):
    
    return render_to_response(
        'index.html', RequestContext(request,{
            'tituloPagina': u'Ronald Miguel Juarez Chambi - Ronald Juarez - Software Engineer - Ingeniero Inform�tico - Developer ',
            'nombreCompleto': u'Ronald Miguel Juarez Chambi',
            'especialidad': u'Ingeniero Inform�tico, PhD Student',
            'universidad': u'Pontificia Universidad Cat�lica del Per�',
            'tituloPrincipal': u'Con�ceme',
            'acercaDeMi': u'En mis (3) primeros a�os como ingeniero adquir� destreza en Seguridad de la Informaci�n, Desarrollo Web, Base de Datos y Administraci�n de Sistemas Operativos. Ahora estoy en una nueva etapa de mi carrera, dedic�ndome a la investigaci�n en procesamiento de im�genes y reconocimiento de patrones en im�genes m�dicas.',
            'informacionAdicional': u'Me considero una pers�na muy vers�til, me adapto f�cilmente a cualquier situaci�n. Soy un buen compa�ero de trabajo con potencial a forjar una gran amistad. En lo personal me gusta mucho la m�sica, cualquier lectura anal�tica y discutir vanalmente sobre pol�tica y deportes. No me gusta la aceituna.',
            'especialidad1': u'Desarrollo de Software',
            'especialidad2': u'Sistemas Operativos',
            'especialidad3': u'Ciencias de la Computaci�n',
            'especialidad4': u'Seguridad de la Informaci�n',
            'descargarCV' : u'Descargar CV',
            'trayectoriaProfesional': u'Trayectoria',
            'experience': u'Experiencia',
            'trabajo3cabecera': u'Grupo de Reconocimiento de Patrones e Inteligencia Artificial - GRPIAA',
            'trabajo3titulo' : u'PUCP - 2014 - Actalidad',
            'trabajo3descripcion' : u'Me desempe�o como investigador en m�todos para caracterizaci�n de im�genes basado en formas, he trabajado con redes complejas, fractales para el reconocimiento de plantas endemicas basadas en el contorno, nervadura y texturas de las hojas.',
            'trabajo2cabecera': u'Desarrollador Aplicaciones Web y Administraci�n de Base de Datos',
            'trabajo2titulo' : u'Engage Software Company, 2013-2014',
            'trabajo2descripcion' : u'Desarrollo de sistema de ventas de tarjetas de cr�dito en banco BCP del Per�, Financiera CrediQ - El Salvador, utilizando tecnologia .NET, Webservices SOAP, SQL SERVER, Javascript.',
            'trabajo1cabecera': u'Analista de Seguridad, Implementaci�n ISO 27001',
            'trabajo1titulo' : u'Ministerio de Transportes y Comunicaciones, 2012',
            'trabajo1descripcion' : u'Desarrollo de pol�ticas, lineamientos y procesos para Tecnolog�as de Informaci�n, Aseguramiento de la Calidad (QA) y Sistemas de Informaci�n (SI)',
            'educacion' : u'Educaci�n',
            'estudio3cabecera': u'Estudiante de Doctorado',
            'estudio3titulo' : u'Texas A&M University 2015 - Actualidad',
            'estudio3descripcion' : u'Mi campo de investigaci�n es la caracterizaci�n de im�genes medicas para el diagn�stico temprano de cancer en tejido cerebral (gliomas), utilizando t�cnicas de relecci�n de im�genes como OCT y FLIM',
            'estudio2cabecera': u'Ingeniero Inform�tico',
            'estudio2titulo' : u'Pontificia Universidad Cat�lica del Per� 2008 - 2013',
            'estudio2descripcion' : u'Durante mi formaci�n como ingeniero adquir� habilidades en desarrollo de software, dise�o e implementaci�n de lineamientos de Tecnolog�as de la Informaci�n, as� como en Ciencias de la Computaci�n',
#            'estudio1cabecera': u'Ingeniero Inform�tico',
#            'estudio1titulo' : u'Pontificia Universidad Cat�lica del Per� 2008 - 2013',
#            'estudio1descripcion' : u'Durante mi formaci�n como ingeniero adquir� habilidades en desarrollo de software, dise�o e implementaci�n de lineamientos de Tecnolog�as de la Informaci�n, as� como en Ciencias de la Computaci�n',
            'habilidades': u'Habilidades',
            'habilidades1titulo':u'Desarrollo Web',
            'habilidades1Descripcion':u'Experiencia en .NET, Python Django, PHP.',
            'habilidades2titulo':u'Base de Datos',
            'habilidades2Descripcion':u'Dominio en T-SQL, PL-SQL (Oracle), MySQL, PostgreSQL, MongoDB',
            'habilidades3titulo':u'Computaci�n Cient�fica',
            'habilidades3Descripcion':u'MATLAB, R programming, OpenCV, SVMLib, Weka Tool, Etc',
            'habilidades4titulo':u'Otros',
            'habilidades4Descripcion':u'Sistemas Operativos Windows y Linux (Nivel Adminstrador), ISO 27000 Series',
        })
    )
