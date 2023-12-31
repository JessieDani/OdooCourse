from odoo import _, api, models, fields
from odoo.exceptions import ValidationError


class APTLog(models.Model):
    _name = 'apt.log'
    _description = 'Amazon Price Tracker Log'
    _inherit = ['add.tag']
    _order = 'datetime desc'

    datetime = fields.Datetime()
    price = fields.Float()
    transport_price = fields.Float()
    # Param store=True para que se guarde en la base de datos
    total_price = fields.Float(
        compute='_compute_total_price',
        readonly=False,
        inverse='_inverse_total_price',
    )
    dummy_price = fields.Float(
        compute='_compute_dummy_price',
        search='_search_dummy_price',
    )
    seller_id = fields.Many2one('amazon.seller')
    seller = fields.Char(string="Seller Create")
    # Cuando crees un `apt.log` con `seller` y no `seller_id`, tiene que crear un `amazon.seller` con name
    # `seller` y asignarlo al `apt.log` creado
    # Pistas: CRUD, super(), self.env['amazon.seller'].create(...)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('seller') and not vals.get('seller_id'):
                seller = self.env['amazon.seller'].create({'name': vals.get('seller')})
                vals.update(seller_id=seller.id)
        return super().create(vals_list)

    # Estructura create y write para modificaciones en creacion/actualizacion de records
    # @api.model_create_multi
    # def create(self, vals_list):
    #     # ... Cosas antes de crear, normalment interactuando con vals_list
    #     records = super().create(vals_list)
    #     # ... Cosas despues de crear, normalmente interactuando con records
    #     return records

    # def write(self, vals):
    #     # ... Cosas antes de escribir, normalment interactuando con self y vals
    #     result = super().write(vals)
    #     # ... Cosas despues de escribir, normalmente interactuando con self
    #     return result

    # Si queremos hacer algo relacion con delete, mejor que sobreescribir unlink, podemos usar
    # @api.ondelete si es para temas de restricciones

    @api.constrains('price', 'transport_price')
    def _check_price(self):
        for log in self:
            if log.transport_price > log.price:
                raise ValidationError(
                    _('Transport price cannot be greater than price: %s > %s', log.transport_price, log.price)
                )

    @api.depends('price', 'transport_price')
    def _compute_total_price(self):
        for log in self:
            log.total_price = log.price + log.transport_price

    @api.depends('price')
    def _compute_dummy_price(self):
        for log in self:
            log.total_price = 2 * log.price

    def _inverse_total_price(self):
        for log in self:
            log.transport_price = log.total_price - log.price

    @api.onchange('datetime')
    def _onchange_datetime(self):
        self.transport_price = 0

    @api.model
    def _search_dummy_price(self, operator, value):
        return [('price', operator, value/2)]
