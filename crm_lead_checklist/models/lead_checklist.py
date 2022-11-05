# -*- coding: utf-8 -*-

from odoo import fields, models, _
from odoo.exceptions import UserError


class LeadChecklistUser(models.Model):
    _name = 'lead.checklist.user'
    _description = 'Lead Checklist User'

    name = fields.Char('Name')
    user_id = fields.Many2one('res.users')

    def unlink(self):
        for rec in self:
            lead_check_ids = self.env['lead.checklist'].search(
                [('checklist_lead_id', '=', rec.id), ('is_check', '=', True)])
            for lead in lead_check_ids:
                raise UserError(_("You can not delete %s Checklist. First uncheck %s checklist from %s Lead") % (
                    rec.name, rec.name, lead.lead_id.name))
        super(LeadChecklistUser, self).unlink()


class LeadChecklist(models.Model):
    _name = 'lead.checklist'
    _description = 'Lead Checklist'

    name = fields.Char('Name')
    is_check = fields.Boolean('')
    lead_id = fields.Many2one('crm.lead')
    checklist_lead_id = fields.Many2one(
        'lead.checklist.user', string='Checklist')
