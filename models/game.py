# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api

class Game(models.Model):
    _name = 'java_gaming.game'
    #declaramos variables de la entidad game
     
    name = fields.Char()
    genre = fields.Char()
    pegi = fields.Integer()
    releaseData = fields.Date()
    price = fields.Float()
    
    #diferentes relaciones 
    #platforms = field.Many2many('java_gaming.platform',String="Platform")
   # employees= field.Many2many('java_gaming.employee',String="Employee")
    #purchases= field.One2Many('java_gaming.purchase','game',String="Purchase")