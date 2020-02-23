import unittest
import geometry as geo


class PointTestCases(unittest.TestCase):

    def test_point_instance(self):
        p = geo.Point3d(1, 1, 1)
        self.assertIsInstance(p, geo.Point3d)

    def test_point_instance_is_correct(self):
        p = geo.Point3d(1, 1, 1)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 1)
        self.assertEqual(p.z, 1)

    def test_points_substraction_return_vector(self):
        p1 = geo.Point3d(1, 1, 1)
        p2 = geo.Point3d(3, 3, 3)
        v1 = p2 - p1
        self.assertIsInstance(v1, geo.Vector3d)

    def test_points_substraction_return_correct_vector(self):
        p1 = geo.Point3d(1, 1, 1)
        p2 = geo.Point3d(3, 3, 3)
        v1 = p2 - p1
        v2 = geo.Vector3d(2, 2, 2)
        self.assertEqual(v1.nx, v2.nx)
        self.assertEqual(v1.ny, v2.ny)
        self.assertEqual(v1.nz, v2.nz)


class VextorTestCases(unittest.TestCase):

    def test_vector_instance(self):
        v = geo.Vector3d(2, 2, 2)
        self.assertIsInstance(v, geo.Vector3d)

    def test_vector_instance_is_correct(self):
        v = geo.Vector3d(2, 2, 2)
        self.assertEqual(v.nx, 2)
        self.assertEqual(v.ny, 2)
        self.assertEqual(v.nz, 2)

    def test_vectors_cross_product_return_vector(self):
        v1 = geo.Vector3d(1, 1, 1)
        v2 = geo.Vector3d(2, 2, 2)
        v = v1 ** v2
        self.assertIsInstance(v, geo.Vector3d)

    def test_vectors_cross_product_return_correct_vector(self):
        v1 = geo.Vector3d(1, 2, 3)
        v2 = geo.Vector3d(4, 5, 6)
        v3 = v1 ** v2
        self.assertEqual(v3.nx, -3)
        self.assertEqual(v3.ny, 6)
        self.assertEqual(v3.nz, -3)

    def test_vectors_substraction_return_vector(self):
        v1 = geo.Vector3d(1, 1, 1)
        v2 = geo.Vector3d(2, 2, 2)
        v = v1 - v2
        self.assertIsInstance(v, geo.Vector3d)

    def test_vectors_substraction_return_correct_vector(self):
        v1 = geo.Vector3d(1, 1, 1)
        v2 = geo.Vector3d(2, 2, 2)
        v3 = v1 - v2
        self.assertEqual(v3.nx, -1)
        self.assertEqual(v3.ny, -1)
        self.assertEqual(v3.nz, -1)

    def test_vectors_dot_product_return_number(self):
        v1 = geo.Vector3d(1, 1, 1)
        v2 = geo.Vector3d(2, 2, 2)
        num = v1 * v2
        self.assertIsInstance(num, int or float)

    def test_vectors_dot_product_return_correct_number(self):
        v1 = geo.Vector3d(1, 1, 1)
        v2 = geo.Vector3d(2, 2, 2)
        num = v1 * v2
        self.assertEqual(num, 6)

    def test_vector_length_is_correct(self):
        v1 = geo.Vector3d(2, 2, 1)
        self.assertEqual(v1.length(), 3)


class LineTestCases(unittest.TestCase):

    def test_line_instance(self):
        line = geo.Line(1, 1, 1, 1, 1, 1)
        self.assertIsInstance(line, geo.Line)

    def test_line_partials_instances(self):
        line = geo.Line(1, 1, 1, 1, 1, 1)
        self.assertIsInstance(line.p, geo.Point3d)
        self.assertIsInstance(line.v, geo.Vector3d)

    def test_line_perpendicular_return_point(self):
        line1 = geo.Line(2, 2, 3, 0, 0, -1)
        line2 = geo.Line(0, -1, 2, 0, -2, 4)
        line3 = line1.perpendicular_line_at_point(line2)
        self.assertIsInstance(line3, geo.Point3d)

    # def test_line_perpendicular_return_correct_line(self):
    #     line1 = geo.Line(2, 2, 3, 0, 0, -1)
    #     line2 = geo.Line(0, -1, 2, 0, -2, 4)
    #     line3 = line1.perpendicular_line(line2)


class LinePerpendicularStepByStepTest(unittest.TestCase):

    def setUp(self) -> None:
        self.line = geo.Line(2, 2, 3, 0, 0, -1)
        self.other = geo.Line(0, -1, 2, 0, -2, 4)

    def test_step1(self):
        n = self.line.v ** self.other.v
        self.assertEqual(n.nx, -2)
        self.assertEqual(n.ny, 0)
        self.assertEqual(n.nz, 0)

    def test_step2(self):
        n = self.line.v ** self.other.v
        n2 = self.other.v ** n
        self.assertEqual(n2.nx, 0)
        self.assertEqual(n2.ny, -8)
        self.assertEqual(n2.nz, -4)

    def test_step3(self):
        wagedpoint = self.other.p - self.line.p
        self.assertEqual(wagedpoint.nx, -2)
        self.assertEqual(wagedpoint.ny, -3)
        self.assertEqual(wagedpoint.nz, -1)

    def test_step4(self):
        n = self.line.v ** self.other.v
        n2 = self.other.v ** n
        wagedpoint = self.other.p - self.line.p
        multiplier = (n2 * wagedpoint) / (self.line.v * n2)
        self.assertEqual(multiplier, 7)


class FunctionsTestCases(unittest.TestCase):

    def test_unpack_data_function(self):
        l1 = (1, 1, 1, 1, 1, 1)
        l2 = geo.unpack_data(l1)
        self.assertEqual(l2.p.x, 1)
        self.assertEqual(l2.p.y, 1)
        self.assertEqual(l2.p.z, 1)
        self.assertEqual(l2.v.nx, 1)
        self.assertEqual(l2.v.ny, 1)
        self.assertEqual(l2.v.nz, 1)

    def test_line_distance_function(self):
        line1 = (2, 2, 3, 0, 0, -1)
        line2 = (0, -1, 2, 0, -2, 4)
        distance = geo.line_distance(line1, line2)
        self.assertEqual(distance, 2)


if __name__ == '__main__':
    unittest.main()
