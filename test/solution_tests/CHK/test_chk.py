from solutions.CHK import checkout_solution


class TestCheckout:

    def test_checkout_0(self):
        assert checkout_solution.checkout(None) == -1

    def test_checkout_lower(self):
        assert checkout_solution.checkout('abc') == -1

    def test_checkout_lower2(self):
        assert checkout_solution.checkout('ABCa') == -1

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


class TestReadInput:

    def test_read_input(self):
        assert isinstance(checkout_solution._read_prices(), dict)


class TestCheckoutV:

    def test_checkout_1V(self):
        assert checkout_solution.checkout("V") == 50

    def test_checkout_2V(self):
        assert checkout_solution.checkout("VV") == 90

    def test_checkout_3V(self):
        assert checkout_solution.checkout("VVV") == 130

    def test_checkout_4V(self):
        assert checkout_solution.checkout("VVVV") == 180

    def test_checkout_5V(self):
        assert checkout_solution.checkout("VVVVV") == 220

    def test_checkout_6V(self):
        assert checkout_solution.checkout("VVVVVV") == 260


class TestGroupDiscount:

    def test_checkout_3S(self):
        assert checkout_solution.checkout("SSS") == 45

    def test_checkout_3T(self):
        assert checkout_solution.checkout("TTT") == 45

    def test_checkout_3X(self):
        assert checkout_solution.checkout("XXX") == 45

    def test_checkout_3Y(self):
        assert checkout_solution.checkout("YYY") == 45

    def test_checkout_3Z(self):
        assert checkout_solution.checkout("ZZZ") == 45

    def test_mix1(self):
        assert checkout_solution.checkout("STX") == 45

    def test_mix2(self):
        assert checkout_solution.checkout("ZZY") == 45

    def test_mix3(self):
        assert checkout_solution.checkout("XSX") == 45


class TestGroupDiscountFavourCustomer:
    """
    Here, because we favour the customer, if there is an ambiguous
    situation with group discount, we will discount the most expensive items first
    """

    def test_group_discount_favour1(self):
        # Z is most expensive, so 3Z = 45
        assert checkout_solution.checkout("ZZZX") == 45 + 17

    def test_group_discount_favour2(self):
        # Z is most expensive, all others the same (20)
        assert checkout_solution.checkout("STYZ") == 45 + 20

