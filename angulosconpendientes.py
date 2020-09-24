import numpy as np
from math import pi
def pendiente(a,b):
    m=(b[1]-a[1])/(b[0]-a[0])
    return m
#Para calcular el angulos entre las rectas ab y bc
def angulo(a,b,c):
    if b[0]<a[0] and c[0]>b[0]:
        m1=pendiente(a,b)
        m2=pendiente(b,c)
        print('primero')
        theta=(np.arctan((m2-m1)/(1+(m2*m1)+0.000001 )))*(180/pi)
        if theta <0:
            theta=180+theta
            print('entre al if')
            return theta
        else:
            return theta

    elif b[0]>a[0] and c[0]>b[0]:
        m1=pendiente(a,b)
        m2=pendiente(b,c)
        print('segundo')
        theta=(np.arctan((m2-m1)/(1+(m2*m1)+0.000001 )))*(180/pi)
        if theta <0:
            theta=180+theta
            print('entre al if')
            return theta
        else:
            theta=180-theta
            return theta

    elif b[0]>a[0] and c[0]<b[0]:
        m1=pendiente(c,b)
        print('tercero')
        m2=pendiente(b,a)
        theta=(np.arctan((m2-m1)/(1+(m2*m1+0.000001))))*(180/pi)
        if theta <0:
            theta=180+theta
            return theta
        else:
            return theta

    elif b[0]<a[0] and c[0]<b[0]:
        m1=pendiente(a,b)
        print(m1)
        print('cuarto')
        m2=pendiente(b,c)
        print(m2)
        theta=(np.arctan((m2-m1)/(1+(m2*m1+0.000001))))*(180/pi)
        if theta <0:
            theta=180+theta
            return theta
        else:
            return theta
#Para el poligono del tronco
RS=(1,8)
LS=(10,8)
RH=(3,2)
LH=(8,3)
#Lista de Puntos para calcular los angulos,la etiqueta de enmedio corresponde a la articulacion
Puntos=(('right hip','right shoulder','left shoulder'),
    ('left hip','left shoulder','right shoulder'),
    ('right shoulder','right hip','left shoulder'),
    ('right shoulder','left hip','left shoulder'),
    ('right wrist','right elbow','right shoulder'),
    ('left wrist','left elbow','left shoulder'),
    ('right ankle','right knee','right hip'),
    ('left ankle','left knee','left hip')
    )
#res=angulo(LS,RH,RS)
#res=angulo(RS,LH,LS)
#print(res)

#Para los brazos
RW=(2,4)
RW2=(7,2)
RE=(5,3)
RS=(8,6)
LS=(13,6)
LE=(14,2)
LW=(16,7)
LW2=(12,1)
#res=angulo(LW2,LE,LS)
#print(res)

#Para las piernas
RH=(4,7)
RK=(2,3)
RK2=(6,3)
RA=(4,0)
LH=(9,7)
LK=(7,3)
LK2=(12,3)
LA=(9,0)
#res=angulo(LA,LK2,LH)
#print(res)
#Etiquetas que arroja el posenet
label=('right shoulder','left shoulder','right hip','left hip','right elbow','left elbow','rigth wrist',
    'left wrist''right knee','left knee','right ankle','left ankle')
xys={}
coordenadas=open('coordenadas.txt','a')
coordenadas.write('\n'+'Nueva entrada del archivo')
coordenadas.close()

xys['right shoulder']=(1,8)
xys['left shoulder']=(10,8)
xys['right hip']=(3,2)
xys['left hip']=(8,3)
coordenadas=open('coordenadas.txt','a')
coordenadas.write('\n'+str(xys['right shoulder']))
coordenadas.close()

angulos=open('angulos.txt','a')
angulos.write('\n'+'Nueva entrada del archivo')
angulos.close()
for a,b,c in Puntos:
    if a not in xys or b not in xys or c not in xys: continue
    etiqueta=b
    a=xys[a]
    b =xys[b]
    c=xys[c]
    theta=angulo(a,b,c)
    angulos=open('angulos.txt','a')
    angulos.write('\n'+etiqueta+' '+str(theta))
    angulos.close()
    print('The angle in '+etiqueta+' is '+str(theta))
