# -*- coding: utf-8 -*-
{
    'name': "Garantías",

    'summary': """
        Garantías""",

    'description': """
        Modulo de Garantías""",

    'author': "Assetel",
    'website': "http://www.assetel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'stock', 'report'], 

    # always loaded
    'data': [
        'data/ir_sequence_data.xml',
        'view/warranty_card_menu.xml',
        'view/warranty_card.xml',
        'view/warranty_card_stage.xml',
        'view/warranty_pdf.xml',
        'view/warranty_requests.xml',
        ],

}