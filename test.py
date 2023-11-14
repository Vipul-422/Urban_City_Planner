import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt

place_name = 'Chandigarh, India'

graph = ox.graph_from_place(place_name)
ox.plot_graph(graph)

nodes, edges = ox.graph_to_gdfs(graph)

nodes = nodes.geometry.tolist()
edges = edges.geometry.tolist()

rangexmin = 1e9
rangexmax = -1e9
rangeymin = 1e9
rangeymax = -1e9

for i in range(len(nodes)):
    s = str(nodes[i])
    s = s.split('(')[1].split(')')[0]
    nodes[i] = s.split(' ')
    nodes[i][0] = float(nodes[i][0])
    nodes[i][1] = float(nodes[i][1])

    if(nodes[i][0] < rangexmin):
        rangexmin = nodes[i][0]
    if(nodes[i][0] > rangexmax):
        rangexmax = nodes[i][0]
    if(nodes[i][1] < rangeymin):
        rangeymin = nodes[i][1]
    if(nodes[i][1] > rangeymax):
        rangeymax = nodes[i][1]

rangex = (rangexmin, rangexmax)
rangey = (rangeymin, rangeymax)