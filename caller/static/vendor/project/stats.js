$(document).ready(function () {

    readLoadStats();

    // setInterval("readLoadStats()", 5000);


});

function addSpinner(el, static_pos) {
    var spinner = el.children('.spinner');
    if (spinner.length && !spinner.hasClass('spinner-remove')) return null;
    !spinner.length && (spinner = $('<div class="spinner' + (static_pos ? '' : ' spinner-absolute') + '"/>').appendTo(el));
    animateSpinner(spinner, 'add');
}

function removeSpinner(el, complete) {
    var spinner = el.children('.spinner');
    spinner.length && animateSpinner(spinner, 'remove', complete);
}

function animateSpinner(el, animation, complete) {
    if (el.data('animating')) {
        el.removeClass(el.data('animating')).data('animating', null);
        el.data('animationTimeout') && clearTimeout(el.data('animationTimeout'));
    }
    el.addClass('spinner-' + animation).data('animating', 'spinner-' + animation);
    el.data('animationTimeout', setTimeout(function () {
        animation == 'remove' && el.remove();
        complete && complete();
    }, parseFloat(el.css('animation-duration')) * 1000));
}

function readLoadStats() {
    $.ajax({
        url: '/ajax/phone_number_scanned',
        beforeSend: function () {
            $('#phone_number_scanned').html('');
            addSpinner($('#phone_number_scanned'));
        },
        complete: function (response) {
            console.log(response);
            let data = "<div class=\"text-right text-green\">\n" +
                "                        <i class=\"fe fe-credit-card\"></i>\n" +
                "                    </div>\n" +
                "                    <div id=\"phone_number_count\" class=\"h1 m-0\">" + response.responseText + "</div>\n" +
                "                    <div class=\"text-muted mb-4\">Phone Number Scanned</div>"
            removeSpinner($('#phone_number_scanned'), function () {
                $('#phone_number_scanned').html(data);
            });
        }
    });

}
