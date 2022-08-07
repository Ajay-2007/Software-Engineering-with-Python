import unittest

from Ex_3_OPP_Player.Player import Player


""" TEST CASES Can test ?
- ARGS Should not be empty
- Class? is that class instansiable ? ===> DONE
- fname, lname --> str ===> DONE
- speed --> int ===> DONE
- EXAMPLE NICKNAME: ====> DONE
    - amr elmasry --> A.Elmasry
- Check the id count of created objects ===> DONE
- [SKIP] Data Persistance: Check for unique values, fname+lname -> storing (json)
"""

# alphabatical order of test methods execution
class TestPlayer(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.p1 = Player("Kareem", "Gamal", 100) # id 2
        # gets executed once only at the start before the rest of test/instance methods

    def setUp(self):
        # this gets executed before every single test method
        # print("...STARTING BEFORE THIS UPCOMING METHOD...")
        pass

    def test_FLnameValType(self):
        self.assertIsInstance(self.p1.fname, str)
        self.assertIsInstance(self.p1.lname, str)

        with self.assertRaises(AssertionError):
            Player("", "", None)

    def test_speedValType(self):
        # Happy path test --> int
        self.assertIsInstance(self.p1.speed, int)

        with self.assertRaises(AssertionError):
            Player("John", "Doe", "212")


    def test_canCreateObj(self):
        with self.assertRaises(TypeError):
            Player()

    def test_nickname(self):
        self.p1.set_nickname()
        self.assertEqual(self.p1.nickname, "K.Gamal")

    def test_PlayerID(self):
        self.assertEqual(self.p1.id, 1)

# pdb ---> Python interactive debugger
# What happens if you want to debug your code? Unfortunately your can't be debugged
# via the VS code GUI

# 1) Redundencies