


from datetime import date
from odoo import models, fields, api

class DuAn(models.Model):
    _name = "du_an"
    _description = "Dự án"
    # _inherit = ['mail.thread']

    project_id = fields.Integer(string="Mã dự án", required=True)
    name = fields.Char(string="Tên dự án")  
    description = fields.Text(string="Thông tin chung")
    start_date = fields.Date(string="Ngày bắt đầu")
    end_date = fields.Date(string="Ngày kết thúc")
    actual_start_date = fields.Date(string="Ngày bắt đầu thực tế",)
    actual_end_date = fields.Date(string="Ngày kết thúc thực tế",)

    total_labor_cost = fields.Integer(string="Tổng Chi Phí Nhân Sự", compute="_compute_total_labor_cost", store=True)
    total_equipment = fields.Integer(string="Tổng dụng cụ sử dụng", compute="_compute_total_equipment", store=True)
    total_project_cost = fields.Float(string="Tổng Chi Phí Dự Án", compute="_compute_total_project_cost", store=True)

    on_du_an_ids = fields.One2many("on_du_an", "project_id", string="Liên hệ")

    progress = fields.Float(string="Progress", compute="_compute_progress", store=True)

    is_favorite = fields.Boolean(string="Favorite", default=False)

    status = fields.Selection([
        ('draft', 'Lên Kế Hoạch'),
        ('in_progress', 'Đang tiến hành'),
        ('completed', 'Hoàn thành'),
        ('paused', 'Tạm dừng'),
        ('canceled', 'Hủy')
    ], string="Trạng thái", default='draft')
    user_id = fields.Many2one('nhan_vien', string="Quản lý")
    task_ids = fields.One2many('cong_viec', 'project_id', string="Công việc")

    def action_start_project(self):
        """Function for 'Start' button: Updates status to in_progress & sets actual_start_date"""
        for record in self:
            if record.status == 'draft':
                record.status = 'in_progress'
                record.actual_start_date = str(date.today())

    def action_pause_project(self):
        """ Pause the project """
        for record in self:
            record.status = 'paused'

    def action_cancel_project(self):
        """ Cancel the project """
        for record in self:
            record.status = 'canceled'
            record.actual_start_date = str(date.today())

    def toggle_favorite(self):
        """
        Toggle the favorite status of the project.
        This method is called when the star icon is clicked in the Kanban or Form view.
        """
        for record in self:
            record.is_favorite = not record.is_favorite
        
        # return {
        #     'type': 'ir.actions.client',
        #     'tag': 'reload',  # Reload the current view
        # }


    @api.depends("task_ids.cost")
    def _compute_total_project_cost(self):
        for record in self:
            record.total_project_cost  = sum(record.task_ids.mapped("cost"))

    @api.depends("task_ids.num_epuip")
    def _compute_total_equipment(self):
        for record in self:
            record.total_equipment  = sum(record.task_ids.mapped("num_epuip"))

    @api.depends("task_ids.num_emp")
    def _compute_total_labor_cost(self):
        for record in self:
            record.total_labor_cost = sum(record.task_ids.mapped("num_emp"))

    @api.depends('task_ids.status')
    def _compute_progress(self):
        for project in self:
            total_tasks = len(project.task_ids)
            if total_tasks > 0:
                completed_tasks = len(project.task_ids.filtered(lambda t: t.status == 'done'))

                project.progress = (completed_tasks / total_tasks) * 100

                if project.progress == 100:
                    project.status = 'completed'
                    project.actual_end_date = str(date.today())
            else:
                project.progress = 0.0
    
    def action_open_task_graph(self):
        """Open the task graph view for the selected project."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tổng quan Công Việc',
            'res_model': 'cong_viec',
            'view_mode': 'graph',
            'domain': [('project_id', '=', self.id)],  # Filter tasks by the selected project
            'context': {
                'search_default_group_by_status': 1,  # Group tasks by status
            },
        }


    

