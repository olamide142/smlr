function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// alert(1);

$(document).ready(function(){
    $('#res').hide();
    var _dashboard = new Vue({
            el: '#dashboard',
            delimiters : ['[[',']]'],
            data: {
                destination : '',
                smlr_url : '',
            },
            mounted : {
                // alert('mounted');
            },
            methods : {
                dashboard_get_smlr : function(){
                    // $('#login_loader').show();
                    $.ajax({
                        url: 'getSmlr/',
                        method: 'POST',
                        data : {
                            'destination':this.destination,
                            'csrfmiddlewaretoken':getCookie('csrftoken'),
                        },
                        success: function (data) {
                            $('#res').show();
                            $('#default_link').html(
                            '<button class="w3-button w3-white w3-right">Edit</button>'+
                            '<button class="w3-button w3-right w3-white @click="copyLink" ">Copy</button>'+
                            '<input class="w3-left" type="text" value="127.0.0.1:8000/'+data.smlr_url+'"id="copy_link">'
                            );

                        },
                        error: function (error) {
                            alert('Try again later');
                        }
                    });
                },
                copyLink: function () {
                    var copyText = document.getElementById("copy_link");
                    copyText.select();
                    copyText.setSelectionRange(0, 99999)
                    document.execCommand("copy");
                    $('#copy_link .toast').toast('show')
                },
            },
        })
});