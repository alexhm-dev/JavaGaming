# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api

class Platform(models.Model):
    _name = 'javaGaming.Platform'
    #declaramos variables de la entidad game  
    name = fields.Char
    releaseData = field.Date
    price = field.Float
    
    #diferentes relaciones 
    #games = field.Many2many('javaGaming.Game',ondelete='cascade',String="Game")
   