"""
utils package is for some quick utility methods

such as parsing
"""

import time
from io import open
from .graph import Node
from .graph import Edge

class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)
    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.x) + str(self.y) + self.symbol)

def parse_grid_file(graph, file_path):
    """
    ParseGridFile parses the grid file implementation from the file path line
    by line and construct the nodes & edges to be added to graph

    Returns graph object
    """
    # TODO: read the filepaht line by line to construct nodes & edges

    # TODO: for each node/edge above, add it to graph

    f = open(file_path, encoding='utf-8')
    data = f.readlines()
    last_row = []
    number_of_rows = len(data)-2
    for j in range(number_of_rows):
        line = data[j+1]
        i = 1
        current_row = []
        while i < len(line)-3:
            value = int((i-1)/2)
            node = Node(Tile(value, j, line[i:i+2]))
            graph.add_node(node)
            i+=2

            if node.data.symbol != "##":
                if node.data.x > 0:
                    last_node = current_row[-1]
                    if last_node.data.symbol != "##":
                        graph.add_edge(Edge(last_node, node, 1))
                        graph.add_edge(Edge(node, last_node, 1))
                if node.data.y > 0:
                    last_node = last_row[value]
                    if last_node.data.symbol != "##":
                        graph.add_edge(Edge(last_node, node, 1))
                        graph.add_edge(Edge(node, last_node, 1))
            current_row.append(node)
        last_row = current_row

    f.close()
    return graph

def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile

    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    """
    output_path = []
    for edge in edges:
        if edge.to_node.data.x - edge.from_node.data.x > 0:
            output_path.append("E")
        elif edge.to_node.data.x - edge.from_node.data.x < 0:
            output_path.append("W")
        elif edge.to_node.data.y - edge.from_node.data.y < 0:
            output_path.append("N")
        elif edge.to_node.data.y - edge.from_node.data.y > 0:
            output_path.append("S")
    return "".join(output_path)
