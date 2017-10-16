"""
quiz2!

Use path finding algorithm to find your way through dark dungeon!

Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9

TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
import codecs

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

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
    response = urlopen(req, jsondataasbytes)
    reader = codecs.getreader('utf-8')
    return json.load(reader(response))

def bfs(initial_node, dest_node):
    Q = []
    Q.append(initial_node)
    visited_nodes = []
    visited_nodes.append(initial_node)
    parent = {}
    parent[initial_node] = None
    distance_of = {}
    distance_of[initial_node] = 0
    edge_to = {}

    while (bool(Q)):
        current_node = get_state(Q.pop(0))
        neighbors = current_node['neighbors']

        for i in range(len(neighbors)):
            v = neighbors[i]
            if (v['id'] not in visited_nodes):
                    Q.append(v['id'])
                    edge_to[v['id']] = transition_state(current_node['id'], v['id'])
                    distance_of[v['id']] = distance_of[current_node['id']] + transition_state(current_node['id'], v['id'])['event']['effect']
                    parent[v['id']] = current_node['id']
                    visited_nodes.append(v['id'])

        if (dest_node in visited_nodes):
            break

    list_edges = []
    last_node = dest_node

    while parent[last_node] is not None:
        list_edges.append(edge_to[last_node])
        last_node = parent[last_node]

    list_edges.reverse()
    return list_edges

def dijkstra_search(initial_node, dest_node):
    """
    Dijkstra Search
    queries the game to do search from the init_node to dest_node
    returns a list of actions going from the init_node to dest_node
    """
    Q = []
    Q.append((0, initial_node))
    distance_of = {}
    distance_of[initial_node] = 0
    parent_of = {}
    edge_to = {}
    visited_node = []

    while (bool(Q)):
        current_node = get_state(Q.pop()[1])
        visited_node.append(current_node['id'])
        neighbors = current_node['neighbors']

        for i in range(len(neighbors)):
            v = neighbors[i]
            alt = distance_of[current_node['id']] + transition_state(current_node['id'], v['id'])['event']['effect']

            if (v['id'] not in visited_node and (v['id'] not in distance_of or alt > distance_of[v['id']])):
                if v['id'] in distance_of:
                    Q.remove((distance_of[v['id']], v['id']))
                Q.append((alt, v['id']))
                distance_of[v['id']] = alt
                parent_of[v['id']] = current_node['id']
                edge_to[v['id']] = transition_state(current_node['id'], v['id'])

        Q = sorted(Q, key=lambda x:x[0])

    list_edges = []
    last_node = dest_node

    while last_node in parent_of:
        list_edges.append(edge_to[last_node])
        last_node = parent_of[last_node]

    list_edges.reverse()

    return list_edges


if __name__ == "__main__":

    initial_node = '7f3dc077574c013d98b2de8f735058b4'
    dest_node = 'f1f131f647621a4be7c71292e79613f9'
    total_cost_bfs = 0
    path_BFS = bfs(initial_node, dest_node)
    prev_id = initial_node
    print("\nBFS Path:")
    for i in range(len(path_BFS)):
        prev_node = get_state(prev_id)
        next_id = path_BFS[i]['id']
        total_cost_bfs += path_BFS[i]['event']['effect']
        print("%s(%s):%s(%s):%i" % (prev_node['location']['name'], prev_id, path_BFS[i]['action'], path_BFS[i]['id'], path_BFS[i]['event']['effect']))
        prev_id = next_id
    print("\nTotal HP: %i" % total_cost_bfs)

    path_dij = dijkstra_search(initial_node, dest_node)
    print("\nDijkstra Path:")
    prev_id = initial_node
    total_cost_dij = 0
    for i in range(len(path_dij)):
        prev_node = get_state(prev_id)
        next_id = path_dij[i]['id']
        total_cost_dij += path_dij[i]['event']['effect']
        print("%s(%s):%s(%s):%i" % (prev_node['location']['name'], prev_id, path_dij[i]['action'], path_dij[i]['id'], path_dij[i]['event']['effect']))
        prev_id = next_id
    print("\nTotal HP: %i" % total_cost_dij)

