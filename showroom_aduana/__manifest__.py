# -*- coding: utf-8 -*-
{
    'name': "showroom_aduana",

    'summary': """
        Modificaciones adicionales en el modulo de inventario""",

    'description': """
        Modificaciones adicionales
    """,

    'author': "Assetel",
    'website': "http://www.Assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'views/aduana_showroom.xml',
    ],
}