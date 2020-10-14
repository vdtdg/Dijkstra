import sys


def deduce_vertices_from_edges(edges):
    """ Create the vertices list from the edges list. Thus, the graph cannot contain an isolated vertex. """
    vertices = set()
    for e in edges:
        vertices.add(e[0])
        vertices.add(e[1])
    return vertices


def weight_of(vertex1, vertex2, edges):
    """ Gives the distance between two vertices. It reads it from the tuple array "edges" """
    if vertex1 == vertex2:
        return None
    for _tuple in edges:
        if vertex1 in _tuple and vertex2 in _tuple:
            return _tuple[2]
    return None


def init(vertices, start_vertex):
    """ Initialization : setting all distances to +infinity except for the starter vertex. """
    distances = dict()
    for vertex in vertices:
        distances[vertex] = sys.float_info.max
    distances[start_vertex] = 0.
    return distances


def find_min_distance_node(graph, distances):
    """ Returns the closest node for the graph with the associated distances. """
    vertices = graph['vertices']
    min_distance = sys.float_info.max
    min_vertex = None
    for vertex in vertices:
        if distances[vertex] < min_distance:
            min_distance = distances[vertex]
            min_vertex = vertex
    return min_vertex


def distances_update(vertex1, vertex2, distances, previous_of, edges):
    """ Check if the new path is shorter, if so rewrite the distance to the vertex and its previous node. """
    distance_of_new_path = distances[vertex1] + weight_of(vertex1, vertex2, edges)
    if distances[vertex2] > distance_of_new_path:
        distances[vertex2] = distance_of_new_path
        previous_of[vertex2] = vertex1


def find_neighbor_of(vertex, edges):
    """ Returns a set of all the neighbor of a vertexes based on the provided edges. """
    neighbor = set()
    for e in edges:
        if vertex in e[0]:
            neighbor.add(e[1])
        elif vertex in e[1]:
            neighbor.add(e[0])
    return neighbor


def dijkstra_shortest_path(graph, start_vertex):
    """ Returns a couple of dict:
         - distances : gives the shortest distances from start_vertex to the key of the value
         - previous  : gives the previous node of a """
    previous = dict()
    distances = init(graph['vertices'], start_vertex)
    vertices_set = graph['vertices']
    while len(vertices_set) != 0:
        vertex = find_min_distance_node(graph, distances)
        vertices_set.remove(vertex)
        for neighbor_vertex in find_neighbor_of(vertex, graph['edges']):
            distances_update(vertex, neighbor_vertex, distances, previous, graph['edges'])
    return distances, previous


def print_shortest_path(graph, node_from, node_to):
    """ Prints the shortest path between node_from and node_to and the path cost in a easily readable way"""
    distances, previous = dijkstra_shortest_path(graph, node_from)
    path_node_list = []
    current_node = node_to
    while current_node != node_from:
        path_node_list.append(current_node)
        current_node = previous[current_node]
    path_node_list.append(node_from)
    path_node_list.reverse()
    print("Path from {} to {} is : ".format(node_from, node_to))
    print(*path_node_list, sep=" -> ")
    print("Cost of this path is {}".format(distances[node_to]))

