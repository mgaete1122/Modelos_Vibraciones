import pandas as pd
import numpy as np
from math import exp
from ecuacion_recta import const_nk


# Se define la función PPV del modelo de Devine para campo lejano
# con cargas explosivas de geometría cilíndrica
def ppvel_1(const_n: float | int, const_k: float | int, 
          dist_ds: float | int, charge_q: float | int):
    
    '''

    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula desde una distancia.

    Entradas:
    * DS = distancia a la cual se cuantifica [m]
    * W = carga del explosivo [kg]
    * K = constante de propagación del medio
    * n = constante de atenuación del medio

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_k * (dist_ds/(charge_q ** 0.5)) ** (const_n)

const = pd.read_csv('vibraciones/coords.csv', sep= ';')
n, k = const_nk(const)

ppv1 = ppvel_1(n, k, 1000, 862)
print('La velocidad peak de partícula es: ', ppv1, 'mm/s')