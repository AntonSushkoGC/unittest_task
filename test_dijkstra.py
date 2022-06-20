import unittest

from dijkstra import Graph


class DijkstraTest(unittest.TestCase):
    def setUp(self) -> None:

        self.graph = Graph(
            [
                ("a", "b", 5),
                ("a", "c", 7),
                ("a", "f", 14),
                ("b", "c", 5),
                ("b", "d", 5),
                ("c", "d", 3),
                ("c", "f", 2),
                ("d", "e", 6),
                ("e", "f", 9),
                ("g", "h", 5),
            ]
        )

    def test_vertex_not_exist(self):
        with self.assertRaises(Exception) as context:
            self.graph.dijkstra('a', 'z')
        self.assertTrue(str(context.exception) != "")

    def test_no_way(self):
        self.assertEqual(['g'], list(self.graph.dijkstra('a', 'g')))

    def test_way_exists(self):
        self.assertEqual(['a', 'b'], list(self.graph.dijkstra("a", "b")))

    def test_two_equal_ways(self):
        self.assertEqual(['a', 'b', 'd'], list(self.graph.dijkstra("a", "d")))
