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
            for edge in self.adjacency_list[node_1]:
                if edge.to_node == node_2:
                    return True
        return False

    def neighbors(self, node):
        neighbors = []
        if node in self.adjacency_list:
            for edge in self.adjacency_list[node]:
                neighbors.append(edge.to_node)
            return neighbors
        else:
            return []

    def add_node(self, node):
        if node in self.adjacency_list:
            return False
        else:
            self.adjacency_list[node] = []
            return True

    def remove_node(self, node):
        result = False
        if node in self.adjacency_list:
            self.adjacency_list.pop(node, None)
            result = True
        for k,v in self.adjacency_list.items():
            for edge in v:
                if edge.to_node == node:
                    v.remove(edge)
                    result = True

        return result

    def add_edge(self, edge):
        # check if the edge is already existed
        if edge.from_node in self.adjacency_list:
            if edge.to_node in self.adjacency_list[edge.from_node]:
                return False
        else:
            self.adjacency_list[edge.from_node].append(edge)
            return True

    def remove_edge(self, edge):
        # if edge is existed
        if edge.from_node in self.adjacency_list:
            if edge in self.adjacency_list[edge.from_node]:
                self.adjacency_list[edge.from_node].remove(edge)
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
        if self.adjacency_matrix[self.__get_node_index(node_1)][self.__get_node_index(node_2)] != 0:
            return True
        else:
            return False

    def neighbors(self, node):
        neighbors = []
        for k in range(len(self.adjacency_matrix(self.__get_node_index(node)))):
            # check if node k in adjacent to node
            if self.adjacency_matrix[self.__get_node_index(node)][k] != 0:
                neighbors.append(self.node(k))

        return neighbors

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            for row_i in self.adjacency_matrix:
                row_i.append(0)

            self.adjacency_matrix.append([0 for x in range(len(self.nodes))])

        return True

    def remove_node(self, node):
        if node not in self.nodes:
            return False
        else:
            for row_i in self.adjacency_matrix:
                row_i.pop(self.__get_node_index(node))
            self.nodes.remove(node)
            self.adjacency_matrix.pop(self.__get_node_index(node))

        return True

    def add_edge(self, edge):
        # check if the edge is already existed
        if self.adjacency_matrix[self.__get_node_index(edge.from_node)][self.__get_node_index(edge.to_node)] == edge.weight:
            return False
        else:
            # addd new adge and assign the weight of the edge
            self.adjacency_matrix[self.__get_node_index(
                edge.from_node)][self.__get_node_index(edge.to_node)] = edge.weight
            return True

    def remove_edge(self, edge):
        # check if the edge is existed
        if (self.adjacency_matrix[self.__get_node_index(edge.from_node)][self.__get_node_index(edge.to_node)]) == 0:
            return False
        else:
            # remove the edge
            self.adjacency_matrix[self.__get_node_index(
                edge.from_node)][self.__get_node_index(edge.to_node)] = 0
            return True

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
        neighbors = []

        for edge in self.edges:
            if node == edge.from_node:
                neighbors.append(edge.to_node)
        return neighbors

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
    new_graph = construct_graph_from_file(AdjacencyMatrix(),"../test/fixtures/graph-2.txt")

if __name__ == "__main__":
    main()

"""
    Explain with the runtime analysis on each method you have implemented in each of the representation using Big-O notation

	If the graph have n nodes and m edges, then
		For the Adjacency Matrix:
			Nodes
			The time to check one node is O(1), so time to check all n nodes is n*O(1) = O(n)
			The time to check one edge connect to a node is O(1), so total time to iterate over edges incident to nodes is m*O(1) = O(m)
			Total time need is: O(n + m)

		For Adjacency Matrix:
			The time to check one node is O(1), and Matrix size is n x n, so time to check all the node is n x n x O(1) = O(n^2)
			Total time is O(n^2)

		For ObjectedOriented:
			The time to check one node is O(1), so time to check all n nodes is n*O(1) = O(n)
			The time to check one edge is O(1), so total time to iterate all the edges is m*O(1) = O(m)
			Total time need is: O(n + m)


    Consider Chess, what is the performance measure, environment, actuator and sensor?
	    performance measure:
            protect the one's king safe, attack and capture the opponent's pieces, especially the opponent's king in order to win the game. make a move fast.
	    environment:
            gameboard with 64 squares arranged in an 8×8 grid, the position and the posibility of the move of the opponent's pieces (initial 16 pieces).The colors of the 64 squares alternate and are referred to as light and dark squares.
	    actuator:
            move the pieces so that they can block the move and attack the opponent's pieces, especially the king, meanwhile, protecting its own king.
	    sensor:
            the position and all the move that each piece can make.


    Same with Chess, formulate the problem in 5 components (initial state, possible actions, transition model, goal test, and path cost)

        initial state:
            Each player begins with 16 pieces: one king, one queen, two rooks, two knights, two bishops, and eight pawns
        possible actions:
            Each of the six piece types moves differently, with the most powerful being the queen and the least powerful the pawn.

            The king moves one square in any direction. The king also has a special move called castling that involves also moving a rook.
            The rook can move any number of squares along a rank or file, but cannot leap over other pieces. Along with the king, a rook is involved during the king's castling move.
            The bishop can move any number of squares diagonally, but cannot leap over other pieces.
            The queen combines the power of a rook and bishop and can move any number of squares along a rank, file, or diagonal, but cannot leap over other pieces.
            The knight moves to any of the closest squares that are not on the same rank, file, or diagonal, thus the move forms an "L"-shape: two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The knight is the only piece that can leap over other pieces.
            The pawn can move forward to the unoccupied square immediately in front of it on the same file, or on its first move it can advance two squares along the same file, provided both squares are unoccupied (black dots in the diagram); or the pawn can capture an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that square (black "x"s). A pawn has two special moves: the en passant capture and promotion.

        transition model:
             Given state, the position, the possible move and the action that the opponent could make, the player will make a move.
        goal test:
            Block or attack the opponent'king in the check.
        path cost:
            Each move would cost 1

    Define Chess environment type, is it fully observable or partially observable, is it deterministic or stochastic, is it discrete or continuous, is it benign or adversarial?

        The Chess environment is fully observable
            since agent can fully observe all variables of environment.
        It is deterministic
            since there is no random effects,each moves determines next state deterministically
        It is discrete
            since Number of states in games is countable.
        It is adversarial.
            since Environment goes against you.
"""
