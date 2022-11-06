# -*- coding: utf-8 -*-

from odoo import fields, models, _
from odoo.exceptions import UserError


class LeadChecklistUser(models.Model):
    _name = 'lead.checklist.user'
    _description = 'Lead Checklist User'

    name = fields.Char('Name', copy=False, required=True)
    user_id = fields.Many2one('res.users')

    _sql_constraints = [('name_user_id_uniq', 'unique (name, user_id,\
                        is_active)', 'Name must be unique per User!')]

    def unlink(self):
        for rec in self:
            # Check if current checklist checked in any Lead or not
            lead_check_ids = self.env['lead.checklist'].search(
                [('checklist_lead_id', '=', rec.id), ('is_check', '=', True)])
            for lead in lead_check_ids:
                raise UserError(_("You can not delete %s Checklist.\
                    First uncheck %s checklist from %s Lead") % (
                    rec.name, rec.name, lead.lead_id.name))
        super(LeadChecklistUser, self).unlink()


class LeadChecklist(models.Model):
    _name = 'lead.checklist'
    _description = 'Lead Checklist'

    name = fields.Char(string='Name')
    is_check = fields.Boolean()
    lead_id = fields.Many2one('crm.lead', string='Lead')
    checklist_lead_id = fields.Many2one(
        'lead.checklist.user', string='Checklist')
