from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    public_api_url = fields.Char(config_parameter='cesumin_integration.public_api_url')
