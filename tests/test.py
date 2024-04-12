import networkx as nx
# создаем граф
G = nx.Graph()

# добавляем пути
G.add_edge("Moscow", "Krasnodar", length=1000, price=150)
G.add_edge("Krasnodar", "Sochi", length=300, price=50)
G.add_edge("Moscow", "Rostov-na-Dony", length=900, price=120)
G.add_edge("Rostov-na-Dony", "Sochi", length=500, price=70)

# ищем кратчайший путь по свойству length (длина пути)
p = nx.shortest_path(G, "Moscow", "Sochi", weight="length")
# -> ['Moscow', 'Krasnodar', 'Sochi']

# ищем кратчайший путь по свойству price (стоимость поездки)
p = nx.shortest_path(G, "Moscow", "Sochi", weight="price")
# -> ['Moscow', 'Rostov-na-Dony', 'Sochi']

import matplotlib.pyplot as plt

# G - граф из примера выше с городами
nx.draw_networkx(G, pos=nx.spiral_layout(G), node_color='r', edge_color='b')
plt.show()