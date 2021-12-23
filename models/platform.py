# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api
from datetime import timedelta

class Platform(models.Model):
    _name = 'java_gaming.platform'
    #declaramos variables de la entidad game  
    name = fields.Char()
    releaseData = fields.Date()
    price = fields.Float()
    
    #diferentes relaciones 
    #games = field.Many2many('java_gaming.game',ondelete='cascade',String="Game")
   