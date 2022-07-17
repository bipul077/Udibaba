function myFunction(x) {
    if (x.matches) { // If media query matches
        $('.owl-carousel').owlCarousel({
            loop:true,
            margin: 10,
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
            margin: 10,
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
//Review Owl Carousel
$('.review-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:false,
    dots:false,
    autoplay: true,
    autoplayTimeout: 3000,
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


var x = window.matchMedia("(max-width: 700px)")
  myFunction(x) // Call listener function at run time
  x.addListener(myFunction) // Attach listener function on state changes
  $('.alink').click(function () {
    console.log("clicked");
    $('#foodtitle').html($(this).data('name'));
    $('#foodprice').html($(this).data('price'));
    $('#fooddesc').html($(this).data('des'));
    $('#prod_id').val($(this).data('id'));
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

//for menulist page add to cart
$(document).on('click',".addtocart",function(){
    var qty= $(this).closest('.contentmodal').find('.qty-input').val();
    var pid= $(this).closest('.contentmodal').find('.product-id').val();
    // var pimg=$(".product-image-"+_index).val();
    var ptitle=$(this).closest('.contentmodal').find('.product-title').val();
    var price=$(this).closest('.contentmodal').find('.product-price').val();
    // var pprice=$(".product-price-"+_index).text();
    console.log(typeof(price));
    console.log(pid,ptitle,qty,price)
    // Ajax
    $.ajax({
        url:'/addtocart',
        data:{
            'id': pid,
            'qty': qty,
            'title': ptitle,
            'price': price,
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
//for home page add to cart
$(document).on('click',".modaladd",function(){
    var qty = document.getElementById("quantity").value;
    var pid = document.getElementById("prod_id").value;
    var ptitle = document.getElementById("foodtitle").textContent;
    var price = document.getElementById("foodprice").textContent;
    console.log(ptitle,qty,pid,price);
    // console.log(pid,ptitle,qty,price)
    //Ajax
    $.ajax({
        url:'/addtocart',
        data:{
            'id': pid,
            'qty': qty,
            'title': ptitle,
            'price': price,
        },
        dataType:'json',
        success:function(res){
            $(".cartlist").text(res.totalitems);
            alertify.success("Item has been added to cart")
        }
    });
    //End
});
// End

// Delete item from cart
$(document).on('click','.removeitem',function(){
    var pid=$(this).attr('data-item');
    var vm=$(this);
    // Ajax
    $.ajax({
        url:'/removecart/',
        data:{
            'id':pid,
        },
        dataType:'json',
        beforeSend:function(){
				vm.attr('disabled',true);
			},
        success:function(res){
            vm.attr('disabled',false);
            $(".cartlist").text(res.totalitems);
            $("#card").html(res.data);
            alertify.success("Item deleted")
        }
    });
    // End
});

// Update item from cart
$(document).on('click','.update-item',function(){
    var _pId=$(this).attr('data-item');
    var _pQty=$(".product-qty-"+_pId).val();
    var vm=$(this);
    // Ajax
    $.ajax({
        url:'/updatecart/',
        data:{
            'id':_pId,
            'qty':_pQty
        },
        dataType:'json',
        beforeSend:function(){
            vm.attr('disabled',true);
        },
        success:function(res){
            vm.attr('disabled',false);
            // $(".cart-list").text(res.totalitems);
            $("#card").html(res.data);
            alertify.success("Quantity and Price updated")
        }
    });
    // End
});

$("#loadmore").on('click',function(){
    var currentproducts = $(".Photos").length;//this currentproducts means how many products are shown in productlist html
    var limit=$(this).attr('data-limit');//this is the number of products we want to show in a row
    var total = $(this).attr('data-total');//this total means the total products we have in database
    console.log("hahha"+currentproducts,limit,total)
    var url = "/load-more-data/"
    //start ajax
    $.ajax({
        url: url,
        data: {//this data is sent to the server
            limit: limit,
            curproducts: currentproducts
        },
        dataType:'json',
        beforeSend:function(){//data fetch hune agadi chalne code when users click on load more button
            $("#loadmore").attr('disabled',true);
            $(".load-more-icon").addClass('fa-spin');
        },
        success:function(res){//catches the data which is given by views.py
            console.log("success")
            $(".mixit-container").append(res.datas);
            $("#loadmore").attr('disabled',false);
            $(".load-more-icon").removeClass('fa-spin');

            var curtotalproducts = $(".Photos").length;
            if(curtotalproducts==total){
                $("#loadmore").remove();
            }
        }
            
    })
    //end ajax
})

$('.plus-cart').click(function () {
    console.log("plus-clicked")
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[1].textContent
    var emls = this.parentNode.children[1]
    console.log("yes"+id)
    console.log("yeseml "+eml)
    
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id,
            qty: eml,//prod_id=id goes to url pluscart
        },
        success: function(data){//if success then success function is called
            console.log(data) 
            console.log(data.quantity) 
            emls.innerText = data.quantity
            document.getElementById("amount").innerText = data.totalamount
            document.getElementById("totamount").innerText = data.finalamount               
        }      
    })
})

$('.minus-cart').click(function () {
    console.log("minus-clicked")
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[1].textContent
    var emls = this.parentNode.children[1]
    console.log("yes"+id)
    console.log("yeseml "+eml)
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id,
            qty: eml,//prod_id=id goes to url minuscart
        },
        success: function(data){//if success then success function is called
            console.log(data)
            if(data.quantity>0){
                console.log("success")
                emls.innerText = data.quantity
                document.getElementById("amount").innerText = data.totalamount
                document.getElementById("totamount").innerText = data.finalamount
            }
        }          
    })
})

function imgSlider(anything){
    console.log("yesnoyesno");
    document.querySelector('.starbucks').src = anything;
}
function changeCircleColor(color){
    var circle = document.querySelector('.circle');
    circle.style.background = color;
}