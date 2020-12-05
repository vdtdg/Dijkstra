from unittest import TestCase
from Dijkstra import *


class Test(TestCase):
    def test_shortest_path_1(self):
        edges = [('A', 'B', 1.0),
                 ('A', 'C', 2.0),
                 ('A', 'E', 3.0),
                 ('B', 'E', 1.0),
                 ('C', 'E', 1.0),
                 ('E', 'D', 1.0),
                 ('C', 'D', 2.0)]
        vertices = deduce_vertices_from_edges(edges)

        graph = {'vertices': vertices,
                 'edges': edges}

        print_shortest_path(graph, 'A', 'E')

    def test_shortest_path_2(self):
        edges = [('A', 'B', 1.0),
                 ('B', 'C', 3.0),
                 ('C', 'D', 6.0),
                 ('D', 'E', 9.0),
                 ('E', 'F', 12.0),
                 ('G', 'H', 8.0),
                 ('H', 'I', 6.0),
                 ('I', 'J', 4.0),
                 ('J', 'A', 2.0),
                 ('A', 'G', 54.0),
                 ('B', 'F', 27.0),
                 ('J', 'F', 106.0),
                 ('A', 'E', 5.0),
                 ('B', 'I', 14.0),
                 ('H', 'C', 0.2),
                 ('G', 'D', 16.0)]

        vertices = deduce_vertices_from_edges(edges)

        graph = {'vertices': vertices,
                 'edges': edges}

        print_shortest_path(graph, 'A', 'G')

    def test_shortest_path_3(self):
        edges = [('A', 'B', 1.0),
                 ('B', 'C', 3.0),
                 ('C', 'D', 6.0),
                 ('D', 'E', 9.0),
                 ('E', 'F', 12.0),
                 ('G', 'H', 8.0),
                 ('H', 'I', 6.0),
                 ('I', 'J', 4.0),
                 ('J', 'A', 2.0),
                 ('A', 'G', 54.0),
                 ('B', 'F', 27.0),
                 ('J', 'F', 106.0),
                 ('A', 'E', 5.0),
                 ('B', 'I', 14.0),
                 ('H', 'C', 0.2),
                 ('G', 'D', 16.0)]

        vertices = deduce_vertices_from_edges(edges)

        graph = {'vertices': vertices,
                 'edges': edges}

        print(dijkstra_shortest_path(graph, 'A'))

    def test_shortest_path_4(self):
        edges = [('A', 'B', 1.0)]

        vertices = deduce_vertices_from_edges(edges)

        graph = {'vertices': vertices,
                 'edges': edges}

        print(dijkstra_shortest_path(graph, 'A'))

    def test_empty_graph(self):
        edges = []

        vertices = deduce_vertices_from_edges(edges)

        graph = {'vertices': vertices,
                 'edges': edges}

        print(dijkstra_shortest_path(graph, 'A'))
