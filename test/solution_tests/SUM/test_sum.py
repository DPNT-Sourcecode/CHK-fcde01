from solutions.SUM import sum_solution


class TestSum:

    def test_sum_12(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_100100(self):
        assert sum_solution.compute(100, 100) == 200
