/* remove the report.url */
DELETE FROM ir_config_parameter WHERE key = 'report.url';
/* remove enterprise code */
DELETE FROM ir_config_parameter WHERE key = 'database.enterprise_code';
/* set database expiration date to 2050 */
UPDATE ir_config_parameter SET value='2050-01-01' WHERE key = 'database.expiration_date';
/* deactivate mail_servers */
UPDATE ir_mail_server SET active = 'f';
/* disable mobile push notifications */
DELETE FROM ir_config_parameter WHERE key IN ('ocn.ocn_push_notification','odoo_ocn.project_id', 'ocn.uuid');
/* remove saas modules */
UPDATE ir_module_module SET state='uninstalled' WHERE name ilike '%saas%';
/* remove view from saas */
DELETE FROM ir_ui_view WHERE name ilike '%saas%';
/* Set the admin user */
UPDATE res_users SET PASSWORD='admin', LOGIN='admin' WHERE id=2;

UPDATE ir_config_parameter SET value = '"+new_uuid+"' WHERE key = 'database.uuid';
INSERT INTO ir_mail_server(active,name,smtp_host,smtp_port,smtp_encryption) VALUES (true,'mailcatcher','localhost',1025,false);
DELETE FROM ir_attachment WHERE name like '%assets_%';
