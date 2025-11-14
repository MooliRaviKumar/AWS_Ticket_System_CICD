from django.test import TestCase

#dummy class to verify test setup
class DummyTest(TestCase):
    # Verify that the testing framework is set up correctly
    def test_dummy(self):
        self.assertEqual(1, 1)

