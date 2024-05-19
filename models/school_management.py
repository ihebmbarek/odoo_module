from odoo import models, fields

class Student(models.Model):
    _name = 'school_management.student'
    _description = 'Student'
    user_id = fields.Many2one('res.users', string='User')

class Professor(models.Model):
    _name = 'school_management.professor'
    _description = 'Professor'
    user_id = fields.Many2one('res.users', string='User')

class Staff(models.Model):
    _name = 'school_management.staff'
    _description = 'Staff'
    user_id = fields.Many2one('res.users', string='User')

class Parent(models.Model):
    _name = 'school_management.parent'
    _description = 'Parent'
    user_id = fields.Many2one('res.users', string='User')
