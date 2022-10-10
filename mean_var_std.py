import pandas as pd
import numpy as np

def calc_req():
  #strip and separate input
  numbers = input("type out a list of 9 numbers:")
  result = [x.strip() for x in numbers.split(',')]
  if len(result) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    #created list and turn into matrix using np
    list = []
    list.append(result)
    x = np.array(list, dtype=int)
    shape = (3,3)
    matrix = (x.reshape(shape))
    return matrix

def calculate():
    mat = calc_req()

    print(f"'mean': [{mat.mean(axis=0)}, {mat.mean(axis=1)}, {mat.mean()}],\n'variance': [{mat.var(axis=0)}, {mat.var(axis=1)}, {mat.var()}],\n'standard deviation': [{mat.std(axis=0)}, {mat.std(axis=1)}, {mat.std()}],\n'max': [{mat.max(axis=0)}, {mat.max(axis=1)}, {mat.max()}],\n'min': [{mat.min(axis=0)}, {mat.min(axis=1)}, {mat.min()}],\n'sum': [{mat.sum(axis=0)}, {mat.sum(axis=1)}, {mat.sum()}]")

calculate()



#calculate()
