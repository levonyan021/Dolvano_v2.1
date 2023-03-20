$(".dolvano_banner").owlCarousel({
    center: true,
    loop: true,
    margin: 10,
    nav: true,
    navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: false,
    dots: false,
    responsive: {
        0: {
            items: 1,
            margin: 0
        },
        600: {
            items: 1,
            margin: 0,
        },
        1000: {
            items: 1,
            margin: 0,
        }
    }
});

// Header navbar show/hode

var position = $(window).scrollTop();
$(window).scroll(function () {
    var scroll = $(window).scrollTop();
    if (scroll > position) {
        $('.header_nav').removeClass('nav_show');
        $('.header_nav').addClass('nav_hide');
    } else {
        $('.header_nav').removeClass('nav_hide');
        $('.header_nav').addClass('nav_show');
    }
    position = scroll;
})


$(document).ready(function() {
    $('.header_').hover(function() {
        $('.header_nav').removeClass('nav_hide');
        $('.header_nav').addClass('nav_show');
    });
  });
// 



$('.menu_btn').on('click', function () {
    if ($('.float_menu').hasClass("menu_close")) {
        $('.float_menu').removeClass("menu_close");
        $('.float_menu').addClass("menu_open");
    } else {
        $('.float_menu').removeClass("menu_open");
        $('.float_menu').addClass("menu_close");
    }
})

$('main').on('click', function () {
    $('.float_menu').removeClass("menu_open");
    $('.float_menu').addClass("menu_close");
})

$('.float_menu_item_1').hover(
    function () {
        $('.float_menu').addClass('bg_pink')
        $('.float_menu').removeClass('bg_gray')
    },
    function () {
        $('.float_menu').removeClass('bg_pink')
        $('.float_menu').addClass('bg_gray')
    }
)
$('.float_menu_item_2').hover(
    function () {
        $('.float_menu').addClass('bg_skyblue')
        $('.float_menu').removeClass('bg_gray')
    },
    function () {
        $('.float_menu').removeClass('bg_skyblue')
        $('.float_menu').addClass('bg_gray')
    }
)
$('.float_menu_item_3').hover(
    function () {
        $('.float_menu').addClass('bg_purpure')
        $('.float_menu').removeClass('bg_gray')
    },
    function () {
        $('.float_menu').removeClass('bg_purpure')
        $('.float_menu').addClass('bg_gray')
    }
)
$('.float_menu_item_4').hover(
    function () {
        $('.float_menu').addClass('bg-info')
        $('.float_menu').removeClass('bg_gray')
    },
    function () {
        $('.float_menu').removeClass('bg-info')
        $('.float_menu').addClass('bg_gray')
    }
)

let search_panel = $('.search_panel');
$('.search_btn').on('click', () => {
    search_panel.removeClass('search_panel_hide')
    search_panel.addClass('search_panel_show')
})
$('.search_close_btn').on('click', () => {
    search_panel.removeClass('search_panel_show')
    search_panel.addClass('search_panel_hide')
})


if (window.innerWidth <= 775) {
    $('.subscribe_').addClass('w-100');
}
else if (window.innerWidth) {
    $('.subscribe_').addClass('w-50');
}



$('.dolvano_video_play').on('click', function () {
    $('.dolvano_video_play').addClass('video_play_banner_hide');
        setTimeout(function() {
        $(".dolvano_video_play").css({'display': 'none'})
    }, 2000);
})



// $('.owl-carousel').owlCarousel({
//     items:3,
//     loop: true,
//     margin: 10,
//     dots: false,
//     responsive: {
//         0: {
//             items: 1,
//             margin: 0
//         },
//         600: {
//             items: 1,
//             margin: 0,
//         },
//         1000: {
//             items: 1,
//             margin: 0,
//         }
//     }
// });






// $(document).ready(function() {
//     // scroll down
//     $("html, body").animate({
//         scrollTop: $(document).height()
//     }, 2000);

//     // scroll back up
//     $("html, body").animate({
//         scrollTop: 0
//     }, 2000);
// });
// ________________________LOADER_____________________________
// $('body').append('<div style="" id="loadingDiv"><div class="loader">Loading...</div></div>');
// $(window).on('load', function(){
//   setTimeout(removeLoader, 2000); //wait for page load PLUS two seconds.
// });
// function removeLoader(){
//     $( "#loadingDiv" ).fadeOut(500, function() {
//       // fadeOut complete. Remove the loading div
//       $( "#loadingDiv" ).remove(); //makes page more lightweight 
//   });  
// }


var swiper = new Swiper(".mySwiper", {
    initialSlide: 2,
    slidesPerView: 2,
    spaceBetween: 30,
    centeredSlides: true,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    loop: true,
});

$(document).ready(function() {
    if ($(window).width() > 768) {
      $('.header_phone_number').append('<span>+374 770 084 89</span>');
    }
    else{
      $('.header_phone_number').append('<i class="fa-solid fa-phone fs-xx-large fs-5"></i>');
    }
  });




$('.mini_navigation').owlCarousel({
    loop: false,
    margin:10,
    nav:false,
    responsive:{
        0:{
            items:3
        }
    }
})

$('.popular').owlCarousel({
    loop: false,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        990:{
            items:3
        },
        1400:{
            items:4
        }
    }
})
// Modal registration

var modal = document.querySelector('.modal');
var closeButton = document.querySelector('.close');

function showModal() {
  modal.style.display = 'block';
}

function hideModal() {
  modal.style.display = 'none';
}

window.addEventListener('click', function(event) {
  if (event.target == modal) {
    hideModal();
  }
});

closeButton.addEventListener('click', hideModal);