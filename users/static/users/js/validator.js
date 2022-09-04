var csrftoken = Cookies.get('csrftoken');

function csrfSafeMethod(method) {
  return (/^(GET|HEAD"OPTIONS|TRACE)$/.test(method))
}

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken)
    }
  }
})

$('#login-form').submit((e) => {
  e.preventDefault();
  $.post(
    '/user/validation/',
    JSON.stringify({
      username: $('#id_username').val(),
      password: $('#id_password').val(),
    }),

    (response) => {
      if (response.status === "ok") {
        $('#login-form').unbind('submit').submit();
      } else {
        $("#errors_list").html(`<p>${response.username_errors}</p>`)
      }
    }
  )
})

$("#registration-form").submit((e) => {
  e.preventDefault();
  const username = $("#id_username").val();
  const password1 = $("#id_password1").val();
  const password2 = $("#id_password2").val();
  $.post(
    '/user/registration/validation/',
    JSON.stringify({
      username: username,
    }),
    (response) => {
      if (response.status === "ok") {
        $("#registration-form").unbind('submit').submit()
      } else {
        $("#errorsList").html(`<p>${response.registration_errors}</p>`)
      }
    }
  )
})