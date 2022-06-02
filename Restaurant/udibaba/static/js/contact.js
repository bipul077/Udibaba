
document.querySelector('#contact-form').addEventListener('submit', (e) => {
    e.preventDefault();
    e.target.elements.name.value = '';
    e.target.elements.email.value = '';
    e.target.elements.message.value = '';
  });
$('.alink').click(function () {
  console.log("clicked");
  $('#modalbody').html($(this).data('name'));
  // var ids = document.getElementById('imgid').src;
  // var div = document.getElementById('modalbody');
  // console.log(ids);
  // console.log(div)
  // var img = document.createElement("img");
  // img.src = ids;
  // div.appendChild(img);
})
