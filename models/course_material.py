from odoo import models, fields

class CourseMaterial(models.Model):
    _name = 'school_management.course_material'
    _description = 'Course Materials'

    title = fields.Char("Title", required=True)
    course_id = fields.Many2one('school_management.course', string="Course")
    content = fields.Html("Content")