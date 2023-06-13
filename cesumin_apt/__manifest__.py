{
    'name': "Cesumin APT",
    'summary': "Cesumin APT",
    'version': '16.0.1.0.0',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/apt_logs_views.xml',
        'views/amazon_seller_views.xml',
        'views/cesumin_apt_menus.xml',
    ],
    'demo': [
        'data/amazon_seller_demo.xml',
        'data/apt_log_demo.xml'
    ]
}
