// Restricts input for the set of matched elements to the given inputFilter function.
(function ($) {
    $.fn.inputFilter = function (inputFilter) {
        return this.on("input keydown keyup mousedown mouseup select contextmenu drop", function () {
            if (inputFilter(this.value)) {
                this.oldValue = this.value;
                this.oldSelectionStart = this.selectionStart;
                this.oldSelectionEnd = this.selectionEnd;
            } else if (this.hasOwnProperty("oldValue")) {
                this.value = this.oldValue;
                this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
            } else {
                this.value = "";
            }
        });
    };
}(jQuery));
$(document).ready(function () {
    $("#phone_number").inputFilter(function (value) {
        return /^\d*$/.test(value);    // Allow digits only, using a RegExp
    });
});

$(function () {
    $body = $("body");
    $("#request").on("submit", function (e) {
        e.preventDefault();
        $.ajax({
            url: '/ajax/search/',
            type: 'post',
            data: new FormData(this),
            processData: false,
            contentType: false,
            success: function (data) {
                var has_error = data['has_error'];
                if (has_error) {
                    var title = data['error_message']['title'];
                    var description = data['error_message']['description'];
                    toastr.options = {
                        "closeButton": true,
                        "debug": false,
                        "newestOnTop": true,
                        "progressBar": true,
                        "positionClass": "toast-bottom-full-width",
                        "preventDuplicates": false,
                        "onclick": null,
                        "showDuration": "300",
                        "hideDuration": "1000",
                        "timeOut": "5000",
                        "extendedTimeOut": "1000",
                        "showEasing": "swing",
                        "hideEasing": "linear",
                        "showMethod": "fadeIn",
                        "hideMethod": "fadeOut"
                    };
                    toastr.error(description, title);

                } else {

                    if (data['not_found']) {
                        var title = data['error_message']['title'];
                        var description = data['error_message']['description'];
                        toastr.options = {
                            "closeButton": true,
                            "debug": false,
                            "newestOnTop": true,
                            "progressBar": true,
                            "positionClass": "toast-bottom-full-width",
                            "preventDuplicates": false,
                            "onclick": null,
                            "showDuration": "300",
                            "hideDuration": "1000",
                            "timeOut": "5000",
                            "extendedTimeOut": "1000",
                            "showEasing": "swing",
                            "hideEasing": "linear",
                            "showMethod": "fadeIn",
                            "hideMethod": "fadeOut"
                        };
                        toastr.warning(description, title);
                    } else {


                        var pakData = data['report']['pak_data'];
                        var sim_registration_details = document.getElementById('sim_registration_details');

                        var user__phone_number = pakData.phone_number;
                        if (user__phone_number) {
                            var user__phone_number_div = document.getElementById('div_phone_number');
                            user__phone_number_div.style.display = "block";
                            sim_registration_details.style.display = "block";
                            document.getElementById("user__phone_number").value = user__phone_number;
                        }
                        var user__name = pakData.name;
                        if (user__name) {
                            var user__name_div = document.getElementById('div_user__name');
                            user__name_div.style.display = "block";
                            sim_registration_details.style.display = "block";
                            document.getElementById("user__name").value = user__name;
                        }
                        var reg__date = pakData.date;
                        if (reg__date) {
                            var div_reg__date = document.getElementById('div_reg__date');
                            div_reg__date.style.display = "block";
                            sim_registration_details.style.display = "block";
                            document.getElementById("reg__date").value = reg__date;
                        }
                        var address__one = pakData.address;
                        if (address__one) {
                            var div_address__one = document.getElementById('div_address__one');
                            div_address__one.style.display = "block";
                            sim_registration_details.style.display = "block";
                            document.getElementById("address__one").value = address__one;
                        }
                        var address__two = pakData.address1;
                        if (address__two) {
                            var div_address__two = document.getElementById('div_address__two');
                            div_address__two.style.display = "block";
                            sim_registration_details.style.display = "block";
                            document.getElementById("address__two").value = address__two;
                        }
                        var address__three = pakData.address2;
                        if (address__three) {
                            var div_address__three = document.getElementById('div_address__three');
                            div_address__three.style.display = "block";
                            sim_registration_details.style.display = "block";
                            document.getElementById("address__two").value = address__three;
                        }
                        var city = pakData.city;
                        if (city) {
                            var div_city = document.getElementById('div_city');
                            div_city.style.display = "block";
                            sim_registration_details.style.display = "block";
                            document.getElementById("city").value = city;
                        }
                        var other_phone_number = pakData.other_phone;
                        if (other_phone_number) {
                            var div_other_phone_number = document.getElementById('div_other_phone_number');
                            div_other_phone_number.style.display = "block";
                            sim_registration_details.style.display = "block";
                            document.getElementById("other_phone_number").value = other_phone_number;
                        }

                        var cnic_info = data['report']['cnic_info'];
                        var cnic_info_details = document.getElementById('cnic_info_details');

                        var gander = cnic_info.gander;
                        if (gander) {
                            var gender_div = document.getElementById('gander_div');
                            gender_div.style.display = "block";
                            cnic_info_details.style.display = "block";
                            document.getElementById("gander").value = gander;
                        }

                        var tehsil = cnic_info.tehsil;
                        if (tehsil) {
                            var tehsil_div = document.getElementById('tehsil_div');
                            tehsil_div.style.display = "block";
                            cnic_info_details.style.display = "block";
                            document.getElementById("tehsil").value = tehsil;
                        }

                        var division = cnic_info.division;
                        if (division) {
                            var division_div = document.getElementById('division_div');
                            division_div.style.display = "block";
                            cnic_info_details.style.display = "block";
                            document.getElementById("division").value = division;
                        }

                        var province = cnic_info.province;
                        if (province) {
                            var province_div = document.getElementById('province_div');
                            province_div.style.display = "block";
                            cnic_info_details.style.display = "block";
                            document.getElementById("province").value = province;
                        }


                        var sim_info = data['report']['sim_info'];
                        var sim_code_details = document.getElementById('sim_code_details');

                        var sim_city = sim_info.city;
                        if (sim_city) {
                            var sim_city_div = document.getElementById('sim_city_div');
                            sim_city_div.style.display = "block";
                            sim_code_details.style.display = "block";
                            document.getElementById("sim_city").value = sim_city;
                        }

                        var sim_network = sim_info.network;
                        if (sim_network) {
                            var sim_network_div = document.getElementById('sim_network_div');
                            sim_network_div.style.display = "block";
                            sim_code_details.style.display = "block";
                            document.getElementById("sim_network").value = sim_network;
                        }

                        var sim_province = sim_info.province;
                        if (sim_province) {
                            var sim_province_div = document.getElementById('sim_province_div');
                            sim_province_div.style.display = "block";
                            sim_code_details.style.display = "block";
                            document.getElementById("sim_province").value = sim_province;
                        }
                    }
                }

            }
        });
    });
});

$(document).ready(function () {
    $("#phone_number").inputFilter(function (value) {
        return /^\d*$/.test(value);    // Allow digits only, using a RegExp
    });
});
$(document).on({
    ajaxStart: function () {
        $body.addClass("loading");
        var sim_registration_details = document.getElementById('sim_registration_details');
        sim_registration_details.style.display = "none";

        var user__phone_number_div = document.getElementById('div_phone_number');
        user__phone_number_div.style.display = "none";
        var user__name_div = document.getElementById('div_user__name');
        user__name_div.style.display = "none";

        var div_reg__date = document.getElementById('div_reg__date');
        div_reg__date.style.display = "none";
        var div_address__one = document.getElementById('div_address__one');
        div_address__one.style.display = "none";

        var div_address__two = document.getElementById('div_address__two');
        div_address__two.style.display = "none";

        var div_address__three = document.getElementById('div_address__three');
        div_address__three.style.display = "none";


        var div_city = document.getElementById('div_city');
        div_city.style.display = "none";


        var div_other_phone_number = document.getElementById('div_other_phone_number');
        div_other_phone_number.style.display = "none";
        var cnic_info_details = document.getElementById('cnic_info_details');

        var gender_div = document.getElementById('gander_div');
        gender_div.style.display = "none";
        cnic_info_details.style.display = "none";


        var tehsil_div = document.getElementById('tehsil_div');
        tehsil_div.style.display = "none";
        var division_div = document.getElementById('division_div');
        division_div.style.display = "none";
        var province_div = document.getElementById('province_div');
        province_div.style.display = "none";
        var sim_code_details = document.getElementById('sim_code_details');
        var sim_city_div = document.getElementById('sim_city_div');
        sim_city_div.style.display = "none";
        sim_code_details.style.display = "none";
        var sim_network_div = document.getElementById('sim_network_div');
        sim_network_div.style.display = "none";
        var sim_province_div = document.getElementById('sim_province_div');
        sim_province_div.style.display = "none";


    },
    ajaxStop: function () {
        $body.removeClass("loading");
    }
});