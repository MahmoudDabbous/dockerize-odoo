from odoo import models, fields, api

class Student(models.Model):
    _name = 'student'
    _description = 'Students'

    name = fields.Char()
    code = fields.Char()
    birthday = fields.Date()
