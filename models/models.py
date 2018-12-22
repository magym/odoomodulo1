from odoo import models, fields
    
class res_partner(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'
	
	brand = fields.Char(String = "marca")
	edge = fields.Integer()

	