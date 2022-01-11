# write tests for bfs
import pytest
from search import graph

# @pytest.fixture
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    G = graph.Graph("./data/tiny_network.adjlist")
    B = G.bfs("Lani Wu")
    assert len(B) == 30
    assert B == ['Lani Wu', '32042149', '32036252', '31806696', '30727954', 
    	'Hani Goodarzi', 'Steven Altschuler', 'Luke Gilbert', 'Michael McManus', 
    	'33232663', '33483487', '31626775', '31540829', '32025019', '29700475', 
    	'Charles Chiu', 'Martin Kampmann', 'Neil Risch', 'Nevan Krogan', 'Atul Butte', 
    	'Michael Keiser', '33242416', '32790644', '34272374', '32353859', '30944313', 
    	'33765435', '31395880', 'Marina Sirota', '31486345']
    bigGraph = graph.Graph("./data/citation_network.adjlist")
    bigBFS = bigGraph.bfs("Charles Chiu")
    assert len(bigBFS) <= 5120
    assert bigGraph.bfs("Charles Chiu", "Elad Ziv") == ['Charles Chiu', '33658326', 'Nevan Krogan', '32353859', 'Elad Ziv']

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    G = graph.Graph("./data/tiny_network.adjlist")
    B = G.bfs("Lani Wu", "Steven Altschuler")
    assert len(B) == 3
    assert B == ['Lani Wu', '32036252', 'Steven Altschuler']
    A = graph.Graph("./data/my_network.txt")
    T = graph.BFSTree(A, "2")
    assert T.shortest_path("5") == None
    assert T.shortest_path("1") == ['2', '3', '1']
    assert T.shortest_path("4") == ['2', '4']
    assert T.traversal == ['2', '3', '4', '1']

def test_start_exception():
	bigGraph = graph.Graph("./data/citation_network.adjlist")
	with pytest.raises(ValueError, match = "Start node not in graph"):
		bigGraph.bfs("Carolyn Ku")

def test_end_exception():
	bigGraph = graph.Graph("./data/citation_network.adjlist")
	with pytest.raises(ValueError, match = "End node not in graph"):
		bigGraph.bfs("Lani Wu","Carolyn Ku")
