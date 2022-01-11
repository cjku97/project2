# Project 2: Breadth-first Search
Breadth-first search is a method of graph search that traverses a nodes nearest neighbors before proceeding to the next depth.

## Initializing a Graph
The Graph class takes in the filename of a semicolon-delimited adjacency list and creates a graph using the [networkx](https://networkx.org/) package.
The bfs function within the Graph class takes in a start and optional end node as strings and creates a BFS tree with the given start node (see BFSTree class description below).

It then returns the following:
* If there's no end node, it returns a list with the order of BFS traversal
* If there is an end node and a path exists, return a list of the shortest path
* If there is an end node and a path does not exist, return None
	
## Building a BFS Tree
The BFSTree class takes in a Graph object and a given start node and creates a representation of a BFS tree.

It has the following attributes:
* visited -- a dictionary with the graph nodes as keys and a boolean value representing whether the node is visited during BFS traversal
	* if visited[v] = True then node v is accessible from the start node
	* if visited[v] = False then node v is not accessible from the start node
* dists -- a dictionary with the graph nodes as keys and a int value representing the distance to the start node
	* if dists[v] = n then node v is distance n from the start node
* parents -- a dictionary with the graph nodes as keys and a string value of that node's parent
	* if dists[v] = u then node u is the parent of node v
* traversal -- a list representation of the BFS traversal through the graph from the start node

The BFSTree class also contains a shortest_path function that takes in an end node and returns the shortest path from the given start node of a BFSTree object to that node.
* If there a path exists it returns a list of the shortest path
* If there a path does not exist it returns None
This function is called within the bfs function of the Graph class.

# Reference Information
## Test Data
Test networks have been provided in an adjacency list format readable by [networkx](https://networkx.org/):
* *citation_network.adjlist* has nodes consisting of all BMI faculty members, the top 100 Pubmed papers *cited by* faculty, and the top 100 papers that *cite* faculty publications. 
Edges are directed and and edge from node A -> B indicates that node A *is cited by* node B. 
There are 5120 nodes and 9247 edges in this network.
* *tiny_network.adjlist* is a subgraph of the first, consisting of only the nodes and edges along the paths between the PIs of all your TAs. 
There are 30 nodes and 64 edges.
* *my_network.txt* is a simple directed graph of five nodes labeled "1" through "5".


