import unittest
from tests_12_1 import RunnerTest #без пропуска тестов
from tests_12_2 import TournamentTest #без пропуска тестов
from tests_12_3 import RunnerTest, TournamentTest #с пропусками тестов


test = unittest.TestSuite()
test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test)