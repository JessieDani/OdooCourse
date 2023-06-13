from odoo import models, fields


class AmazonSeller(models.Model):
    _name = 'amazon.seller'
    _description = 'Amazon Seller'

    name = fields.Char(string="Seller")
    log_ids = fields.One2many('apt.log', inverse_name='seller_id')
    # Parametros en m2m para cambiar nombre tabla y columnas, esto es el por defecto
    # relation="amazon_seller_amazon_seller_tag_rel"
    # column1="amazon_seller_id"    column2="amazon_seller_tag_id"
    # A veces necesario (m2m a si mismo, varios m2m...)
    tag_ids = fields.Many2many('amazon.seller.tag')

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'You cannot repite names!'),
    ]

    def action_increase_price(self):
        # Incrementa 10% el precio en todos los logs relacionados
        self.ensure_one()
        for log in self.log_ids:
            log.price = log.price * 1.1

    def action_context(self):
        self.ensure_one()
        self = self.with_context(always=1111)
        self.with_context(example=432)._action_context1()
        self.with_context(example_2=312321)._action_context2()
        # Aqui self._context no tiene definido ni example ni example_2, porque el contexto se pierde
        # una vez la llamada se devuelve, pero si tiene self._context.get('always') = 1111

    def _action_context1(self):
        # Aqui self._context.get('example') = 432
        # self._context.get('always') = 1111
        pass

    def _action_context2(self):
        # Aqui self._context.get('example_2') = 312321
        # self._context.get('always') = 1111
        pass
