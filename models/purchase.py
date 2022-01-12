# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api

class Purchase(models.Model):
    _name='java_gaming.purchase'
   
    purchaseDate = fields.Date()
    
    client = fields.Many2one('java_gaming.client',String="Client")
    game = fields.Many2one('java_gaming.game',String="Game")