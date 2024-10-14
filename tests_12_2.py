from checking_classes import Tournament, Runner
import unittest

class TournamentTest(unittest.TestCase): #создаем класс для тестировангия

    @classmethod #добавляем через данный метод атрибут класса
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(cls): #создаем участнков пробега
        cls.runner1 = Runner('Уэйн', 10)
        cls.runner2 = Runner('Андрей', 9)
        cls.runner3 = Runner('Ник', 3)

    @classmethod #после отраболтки всех тестов этот метод выводит историю забегов
    def tearDownClass(cls):
        for el in cls.all_results:
            print(cls.all_results[el])

    def test_tournament_1(cls): #1-й тест метод
        cls.race1 = Tournament(90, cls.runner1, cls.runner3) #создаем экз класса забега с участниками по заданию
        res = cls.race1.start() #запускаем метод start() этого экз
        cls.all_results['race1'] = res #полученный результат забега добавляем в историю забегов с ключом - идентификатором забега
        key_max = (max(res.keys())) #в значении получившегося словря (тоже словарь), получаем максимальное значение ключа
        val_last = res[key_max] #по полученному ключу извлекаем значение
        cls.assertTrue({2: 'Ник'} == {key_max: val_last}) #проверяем соответствие друг другу тестового шаблона и полученнного результата

    def test_tournament_2(cls):  # 2-й тест метод
        cls.race2 = Tournament(90, cls.runner2, cls.runner3)
        res = cls.race2.start()
        cls.all_results['race2'] = res
        key_max = (max(res.keys()))
        val_last = res[key_max]
        cls.assertTrue({2: 'Ник'} == {key_max: val_last})

    def test_tournament_3(cls):  # 3-й тест метод
        cls.race3 = Tournament(90, cls.runner1, cls.runner2, cls.runner3)
        res = cls.race3.start()
        cls.all_results['race3'] = res
        key_max = (max(res.keys()))
        val_last = res[key_max]
        cls.assertTrue({3: 'Ник'} == {key_max: val_last})

    if __name__ == '__main__':
        unittest.main()
