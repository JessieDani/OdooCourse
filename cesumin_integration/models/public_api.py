import requests
import logging
from odoo import api, models, fields, Command

_logger = logging.getLogger(__name__)


class PublicAPI(models.Model):
    _name = 'public.api'
    _description = "Public API Entries"

    api_name = fields.Char()
    description = fields.Text()
    auth = fields.Selection(selection=[('oauth', 'OAuth'), ('apikey', 'ApiKey')])
    https = fields.Boolean()
    cors = fields.Boolean()
    link = fields.Char()
    category = fields.Char()

    _sql_constraints = [
        ('unique_api_name', 'UNIQUE (api_name)', 'API name has to be unique')
    ]

    @api.model
    def cron_fetch_public_api(self):
        try:
            response = False
            url = self.env['ir.config_parameter'].get_param('cesumin_integration.public_api_url')
            response = requests.get(url)
            data_list = response.json()['entries']
        except:
            if response:
                _logger.error(f'Error trying to get public API, Status: {response.status_code}\nBody: {response.text}')
            else:
                _logger.error('No response object in public API cron')
            return
        self._cron_create_public_api(data_list)
        self._cron_create_sale_order(data_list)

    @api.model
    def _cron_create_public_api(self, data_list):
        vals_list = []
        for data in data_list:
            if not self.env['public.api'].search([('api_name', '=', data['API'])]):
                vals_list.append({
                    'api_name': data['API'],
                    'description': data['Description'],
                    'auth': data['Auth'].lower() if data['Auth'] != '' else False,  # data['Auth'].lower() or False
                    'https': data['HTTPS'],
                    'cors': data['Cors'] == 'yes',
                    'link': data['Link'],
                })
        # Nadie puede crear records public.api segun los access rights, pero los cron se corren como
        # superusuario y para este usuario no se checkean los derechos de accesso, siempre tiene accesso
        # a todo
        # Si queremos ejecutar algo como superusuario en el codigo llamamos a sudo()
        self.env['public.api'].create(vals_list)

    @api.model
    def _cron_create_sale_order(self, data_list):
        vals_list = []
        for data in data_list:
            partner = self.env['res.partner'].search([('name', '=', data['API'])], limit=1)
            if not partner:
                partner = self.env['res.partner'].create({'name': data['API']})
            product = self.env['product.product'].search([('name', '=', data['Category'])], limit=1)
            if not product:
                product = self.env['product.product'].create({'name': data['Category']})
            qty = 0
            for value in data.values():
                if value:
                    qty += 1
            vals_list.append({
                'partner_id': partner.id,
                'order_line': [Command.create({
                    'product_id': product.id,
                    'product_uom_qty': qty,
                })],
            })
        # Si queremos correrlo con un usuario distinto usar metodo with_user
        self.env['sale.order'].create(vals_list)
