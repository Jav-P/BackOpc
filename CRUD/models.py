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
    rostro=models.ImageField(null=True, blank=True)
    foto=models.ImageField(null=True, blank=True)
    estado=models.CharField(max_length=20)
    habitacion=models.ForeignKey(Habitacion, on_delete=models.CASCADE, 
                                 null=False, blank=False, related_name='visitantes')
    paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE, 
                                null=True, blank=True, related_name='visitantes')
    class Meta:
        db_table='visitante'
        
   

    def reg_rostro(imagen):
        b=base64.b64decode(imagen)
        pixels=Image.open(io.BytesIO(b))
        pixels.save('prueba'+"org.jpg")

        img = 'prueba'+"org.jpg"	
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
            cv2.imwrite('prueba'+"cort.jpg", cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
       

    