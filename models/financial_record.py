from odoo import models, fields

class financialRecord(models.Model):
    _name = 'school_management.financial_record'
    _description = 'Financial Information'

    transaction_date = fields.Date("Transaction Date")
    amount = fields.Float("Amount")