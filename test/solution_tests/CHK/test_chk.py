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

    def test_checkout_2(self):
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_3(self):
        assert checkout_solution.checkout("ABCDEF") == 115 + 40 + 10


class TestCheckoutA:

    def test_checkout_3A(self):
        assert checkout_solution.checkout("AAA") == 130

    def test_checkout_4A(self):
        assert checkout_solution.checkout("AAAA") == 180

    def test_checkout_5A(self):
        assert checkout_solution.checkout("AAAAA") == 200

    def test_checkout_6A(self):
        assert checkout_solution.checkout("AAAAAA") == 250

    def test_checkout_7A(self):
        assert checkout_solution.checkout("AAAAAAA") == 300

    def test_checkout_8A(self):
        assert checkout_solution.checkout("AAAAAAAA") == 330

    def test_checkout_11A(self):
        assert checkout_solution.checkout("AAAAAAAAAAA") == 450


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

    def test_checkout_2E2B(self):
        assert checkout_solution.checkout("EEBB") == 80 + 30

    def test_checkout_2E3B(self):
        assert checkout_solution.checkout("EEBBB") == 80 + 45

    def test_checkout_3E(self):
        assert checkout_solution.checkout("EEE") == 120

    def test_checkout_4E(self):
        assert checkout_solution.checkout("EEEE") == 160

    def test_checkout_4E1B(self):
        assert checkout_solution.checkout("EEEEB") == 160

    def test_checkout_4E2B(self):
        assert checkout_solution.checkout("EEEEBB") == 160

    def test_checkout_4E3B(self):
        assert checkout_solution.checkout("EEEEBBB") == 160 + 30

    def test_checkout_4E4B(self):
        assert checkout_solution.checkout("EEEEBBBB") == 160 + 45


class TestCheckoutF:

    def test_checkout_1F(self):
        assert checkout_solution.checkout("F") == 10

    def test_checkout_2F(self):
        assert checkout_solution.checkout("FF") == 20

    def test_checkout_3F(self):
        assert checkout_solution.checkout("FFF") == 20

    def test_checkout_4F(self):
        assert checkout_solution.checkout("FFFF") == 30

    def test_checkout_5F(self):
        assert checkout_solution.checkout("FFFFF") == 40

    def test_checkout_6F(self):
        assert checkout_solution.checkout("FFFFFF") == 40
