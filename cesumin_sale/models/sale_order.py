from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    example = fields.Char()

    def action_cancel(self):
        self.example = "Cancelado"
        return super().action_cancel()

    @api.model
    def load(self, fields, data):
        # operaciones con uom
        return super().load(fields, data)
