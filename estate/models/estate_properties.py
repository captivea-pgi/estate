# -*- coding: utf-8 -*-

from odoo import fields, models

class RealEstate(models.Model):
    _name = "estate.property"
    _description = "Real estate management"

    name = fields.Char()