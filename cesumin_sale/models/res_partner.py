from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_view_create_sale_order(self):
        pass
