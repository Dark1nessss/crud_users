$(document).ready(function() {
    var asc = true;
    
    $('th.sortable').click(function() {
        var column = $(this).index();
        var rows = $('tbody').find('tr').get();

        rows.sort(function(a, b) {
            var A = $(a).children('td').eq(column).text().toUpperCase();
            var B = $(b).children('td').eq(column).text().toUpperCase();

            if (asc) {
                if (A < B) return -1;
                if (A > B) return 1;
            } else {
                if (A > B) return -1;
                if (A < B) return 1;
            }
            return 0;
        });

        $.each(rows, function(index, row) {
            $('tbody').append(row);
        });

        asc = !asc;
        
        $('th.sortable').find('.sort-icon').remove();
        $(this).append('<span class="sort-icon ' + (asc ? 'up' : 'down') + '"></span>');
    });
});