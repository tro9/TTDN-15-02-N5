from odoo import models, fields

class OnDuAn(models.Model):
    _name = "on_du_an"
    _description = "on_du_an"

    project_id = fields.Many2one("du_an", string="Dự án", required=True, ondelete="cascade")
    cp_name = fields.Many2one("cp", string="Liên hệ", required=True, ondelete="cascade")

    email = fields.Char(string="Email", related="cp_name.email", readonly=True)

    role = fields.Selection([
        ('consultant', 'Tư vấn'),
        ('partner', 'Đối tác'),
        ('invester', 'Nhà đầu tư')
        
        
    ], string="Vai trò", default='partner')