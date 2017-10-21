"""
Searches module defines all different search algorithms
"""

def bfs(graph, start_node, end_node):
    Q = []
    Q.append(start_node)
    visited_nodes = []
    visited_nodes.append(start_node)
    parent_of = {}
    parent_of[start_node] = None
    distance_of = {}
    distance_of[start_node] = 0
    last_node = end_node

    while (bool(Q)):
        current_node = Q.pop(0)
        for node in graph.neighbors(current_node):
            if (node not in visited_nodes):
                    Q.append(node)
                    distance_of[node] = distance_of[current_node] + graph.distance(current_node,node)
                    parent_of[node] = current_node
                    visited_nodes.append(node)
        if (end_node in visited_nodes):
            break

    list_edges = []
    while parent_of[last_node] is not None:
        list_edges = [graph.get_edge(parent_of[last_node],last_node)]+ list_edges
        last_node = parent_of[last_node]
    return list_edges

def dfs(graph, start_node, end_node):
    Q = []
    Q.append(start_node)
    visited_nodes = []
    visited_nodes.append(start_node)
    parent_of = {}
    parent_of[start_node] = None
    distance_of = {}
    distance_of[start_node] = 0
    last_node = end_node

    while (bool(Q)):
        current_node = Q[0]
        is_neigbors = True
        neighbors = graph.neighbors(current_node)
        neighbors.sort(key=lambda x: x.data)
        for i in neighbors:
            if (i not in visited_nodes):
                is_neigbors = False
                Q = [i] + Q
                distance_of[i] = distance_of[current_node] + graph.distance(current_node, i)
                parent_of[i] = current_node
                visited_nodes.append(i)
                break
        if (is_neigbors):
            Q.pop(0)
        if (end_node in visited_nodes):
            break

    list_edges = []
    while parent_of[last_node] is not None:
        list_edges = [graph.get_edge(parent_of[last_node], last_node)] + list_edges
        last_node = parent_of[last_node]

    return list_edges


def dijkstra_search(graph, start_node, end_node):
    Q = {}
    Q[start_node] = 0
    visited_nodes = []
    visited_nodes.append(start_node)
    parent_of = {}
    parent_of[start_node] = None
    distance_of = {}
    distance_of[start_node] = 0
    last_node = end_node
    temp_nodes = []

    while (bool(Q)):
        current_node = min(Q, key=Q.get)
        Q.pop(current_node)
        visited_nodes.append(current_node)
        for node in graph.neighbors(current_node):
            if ((node not in visited_nodes and node not in temp_nodes) or (distance_of[node]>distance_of[current_node] + graph.distance(current_node, node))):
                Q[node] = distance_of[current_node] + graph.distance(current_node, node)
                distance_of[node] = distance_of[current_node] + graph.distance(current_node, node)
                parent_of[node] = current_node
                temp_nodes.append(node)
        if (end_node in visited_nodes):
            break

    list_edges = []
    while parent_of[last_node] is not None:
        list_edges = [graph.get_edge(parent_of[last_node], last_node)] + list_edges
        last_node = parent_of[last_node]
    return list_edges

def a_star_search(graph, start_node, end_node):

    source_tile = start_node.data.x
    parent_of = {}
    parent_of[start_node] = None
    distance_of = {}
    distance_of[start_node] = 0
    Q = {}
    Q[start_node] = 0
    heuristic_cost = {}
    visited_nodes = []
    visited_nodes.append(start_node)
    temp_nodes = []
    last_node = end_node
    heuristic_cost[start_node] = get_Euclidean_distance(start_node, end_node)

    while (bool(Q)):
        current_node = min(heuristic_cost, key=heuristic_cost.get)
        heuristic_cost.pop(current_node)
        Q.pop(current_node)
        visited_nodes.append(current_node)

        for node in graph.neighbors(current_node):
            if ((node not in visited_nodes and node not in temp_nodes) or (distance_of[node]>distance_of[current_node] + graph.distance(current_node, node))):
                Q[node] = distance_of[current_node] + graph.distance(current_node, node)
                heuristic_cost[node] = get_Euclidean_distance(node, end_node) + graph.distance(current_node, node)
                distance_of[node] = distance_of[current_node] + graph.distance(current_node, node)
                parent_of[node] = current_node
                temp_nodes.append(node)
        if (end_node in visited_nodes):
            break
    list = []
    while parent_of[last_node] is not None:
        list = [graph.get_edge(parent_of[last_node], last_node)] + list
        last_node = parent_of[last_node]
    for i in list:
        pass
    return list

def get_heuristic_cost(start_node, end_node):

    x_diff= abs(start_node.data.x - end_node.data.x)
    y_diff =abs(start_node.data.y - end_node.data.y)
    return x_diff + y_diff

def get_Euclidean_distance(start_node, end_node):
    x_diff = ((start_node.data.x - end_node.data.x) ** 2)
    y_diff = ((start_node.data.y - end_node.data.y) ** 2)
    distance_x_to_y = ((x_diff + y_diff)**0.5)
    return distance_x_to_y
