# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api

class Purchase(models.model):
    _name='javaGaming.Purchase'
   
    purchaseDate = fields.Date()
    #client = Many2One('javaGaming.Purchases',String="Client")
    #game = Many2One('javaGaming.Game',String="Game")