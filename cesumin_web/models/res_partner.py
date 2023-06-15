from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def controller_equivalent(self, example, *args):
        return {
            "a": 1112,
            "example": example,
            **{i: args[i] for i in range(0, len(args))}
        }
