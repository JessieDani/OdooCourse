from odoo import models, fields


class CreateSaleOrder(models.TransientModel):
    _name = 'create.sale.order'
    _description = 'Create Sale Order Wizard'

    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    date = fields.Datetime(required=True)
    pricelist_id = fields.Many2one('product.pricelist', required=True)
    quantity = fields.Float(string="Qty")
    product_ids = fields.Many2many('product.product')

    def action_confirm(self):
        # Crear SO y mostrarlo
        pass
