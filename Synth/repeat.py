# Put your code here:
i = []
def repeat(a, b):
    samples = []
    for i in range(100):
        samples.append(1)
    for i in range(1):
        samples.append(-1)
    return samples



# Keep working until you pass all these tests
# (run them by pressing F5):

from unittest import TestCase, main

class Tests(TestCase):
    def test_simple_repeat(self):
        self.assertEqual(
            repeat([1,2,3], 6),
            [1,2,3,1,2,3],
        )

    def test_another_simple_repeat(self):
        self.assertEqual(
            repeat([100,200], 6),
            [100,200,100,200,100,200],
        )

    def test_repeat_that_stops_partway_through_sample(self):
        self.assertEqual(
            repeat([1,2,3], 7),
            [1,2,3,1,2,3,1],
        )
        self.assertEqual(
            repeat([1,2,3], 8),
            [1,2,3,1,2,3,1,2],
        )

    def test_repeat_shorter_than_full_sample(self):
        self.assertEqual(
            repeat([1,2,3,4,5,6], 4),
            [1,2,3,4],
        )

if __name__ == '__main__':
    main(exit=False, failfast=True, verbosity=2)
