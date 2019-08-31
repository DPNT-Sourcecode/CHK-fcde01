from solutions.CHK import checkout_solution


class TestCheckout:

    def test_checkout_1(self):
        assert checkout_solution.checkout("ABC") == 50+30+20

    def test_checkout_2(self):
        assert checkout_solution.checkout("AAA") == 130

    def test_checkout_3(self):
        assert checkout_solution.checkout("BB") == 45

    def test_checkout_4(self):
        assert checkout_solution.checkout("AAAA") == 180

    def test_checkout_5(self):
        assert checkout_solution.checkout("BBB") == 75

    def test_checkout_6(self):
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_7(self):
        assert checkout_solution.checkout("AAAAAAAAAAA") == 490

    def test_checkout_8(self):
        assert checkout_solution.checkout("BBBB") == 90


