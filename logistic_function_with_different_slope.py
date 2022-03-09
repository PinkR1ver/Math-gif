import matplotlib.pyplot as plt
import numpy as np
import math
import os
import imageio
import re
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

basePath = os.path.dirname(__file__)
x = np.arange(start=-10, stop=10, step=0.01)
a = np.arange(start=0.1, stop=5, step=0.01)
for i, params in enumerate(a):
    y = [1 / (1 + math.exp(-params * j)) for j in x]
    plt.plot(x, y)
    plt.savefig(os.path.join(basePath, 'tmp', f'{i}.png'))
    plt.close()

print(sorted_alphanumeric(os.listdir(os.path.join(basePath, 'tmp'))))

images = []
for i in sorted_alphanumeric(os.listdir(os.path.join(basePath, 'tmp'))):
    images.append(imageio.imread(os.path.join(basePath, 'tmp', i)))

imageio.mimsave(os.path.join(basePath, 'results', 'logistic_function_with_different_slope.gif'), images)

for i in os.listdir(os.path.join(basePath, 'tmp')):
    os.remove(os.path.join(basePath, 'tmp', i))

    