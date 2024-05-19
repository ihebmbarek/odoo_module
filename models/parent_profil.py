"""from odoo import models, fields

class ParentProfile(models.Model):
    _name = 'school_management.parent_profile'
    _description = 'Parent Profile'

    name = fields.Char("Parent Name")
    user_id = fields.Many2one('res.users', string="User")
    contact_info = fields.Char("Contact Information")"""