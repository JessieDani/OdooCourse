from odoo import models, fields


class AmazonSeller(models.Model):
    _name = 'amazon.seller'
    _description = 'Amazon Seller'

    name = fields.Char()
    log_ids = fields.One2many('apt.log', inverse_name='seller_id')
