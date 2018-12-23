from odoo import models, fields, api
    
class res_partner(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'
	
	brand = fields.Char('Marca')
	edge = fields.Integer('Edad')

	#field_Many2one = fields.Many2one('odoomodulo.brand', String='Brand')