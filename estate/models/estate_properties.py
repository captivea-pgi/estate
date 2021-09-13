# -*- coding: utf-8 -*-

from odoo import fields, models

class RealEstate(models.Model):
    _name = "estate.property"
    _description = "Real estate management"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda self: fields.Date.today()+relativedelta(month=+6))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[
            ('north','North'),
            ('south','South'),
            ('east','East'),
            ('west','West')
        ]
    )
    active =  fields.Boolean(string='Active', default=True)
    state = fields.Selection(
        string='Type',
        selection=[
            ('new','New'),
            ('offer received','Offer Received'),
            ('offer accepted','Offer Accepted'),
            ('sold','Sold'),
            ('canceled','Canceled')
        ],
        required=True,
        copy=False,
        default="New"
    )