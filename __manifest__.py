# -*- coding: utf-8 -*-
{
    'name': "Gaming",

    'summary': """Tienda de juegos""",

    'description': """
       Tienda  de juegos online donde los usuarios podran interactuar
        con la aplicacion 
    """,

    'author': "G5c",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         #'security/ir.model.access.csv',
         'views/templates.xml',
          #'views/game.xml',
         
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}