# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Client(models.model):
    _name='javaGaming.Client'
    _inherit='res.users'
    fechaRegistro = fields.Date()
    
    purchases=fields.One2Many('javaGaming.Purchase','idPurchase',String="Purchase")

