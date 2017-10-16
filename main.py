"""
quiz2!

Use path finding algorithm to find your way through dark dungeon!

Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9

TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def bfs(graph, initial_node, dest_node):
    parent = {}
    parent[initial_node] = None
    visited_nodes = []
    visited_nodes.append(initial_node)
    distance = {}
    distance[initial_node] = 0
    Q = []
    Q.append(initial_node)
    last_node = dest_node
    while (bool(Q)):
        current_node = Q.pop(0)
        for neighbor in graph.neighbors(current_node):
            if (neighbor not in visited_nodes):
                    Q.append(neighbor)
                    distance[neighbor] = distance[current_node] + graph.distance(current_node,neighbor)
                    parent[neighbor] = current_node
                    visited_nodes.append(neighbor)
        if (dest_node in visited_nodes):
            break
    path = []
    while parent[last_node] is not None:
        path = [graph.get_edge(parent[last_node],last_node)]+ path
        last_node = parent[last_node]
    return path

def dijkstra_search(graph, initial_node, dest_node):
    parent = {}
    parent[initial_node] = None
    visited_nodes = []
    visited_nodes.append(initial_node)
    distance = {}
    distance[initial_node] = 0
    temp_nodes = []
    Q = {}
    Q[initial_node] = 0
    last_node = dest_node
    while (bool(Q)):
        current_node = min(Q, key=Q.get)
        Q.pop(current_node)
        visited_nodes.append(current_node)
        if (dest_node in visited_nodes):
            break
        for neighbor in graph.neighbors(current_node):
            if ((neighbor not in visited_nodes and neighbor not in temp_nodes) or (distance[neighbor]>distance[current_node] + graph.distance(current_node, neighbor))):
                Q[neighbor] = distance[current_node] + graph.distance(current_node, neighbor)
                distance[neighbor] = distance[current_node] + graph.distance(current_node, neighbor)
                parent[neighbor] = current_node
                temp_nodes.append(neighbor)

    path = []
    while parent[last_node] is not None:
        path = [graph.get_edge(parent[last_node], last_node)] + path
        last_node = parent[last_node]

    return path


def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.

    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = json.load(urlopen(req, jsondataasbytes))
    return response

if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    dark_room = get_state('f1f131f647621a4be7c71292e79613f9')

    print("BFS Path:")
    print(empty_room)
    print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
    BFS_Path = bfs(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']), empty_room, dark_room)
    print("Total hp: ")
    print(len(BFS_Path))

    print("Dijkstra Path:")
    print(empty_room)
    print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
    Dijkstra_Path = dijkstra_search(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']), empty_room, dark_room)
    print("Total hp:")
    print(len(Dijkstra_Path))
