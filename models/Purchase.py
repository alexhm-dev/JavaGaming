# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api

class Purchase(models.Model):
    _name='java_gaming.Purchase'
   
    purchaseDate = fields.Date()
    #client = Many2One('java_gaming.Purchases',String="Client")
    #game = Many2One('java_gaming.Game',String="Game")