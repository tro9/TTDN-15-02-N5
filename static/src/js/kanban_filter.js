odoo.define('quan_ly_du_an.kanban_filter', function (require) {
    "use strict";

    var KanbanController = require('web.KanbanController');
    var KanbanView = require('web.KanbanView');
    var viewRegistry = require('web.view_registry');

    var CustomKanbanController = KanbanController.extend({
        events: _.extend({}, KanbanController.prototype.events, {
            'click .o_kanban_apply_filter': '_onApplyFilter',
        }),

        _onApplyFilter: function (ev) {
            ev.preventDefault();
            var selectedProjectId = this.$('.o_kanban_project_filter').val();
            var domain = [];

            if (selectedProjectId && selectedProjectId !== '0') {
                domain = [['project_id', '=', parseInt(selectedProjectId)]];
            }

            this.reload({ domain: domain });
        },
    });

    var CustomKanbanView = KanbanView.extend({
        config: _.extend({}, KanbanView.prototype.config, {
            Controller: CustomKanbanController,
        }),
    });

    viewRegistry.add('custom_kanban', CustomKanbanView);
});


// odoo.define('your_module.kanban_filter', function (require) {
//     "use strict";

//     var core = require('web.core');
//     var KanbanView = require('web.KanbanView');
//     var viewRegistry = require('web.view_registry');

//     var KanbanViewWithFilter = KanbanView.extend({
//         start: function () {
//             var self = this;
//             this._super.apply(this, arguments);

//             // Wait for DOM to load, then attach event to select
//             this.$el.find("#kanban_project_filter").on("change", function () {
//                 var selectedProject = $(this).val();
//                 self.do_action({
//                     type: "ir.actions.client",
//                     tag: "reload",
//                     params: { project_id: selectedProject }
//                 });
//             });
//         }
//     });

//     viewRegistry.add('kanban_with_filter', KanbanViewWithFilter);
// });
