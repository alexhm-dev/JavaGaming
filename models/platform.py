# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api
from datetime import timedelta

class Platform(models.Model):
    _name = 'java_gaming.platform'
    #declaramos variables de la entidad game  
    platform_name = fields.Char()
    platform_releaseData = fields.Date()
    platform_price = fields.Float()
    
    #diferentes relaciones 
    games = fields.Many2many('java_gaming.game',String="Game")
   