from odoo import api, models, fields

class CongViec(models.Model):
    _name = "cong_viec"
    _description = "cong_viec"

    # task_id = fields.Integer(string="Mã công việc", required=True)

    name = fields.Char(string="Tên công việc", required=True)
    description = fields.Text(string="Thông tin")
    project_id = fields.Many2one('du_an', string="Dự án", ondelete='cascade')

    assigned_to = fields.Many2one('nhan_vien', string="Nhân viên phụ trách")

    num_emp = fields.Integer(string="Số nhân viên")
    cost = fields.Float(string="Chi phí")
    num_epuip = fields.Integer(string="Số dụng cụ sử dụng")
    
    priority = fields.Selection([
        ('low', 'Thấp'),
        ('medium', 'Vừa'),
        ('high', 'Cao')
    ], string="Mức độ ưu tiên", default='medium')
    deadline = fields.Date(string="Deadline")
    status = fields.Selection([
        ('todo', 'To Do'),
        ('in_progress', 'Đang tiến hành'),
        ('done', 'Hoàn thành')
    ], string="Trạng thái", default='todo')

    project_status = fields.Selection(
        related='project_id.status', 
        string="Project Status", 
        store=True
    )


    
    def action_start_task(self):
        """ Change task status to 'in_progress' """
        for task in self:
            task.status = 'in_progress'

    
    def action_complete_task(self):
        """ Change task status to 'done' """
        for task in self:
            task.status = 'done'


    @api.model
    def _get_kanban_view(self):
        res = super(CongViec, self)._get_kanban_view()
        projects = self.env['du_an'].search([])
        res['context']['projects'] = projects.read(['id', 'name'])
        return res

    # timesheet_ids = fields.One2many('thoi_gian_bieu', 'task_id', string="Bảng thời gian")
