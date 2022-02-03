

from odoo import models,fields,api,exceptions

class Employee(models.Model):
    _name='java_gaming.employee'
    _inherit='res.users'
   
    fechaContratacion = fields.Date()
    salario = fields.Float()  


    games=fields.Many2many('java_gaming.game',String="Game")


  #VALIDACIONES
      
    @api.onchange('salario')
    def _verify_pegi_value(self):
        if self.salario < 0 or self.salario>2000:
            return {
                'warning': {
                    'title': "Salario ",
                    'message': "El salario tiene que ser entre (0,2000)",
                },
            }
 
    @api.constrains('salario')
    def _verify_pegi_value_save(self):
        if self.salario < 0 or self.salario>2000:
            raise exceptions.ValidationError("El salario tiene que ser entre (0,2000)")
        