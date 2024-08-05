from odoo import models, api

class AssetAsset(models.Model):
    _inherit = 'eg.asset'  # Ensure this is the correct model name for the assets in the `eg_asset_management` module

    @api.model
    def create(self, vals):
        location_id = vals.get('location_id')
        category_id = vals.get('category_id')

        if location_id and category_id:
            location = self.env['res.partner'].browse(location_id)
            category = self.env['asset.category'].browse(category_id)
            sequence_code = f"TW/{location.name}/{category.short_code}/%(range_year)s"

            vals['code'] = self.env['ir.sequence'].next_by_code(sequence_code) or '/'
        return super(AssetAsset, self).create(vals)

