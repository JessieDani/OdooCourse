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
    def test_action_increase_price(self):
        prices = list(range(0, 100, 10))
        logs = self.env['apt.log'].create([
            {
                "price": price,
                "seller_id": self.seller.id
            } for price in prices
        ])
        self.assertEqual(logs, self.seller.log_ids)
        to_check = logs.mapped(lambda l: (l, l.price))
        self.seller.action_increase_price()
        for log, old_price in to_check:
            self.assertAlmostEqual(log.price, old_price*1.1)
    # Cuando desarrollar tests:
    # - Cuando implementamos nueva logica
    # - Para testear constraints
    # - Cuando arreglamos un bug, crear test recreando el comportamiento que hacia fallar el codigo, checkear que falla antes del commit del fix y pasa despues
