
from unittest import TestCase
from sparkprob import sparkprob


class TestSparkprob(TestCase):
    def test_string(self):
        self.assertTrue(isinstance(sparkprob([0.05, 0.2, 0.55, 0.1, 0.1]), str))
