# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api

class Game(models.Model):
    _name = 'javaGaming.Game'
    #declaramos variables de la entidad game
     
    name = fields.Char
    genre = fields.Char
    pegi = field.Integer
    releaseData = field.Date
    price = field.Float
    
    #diferentes relaciones 
    #platforms = field.Many2many('javaGaming.Platform',String="Platform")
   # employees= field.Many2many('javaGaming.Employee',String="Employee")
    #purchases= field.One2Many('javaGaming.Purchase','game',String="Purchase")