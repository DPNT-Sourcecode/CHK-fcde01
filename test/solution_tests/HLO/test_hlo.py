from solutions.HLO import hello_solution


class TestHello:

    def test_hlo1(self):
        assert isinstance(hello_solution.hello("world"), str)
        assert hello_solution.hello("Craftsman") == "Hello, World!"

    def test_hlo2(self):
        assert isinstance(hello_solution.hello("dskgfldfkjf sdgkdlfj"), str)
        assert hello_solution.hello("Mr. X") == "Hello, World!"


