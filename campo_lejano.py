import pandas as pd
import numpy as np
from math import exp
from math import cos
from ecuacion_recta import const_bk

'Modelo de Devine'
def ppv_1(const_b: float | int, const_k: float | int, 
          dist_d: float | int, charge_q: float | int):
    
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_k * (dist_d/(charge_q ** 0.5)) ** (const_b)

const = pd.read_csv('vibraciones/coords.csv', sep= ';')
b, k = const_bk(const)

ppv1 = ppv_1(b, k, 1000, 862)
print('La velocidad peak de partícula es: ', ppv1, 'mm/s')


'Langefors y Kihlström'

def ppv_2(const_b: float | int, const_k: float | int, 
          dist_d: float | int, charge_q: float | int):
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_k * (charge_q / (dist_d ** 2/3)) ** (const_b / 2)

'Davies et al'
def ppv_3(const_b: float | int, const_k: float | int, 
          dist_d: float | int, charge_q: float | int, 
          const_a: float | int):
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso
    * a = constante empírica del macizo rocoso

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_k * (dist_d ** const_b) * (charge_q ** const_a)

'Indian Standard'
def ppv_4(const_b: float | int, const_k: float | int, 
          dist_d: float | int, charge_q: float | int):
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_k * ((dist_d ** 2/3) / charge_q) ** -const_b

'Ghosh y Daemen (cargas cilíndricas)'
def ppv_5(const_b: float | int, const_k: float | int, 
          dist_d: float | int, charge_q: float | int,
          const_a: float | int):
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso
    * a = constante empírica del macizo rocoso

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_k * (dist_d / (charge_q ** 0.5) ** (-const_b)) * exp(-const_a * dist_d)

'Gupta et al'
def ppv_6(const_b: float | int, const_k: float | int, 
          dist_d: float | int, charge_q: float | int,
          const_a: float | int):
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso
    * a = constante empírica del macizo rocoso

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_k * ((dist_d / (charge_q ** 1/3)) ** -const_b) * exp(-const_a * (dist_d / charge_q))

'Ghosh y Daemen (cargas esféricas)'
def ppv_7(const_b: float | int, const_k: float | int, 
          dist_d: float | int, charge_q: float | int,
          const_a: float | int):
   '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso
    * a = constante empírica del macizo rocoso

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
   return const_k * (dist_d / (charge_q ** 1/3) ** (-const_b)) * exp(-const_a * dist_d)

'Roy (cargas esféricas)'
def ppv_8(const_k: float | int, dist_d: float | int, 
            charge_q: float | int, const_n: float | int):
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * K = constante empírica del macizo rocoso
    * n = constante empírica del macizo rocoso
    
    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_n + const_k * (dist_d / (charge_q ** 1/3)) ** -1

'Bilgin et al'
def ppv_9(const_k: float | int, dist_d: float | int, 
            charge_q: float | int, burden_B: float | int, 
            const_gamma: float | int, const_b: float | int):
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso
    * B = burden [m]
    * γ = peso específico de la roca [kN/m3]

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_k * ((dist_d / (charge_q ** 0.5) ** -const_b)) * (burden_B ** const_gamma)

'Rai and Singh'
def ppv_10(const_b: float | int, const_k: float | int, 
          dist_d: float | int, charge_q: float | int, 
          const_a: float | int):
   '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso
    * a = constante empírica del macizo rocoso

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
   return const_k * (dist_d ** -const_b) * (charge_q ** const_a) * exp(-const_a * dist_d)

'Ak y Kounuk'
def ppv_11(const_k: float | int, dist_d: float | int,
             charge_q: float | int, const_b: float | int,
             frec_lambda: float | int, const_a: float | int):
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso
    * a = constante empírica del macizo rocoso
    * λ = frecuencia de discontinuidades

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_k * ((dist_d / (charge_q ** 0.5)) ** -const_b) * (frec_lambda ** const_a)

'Giraudi et al'
def ppv_12(const_k: float | int, dist_d: float | int,
             charge_q: float | int, const_b: float | int,
             time_det: float | int):
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso
    * Tdet = tiempo de detonación [s]

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_k * ((dist_d ** 2) / ((charge_q * time_det) ** 0.5)) ** -const_b

'Simangunsong y Wahyud'
def ppv_13(const_k: float | int, incidence_angle: float | int,
             number_nc: float | int, dist_d: float | int,
             charge_q: float | int, const_b: float | int):
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso
    * θi = ángulo de incidencia []
    * Nc = capas de mineral entre el área de tronadura y el punto de monitoreo

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_k * ((1 + cos(incidence_angle) + number_nc * (dist_d / (charge_q ** 0.5))
                       )) * -const_b

'Kumar et al'
def ppv_14(factor_fc: float | int, dist_d: float | int,
             const_gamma: float | int):
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * fc = factor que relaciona PPV con RQD
    * γ = peso específico de la roca [kN/m3]

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return ((factor_fc ** 0.642) * (dist_d ** -1.463)) / const_gamma

'Murmu et al'
def ppv_15(const_k: float | int, dist_d: float | int,
             charge_q: float | int, const_b: float | int):
    '''
    PPV (Peak Particle Velocity)
    Esta función calcula la velocidad máxima de propagración
    de una partícula en un punto distanciado.

    Entradas:
    * D = distancia a la cual se cuantifica [m]
    * Q = carga del explosivo [kg]
    * b = constante empírica del macizo rocoso
    * K = constante empírica del macizo rocoso

    Salidas:
    * PPV = peak particle velocity [mm/s]
    '''
    return const_k * (dist_d / (charge_q ** 2/5)) ** -const_b