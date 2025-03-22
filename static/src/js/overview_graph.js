odoo.define('quan_ly_du_an.OverviewGraph', function (require) {
    "use strict";

    var GraphView = require('web.GraphView');
    var viewRegistry = require('web.view_registry');

    var OverviewGraphView = GraphView.extend({
        events: _.extend({}, GraphView.prototype.events, {
            'click .o_graph_field[data-field="project_id"]': '_onProjectClick',
        }),

        _onProjectClick: function (ev) {
            ev.preventDefault();
            ev.stopPropagation();

            // Get the project ID from the clicked element
            var projectId = $(ev.currentTarget).data('id');
            if (!projectId) {
                return;
            }

            // Open the task graph view for the selected project
            this.do_action({
                type: 'ir.actions.act_window',
                name: 'Tổng quan Công Việc',
                res_model: 'cong_viec',
                view_mode: 'graph',
                views: [[false, 'graph']],
                domain: [['project_id', '=', projectId]],
                context: {
                    search_default_group_by_status: 1, // Group tasks by status
                },
            });
        },
    });

    // Register the custom graph view
    viewRegistry.add('overview_graph', OverviewGraphView);
});