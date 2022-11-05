# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Lead(models.Model):
    _inherit = 'crm.lead'
    _description = 'CRM Lead'

    @api.depends('lead_checklist_ids')
    def _compute_progress(self):
        for rec in self:
            rec.progress_rate = (len(rec.lead_checklist_ids.filtered(
                lambda x: x.is_check)) / len(rec.lead_checklist_ids) * 100) if rec.lead_checklist_ids else 0

    lead_checklist_ids = fields.One2many('lead.checklist', 'lead_id')
    progress_rate = fields.Float(compute=_compute_progress)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('user_id'):
                user_id = self.env['res.users'].browse(vals.get('user_id'))
                checklist_data = [{
                    'name': check.name,
                    'checklist_lead_id': check.id}
                    for check in user_id.lead_checklist_ids]
                if checklist_data:
                    vals['lead_checklist_ids'] = [
                        (0, 0, cd) for cd in checklist_data]
        leads = super(Lead, self).create(vals_list)
        return leads
