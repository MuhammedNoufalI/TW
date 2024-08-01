from odoo import fields, models, api


class AssetHistory(models.Model):
    _name = 'asset.history'

    asset_id = fields.Many2one('asset.detail', string=" Asset")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    date_from = fields.Datetime(string="From")
    date_till = fields.Datetime(string="To")
    note = fields.Text(string="Note")
