# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Courses(models.Model):
    _name = 'courses'
    _description = 'Courses System'

    name = fields.Char(string="Course Name")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    cost = fields.Float()
    professor_id = fields.Many2one('res.partner', string="Professor")
    enroll_ids = fields.One2many(
        string='enrolls',
        comodel_name='enroll',
        inverse_name='course_id',
    )
    count = fields.Float(compute='_get_number_of_enrollment' , readonly=True, store=True)
    phone = fields.Char(related="professor_id.phone", readonly=False)
    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'), ('open', 'Open'), ('close', 'Close')],
        default="draft"
    )

    tag_ids = fields.Many2many('res.partner.category', string="Tags")
    
    
    @api.depends('enroll_ids')
    def _get_number_of_enrollment(self):
        for record in self:
            record.count = len(record.enroll_ids.ids)

    @api.onchange('name')
    def _get_data(self):
        for record in self:
            record.professor_id = 2

    def open_course(self):
        self.state = 'open'
        
    def close_course(self):
        self.state = 'close'



