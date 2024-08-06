from odoo import fields, models, api
from datetime import datetime
from odoo.exceptions import UserError


class AssetDetail(models.Model):
    _name = "asset.detail"
    _description = "Asset Detail"

    name = fields.Char(string="Name")
    file_data = fields.Binary(string="Attachment")
    file_name = fields.Char(string="File Name")
    category_id = fields.Many2one(comodel_name="asset.category", string="Category")
    asset_code = fields.Char(string="Asset Code")
    asset_model = fields.Char(string="Asset Model")
    asset_brand = fields.Char(string="Asset Brand")
    serial_no = fields.Char(string="Serial No.")
    purchase_date = fields.Date(string="Purchase Date")
    purchase_value = fields.Float(string="Purchase Value")
    location_id = fields.Many2one(comodel_name="asset.location", string="Current Location")
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee")
    vendor_id = fields.Many2one(comodel_name="res.partner", string="Vendor")
    warranty_start = fields.Date(string="Warranty Start")
    warranty_end = fields.Date(string="Warranty End")
    note = fields.Html(string="Note")
    state = fields.Selection([('draft', 'New'),('release', 'Release'), ('active', 'Assigned'), ('scrap', 'Scrap') ], string='State', default="draft")
    history_ids = fields.One2many('asset.history', 'asset_id', string="Asset History")
    spec_ids = fields.One2many('asset.specification', 'asset_id', string="Asset Configuration")
    date_from = fields.Datetime(string="From")
    date_till = fields.Datetime(string="To")
    reassigned = fields.Boolean(string="Reassigned",default="false")


    @api.model
    def create(self, vals):
        location_id = self.env["asset.location"].search([("is_default", "=", True)], limit=1)
        vals["asset_code"] = self.env["ir.sequence"].next_by_code("asset.detail", sequence_date=datetime.now().year) or "New"
        vals["location_id"] = location_id.id if location_id else None
        return super(AssetDetail, self).create(vals)

    def scrap_asset(self):
        for asset_id in self:
            location_id = self.env["asset.location"].search([("is_scrap", "=", True)], limit=1)
            if location_id:
                asset_id.state = "scrap"

    def confirm_asset(self):
        for asset_id in self:
            asset_id.state = "active"
    def release_asset(self):
        for asset_id in self:
            if not asset_id.date_till:
                raise UserError("Please add an end date to release this asset.")
            asset_id.state = "release"
            prev_emp = asset_id.employee_id
            prev_date_from = asset_id.date_from
            prev_date_till = asset_id.date_till
            asset_id.write({
                'history_ids': [(0, 0, {
                    'employee_id': prev_emp.id,
                    'date_from': prev_date_from,
                    'date_till': prev_date_till,
                    'asset_id': asset_id.id,
                })]
            })
            asset_id.employee_id = None
            asset_id.date_from = None
            asset_id.date_till = None



