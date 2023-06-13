from odoo import models, fields


class AmazonSellerTag(models.Model):
    _name = 'amazon.seller'
    _description = 'Amazon Seller'

    name = fields.Char()

   
