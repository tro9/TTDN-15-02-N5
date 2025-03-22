from odoo import models, fields

class DinhKem(models.Model):
    _name = "dinh_kem"
    _description = "Đính kèm"

    task_id = fields.Many2one('cong_viec', string="Công việc", ondelete='cascade')
    project_id = fields.Many2one('du_an', string="Dự án", ondelete='cascade')

    file_name = fields.Char(string="Tên File")
    file_data = fields.Binary(string="File")
    uploaded_by = fields.Many2one('nhan_vien', string="Người tải lên") 
    upload_date = fields.Datetime(string="Ngày tải lên", default=fields.Datetime.now)