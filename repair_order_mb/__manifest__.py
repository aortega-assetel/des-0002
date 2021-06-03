# -*- coding: utf-8 -*-
{
    'name': "Orden de reparación MB",

    'summary': """
        Orden de reparación MB""",

    'description': """
        Orden de reparación MB
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','repair'],

    # always loaded
    'data': [
        'views/repair_order.xml',
    ],
}