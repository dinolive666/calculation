# 试验networkx中关于circle的算法
import pandas as pd
import networkx as nx
import numpy as np
import csv 
import matplotlib.pyplot as plt 

G = nx.Graph()
nx.add_cycle(G, [0, 1, 2, 3])
nx.add_cycle(G, [0, 3, 4, 5])
nx.draw(G, with_labels = True)
print(nx.cycle_basis(G, 0))














#找出所有连接的点

import pandas as pd
import networkx as nx
import numpy as np
import csv 
import matplotlib.pyplot as plt 

relation2 = pd.read_csv("./data4/relation2.csv")

edges = list(zip(relation2.source, relation2.target))

# 创建有向图
graph = nx.Graph()
graph.add_edges_from(edges)
nx.draw(graph, with_labels = True)

#找出连接
list(nx.node_connected_component(graph, "kk"))
