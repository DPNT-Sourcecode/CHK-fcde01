from solutions.HLO import hello_solution


class TestSum:

    def test_hlo1(self):
        assert isinstance(hello_solution.hello("world"), str)

    def test_hlo2(self):
        assert isinstance(hello_solution.hello("dskgfldfkjf sdgkdlfj"), str)

