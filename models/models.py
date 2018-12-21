from odoo import models, fields
    
class res_partner(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'
	
	hola = fields.Boolean('Hola')
	