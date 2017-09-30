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
    with open(file_path) as f:
        lines = f.read().splitlines()

    number_nodes = int(lines[0])

    for k in range(1, len(lines)):
        data = lines[k].split(":")
        edge = Edge(Node(int(data[0])),  Node(int(data[1])), int(data[2]))
        graph.add_edge(edge)

    for i in range(number_nodes):
        graph.add_node(Node(i))

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
        # initial assume the node is not in the graph
        isRemove = False
        # if the node is in the graph
        if node in self.adjacency_list:
            self.adjacency_list.pop(node, None)
            isRemove = True
        for nodes, edges in self.adjacency_list.items():
            if node in nodes:
                nodes.remove(node)
                isRemove = True
        return isRemove

    def add_edge(self, edge):
        # check if the edge is already existed
        if edge.from_node in self.adjacency_list:
            if edge.to_node in self.adjacency_list[edge.from_node]:
                return False
        else:
            self.adjacency_list[edge.from_node].append(edge.to_node)
            return True

    def remove_edge(self, edge):
        # if edge is existed
        if edge.from_node in self.adjacency_list:
            if edge.to_node in self.adjacency_list[edge.from_node]:
                self.adjacency_list[edge.from_node].remove(edge.to_node)
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

    def __get_node_index(self, node):
        """helper method to find node index"""
        if node not in self.nodes:
            return False
        else:
            return self.nodes.index(node)

    def adjacent(self, node_1, node_2):
        # check if the two nodes are adjacent
        if self.adjacency_matrix[__get_node_index(node_1)][__get_node_index(node_2)] != 0:
            return True
        else:
            return False

    def neighbors(self, node):
        neighbors = []
        for k in range(len(self.adjacency_matrix)):
            # check if node k in adjacent to node
            if self.adjacency_matrix[__get_node_index(node)][k] != 0:
                neighbors.append(Node(k))
        return neighbors

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            newRow = []
            for k in range(len(self.nodes)):
                self.adjacency_matrix[k].append(0)
                newRow.append(0)
        self.adjacency_matrix.append(newRow)
        return True

    def remove_node(self, node):
        if node not in self.nodes:
            return False
        else:
            self.nodes.remove(node)
            # delete a row of index of the node
            del self.adjacency_matrix[__get_node_index(node)]
            for num in range(len(self.nodes)):
                # delete all the column of the index of the node
                del self.adjacency_matrix[num][(__get_node_index(node))]
            return True

    def add_edge(self, edge):
        # check if the edge is already existed
        if self.adjacency_matrix[__get_node_index(edge.from_node)][__get_node_index(edge.to_node)] != 0:
            return False
        else:
            # addd new adge and assign the weight of the edge
            self.adjacency_matrix[__get_node_index(
                edge.to_node)][__get_node_index(edge.from_node)] = edge.weight
            self.adjacency_matrix[__get_node_index(
                edge.from_node)][__get_node_index(edge.to_node)] = edge.weight
            return True

    def remove_edge(self, edge):
        # check if the edge is existed
        if (self.adjacency_matrix[__get_node_index(edge.from_node)][__get_node_index(edge.to_node)]) != 0:
            # remove the edge
            self.adjacency_matrix[__get_node_index(edge.to_node)][__get_node_index(edge.from_node)] = 0
            self.adjacency_matrix[__get_node_index(
                edge.from_node)][__get_node_index(edge.to_node)] = 0
            return True
        else:
            return False




class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""

    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        for edge in self.edges:
            if edge.from_node == node_1 and edge.to_node == node_2:
                return True
        return False

    def neighbors(self, node):
        new_num = []

        for edge in self.edges:
            if node == edge.from_node:
                new_num.append(edge.to_node)
        return new_num

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            return True

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            for edge in self.edges:
                if edge.from_node == node or edge.to_node == node:
                    self.edges.remove(edge)
            return True
        else:
            return False

    def add_edge(self, edge):
        if edge in self.edges:
            return False
        else:
            self.edges.append(edge)
            return True

    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
            return True
        else:
            return False


def main():
    new_graph = construct_graph_from_file(
        ObjectOriented(), "../test/fixtures/graph-1.txt")


if __name__ == "__main__":
    main()
