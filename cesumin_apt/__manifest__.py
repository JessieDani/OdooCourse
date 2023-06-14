{
    'name': "Cesumin APT",
    'summary': "Cesumin APT",
    'version': '16.0.1.0.0',
    'depends': [
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/cesumin_apt_menus.xml',
        'views/apt_log_views.xml',
        'views/amazon_seller_views.xml',
    ],
    'demo': [
        'data/amazon_seller_demo.xml',
        'data/apt_log_demo.xml',
    ],
}
