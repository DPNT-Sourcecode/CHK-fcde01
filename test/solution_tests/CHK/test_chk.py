from solutions.CHK import checkout_solution


class TestSum:

    def test_sum_12(self):
        assert checkout_solution.compute(1, 2) == 3

    def test_sum_100100(self):
        assert checkout_solution.compute(100, 100) == 200
