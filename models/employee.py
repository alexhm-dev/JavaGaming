
from datetime import datetime
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError
import re



class Employee(models.Model):
    _name = 'java_gaming.employee'
    _inherit = 'res.users'
   
    fechaContratacion = fields.Date(default=datetime.today())
    salario = fields.Float(string="salario", default=1000)  


    games = fields.Many2many('java_gaming.game', String="Game")


#VALIDACIONES
      
    @api.onchange('salario')
    def _verify_pegi_value(self):
        if self.salario < 0 or self.salario > 2000:
            return {
                'warning': {
                    'title': "Salario ",
                    'message': "El salario tiene que ser entre (0,2000)",
                },
            }
 
    @api.constrains('salario')
    def _verify_pegi_value_save(self):
        if self.salario < 0 or self.salario > 2000:
            raise exceptions.ValidationError("El salario tiene que ser entre (0,2000)")
        
        
    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                return {
                    'warning': {
                        'title': "Email",
                        'message': "El email no es correcto",
                    },
                }
    @api.constrains('email')
    def validate_mail_save(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise exceptions.ValidationError("El formato de email no es correcto")
                
    @api.onchange('name')
    def validate_name(self):
        if self.name:
            match = re.match('^[A-Za-z]+$', self.name)
            if match == None:
                return {
                    'warning': {
                        'title': "Nombre",
                        'message': "El nombre solo puede tener letras sin espacios",
                    },
                }
    @api.constrains('name')
    def validate_name_save(self):
        if self.name:
            match = re.match('^[A-Za-z]+$', self.name)
            if match == None:
                raise exceptions.ValidationError("El nombre solo puede tener letras sin espacios")



        