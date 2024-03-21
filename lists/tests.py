from django.test import TestCase


# 冒烟测试
class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)

# Create your tests here.
