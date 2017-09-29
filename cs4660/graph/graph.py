"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter


def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """
    # graph = AdjacencyList();
    with open('file_path') as f:
        lines = f.read().splitlines()

    nodes = int(lines[0])

    for k in range(1, len(lines)):
        data = lines[k].split(":")
        edge = Edge(Node(int(data[0])),  Node(int(data[1])), int(data[2]))
        graph.add_edge(edge)

    for i in range(nodes):
        node = Node(i)
        graph.add_node(node)

    return graph


class Node(object):
    """Node represents basic unit of graph"""

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)

    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)


class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""

    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """

    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        if node_1 in self.adjacency_list:
            if node_2 in self.adjacency_list[node_1]:
                return True
            else:
                return False
        else:
            return False

    def neighbors(self, node):
        neighbors = []
        if node in self.adjacency_list:
            for key in self.adjacency_list[node]:
                neighbors.append(key)
            return neighbors
        else:
            return 0

    def add_node(self, node):
        if node in self.adjacency_list:
            return False
        else:
            self.adjacency_list[node] = {}
            return True

    def remove_node(self, node):
        isRemove = False
        if node in self.adjacency_list:
            self.adjacency_list.pop(node, None)
            isRemove = True
        for nodes, edges in self.adjacency_list.items():
            if node in nodes:
                nodes.remove(node)
                isRemove = True
        return isRemove

    def add_edge(self, edge):
        if edge.from_node in self.adjacency_list:
            edgeList = self.adjacency_list[edge.from_node]
            if edge.to_node in edgeList:
                return False
        else:
            self.adjacency_list[edge.from_node].append(edge.toto_node)
            return True

    def remove_edge(self, edge):
        if edge.from_node in self.adjacency_list:
            if edge.to_node in self.adjacency_list[edge.from_node]:
                self.adjacency_list[adge.from_node].remove(edge.to_node)
                return True
        else:
            return False


class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        if self.adjacency_matrix[node_1.data][node_2.data] != 0:
            return True
        else:
            return False

    def neighbors(self, node):
        neighbors = []
        for k in range(len(self.adjacency_matrix[node.data])):
            if self.adjacency_matrix[node.data][k] != 0:
                neighbors.append(Node(k))
        return result

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)

    def remove_node(self, node):
        if node not in self.nodes:
            return False
        else:
            self.nodes.remove(node)
            del self.adjacency_matrix(__get_node_index(node))
            for num in range(0, len(self.nodes)):
                del self.adjacency_matrix[num][(__get_node_index(node))]
            return True

    def add_edge(self, edge):
        if self.adjacency_matrix[edge.from_node][edge.to_node] != 0:
            return False
        else:
            self.adjacency_matrix[edge.to_node][edge.from_node] = edge.weight
            self.adjacency_matrix[edge.from_node][edge.to_node] = edge.weight
            return True

    def remove_edge(self, edge):
        if self.adjacency_matrix[edge.from_node][edge.to_node] != 0:
            self.adjacency_matrix[edge.to_node][edge.from_node] = 0
            self.adjacency_matrix[edge.from_node][edge.to_node] = 0
            return True
        else:
            return False

    def __get_node_index(self, node):
        """helper method to find node index"""
        for index in range(0, len(self.nodes)):
            if self.nodes(index) = node:
                return index
        return False


class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""

    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):

    def neighbors(self, node):
        pass

    def add_node(self, node):
        pass

    def remove_node(self, node):
        pass

    def add_edge(self, edge):
        pass

    def remove_edge(self, edge):
        pass
