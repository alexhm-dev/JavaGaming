


class Employee(models.model):
    _name='java_gaming.employee'
    _inherit='res.users'
   
    fechaContratacion = fields.Date()
    salario = fields.Float()  
    games=fields.Many2many('java_gaming.game',String="Games")
