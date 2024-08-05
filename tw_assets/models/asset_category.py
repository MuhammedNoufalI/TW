from odoo import models, fields

class AssetCategory(models.Model):
    _inherit = 'eg.asset.category'

    short_code = fields.Char(string="Short Code", required=True)
