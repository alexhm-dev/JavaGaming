# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


from odoo import models,fields,api,exceptions
class Game(models.Model):
    _name = 'java_gaming.game'
    #declaramos variables de la entidad game
     
    name = fields.Char()
    genre = fields.Char()
    pegi = fields.Integer()
    releaseData = fields.Date()
    price = fields.Float()
    
    #diferentes relaciones 
    platforms = fields.Many2many('java_gaming.platform', String="Platform")
    employees = fields.Many2many('java_gaming.employee', String="Employee")
    purchases = fields.One2many('java_gaming.purchase', 'game', String="Purchase")
    
    
    #VALIDACIONES
    #def es el metodo y el self es el equivalente al this.
    
    @api.onchange('price')
    def _verify_price_value(self):
        if self.price < 0:
            return {
                'warning': {
                    'title': "Precio negativo",
                    'message': "El precio no debe ser menor que 0",
                },
            }
   
   
    @api.constrains('price')
    def _verify_price_value_save(self):
        if self.price < 0:
            raise exceptions.ValidationError("El precio no debe ser menor que 0")
    
    
 
    @api.onchange('pegi')
    def _verify_pegi_value(self):
        if self.pegi < 0 or self.pegi>18:
            return {
                'warning': {
                    'title': "Pegi ",
                    'message': "El pegi no debe ser menor que 0  o mayor que 18",
                },
            }
 
    @api.constrains('pegi')
    def _verify_pegi_value_save(self):
         if self.pegi < 0 or self.pegi>18:
            raise exceptions.ValidationError("El pegi no debe ser menor que 0  o mayor que 18")
        
        
   