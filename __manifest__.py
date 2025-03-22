# -*- coding: utf-8 -*-
{
    'name': "quan_ly_du_an",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        
        'views/cong_viec_graph_views.xml',
        'views/cost_overview.xml',
        'views/du_an_view.xml',
        'views/cong_viec_view.xml',
        'views/nhan_vien_view.xml',
        'views/cp_view.xml',
        'views/on_du_an_view.xml',
        'views/overview.xml',
        
        

        'views/menu.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'quan_ly_du_an/static/src/js/kanban_favorite.js',
            'quan_ly_du_an/static/src/js/kanban_filter.js',
            'quan_ly_du_an/static/src/js/overview_graph.js',
            'quan_ly_du_an/static/src/js/graph_view.js',
            'quan_ly_du_an/static/src/css/kanban_favorite.scss',
            
            
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
