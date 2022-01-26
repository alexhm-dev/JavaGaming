
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError
import re

class Employee(models.Model):
    _name = 'java_gaming.employee'
    _inherit = 'res.users'
   
    fechaContratacion = fields.Date(default=fields.Date.today)
    salario = fields.Float(string="Pajin")  
    

    games = fields.Many2many('java_gaming.game', String="Game")
    
   