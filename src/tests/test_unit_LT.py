import unittest
from oxrse_unit_conv.units import LT, kg


class TestPound(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(LT.si_unit.matches(kg))
        self.assertTrue(LT.name, "long ton")

    def test_to_si(self):
        self.assertEqual(LT.to_si(1), 1016.)
    
    def test_from_si(self):
        self.assertAlmostEqual(kg.to_unit(5, LT), 0.00492126)


if __name__ == '__main__':
    unittest.main()
