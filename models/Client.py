
from odoo import models,fields,api

class Client(models.Model):
    _name = 'java_gaming.Client'
    #declaramos variables de la entidad game 
   _inherit='res.users'
   signUpDate =fields.Date(default=fields.Date.today)
   
    
    #diferentes relaciones 
    #client_purchases = field.One2many('java_gaming.Client','purchase',String="Purchase")