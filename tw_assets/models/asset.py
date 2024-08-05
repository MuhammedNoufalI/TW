from odoo import models, api

class AssetAsset(models.Model):
    _inherit = 'eg.asset'

    @api.model
    def create(self, vals):
        location_id = vals.get('location_id')
        category_id = vals.get('category_id')

        if location_id and category_id:
            location = self.env['res.partner'].browse(location_id)
            category = self.env['eg.asset.category'].browse(category_id)
            sequence_code = f"TW/{location.name}/{category.short_code}/%(range_year)s"

            vals['code'] = self.env['ir.sequence'].next_by_code(sequence_code) or '/'
        return super(AssetAsset, self).create(vals)
