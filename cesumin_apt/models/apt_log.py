from odoo import models, fields


class APTLog(models.Model):
    _name = 'apt.log'
    _description = 'Amazon Price Tracker Log'

    datetime = fields.Datetime()
    price = fields.Float()
    seller_id = fields.Many2one('amazon.seller')
