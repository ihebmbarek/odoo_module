from odoo import models, fields

class Course(models.Model):
    _name = 'school_management.course'
    _description = 'Course Information'

    name = fields.Char("Course Name", required=True)
    description = fields.Text("Description")
    professor_id = fields.Many2one('school_management.professor', string="Professor")
    
