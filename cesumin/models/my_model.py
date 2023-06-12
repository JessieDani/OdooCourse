from odoo import models, fields

class my_model(models.Model):
    _name = "my.model"
    _description = "My Model"

    name = fields.Char()
    surname = fields.Char()