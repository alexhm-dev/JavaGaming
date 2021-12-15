# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Employee(models.model):
    _name='javaGaming.Employee'
    _inherit='res.users'
    
    fechaContratacion = fields.Date()
    salario = fields.Float()  
    games=fields.Many2many('javaGaming.Game',String="Games")
