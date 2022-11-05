# -*- coding: utf-8 -*-

from odoo import api, fields, models

class CRMLead(models.Model):
	_inherit = 'crm.lead'
	_description = 'CRM Lead'