$(document).ready(function () {
  $('.sidenav').sidenav();
  $('select').formSelect();

});

$(".star-rating").click(function () {
  for (let i = 1; i <= 5; i++) {
    let star = "star-" + i;
    $("#"+star).removeClass("golden-star");
    $("#"+star).addClass("grey-star");
  }
  for (let i = 1; i <= 5; i++) {
    let star = "star-" + i;
    $("#"+star).removeClass("grey-star");
    $("#"+star).addClass("golden-star");
    if (this.id === star) {
      $("#star_score").val(i);
      break;
    }
  }

});