
from odoo import api
from odoo import fields
from odoo import models

class Client(models.Model):
    _name = 'java_gaming.client'
    #declaramos variables de la entidad game 
    _inherit = 'res.users'
    signUpDate = fields.Date(default=fields.Date.today)
   
    
        #diferentes relaciones 
    client_purchases = fields.One2many('java_gaming.purchase','client',String="Purchase")