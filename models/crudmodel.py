from odoo import models, fields

class Brand(models.Model):
	_name = 'odoomodulo1.brand'
	_description = 'Nombre de la marca'

	name = fields.Char(string='Name')
    res_partner_id = fields.One2many('res.partner', String='Name')
