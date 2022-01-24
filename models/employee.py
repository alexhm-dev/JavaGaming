
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError
import re

class Employee(models.Model):
    _name = 'java_gaming.employee'
    _inherit = 'res.users'
   
    fechaContratacion = fields.Date(default=fields.Date.today)
    salario = fields.Float(string="Pajin")  
    

    games = fields.Many2many('java_gaming.game', String="Game")
    
    @api.onchange('email')
    def validate_mail(self):
        if self.email:
         match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email_id)
        if match == None:
            raise ValidationError('Not a valid E-mail ID')
    @api.onchange('salario')
    def _verify_salario(self):
        if self.salario < 1000:
            return {
                'warning': {
                    'title': "Valor 'salario' incorrecto",
                    'message': "El salario no debe de ser menor que 1000",
                },
            }