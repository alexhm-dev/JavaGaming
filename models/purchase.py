# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


class Purchase(models.model):
    _name='java_gaming.purchase'
   
    purchaseDate = fields.Date()
    client = Many2One('java_gaming.purchases',String="Client")
    game = Many2One('java_gaming.game',String="Game")