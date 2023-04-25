from .models import Visitante, Paciente, Habitacion, Piso
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http.response import JsonResponse
import json
# Create your views here.


class PisosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            pisos=list(Piso.objects.filter(id=id).values())
            if len(pisos)>0:
                piso=pisos[0]
                datos={'message':"Succes",'Piso':piso}
            else:
                datos={'message':"Piso no encontrado, acá no es ..."}  
            return JsonResponse(datos)
        else:
            pisos=list(Piso.objects.values())
            if len(pisos)>0:
                datos={'message':"Succes",'Pisos':pisos}
            else:
                datos={'message':"Pisos no encontrados aaaa..."}
            return JsonResponse(datos)

    def post(self, request):
        print(request)
        jd =json.loads(request.body)
        Piso.objects.create(num_piso=jd['num_piso'])
        datos={'message':"Succes"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        pisos = list(Piso.objects.filter(id=id).values())
        if(len(pisos)>0):
            piso = Piso.objects.get(id=id)
            piso.num_piso = jd['num_piso']
            piso.save()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Piso no encontrado eeee..."}
        return JsonResponse(datos)        

    def delete(self, request, id):
        pisos = list(Piso.objects.filter(id=id).values())
        if(len(pisos)>0):
            Piso.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Piso no encontrado ..."}
        return JsonResponse(datos)    

class HabitacionesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            habitaciones=list(Habitacion.objects.filter(id=id).values())
            if len(habitaciones)>0:
                habitacion=habitaciones[0]
                datos={'message':"Succes",'Habitación':habitacion}
            else:
                datos={'message':"habitación no encontrado ..."}
            return JsonResponse(datos)
        else:
            habitaciones=list(Habitacion.objects.values())
            if len(habitaciones)>0:
                datos={'message':"Succes",'Habitaciones':habitaciones}
            else:
                datos={'message':"Habitaciones no encontrados ..."}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        pisos=Piso.objects.get(id=jd['piso'])
        Habitacion.objects.create(num_habitacion=jd['num_habitacion'],
                                  capacidad=jd['capacidad'], 
                                  piso=pisos)
        datos={'message':"Succes"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd= json.loads(request.body)
        habitaciones = list(Habitacion.objects.filter(id=id).values())
        piso=Piso.objects.get(id=jd['piso'])
        if(len(habitaciones)>0):
            habitacion = Habitacion.objects.get(id=id)
            habitacion.num_habitacion = jd['num_habitacion']
            habitacion.capacidad = jd['capacidad']
            habitacion.piso = piso
            habitacion.save()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Visitante no encontrado ..."}
        return JsonResponse(datos)        

    def delete(self, request, id):
        habitacion = list(Habitacion.objects.filter(id=id).values())
        if(len(habitacion)>0):
            Habitacion.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Habitacion no encontrado ..."}
        return JsonResponse(datos)    

class PacientesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            pacientes=list(Paciente.objects.filter(id=id).values())
            if len(pacientes)>0:
                paciente=pacientes[0]
                datos={'Paciente':paciente}
            else:
                datos={'message':"Paciente no encontrados ..."}  
            return JsonResponse(datos)
        else:
            pacientes=list(Paciente.objects.values())
            if len(pacientes)>0:
                datos={'Pacientes':pacientes}
            else:
                datos={'message':"Pacientes no encontrados ..."}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        habita=Habitacion.objects.get(id=jd['habitacion'])
        Paciente.objects.create(cc_paciente=jd['cc_paciente'], nombre=jd['nombre'], habitacion=habita)
        datos={'message':"Succes"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        paciente = list(Paciente.objects.filter(id=id).values())
        habita=Habitacion.objects.get(id=jd['habitacion'])
        if(len(paciente)>0):
            paciente = Paciente.objects.get(id=id)
            paciente.cc_paciente = jd['cc_paciente']
            paciente.nombre = jd['nombre']
            paciente.habitacion = habita
            paciente.save()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Paciente no encontrado ..."}
        return JsonResponse(datos)        

    def delete(self, request, id):
        paciente = list(Paciente.objects.filter(id=id).values())
        if(len(paciente)>0):
            Paciente.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Paciente no encontrado ..."}
        return JsonResponse(datos)    

class VisitantesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        
        Visitante.reg_rostro()

        if (id>0):
            visitantes=list(Visitante.objects.filter(id=id).values())
            if len(visitantes)>0:
                visitante=visitantes[0]
                datos={'message':"Succes",'Visitantes':visitante}
            else:
                datos={'message':"Visitante no encontrados ..."}  
            return JsonResponse(datos)
        else:
            visitantes=list(Visitante.objects.values())
            if len(visitantes)>0:
                datos={'message':"Succes",'Visitantes':visitantes}
            else:
                datos={'message':"Visitantes no encontrados ..."}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        habita=Habitacion.objects.get(id=jd['habitacion'])
        pacientes=Paciente.objects.get(id=jd['paciente'])
        Visitante.objects.create(cc_visitante=jd['cc_visitante'], 
                                 rostro=jd['rostro'], 
                                 estado=jd['estado'],
                                 habitacion=habita,
                                 paciente=pacientes)
        datos={'message':"Succes"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        visitantes = list(Visitante.objects.filter(id=id).values())
        habita=Habitacion.objects.get(id=jd['habitacion'])
        pacientes=Paciente.objects.get(id=jd['paciente'])
        if(len(visitantes)>0):
            visitante = Visitante.objects.get(id=id)
            visitante.cc_visitante = jd['cc_visitante']
            visitante.rostro = jd['rostro']
            visitante.estado = jd['estado']
            visitante.habitacion = habita
            visitante.paciente = pacientes
            visitante.save()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Visitante no encontrado ..."}
        return JsonResponse(datos)        

    def delete(self, request, id):
        visitantes = list(Visitante.objects.filter(id=id).values())
        if(len(visitantes)>0):
            Visitante.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Visitante no encontrado ..."}
        return JsonResponse(datos)    
