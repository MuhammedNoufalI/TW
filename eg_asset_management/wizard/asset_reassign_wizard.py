from odoo import fields, models, api


class AssetReassign(models.Model):
    _name = 'asset.reassign.wizard'
    _description = 'Asset Reassign'

    employee_id = fields.Many2one('hr.employee', string="Employee")
    date_from = fields.Datetime(string="From")
    date_till = fields.Datetime(string="To")
    note = fields.Text(string="Note")

    def action_asset_reassign(self):
        """"""
        for rec in self:
            active_asset = self.env['asset.detail']._context.get('active_id')
            asset = self.env['asset.detail'].browse(active_asset)
            prev_emp = asset.employee_id
            prev_date_from = asset.date_from
            prev_date_till = asset.date_till
            asset.write({
                'employee_id': rec.employee_id.id,
                'date_from': rec.date_from,
                'date_till': rec.date_till,
                'history_ids': [(0, 0, {
                    'employee_id': prev_emp.id,
                    'date_from': prev_date_from,
                    'date_till': prev_date_till,
                    'asset_id': rec.id,
                })]
            })


