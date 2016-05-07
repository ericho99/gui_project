$('.picture-small').click(
  function highlight(e) {
    $('.picture-highlighted').removeClass('picture-highlighted');
    $(this).addClass('picture-highlighted'); 
    var attr = $(this).attr("src");
    $('.picture-big').attr("src", attr);
  }
);
