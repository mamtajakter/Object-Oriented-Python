"""Unit tests for testme.py"""

import unittest
from buggy import *

class TestMaxRun(unittest.TestCase):

    def test_max_run_example(self):
        self.assertEqual(max_run([1, 2, 2, 2, 3]), [2, 2, 2])
        self.assertEqual(max_run([]), [])
        self.assertEqual(max_run([1]), [1])

if __name__ == "__main__":
    unittest.main()

#
# import model
# from model import Vec, Board, Tile
# import unittest
# import sys
#
#
# class TestVec(unittest.TestCase):
#
#     def test_equality(self):
#         v1 = Vec(7, 12)
#         v2 = Vec(8, 13)
#         self.assertNotEqual(v1, v2)
#         v3 = Vec(7, 12)
#         self.assertEqual(v1, v3)
#
#     def test_addition(self):
#         v1 = Vec(8, 7)
#         v2 = Vec(12, 15)
#         self.assertEqual(v1 + v2, Vec(20, 22))
#         # Addition does not modify the points that have been added
#         self.assertEqual(v1, Vec(8, 7))
#         self.assertEqual(v2, Vec(12, 15))
#
# class TestBoardConstructor(unittest.TestCase):
#
#     def test_default(self):
#         board = Board()
#         self.assertEqual(board.tiles, [[None, None, None, None],
#                                        [None, None, None, None],
#                                        [None, None, None, None],
#                                        [None, None, None, None]])
#
#     def test_3x5(self):
#         board = Board(rows=3, cols=5)
#         self.assertEqual(board.tiles, [[None, None, None, None, None],
#                                  [None, None, None, None, None],
#                                  [None, None, None, None, None]])
#
#
#     def test_constructed_empties(self):
#         """A newly constructed Board should always have at least
#         one empty space.
#         """
#         board = model.Board()
#         self.assertTrue(board.has_empty())
