from odoo import models, fields


class AmazonSellerTag(models.Model):
<<<<<<< HEAD
    _name = 'amazon.seller.tag'
    _description = 'Amazon Seller Tag'

    # Algunos parametros interesantes
    # default -> valor o funcion
    # required -> boolean
    # string -> texto
    # index: crea indice en SQL -> boolean
    # m2o -> ondelete
    # docs https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html#fields
    name = fields.Char(index=True)
    color = fields.Integer(default='1')
=======
    _name = 'amazon.seller'
    _description = 'Amazon Seller'

    name = fields.Char()

   
>>>>>>> 36cff15413a417ee009cb2fd60ea4c354b293bb1
