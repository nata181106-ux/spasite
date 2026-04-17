import unittest

from common.r3 import R3
from shadow.polyedr import Facet, is_good_point, Polyedr


class TestGoodPoint(unittest.TestCase):

    def test_good_point_true_upper(self):
        self.assertTrue(is_good_point(R3(0, 2, 0), 1))  # y > 1

    def test_good_point_true_lower(self):
        self.assertTrue(is_good_point(R3(0, -4, 0), 1))  # y < -3

    def test_good_point_false(self):
        self.assertFalse(is_good_point(R3(0, 0, 0), 1))  # внутри


class TestFacetGood(unittest.TestCase):

    def test_two_good_vertexes(self):
        f = Facet([
            R3(0, 2, 0),   # good
            R3(0, -4, 0),  # good
            R3(0, 0, 0)    # bad
        ])
        self.assertTrue(f.has_two_good_vertexes(1))

    def test_not_enough_good(self):
        f = Facet([
            R3(0, 2, 0),   # good
            R3(0, 0, 0),   # bad
            R3(0, 0, 1)    # bad
        ])
        self.assertFalse(f.has_two_good_vertexes(1))


class TestFacetArea(unittest.TestCase):

    def test_triangle_area(self):
        f = Facet([
            R3(0, 0, 0),
            R3(1, 0, 0),
            R3(0, 1, 0)
        ])
        self.assertAlmostEqual(f.area(), 0.5)


class TestPolyedrGoodAreaCube(unittest.TestCase):

    def test_good_facets_area_real(self):
        p = Polyedr("data/cube.geom")
        area = p.good_facets_area()

        self.assertTrue(area == 0)


class TestPolyedrGoodAreaCCC(unittest.TestCase):

    def test_good_facets_area_real(self):
        p = Polyedr("data/ccc.geom")
        area = p.good_facets_area()

        self.assertTrue(-0.000000001 < area - 50 < 0.000000001)


class TestPolyedrGoodAreaBox(unittest.TestCase):

    def test_good_facets_area_real(self):
        p = Polyedr("data/box.geom")
        area = p.good_facets_area()

        self.assertTrue(area == 0)


class TestPolyedrGoodAreaBox10(unittest.TestCase):

    def test_good_facets_area_real(self):
        p = Polyedr("data/box10.geom")
        area = p.good_facets_area()

        self.assertTrue(-0.000000001 < area - 500 < 0.000000001)


class TestPolyedrGoodAreaBox10a(unittest.TestCase):

    def test_good_facets_area_real(self):
        p = Polyedr("data/box10a.geom")
        area = p.good_facets_area()

        self.assertTrue(-0.000000001 < area - 400 < 0.000000001)


class TestPolyedrGoodAreaCube10(unittest.TestCase):

    def test_good_facets_area_real(self):
        p = Polyedr("data/cube10.geom")
        area = p.good_facets_area()

        self.assertTrue(-0.000000001 < area - 600 < 0.000000001)


class TestPolyedrGoodAreaCube10a(unittest.TestCase):

    def test_good_facets_area_real(self):
        p = Polyedr("data/cube10a.geom")
        area = p.good_facets_area()

        self.assertTrue(-0.000000001 < area - 500 < 0.000000001)


class TestPolyedrGoodAreaPiramid(unittest.TestCase):

    def test_good_facets_area_real(self):
        p = Polyedr("data/piramid.geom")
        area = p.good_facets_area()

        self.assertTrue(-0.001 < area - 20.1 < 0.001)


class TestFacetDegenerate(unittest.TestCase):

    def test_area_less_than_three_points(self):
        f = Facet([
            R3(0, 0, 0),
            R3(1, 0, 0)
        ])
        self.assertEqual(f.area(), 0.0)
