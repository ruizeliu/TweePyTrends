import networkx as nx
import matplotlib.pyplot as plt
import util

###### Network Plotting ######

def plot_network(dic, key):
	'''
	Plot network plot showing related hashtags
	Size of circles indicating the time it's mentioned
	'''

	edge = []

	for k in dic.keys():
		for j in dic[k][0]:
			edge.append((k, j))
	G = nx.Graph()
	G.add_edges_from(edge)

	node = util.extract_hash(dic)
	node_set = list(set(node))
	G.add_nodes_from(node_set)

	freq = [node.count(k)*200 for k in node_set]
	color = {}
	for n in node_set:
		if n != key:
			color.update({n:"lightblue"})
		else:
			color.update({n:"salmon"})

	plt.figure(figsize=(10,10))
	plt.title("Hashtag Network Plot of #{}".format(key),fontsize=20, 
				weight = 'bold', fontfamily='sans-serif')
	nx.draw(G, with_labels= True, 
			node_color=[color[n] for n in G], node_shape="o", 
			alpha=0.75, linewidths=4, font_size=6, 
			font_color="black", font_weight="bold", 
			width=2, edge_color="grey",
			node_size = freq)
	plt.savefig("image/twitter_network.png")
	plt.close()


