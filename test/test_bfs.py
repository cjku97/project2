# write tests for bfs
import pytest
from search import graph

@pytest.fixture
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    G = Graph("./data/tiny_network.adjlist")
    B = G.bfs("Lani Wu")
    assert len(B) == 30
    assert G.bfs == ['Lani Wu', '32042149', '32036252', '31806696', '30727954', 
    	'Hani Goodarzi', 'Steven Altschuler', 'Luke Gilbert', 'Michael McManus', 
    	'33232663', '33483487', '31626775', '31540829', '32025019', '29700475', 
    	'Charles Chiu', 'Martin Kampmann', 'Neil Risch', 'Nevan Krogan', 'Atul Butte', 
    	'Michael Keiser', '33242416', '32790644', '34272374', '32353859', '30944313', 
    	'33765435', '31395880', 'Marina Sirota', '31486345']
    pass

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
    pass
