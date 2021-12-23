

from odoo import models,fields,api

class Employee(models.Model):
    _name='java_gaming.Employee'
    _inherit='res.users'
   
    fechaContratacion = fields.Date()
    salario = fields.Float()  
   
    
    
    #games=fields.Many2many('java_gaming.Game',String="Game")
