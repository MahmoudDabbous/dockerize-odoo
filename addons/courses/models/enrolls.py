from odoo import models, fields, api

class Enroll(models.Model):
    _name = 'enroll'
    _description = 'Enroll'

    name = fields.Char(readonly=True)
    student_id = fields.Many2one('student', string="Student")
    course_id = fields.Many2one('courses')
    enroll_date = fields.Date()

    
    @api.model
    def create(self, values):
        result = super(Enroll, self).create(values)
        result.name = result.student_id.name + ','+ result.course_id.name
    
        return result
    
    
    def write(self, values):
        if 'course_id' in values:
            course = self.env['courses'].search([('id','=', values.get('course_id'))])
            values['name'] = self.student_id.name +',' + course.name
    
        result = super(Enroll, self).write(values)
    
        return result
    
    
