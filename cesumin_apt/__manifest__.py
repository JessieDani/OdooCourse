{
    'name': "Cesumin APT",
    'summary': "Cesumin APT",
    'version': '16.0.1.0.2',
    'depends': [
        'mail',
    ],
    'data': [
        'security/cesumin_apt_groups.xml',
        'security/cesumin_apt_security.xml',
        'security/ir.model.access.csv',
        'views/cesumin_apt_menus.xml',
        'views/apt_log_views.xml',
        'views/amazon_seller_views.xml',
        'views/amazon_tag_views.xml',
        'reports/amazon_seller_reports.xml',
        'reports/amazon_seller_templates.xml',
    ],
    'demo': [
        'data/amazon_seller_demo.xml',
        'data/apt_log_demo.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'cesumin_apt/static/src/scss/*.scss',
        ],
    },
}
