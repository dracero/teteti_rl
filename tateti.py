import numpy as np
import gymnasium as gym
from gymnasium.spaces import Discrete, Box #Esto lo cambié, porque gymnasium usa otra sinstaxis
import random


class tresEnRaya(gym.Env):

  def __init__(self, columns=3, rows=3):
    self.columns = columns
    self.rows = rows
    self.tablero = np.zeros(9, np.uint8)
    self.terminated = False
    self.truncated = False
    self.turno = 0
    self.render()

    # Definimos el número de acciones que queremos realizar
    self.action_space = Discrete(9)

    # Vamos a definir el entorno
    self.observation_space = Box(
        low=0, 
        high=2,
        shape=(9,), 
        dtype=np.uint8)
    

  def __turno_aleatorio(self):
    colocada = 0
    while colocada == 0:
      alea = random.randint(0, 8)
      if self.tablero[alea] == 0:
        self.tablero[alea] = 2
        colocada = 1
    return self.tablero

  def __comprobar_ganador(self):
    # Comprobamos si gana la IA ha ganado
    # Horizontales
    if self.tablero[0] == 1 and self.tablero[1] == 1 and self.tablero[2] == 1:
      self.terminated = True
      self.truncated = True
      return 1
    if self.tablero[3] == 1 and self.tablero[4] == 1 and self.tablero[5] == 1:
      self.terminated = True
      self.truncated = True
      return 1
    if self.tablero[6] == 1 and self.tablero[7] == 1 and self.tablero[8] == 1:
      self.terminated = True
      self.truncated = True
      return 1
    # Verticales
    if self.tablero[0] == 1 and self.tablero[3] == 1 and self.tablero[6] == 1:
      self.terminated = True
      self.truncated = True
      return 1
    if self.tablero[1] == 1 and self.tablero[4] == 1 and self.tablero[7] == 1:
      self.terminated = True
      self.truncated = True
      return 1
    if self.tablero[2] == 1 and self.tablero[5] == 1 and self.tablero[8] == 1:
      self.terminated = True
      self.truncated = True
      return 1
    # Diagonales
    if self.tablero[0] == 1 and self.tablero[4] == 1 and self.tablero[8] == 1:
      self.terminated = True
      self.truncated = True
      return 1
    if self.tablero[2] == 1 and self.tablero[4] == 1 and self.tablero[6] == 1:
      self.terminated = True
      self.truncated = True
      return 1

    # Comprobamos si ha ganado el aleatorio
    # Horizontales
    if self.tablero[0] == 2 and self.tablero[1] == 2 and self.tablero[2] == 2:
      self.terminated = True
      self.truncated = True
      return -1
    if self.tablero[3] == 2 and self.tablero[4] == 2 and self.tablero[5] == 2:
      self.terminated = True
      self.truncated = True
      return -1
    if self.tablero[6] == 2 and self.tablero[7] == 2 and self.tablero[8] == 2:
      self.terminated = True
      self.truncated = True
      return -1
    # Verticales
    if self.tablero[0] == 2 and self.tablero[3] == 2 and self.tablero[6] == 2:
      self.terminated = True
      self.truncated = True
      return -1
    if self.tablero[1] == 2 and self.tablero[4] == 2 and self.tablero[7] == 2:
      self.terminated = True
      self.truncated = True
      return -1
    if self.tablero[2] == 2 and self.tablero[5] == 2 and self.tablero[8] == 2:
      self.terminated = True
      self.truncated = True
      return -1
    # Diagonales
    if self.tablero[0] == 2 and self.tablero[4] == 2 and self.tablero[8] == 2:
      self.terminated = True
      self.truncated = True
      return -1
    if self.tablero[2] == 2 and self.tablero[4] == 2 and self.tablero[6] == 2:
      self.terminated = True
      self.truncated = True
      return -1
    return 0.5
    
  def reset(self, seed=None):
    """
    Importante: the observation must be a numpy array
    :return: (np.array) 
    """
    self.tablero = np.zeros(9, np.uint8)
    observation = np.zeros(9, np.uint8)
    self.turno = 0
    self.terminated = False
    self.truncated = False
    return observation, {} 
    
  def step(self, action):
    if self.tablero[action] != 0:
      observation = self.tablero
      self.terminated = True
      self.truncated = False
      reward = -1
      info = {"Error": "Intento hacer trampa"}
      return observation, reward, self.terminated, self.truncated, info
    self.tablero[action] = 1
    self.turno += 1
    observation = self.tablero
    reward = self.__comprobar_ganador()
    if self.turno == 5:
      self.terminated = True
      self.truncated = True
    info = {}
    if self.terminated == False:
      self.tablero = self.__turno_aleatorio()
      observation = self.tablero
    return observation, reward, self.terminated,self.truncated, info
 
  def render(self, mode='human'):
    print("")
    print("turno: " + str(self.turno))
    for i in range(9):
      if self.tablero[i]==0:
        print("   |", end="")
      elif self.tablero[i]==1:
        print(" O |",end="")
      elif self.tablero[i]==2:
        print(" X |",end="")
      if (i+1) % 3 == 0:
        print("")
    print("")