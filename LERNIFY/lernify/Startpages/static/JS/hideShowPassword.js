$(document).ready(function() {

  $(".show-password, .hide-password").on('click', function() {
    if ($(this).context.classList.contains("show-password")) {
      $(this).parent().find(".show-password").hide();
      $(this).parent().find(".hide-password").show();
    } else {
      $(this).parent().find(".hide-password").hide();
      $(this).parent().find(".show-password").show();
    }
  });
});