from odoo import _, models, fields, Command


class CreateSaleOrder(models.TransientModel):
    _name = 'create.sale.order'
    _description = 'Create Sale Order Wizard'

    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    date = fields.Datetime(required=True, default=fields.Datetime.now)
    pricelist_id = fields.Many2one('product.pricelist', required=True)
    quantity = fields.Float(string="Qty")
    product_ids = fields.Many2many('product.product')

    def action_confirm(self):
        self.ensure_one()
        order = self.env['sale.order'].create({
            'partner_id': self.partner_id.id,
            'date_order': self.date,
            'pricelist_id': self.pricelist_id.id,
            'order_line': [Command.create({
                'product_id': product.id,
                'product_uom_qty': self.quantity,
            }) for product in self.product_ids],
        })
        # Otra forma (mejor usando Command)
        # self.env['sale.order.line'].create([
        #     {
        #         'product_id': product.id,
        #         'order_id': order.id,
        #         'product_uom_qty': self.quantity,
        #     } for product in self.product_ids
        # ])
        return {
            "name": _("Sale Order"),
            "type": "ir.actions.act_window",
            "res_model": "sale.order",
            "res_id": order.id,
            "view_mode": "form",
            "target": "current",
        }
