# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = "Wizard to assign levels to the courses."
    
    def _get_courses(self):
        return self.env['openacademy.course'].browse(self.env.context.get('active_ids'))
    
    course_ids = fields.Many2many('openacademy.course', string="Courses", default=_get_courses)
    level = fields.Selection([(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], string="Difficulty Level")

    
    @api.multi
    def set_course_level(self):
        for record in self:
            if record.course_ids:
                for course in record.course_ids:
                    course.level = self.level