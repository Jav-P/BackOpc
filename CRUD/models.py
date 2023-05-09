from django.db import models

from tkinter import *
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import numpy as np

import PIL.Image as Image
import io
import base64

# Create your models here.

class Piso(models.Model):
    num_piso=models.PositiveIntegerField()  
    class Meta:
        db_table='piso'

class Habitacion(models.Model):
    num_habitacion=models.PositiveIntegerField(unique=True)
    capacidad=models.PositiveIntegerField()
    piso=models.ForeignKey(Piso, on_delete=models.CASCADE,
                            null=False, blank=False, 
                            related_name='habitaciones')
        
    class Meta:
        db_table='habitacion'
    
class Paciente(models.Model):
    cc_paciente=models.PositiveIntegerField()
    nombre=models.CharField(max_length=20)
    habitacion = models.OneToOneField(Habitacion, on_delete=models.CASCADE, 
                                      null=False, blank=False, 
                                      related_name='pacientes')
    class Meta:
        db_table='paciente'

class Visitante(models.Model):
    cc_visitante=models.PositiveIntegerField()
    rostro=models.CharField(null=True, blank=True, max_length=99)
    foto=models.CharField(null=True, blank=True, max_length=99)
    estado=models.CharField(max_length=20)
    habitacion=models.ForeignKey(Habitacion, on_delete=models.CASCADE, 
                                 null=False, blank=False, related_name='visitantes')
    paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE, 
                                null=True, blank=True, related_name='visitantes')
    class Meta:
        db_table='visitante'
   

    def reg_rostro(imagen, name):
        imagen2=imagen
        b=base64.b64decode(imagen2)
        pixels=Image.open(io.BytesIO(b))
        pixels.save(str(name)+"org.jpg")

        img = str(name)+"org.jpg"	
        pixeles = pyplot.imread(img)
        detector = MTCNN()	
        caras = detector.detect_faces(pixeles)
        print(len(caras))

        data = pyplot.imread(img)
        for i in range(len(caras)):
            x1,y1,ancho, alto = caras[i]['box']
            x2,y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(caras), i+1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg, (150, 200), interpolation = cv2.INTER_CUBIC)
            cv2.imwrite(str(name)+"cort.jpg", cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])

    def log_rostro(cc):
        imagen1=cv2.imread(str(cc)+"cort.jpg", 0)
        imagen2=cv2.imread(str(cc)+"Logcort.jpg", 0)
        orb = cv2.ORB_create()
        porcentaje=0

        kpa, descr_a = orb.detectAndCompute(imagen1, None)
        kpa, descr_b = orb.detectAndCompute(imagen2, None)

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
        matches = comp.match(descr_a, descr_b)

        regiones_similares = [i for i in matches if i.distance < 70]
        if len(matches) == 0:
            porcentaje = 0
        else:
            porcentaje = len(regiones_similares)/len(matches)
        
        if porcentaje >= 0.9:
            return porcentaje
        else:
            return "Usuario no encontrado"



        
            
       

    