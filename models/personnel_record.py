from odoo import models, fields

class personnelRecord(models.Model):
    _name = 'school_management.personnel_record'
    _description = 'Personnel Record'

    employee_name = fields.Char("Employee Name")
    hire_date = fields.Date("Hire Date")