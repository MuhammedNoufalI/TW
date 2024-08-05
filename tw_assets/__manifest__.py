{
    'name': 'TW Assets Management Extension',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Extend Asset Management with custom sequences and short codes',
    'description': """
        This module extends the EG Asset Management module by adding short codes to asset categories
        and customizing asset sequences to include location and category information.
    """,
    'depends': ['eg_asset_management'],
    'data': [
        'views/asset_category_views.xml',
    ],
    'installable': True,
    'application': False,
}
