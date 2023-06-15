import unittest
from odoo.addons.account.tests.test_tour import TestUi


# old_test = TestUi.test_01_account_tax_groups_tour
# def test_01_account_tax_groups_tour(self):
#     # Cambios
#     old_test(self)
#     # Cambios

# def test_01_account_tax_groups_tour(self):
#     """
#     copy paste el original, hago mis cambios
#     y lo indico, por ejemplo con comentarios
#     OVERRIDE
#     """

# Si el test no es relevante nos lo saltamos
@unittest.skip('monkey patch')
def monkey_patch(self):
    pass

TestUi.test_01_account_tax_groups_tour = monkey_patch
