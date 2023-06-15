from odoo import http


class CesuminWeb(http.Controller):
    @http.route('/my_route/<string:example>', auth="user", type="json")
    def my_route(self, example, **kw):
        return {
            "a": 1112,
            "example": example,
            **kw
        }

    # Si queremos usarlo para website, anadimos website=True en el decorador, esto nos anade
    # la barra de arriba y el footer
    @http.route('/my_route_http/<string:example>', auth="none", type="http")
    def my_route(self, example, **kw):
        # Tenemos acceso al env de Odoo http.request.env
        return http.request.render("cesumin_web.hola_template", {
            "arg1": example,
            **kw
        })
