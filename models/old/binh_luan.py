from odoo import models, fields

class BinhLuan(models.Model):
    _name = "binh_luan"
    _description = "Bình luận công việc"

    task_id = fields.Many2one('cong_viec', string="Công việc", ondelete='cascade')
    user_id = fields.Many2one('nhan_vien', string="Nhân viên")
    comment = fields.Text(string="Bình luận")
    timestamp = fields.Datetime(string="Dấu thời gian", default=fields.Datetime.now)
