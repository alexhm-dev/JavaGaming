


class Employee(models.model):
    _name='javaGaming.Employee'
    _inherit='res.users'
   
    fechaContratacion = fields.Date()
    salario = fields.Float()  
    games=fields.Many2many('javaGaming.Game',String="Games")
