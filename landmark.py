#%% read in data - use a pandas dataframe just for convenience

import pandas as pd
data = pd.read_table("~/Desktop/Project/data/melbourne_graph.txt",
                     sep = " ",
                     header = None, 
                     names = ['vx', 'vy', 'weight'])

# d : landmark number
d = 1000
# degreee heuristic
degree = data.vx.value_counts()
print(type(degree))
landmarks = degree[0:1000]

# centrality heuristic
