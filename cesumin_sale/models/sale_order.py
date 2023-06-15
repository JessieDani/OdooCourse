from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # CRUD metodos, tienen que sobreescribirse muchas veces
    # create, write, unlink (mejor a traves de @api.ondelete()), read
    example = fields.Char()

    def action_cancel(self):
        self.example = "Cancelado"
        return super().action_cancel()

    @api.model
    def load(self, fields, data):
        # operaciones con uom
        return super().load(fields, data)

    @api.model
    def cron_print(self):
        print(self.env['sale.order'].search_count([]))
