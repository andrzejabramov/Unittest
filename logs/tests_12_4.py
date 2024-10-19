import logging
from class_12_4 import Runner
import unittest


logging.basicConfig(level=logging.INFO, filename="runner_tests.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8")


class RunnerTest(unittest.TestCase):

    def test_run(self):
        try:
            ex_run = Runner(9)
            for r in range(10):
                ex_run.run()
            self.assertEqual(ex_run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            print("Неверный тип данных для объекта Runner")
            logging.exception("Неверный тип данных для объекта Runner")

    def test_walk(self):
        try:
            ex_walk = Runner('Вася', -6)
            for f in range(10):
                ex_walk.walk()
            self.assertEqual(ex_walk.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            print('Неверная скорость для Runner')
            logging.exception('Неверная скорость для Runner')

    def test_challenge(self):
         el_walk = Runner('Name')
         el_run = Runner('Name')
         for f in range(10):
             el_walk.walk()
             el_run.run()
         self.assertNotEqual(el_run.distance, el_walk.distance)



if __name__ == '__main__':
    unittest.main()