from odoo import models, fields

class ThoiGianBieu(models.Model):
    _name = "thoi_gian_bieu"
    _description = "thoi_gian_bieu"

    task_id = fields.Many2one('cong_viec', string="Công việc", ondelete='cascade')
    user_id = fields.Many2one('nhan_vien', string="Nhân viên")
    date = fields.Date(string="Ngày làm việc")
    hours_spent = fields.Float(string="Số giờ làm việc")
