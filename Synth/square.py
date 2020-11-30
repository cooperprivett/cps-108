# Put your code here:
i = []
def square_wave(n):
    samples = []
    for i in range(n):
        samples.append(1)
    for i in range(n):
        samples.append(-1)
    return samples

# Keep working until you pass all these tests
# (run them by pressing F5):

from unittest import TestCase, main

class Tests(TestCase):
    def test_square_wave_function_exists(self):
        assert callable(square_wave)

    def test_square_wave_1(self):
        self.assertEqual(square_wave(1), [1, -1])

    def test_square_wave_2(self):
        self.assertEqual(square_wave(2), [1, 1, -1, -1])

    def test_square_wave_3(self):
        self.assertEqual(square_wave(3), [1, 1, 1, -1, -1, -1])

    def test_square_wave_4(self):
        self.assertEqual(square_wave(4), [1, 1, 1, 1, -1, -1, -1, -1])

if __name__ == '__main__':
    main(exit=False, failfast=True, verbosity=2)
