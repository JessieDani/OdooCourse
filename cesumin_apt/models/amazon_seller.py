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
