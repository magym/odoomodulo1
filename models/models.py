from odoo import models, fields
    
class res_partner(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'
	
	brand = fields.Char(String = 'Marca')
	edge = fields.Integer()

	brand_id = fields.Many2one('odoomodulo.brand', String="Marca")
