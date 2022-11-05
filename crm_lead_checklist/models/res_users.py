# -*- coding: utf-8 -*-

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'
    _description = 'Users'

    lead_checklist_ids = fields.One2many('lead.checklist.user', 'user_id')
