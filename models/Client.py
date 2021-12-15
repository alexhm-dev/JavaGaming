# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


class Game(models.Model):
    _name = 'javaGaming.client'
    #declaramos variables de la entidad game 
   _inherit='res.users'
   signUpDate :fields.Date
   
    
    #diferentes relaciones 
    client_purchases = field.One2many('javaGaming.client','purchase',String="Purchase")