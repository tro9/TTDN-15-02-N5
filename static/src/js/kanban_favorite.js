odoo.define('quan_ly_du_an.kanban_favorite', function (require) {
    "use strict";

    var KanbanRecord = require('web.KanbanRecord');

    // Add the click handler for the star icon
    KanbanRecord.include({
        events: _.extend({}, KanbanRecord.prototype.events, {
            'click .o_kanban_favorite i': '_onFavoriteToggle',
        }),

        _onFavoriteToggle: function (ev) {
            ev.stopPropagation(); // Prevent the card from being clicked
            var self = this;
            var recordId = $(ev.currentTarget).data('record-id');
            var isFavorite = !this.recordData.is_favorite.value;

            // Update the favorite status
            this._rpc({
                model: 'du_an',
                method: 'toggle_favorite',
                args: [[recordId]],
            }).then(function () {
                self.trigger_up('reload'); // Reload the Kanban view

                // self.recordData.is_favorite.value = isFavorite;
                // self.renderElement(); // Re-render the Kanban card
            });
        },
    });
});