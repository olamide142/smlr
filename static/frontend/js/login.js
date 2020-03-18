// Get the modal
var modal = document.getElementById('login');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

$(document).ready(function(){
    
  var login = new Vue({
          el : '#login',
          delimiters : ['${','}'],
          data : {
              username : '',
              password : '',
          },
          methods : {
              log_user_in : function(){
                //   $('#login_loader').show();
                  $.ajax({
                      url: 'login/',
                      method: 'POST',
                      data : {
                          'username':this.username,
                          'password':this.password, 
                          'csrfmiddlewaretoken':getCookie('csrftoken'),
                      },
                      success: function (data) {
                          if(data.status == 'true'){
                              window.location.replace("/dashboard");
                          }else{
                              alert("Something went wromg");
                          }
                      },
                      error: function (error) {
                          this.usernameCheck = 'Try again later'
                      }
                  });
              }
          },
      })

});