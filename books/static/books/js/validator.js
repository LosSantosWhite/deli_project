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

$("#create-form").submit((e) => {
  e.preventDefault();
  const bookName = $("#id_name").val();
  console.log(bookName)
  $.get(
    '/books/validate-name/',
    {bookName: bookName},
    (response) => {
      if (response.status === "ok") {
        $('#create-form').unbind('submit').submit()
      }
      else if (response.status === "failed") {
        $("#errors_list").html(`<p>${response.book_error}</p>`)
      }
    },
  )
})