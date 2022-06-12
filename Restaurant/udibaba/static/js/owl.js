function myFunction(x) {
    if (x.matches) { // If media query matches
        $('.owl-carousel').owlCarousel({
            loop:true,
            margin: 20,
            nav:false,
            dots:false,
            autoplay: false,
            autoplayTimeout: 1000,
            stagePadding: 30,
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:3
                },
                1000:{
                    items:4
                }
            }
        }) 
    } else {
        $('.owl-carousel').owlCarousel({
            loop:true,
            margin: 20,
            nav:false,
            dots:false,
            autoplay: false,
            autoplayTimeout: 1000,
            stagePadding: 50,
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:3
                },
                1000:{
                    items:5
                }
            }
        })
    }
  }
  
  var x = window.matchMedia("(max-width: 700px)")
  myFunction(x) // Call listener function at run time
  x.addListener(myFunction) // Attach listener function on state changes
  $('.alink').click(function () {
    console.log("clicked");
    $('#foodtitle').html($(this).data('name'));
    $('#foodprice').html($(this).data('price'));
    $('#fooddesc').html($(this).data('des'));
    console.log($(this).data('des'));
    a = $(this).data('img')
    console.log(a);
    document.getElementById("imgpop").setAttribute("src", a);
    // $('#imgpop').src($(this).data('img'));
  
    // var ids = document.getElementById('imgid').src;
    // var div = document.getElementById('modalbody');
    // console.log(ids);
    // console.log(div)
    // var img = document.createElement("img");
    // img.src = ids;
    // div.appendChild(img);
})
$(document).ready(function(){
    $("#menulistpop").modal('show');
});
$('.menulink').click(function () {
    console.log("clicked");
    console.log($(this).data('id'));
})

//increment btn in product detail
$('.increment-btn').click(function (e) {
    e.preventDefault();
   
    var inc_value = $(this).closest('.pro-qty').find('.qty-input').val();
    var value = parseInt(inc_value,10);
    value = isNaN(value) ? 0 : value;
    if(value < 10)
    {
        value++;
        $(this).closest('.pro-qty').find('.qty-input').val(value);
    }
});
//decrement btn in product detail
$('.decrement-btn').click(function (e) {
    e.preventDefault();
    var inc_value = $(this).closest('.pro-qty').find('.qty-input').val();
    var value = parseInt(inc_value,10);
    value = isNaN(value) ? 0 : value;
    if(value > 1)
    {
        value--;
        $(this).closest('.pro-qty').find('.qty-input').val(value);
    }
});

//for menulist page
//increment btn in product detail
$('.increments-btn').click(function (e) {
    e.preventDefault();
   
    var inc_value = $(this).closest('.menulistqty').find('.qty-input').val();
    var value = parseInt(inc_value,10);
    value = isNaN(value) ? 0 : value;
    if(value < 10)
    {
        value++;
        $(this).closest('.menulistqty').find('.qty-input').val(value);
    }
});
//decrement btn in product detail
$('.decrements-btn').click(function (e) {
    e.preventDefault();
    var inc_value = $(this).closest('.menulistqty').find('.qty-input').val();
    var value = parseInt(inc_value,10);
    value = isNaN(value) ? 0 : value;
    if(value > 1)
    {
        value--;
        $(this).closest('.menulistqty').find('.qty-input').val(value);
    }
});

$(document).on('click',".addtocart",function(){
    var qty= $(this).closest('.contentmodal').find('.qty-input').val();
    var pid= $(this).closest('.contentmodal').find('.product-id').val();
    // var pimg=$(".product-image-"+_index).val();
    var ptitle=$(this).closest('.contentmodal').find('.product-title').val();
    var pimage=$(this).closest('.contentmodal').find('.product-image').val();
    var price=$(this).closest('.contentmodal').find('.product-price').val();
    // var pprice=$(".product-price-"+_index).text();
    console.log(pid,ptitle,qty,price)
    // Ajax
    $.ajax({
        url:'/addtocart',
        data:{
            'id': pid,
            'qty': qty,
            'title': ptitle,
            'price': price,
            'image': pimage
        },
        dataType:'json',
        success:function(res){
            $(".cartlist").text(res.totalitems);
            alertify.success("Item has been added to cart")
        }
    });
    // End
});
// End

// Delete item from cart
$(document).on('click','.removeitem',function(){
    var pid=$(this).attr('data-item');
    var _vm=$(this);
    // Ajax
    $.ajax({
        url:'/removecart/',
        data:{
            'id':pid,
        },
        dataType:'json',
        success:function(res){
            $(".cartlist").text(res.totalitems);
            $("#card").html(res.data);
        }
    });
    // End
});

// Update item from cart
$(document).on('click','.update-item',function(){
    var _pId=$(this).attr('data-item');
    var _pQty=$(".product-qty-"+_pId).val();
    var _vm=$(this);
    // Ajax
    $.ajax({
        url:'/updatecart/',
        data:{
            'id':_pId,
            'qty':_pQty
        },
        dataType:'json',
        success:function(res){
            // $(".cart-list").text(res.totalitems);
            $("#card").html(res.data);
        }
    });
    // End
});