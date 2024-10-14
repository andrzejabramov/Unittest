import unittest as ut


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(ut.TestCase):

    def test_run(self):
         ex_run = Runner('Name')
         for r in range(10):
            ex_run.run()
         self.assertEqual(ex_run.distance, 100)

    def test_walk(self):
        ex_walk = Runner('Name')
        for f in range(10):
            ex_walk.walk()
        self.assertEqual(ex_walk.distance, 50)

    def test_challenge(self):
         el_walk = Runner('Name')
         el_run = Runner('Name')
         for f in range(10):
             el_walk.walk()
             el_run.run()
         self.assertNotEqual(el_run.distance, el_walk.distance)


if __name__ == '__main__':
    ut.main()


