## Importante!
En Odoo toda la informacion son records, todo se hace a partir de modelos

## CLI info (opciones odoo-bin)
https://www.odoo.com/documentation/16.0/developer/reference/cli.html

## Guidelines
https://www.odoo.com/documentation/16.0/contributing/development/coding_guidelines.html
### Git guidelines
https://www.odoo.com/documentation/16.0/contributing/development/git_guidelines.html

## Git
Clonar una sola rama con git clone --single-branch -b 16.0 git@github.com:odoo/odoo.git
Tutorial para comprender git https://learngitbranching.js.org/

## Recordset
https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html#record-set-information

## API
https://www.odoo.com/documentation/16.0/developer/reference/external_api.html

## Mixins
https://www.odoo.com/documentation/16.0/developer/reference/backend/mixins.html

## QWeb
https://www.odoo.com/documentation/16.0/developer/reference/frontend/qweb.html

### PDF
Normalmente tendremos que crear una report.action y el template que sera usada para la misma
O modificar directamente el template que queramos
Para desarrollar rapido, vamos a
http://localhost:8069/report/pdf/cesumin_apt.amazon_seller_report/1
http://localhost:8069/report/html/cesumin_apt.amazon_seller_report/1
Docs:
https://www.odoo.com/documentation/15.0/developer/tutorials/pdf_reports.html

## Assets
https://www.odoo.com/documentation/16.0/developer/reference/frontend/assets.html

## ORM metodos comunes (CRUD + otros)
https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html#common-orm-methods
### Command
Especial para manipular campos o2m y m2m
https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html?highlight=command#odoo.fields.Command

## SQL View y Dashboard (Views)
https://www.odoo.com/documentation/15.0/developer/tutorials/dashboards.html
Ejmplo de sql view: https://github.com/odoo/odoo/blob/16.0/addons/im_livechat/report/im_livechat_report_operator.py

## Campos reservados
https://www.odoo.com/documentation/16.0/developer/reference/backend/orm.html#reference-orm-fields-reserved

## Accion para descargar un attachment
Los attachments tambien son records, en particular del modelo ir.attachment
Hay un controller definido con la siguiente ruta, que si se accede se descarga el fichero
Si quereis crear una accion que descarga algo podeis hacerlo asi (ejemplo desde python, se podria hacer con xml)
```
return {
    "type": "ir.actions.act_url",
    "url": f"/web/content/{attachment_id.id}",
    "target": "self",
}
```

## Widgets existentes
https://www.odoo.com/documentation/15.0/developer/reference/frontend/javascript_reference.html#field-widgets

## Inheritance
https://www.odoo.com/documentation/15.0/developer/reference/backend/orm.html#reference-orm-inheritance

## External API
https://www.odoo.com/documentation/16.0/developer/reference/external_api.html#configuration

## Rendimiento
https://www.odoo.com/documentation/16.0/developer/reference/backend/performance.html

## Ejemplo modificando tour
No pudimos verlo en la formacion, pero aqui teneis un ejemplo de modificar un tour existent (test js)
https://github.com/odoo/odoo/commit/fba4e1036b47cbd01f31e593919025faaf4ede55

## Otros tipos de vistas
En particular la de graficos
https://www.odoo.com/documentation/16.0/developer/reference/backend/views.html#graph

## Odoo 17 roadmap
https://www.odoo.com/forum/help-1/new-features-of-odoo-17-219421

## Tutoriales Dashboard (aplicacion dashboard)
### Enterpise
https://www.youtube.com/watch?v=KOSlYfhC9Rk
### Community
https://www.youtube.com/watch?v=d_Ot5Hu5iQ0
