from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_view_create_sale_order(self):
        self.ensure_one()
        return {
            "name": "Create Sale Order",
            "type": "ir.actions.act_window",
            "res_model": "create.sale.order",
            "view_mode": "form",
            "target": "new",  # para abrir en un popup
            "context": {
                'default_partner_id': self.id,
            },
        }
