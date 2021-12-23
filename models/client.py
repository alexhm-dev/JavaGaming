# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


class Client(models.Model):
    _name = 'java_gaming.client'
    #declaramos variables de la entidad game 
   _inherit='res.users'
   signUpDate :fields.Date
   
    
    #diferentes relaciones 
    client_purchases = field.One2many('java_gaming.client','purchase',String="Purchase")