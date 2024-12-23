import numpy as np
import pandas as pd

const = pd.read_csv('vibraciones/coords.csv', sep= ';')

def const_nk(const):
    
    x = const['De'].values
    y = const['PPV'].values
    const['Log(De)'] = np.log10(const['De'])
    const['Log(PPV)'] = np.log10(const['PPV'])
    n, k = np.polyfit(const['Log(De)'], const['Log(PPV)'], 1)

    return [n, 10 ** k]

