#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

#Masa del cuerpo central: M = 1.498 x 10^10 kg (tal que G*M = 1 N m^2/kg)
GM = 1

class Planeta(object):
    '''
    Esta clase permite construir planetas, con una masa, condiciones iniciales
    y una corrección relativista. La clase permite avanzar al planeta en su
    órbita, guardando la posición actual, el instante de tiempo actual,
    y la posición anterior. También permite evaluar la energía del planeta en
    el instante actual.
    '''

    def __init__(self, condicion_inicial, alpha=0, masa=1):
        '''
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Ej. de uso:
        >> mercurio = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        '''
        self.y_anterior = np.array([])
        self.y_actual = np.array(condicion_inicial)
        self.t_actual = 0.
        self.alpha = alpha
        self.mass = masa

    def ecuacion_de_movimiento(self):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciones de
        primer orden.
        '''
        x, y, vx, vy = self.y_actual
        r = np.sqrt(x**2 + y**2)
        cos_p = x/r
        sen_p = y/r
        a_radial = 2*self.alpha/(r**3) - 1/(r**2)
        ax = a_radial*GM*cos_p
        ay = a_radial*GM*sen_p
        return np.array([vx, vy, ax, ay])

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        pos = self.y_actual
        dpos = self.ecuacion_de_movimiento()
        self.y_anterior = pos
        self.y_actual = pos + dt*dpos
        self.t_actual += dt
        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        pos = self.y_actual
        K1 = self.ecuacion_de_movimiento()
        self.y_actual = pos + dt*K1/2.
        K2 = self.ecuacion_de_movimiento()
        self.y_actual = pos + dt*K2/2.
        K3 = self.ecuacion_de_movimiento()
        self.y_actual = pos + dt*K3
        K4 = self.ecuacion_de_movimiento()
        self.y_anterior = pos
        self.y_actual = pos + (K1+2*K2+2*K3+K4)*dt/6.
        self.t_actual += dt
        pass

    def avanza_verlet(self, dt):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        acel = self.ecuacion_de_movimiento()
        pos_n1 = 2*self.y_actual[0:2] - self.y_anterior[0:2] + (dt**2)*acel[2:4]
        vel_n1 = (pos_n1 - self.y_actual[0:2])/dt
        self.y_anterior = self.y_actual
        self.y_actual = np.concatenate((pos_n1,vel_n1))
        self.t_actual += dt
        pass

    def energia_total(self):
        '''
        Calcula la energía total del sistema en las condiciones actuales.
        '''
        pos = self.y_actual
        K = (pos[2]**2 + pos[3]**2)/2
        r = np.sqrt(pos[0]**2 + pos[1]**2)
        U = -GM/r + self.alpha*GM/r**2
        return (K + U)*self.mass
