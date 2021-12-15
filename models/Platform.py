# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


class Platform(models.Model):
    _name = 'javaGaming.platform'
    #declaramos variables de la entidad game
    idplatform = field.Integer(required=true)    
    name = fields.Char
    releaseData = field.Date
    price = field.Float
    
    #diferentes relaciones 
    games = field.Many2many('javaGaming.game',ondelete='cascade',String="Game")
   