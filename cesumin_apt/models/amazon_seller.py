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