from solutions.CHK import checkout_solution


class TestCheckout:

    def test_checkout_0(self):
        assert checkout_solution.checkout(None) == -1

    def test_checkout_lower(self):
        assert checkout_solution.checkout('abc') == -1

    def test_checkout_other_string(self):
        assert checkout_solution.checkout('-') == -1

    def test_checkout_1(self):
        assert checkout_solution.checkout("ABC") == 50+30+20



    def test_checkout_6(self):
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_7(self):
        assert checkout_solution.checkout("AAAAAAAAAAA") == 490


class TestCheckoutA:

    def test_checkout_3A(self):
        assert checkout_solution.checkout("AAA") == 130

    def test_checkout_4A(self):
        assert checkout_solution.checkout("AAAA") == 180

    def test_checkout_5A(self):
        assert checkout_solution.checkout("AAAAA") == 180


class TestCheckoutB:

    def test_checkout_2B(self):
        assert checkout_solution.checkout("BB") == 45

    def test_checkout_3B(self):
        assert checkout_solution.checkout("BBB") == 75

    def test_checkout_4B(self):
        assert checkout_solution.checkout("BBBB") == 90


class TestCheckoutE:

    def test_checkout_1E(self):
        assert checkout_solution.checkout("E") == 40

    def test_checkout_2E(self):
        assert checkout_solution.checkout("EE") == 80

    def test_checkout_2E1B(self):
        assert checkout_solution.checkout("EEB") == 80


