odoo.define('quan_ly_du_an.custom_graph_view', function (require) {
    "use strict";

    var GraphView = require('web.GraphView');
    var core = require('web.core');

    var CustomGraphRenderer = GraphView.prototype.config.Renderer.extend({
        _render: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                // Get the bars in the graph
                var bars = self.$el.find('.nv-bar');
                bars.each(function () {
                    var bar = $(this);
                    var dataPoint = bar.data('point');
                    if (dataPoint && dataPoint.data) {
                        // Get the status value from the data point
                        var status = dataPoint.data.status;
                        var color = 'black'; // Default color

                        // Map the status to a CSS color
                        if (status === 'canceled') {
                            color = 'red'; // Hủy
                        } else if (status === 'in_progress') {
                            color = 'blue'; // Đang thực hiện
                        } else if (status === 'completed') {
                            color = 'green'; // Hoàn thành
                        }

                        // Apply the color to the bar
                        bar.css('fill', color);
                    }
                }); 
            });
        },
    });

    GraphView.include({
        config: _.extend({}, GraphView.prototype.config, {
            Renderer: CustomGraphRenderer,
        }),
    });
});