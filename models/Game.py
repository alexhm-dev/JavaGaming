# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


class Game(models.Model):
    _name = 'javaGaming.game'
    #declaramos variables de la entidad game
    idgame = field.Integer(required=true)    
    name = fields.Char
    genre = fields.Char
    pegi = field.Integer
    releaseData = field.Date
    price = field.Float
    
    #diferentes relaciones 
    platforms = field.Many2many('javaGaming.platform',String="Platform")
    employees= field.Many2many('javaGaming.employee',String="Employee")
    purchase= field.One2Many('javaGaming.purchase',String="Purchase")