from odoo import models, fields


class AmazonTagParent(models.Model):
    _name = 'amazon.tag.parent'
    _description = 'Amazon Parent Tag'

    name = fields.Char()
