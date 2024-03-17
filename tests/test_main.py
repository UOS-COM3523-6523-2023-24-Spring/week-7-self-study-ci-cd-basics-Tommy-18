import unittest
from main import simple_count, complex_function


class MyTestCase(unittest.TestCase):
    def test_simple_function1(self):
        self.assertEqual(0, simple_count(''))

    def test_simple_function2(self):
        self.assertEqual(5, simple_count('hello'))

    #def test_complex_function(self):
    #     self.assertEqual('behaviour 1', complex_function())


    #Task 2
    #Ideas on how to tackle this issue:
    #   idea 1: create a function in that works as a Dummy or Fakes
    #       - Passes the tests and shows how it should work in a simplified form
    #       - Problem is that it assumes that the tested code works correctly in the first place
    #
    #   idea 2: Have a series of the tests and see if any pass for the less likely result
    #       - Shows that there is a possibility of achieving that particular outcome
    #       - Problems:
    #               - It will require a lot of repeated calls to test for that situation and it is not guaranteed to work
    #               - Increases the run time of the tests considerably and will require a lot more computation
    #
    #   idea 3: Not to test it using unit tests but use manual testing instead
    #        - Have a tester pretend to be a user and manually test that function.
    #        - Problems:
    #               - It will take a long time to test every possibility for every function
    #               - Human error is introduced.
    #
    #   idea 4: just give up and cry (my most likely choice)
    #        - This will not help the program but the programmer will most likely take this route if frustrated enough
    #        - Problem:
    #               - This will not actually help any part of the program
    #        - Positive:
    #               - The programmer may keep what little sanity they have left after failing to test this kind of program
    #
    #

