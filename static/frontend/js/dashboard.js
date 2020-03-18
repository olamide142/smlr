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
                            '<input class="w3-input" type="text" value="127.0.0.1:8000/'+data.smlr_url+'"id="copy_link">'
                            );
                            setTimeout(1000);
                            window.location.replace("/dashboard");

                            // $('#list_smlr').append('<tr><td>{{forloop.counter}}</td>'
                            // +'<td><a href="http://127.0.0.1:8000/'{{url.smlr_url_id}}'">{{url.smlr_url_id}}</a></td>'+
                            // +'<td><a href="{{url.destination_url}}">{{url.destination_url|reduceLen:20}}...</a></td>'+
                            // +'<td><button class="w3-center w3-tiny w3-button w3-grey w3-text-white w3-round">Chart</button></td>'+
                            // +'<td><button class="w3-center w3-tiny w3-button w3-grey w3-text-white w3-round">Edit</button></td>'+
                            // +'<td><button class="w3-center w3-tiny w3-button w3-grey w3-text-white w3-round" onclick="">Delete</button></td>'+
                            // '</tr>');

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