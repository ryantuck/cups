import json
import sys

import matplotlib.pyplot as plt

x = []
y = []

for line in sys.stdin:
    data = json.loads(line)
    x.append(data['x'])
    y.append(data['y'])

plt.scatter(x, y)
plt.plot(x, y)
plt.savefig('scatter.png')
