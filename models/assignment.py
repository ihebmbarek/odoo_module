from odoo import models, fields

class Assignment(models.Model):
    _name = 'school_management.assignment'
    _description = 'Assignment Details'

    title = fields.Char("Title", required=True)
    description = fields.Text("Description")
    due_date = fields.Date("Due Date")
    course_id = fields.Many2one('school_management.course', string="Course")