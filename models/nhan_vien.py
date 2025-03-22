from odoo import models, fields

class NhanVien(models.Model):
    _name = "nhan_vien"
    _description = "nhan_vien"

    name = fields.Char(string="Tên nhân viên", required=True)
    # email = fields.Char(string="Email")
    # phone = fields.Char(string="Số điện thoại")
    # role = fields.Selection([
    #     ('manager', 'Quản lý'),
    #     ('developer', 'Lập trình viên'),
    #     ('designer', 'Thiết kế'),
    #     ('tester', 'Kiểm thử viên')
    # ], string="Vai trò", default='developer')
    # active = fields.Boolean(string="Đang hoạt động", default=True)
    project_ids = fields.Many2many('du_an', string="Dự án tham gia")
