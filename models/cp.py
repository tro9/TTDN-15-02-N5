from odoo import models, fields

class CP(models.Model):
    _name = "cp"
    _description = "cp"

    name = fields.Char(string="Tên", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Số điện thoại")
    