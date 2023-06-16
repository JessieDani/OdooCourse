from odoo import api, SUPERUSER_ID


def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    cr.execute("SELECT id, parent FROM amazon_tag WHERE parent IS NOT NULL")
    tags_data = cr.fetchall()
    for amazon_tag_id, parent_name in tags_data:
        tag = env['amazon.tag'].browse(amazon_tag_id)
        parent = env['amazon.tag.parent'].search([('name', '=', parent_name)])
        if not parent:
            parent = env['amazon.tag.parent'].create({'name': parent_name})
        tag.parent_id = parent
