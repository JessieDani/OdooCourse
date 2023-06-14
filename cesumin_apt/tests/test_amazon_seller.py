from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger
from psycopg2.errors import UniqueViolation

class AmazonSellerTest(TransactionCase):
    # setup         se ejecuta antes de cada test
    # setupClass    se ejecuta una unica vez antes de todos los tests
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.seller = cls.env['amazon.seller'].create({'name': 'Test Seller'})

    @mute_logger('odoo.sql_db')
    def test_unique_name(self):
        self.env['amazon.seller'].create({'name': 'Different Seller'})
        with self.assertRaises(UniqueViolation):
            self.env['amazon.seller'].create({'name': 'Test Seller'})

    # Crear test que prueba la accion action_increase_price
    # Pista: self.assertEqual
