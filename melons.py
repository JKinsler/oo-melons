"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """An abstract base clasee that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """ """

        self.species = species
        self.qty = qty
        self.shipped = False

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """ """
    order_type = "government"
    tax = 0
    # passed = False
    passed_inspection = False

    def mark_inspection(self, passed):
        # if passed:
        passed_inspection = passed
        return passed_inspection


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""

    order_type = "domestic"
    tax = 0.08

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    # requires 4 arguments
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        #  taking species and qty from AbstractMelonOrder
        super().__init__(species, qty)

        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax."""

        if self.qty < 10:
            flat_fee = 3
        else:
            flat_fee = 0

        base_price = 5

        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price + flat_fee

        return total
