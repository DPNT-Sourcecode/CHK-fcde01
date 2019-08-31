from solutions.HLO import hello_solution


class TestHello:

    def test_hlo1(self):
        assert isinstance(hello_solution.hello("world"), str)
        assert hello_solution.hello("Craftsman") == "Hello, Craftsman!"

    def test_hlo2(self):
        assert isinstance(hello_solution.hello("dskgfldfkjf sdgkdlfj"), str)
        assert hello_solution.hello("Mr. X") == "Hello, Mr. X!"

    def test_hlo3(self):
        assert isinstance(hello_solution.hello("3453443"), str)
        assert hello_solution.hello("  Mr. X  ") == "Hello, Mr. X!"
