# -*- coding: utf-8 -*-

from odoo import models, fields, api

class prueba(models.Model):
    _inherit = 'res.partner.bank'
    
    clabe_campo = fields.Char(string="Clave")

class AddCampClave(models.Model):
    _inherit = 'res.partner'

    clabe_campo = fields.Char(string="Clave")    