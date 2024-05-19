from odoo import models, fields

class studentRecord(models.Model):
    _name = 'school_management.student_record'
    _description = 'Student Record'

    name = fields.Char("Student Name")
    student_id = fields.Many2one('res.users', string="User")