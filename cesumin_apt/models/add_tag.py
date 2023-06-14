from odoo import models, fields


class AddTag(models.AbstractModel):
    _name = 'add.tag'
    _description = 'Add Amazon Tags to Models'

    tag_ids = fields.Many2many('amazon.tag')
