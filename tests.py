"""Tests for methods found in main to solve Problem 107 on Project Euler"""
from unittest import TestCase
from main import generate_matrix, total_weight, generate_network_graph, prim


class TestProblem107(TestCase):
    """These tests are derived from the example shown on the
    webpage for Problem 107.
    """

    def test_generate_matrix(self):
        example_matrix = [[0, 16, 12, 21, 0, 0, 0],
                          [16, 0, 0, 17, 20, 0, 0],
                          [12, 0, 0, 28, 0, 31, 0],
                          [21, 17, 28, 0, 18, 19, 23],
                          [0, 20, 0, 18, 0, 0, 11],
                          [0, 0, 31, 19, 0, 0, 27],
                          [0, 0, 0, 23, 11, 27, 0]]
        generated_matrix = generate_matrix('example_network.txt')
        self.assertEqual(generated_matrix, example_matrix)

    def test_total_weight(self):
        matrix = generate_matrix('example_network.txt')
        self.assertEqual(total_weight(matrix), 243)

    def test_generate_network_graph(self):
        example_network_graph = {0: {1: 16, 2: 12, 3: 21},
                                 1: {0: 16, 3: 17, 4: 20},
                                 2: {0: 12, 3: 28, 5: 31},
                                 3: {0: 21, 1: 17, 2: 28, 4: 18, 5: 19, 6: 23},
                                 4: {1: 20, 3: 18, 6: 11},
                                 5: {2: 31, 3: 19, 6: 27},
                                 6: {3: 23, 4: 11, 5: 27}}
        generated_matrix = generate_matrix('example_network.txt')
        generated_network_graph = generate_network_graph(generated_matrix)
        self.assertEqual(generated_network_graph, example_network_graph)

    def test_prim(self):
        example_mst = {frozenset({3, 4}): 18,
                       frozenset({0, 1}): 16,
                       frozenset({4, 6}): 11,
                       frozenset({0, 2}): 12,
                       frozenset({1, 3}): 17,
                       frozenset({3, 5}): 19}
        generated_matrix = generate_matrix('example_network.txt')
        generated_network_graph = generate_network_graph(generated_matrix)
        generated_mst = prim(generated_network_graph)
        self.assertEqual(generated_mst, example_mst)
