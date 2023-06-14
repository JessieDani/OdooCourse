from odoo import models, fields


class AmazonTag(models.Model):
    _name = 'amazon.tag'
    _description = 'Amazon Tag'

    # Algunos parametros interesantes
    # default -> valor o funcion
    # required -> boolean
    # string -> texto
    # index: crea indice en SQL -> boolean
    # m2o -> ondelete
    # docs https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html#fields
    name = fields.Char(index=True)
    color = fields.Integer(default='1')
