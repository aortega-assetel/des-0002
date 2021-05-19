# -*- coding: utf-8 -*-
{
    'name': "Contacts_module",

    'summary': """
        Cambios adicionales al modulo de contactos para una mejor administración en los contactos""",

    'description': """
        Modificaciones adicionales al modulo de contactos
    """,

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'views/res_partner.xml',
    ],
}