# -*- coding: utf-8 -*-
from odoo import models, fields


class Property(models.Model):
    _name = 'property.management'
    _description = 'Property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    value = fields.Float(string='Value')
