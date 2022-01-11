import networkx as nx

class Graph:
	"""
    Class to contain a graph and your bfs function
    """
	def __init__(self, filename: str):
		"""
		Initialization of graph object which serves as a container for 
		methods to load data and     
		"""
		self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
	
	def bfs(self, start, end=None):
		"""
		TODO: write a method that performs a breadth first traversal and pathfinding on graph G
		* If there's no end node, just return a list with the order of traversal
		* If there is an end node and a path exists, return a list of the shortest path
		* If there is an end node and a path does not exist, return None
		"""
		bfs_tree = BFSTree(self, start)
		if end == None:
			print("Returning BFS traversal starting from " + start)
			return bfs_tree.traversal
		else:
			return bfs_tree.shortest_path(end)

class BFSTree:
	"""
	Class that contains a representation of a bfs tree for of a Graph object
	starting at the given "start" node
	* the visited dictionary keeps track of the visited nodes during BFS traversal
	* the dists dictionary keeps track of the distance of each node to the start node
	* the parents dictionary keeps track of each nodes parent
	* the traversal list is the in-order traversal during BFS
	"""
	def __init__(self, G: Graph, start):
		self.start = start
		self.graph = G.graph
		self.visited = dict.fromkeys(G.graph.nodes, False)
		self.dists = dict.fromkeys(G.graph.nodes, -1)
		self.parents = dict.fromkeys(G.graph.nodes,"")
		self.traversal = []
		if not(G.graph.has_node(start)):
			raise ValueError("Start node not in graph")
		else:
			q = [start]
			self.visited[start] = True
			self.dists[start] = 0
			while q:
				u = q.pop(0)
				self.traversal.append(u)
				for v in G.graph.neighbors(u):
					if not(self.visited[v]):
						q.append(v)
						self.visited[v] = True
						self.dists[v] = self.dists[u] + 1
						self.parents[v] = u
	
	def shortest_path(self, end):
		"""
		Returns shortest path to end node
		"""
		if not(self.graph.has_node(end)):
			raise ValueError("End node not in graph")
		elif not(self.visited[end]):
			print(end + " is not accessible from " + self.start)
			return None
		else:
			print("Returning shortest path from " + self.start + " to " + end)
			p = [end]
			prev = end
			while not(self.parents[prev] == ""):
				prev = self.parents[prev]
				p = [prev] + p
			return p
						

		
					
""" 
G = Graph("./data/tiny_network.adjlist")
print(G.bfs("Lani Wu"))
print(G.bfs("Lani Wu", "Steven Altschuler"))
B = BFSTree(G, "Lani Wu")
print(B.shortest_path("Steven Altschuler"))
# print(B.shortest_path("Charles Chiu"))
# print(B.shortest_path("Atul Butte"))

# F = BFSTree(G, "Carolyn Ku")
# B.shortest_path("Carolyn Ku")
"""
