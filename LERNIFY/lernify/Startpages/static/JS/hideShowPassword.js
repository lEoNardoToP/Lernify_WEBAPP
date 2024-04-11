$(document).ready(function() {

  $(".show-password, .hide-password").on('click', function() {
    var password = $(this).parent().find('input');
    console.log($(this).hasClass('show-password'), $(this))
    if ($(this).context.classList.contains("show-password")) {
      password.attr("type", "text");
      $(this).parent().find(".show-password").hide();
      $(this).parent().find(".hide-password").show();
    } else {
      password.attr("type", "password");
      $(this).parent().find(".hide-password").hide();
      $(this).parent().find(".show-password").show();
    }
  });
});