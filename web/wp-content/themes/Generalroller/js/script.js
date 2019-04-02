 $.fn.left_opacitys=function () {$(this).animate({"opacity":"1","right":"0"},800,'easeOutSine');}
$.fn.left_opacitys_no=function () {$(this).animate({"opacity":"0","right":"-100px"},500,'easeOutSine');}
$.fn.up_opacitys=function () {$(this).animate({"opacity":"1","top":"0"},800,'easeOutSine');}
$.fn.up_opacitys_no=function () {$(this).animate({"opacity":"0","top":"-100px"},500,'easeOutSine');}
 $.extend({news_open:function(){
	$('.index_swipers').css({width : $('body').width()})
	$('.swiper-wrapper .left_right.swiper-slide-active').children(".swiper-slide_in").children('.left_pic').children("img").delay(500).animate({"opacity":"1","left":"0"},800,'easeOutSine');
	$('.swiper-wrapper .left_right.swiper-slide-active').children(".swiper-slide_in").children('.right_text').children('#alpha').children(".title_lr_mod").delay(500).left_opacitys();
	$('.swiper-wrapper .left_right.swiper-slide-active').children(".swiper-slide_in").children('.right_text').children('#alpha').children("h3").delay(700).left_opacitys();
	$('.left_right.swiper-slide-active').children(".swiper-slide_in").children('.right_text').children('#alpha').children("p").delay(900).left_opacitys();
	$('.swiper-wrapper .left_right.swiper-slide-active').children(".swiper-slide_in").children('.right_text').children(".btn").delay(1000).left_opacitys();
	
	$('.swiper-wrapper .left_right').not('.swiper-slide-active').children(".swiper-slide_in").children('.left_pic').children("img").animate({"opacity":"0","left":"-100px"},800,'easeOutSine');
	$('.swiper-wrapper .left_right').not('.swiper-slide-active').children(".swiper-slide_in").children('.right_text').children('#alpha').children(".title_lr_mod").left_opacitys_no();
	$('.swiper-wrapper .left_right').not('.swiper-slide-active').children(".swiper-slide_in").children('.right_text').children('#alpha').children("h3").left_opacitys_no();
	$('.swiper-wrapper .left_right').not('.swiper-slide-active').children(".swiper-slide_in").children('.right_text').children('#alpha').children("p").left_opacitys_no();
	$('.swiper-wrapper .left_right').not('.swiper-slide-active').children(".swiper-slide_in").children('.right_text').children("a").left_opacitys_no();
	
	$('.swiper-wrapper .up_down.swiper-slide-active').children(".swiper-slide_in").children('.down_pic').children("img").delay(500).animate({"opacity":"1","top":"0"},1500,'easeOutCubic');
	
	$('.swiper-wrapper .up_down.swiper-slide-active').children(".swiper-slide_in").children('.down_pic').children(".swiper-wrapper").children(".swiper-slide").delay(500).animate({"opacity":"1","top":"0"},1500,'easeOutCubic');
	
	
	$('.swiper-wrapper .up_down.swiper-slide-active').children(".swiper-slide_in").children('.up_text').children('#alpha').children("h3").delay(500).up_opacitys();
	$('.swiper-wrapper .up_down.swiper-slide-active').children(".swiper-slide_in").children('.up_text').children('#alpha').children("p").delay(700).up_opacitys();
	$('.swiper-wrapper .up_down.swiper-slide-active').children(".swiper-slide_in").children('.up_text').children(".btn").delay(1000).up_opacitys();
	$('.swiper-wrapper .up_down').not('.swiper-slide-active').children(".swiper-slide_in").children('.down_pic').children("img").delay(500).animate({"opacity":"0","top":"800px"},800,'easeOutSine');
	$('.swiper-wrapper .up_down').not('.swiper-slide-active').children(".swiper-slide_in").children('.down_pic').children(".swiper-wrapper").children(".swiper-slide").delay(500).animate({"opacity":"0","top":"800px"},800,'easeOutSine');
	
	$('.swiper-wrapper .up_down').not('.swiper-slide-active').children(".swiper-slide_in").children('.up_text').children('#alpha').children("h3").up_opacitys_no();
	$('.swiper-wrapper .up_down').not('.swiper-slide-active').children(".swiper-slide_in").children('.up_text').children('#alpha').children("p").up_opacitys_no();
	$('.swiper-wrapper .up_down').not('.swiper-slide-active').children(".swiper-slide_in").children('.up_text').children(".btn").up_opacitys_no();
	
	
	
	

}});

	
	
$.fn.caseshow=function () { 
	if( $(window).scrollTop() >= $(this).offset().top-550 ){
   var Timers = 0;
    Timers+=200;
	var  Timerss=0;
	$(this).children(".about_ttile_line").children(".about_title").children(".line_left").delay(Timers+100).animate({left:"100%",opacity:"1"},1000);
  $(this).children(".about_ttile_line").children(".about_title").children(".line_right").delay(Timers+100).animate({right:"100%",opacity:"1"},1000);
  $(this).children(".about_ttile_line").children(".about_title").children(".mantitle").delay(Timers+500).animate({top:"0",opacity:"1"},1000);
 $(this).children(".about_ttile_line").children(".about_title").children(".sectitle").delay(Timers+800).animate({top:"0",opacity:"1"},1000);
	 $(this).children(".caseshow_in").children("ul").children('li').each(function() {
		  Timerss+=100;
		$(this).delay(Timerss+300).animate({top:"0",opacity:"1"},1000);
	
             }); 
	};};
	
	
$.fn.about=function () { 
	if( $(window).scrollTop() >= $(this).offset().top-550 ){
   var Timers = 0;
  
 $(this).children(".about_ttile_line").children(".about_title").children(".line_left").delay(Timers+100).animate({left:"100%",opacity:"1"},1000);
  $(this).children(".about_ttile_line").children(".about_title").children(".line_right").delay(Timers+100).animate({right:"100%",opacity:"1"},1000);
  $(this).children(".about_ttile_line").children(".about_title").children(".mantitle").delay(Timers+500).animate({top:"0",opacity:"1"},1000);
 $(this).children(".about_ttile_line").children(".about_title").children(".sectitle").delay(Timers+800).animate({top:"0",opacity:"1"},1000);
  $(this).children(".about_p").delay(Timers+1000).animate({top:"0",opacity:"1"},1000);
 $(this).children(".about_btn").delay(Timers+1300).animate({top:"0",opacity:"1"},1000);
	};};

$.fn.severs=function () { 
	if( $(window).scrollTop() >= $(this).offset().top-550 ){
   var Timers = 0;
  var  Timerss=0;
 $(this).children(".about_ttile_line").children(".about_title").children(".line_left").delay(Timers+100).animate({left:"100%",opacity:"1"},1000);
  $(this).children(".about_ttile_line").children(".about_title").children(".line_right").delay(Timers+100).animate({right:"100%",opacity:"1"},1000);
  $(this).children(".about_ttile_line").children(".about_title").children(".mantitle").delay(Timers+500).animate({top:"0",opacity:"1"},1000);
 $(this).children(".about_ttile_line").children(".about_title").children(".sectitle").delay(Timers+800).animate({top:"0",opacity:"1"},1000);
  $(this).children(".nav_poket_in").children(".nav_poket_ul").children("li").each(function() {
		  Timerss+=100;
		$(this).delay(Timerss+300).animate({top:"0",opacity:"1"},1000);
	
             }); 
  
  
  
  
	};};



$.fn.cunst=function () { 
	if( $(window).scrollTop() >= $(this).offset().top-550 ){
   var Timers = 0;
  var  Timerss=0;
 $(this).children(".about_ttile_line").children(".about_title").children(".line_left").delay(Timers+100).animate({left:"100%",opacity:"1"},1000);
  $(this).children(".about_ttile_line").children(".about_title").children(".line_right").delay(Timers+100).animate({right:"100%",opacity:"1"},1000);
  $(this).children(".about_ttile_line").children(".about_title").children(".mantitle").delay(Timers+500).animate({top:"0",opacity:"1"},1000);
 $(this).children(".about_ttile_line").children(".about_title").children(".sectitle").delay(Timers+800).animate({top:"0",opacity:"1"},1000);

  $(this).children(".cunster_in").children(".cunster_container").delay(Timers+1000).animate({top:"0",opacity:"1"},1000);
   $(this).children(".cunster_nav").delay(Timers+1200).animate({top:"0",opacity:"1"},1000);
  
  
  
	};};
	

$.fn.news=function () { 
	if( $(window).scrollTop() >= $(this).offset().top-550 ){
   var Timers = 0;
  var  Timerss=0;
 $(this).children(".about_ttile_line").children(".about_title").children(".line_left").delay(Timers+100).animate({left:"100%",opacity:"1"},1000);
  $(this).children(".about_ttile_line").children(".about_title").children(".line_right").delay(Timers+100).animate({right:"100%",opacity:"1"},1000);
  $(this).children(".about_ttile_line").children(".about_title").children(".mantitle").delay(Timers+500).animate({top:"0",opacity:"1"},1000);
 $(this).children(".about_ttile_line").children(".about_title").children(".sectitle").delay(Timers+800).animate({top:"0",opacity:"1"},1000);

  $(this).children(".news_touch_in").children("ul").children("li").each(function() {
		  Timerss+=100;
		$(this).delay(Timerss+300).animate({top:"0",opacity:"1"},1000);
	
             }); 
  
  
  
	};};
	


$(document).ready(function() {
	
$(window).scroll(function () {
 if ($(document).scrollTop() + $(window).height() >= $(document).height()) {
   var Timers = 0;
  var  Timerss=0;
 $(".footer").children(".footer_in").children("#footer_in_box").each(function() {
		  Timerss+=100;
		$(this).delay(Timerss+300).animate({top:"0",opacity:"1"},1000);
	
 }); 
  
   $("#footer_bottom_link").delay(Timers+800).animate({top:"0",opacity:"1"},1000);
   $(".footer_bottom").delay(Timers+1200).animate({top:"0",opacity:"1"},1000);
  
	};
	
	
	if( $(window).scrollTop() >= $('.index_content').offset().top-550 ){
		$("#show,.header_bottom").fadeIn(1000);
		if(!$("#kefu").hasClass("show_height")){$("#kefu").fadeIn(1000);}

		}else{
			
			 $("#kefu,#show,.header_bottom").fadeOut(1000);
			
			}
	
	});
	
  
$(".kefu").mouseleave(function() {$(this).addClass("show_height");$(this).fadeOut(1000)});
		   
 $("#show").mouseenter(function() {$(".kefu").addClass("show_height");$(".kefu").fadeIn(1000)});   
	 
	  
	  
	  
  $(".nav_product_mu li .sub-menu li a.select").append("<div class='no_select'></div>");
  
  $("#menu_widgetss li.menu-item-has-children").append("<div class='has_kid'>+</div>");
 $("#menu_widgetss li") .mouseenter(function() { $(this).children(".sub-menu").stop(true, true).slideDown(500);});
   
    $("body").click(function() {  $("#menu_widgetss li").children(".sub-menu").stop(true, true).slideUp(500);});
       


       
 
  
  
   $(".header_menu_ul li,.index_swipers,#post_form_menu li").hover(function() {
   
        $(this).children(".sub-menu,.index_next,.index_prve").stop(true, true).fadeIn("200");
    }, function() {

        $(this).children(".sub-menu,.index_next,.index_prve").stop(true, true).fadeOut("1000");
    });
 $(".pic_l_in ul li").mouseenter(function() { $(this).children(".vedio_over_li").animate({ "bottom": 0},500);});
$(".pic_l_in ul li").mouseleave(function() { $(this).children(".vedio_over_li").animate({ "bottom": "-100%"}, 500);});
	 

$(".cunst_code").click(function() { $(this).children('.cunst_vedio').fadeIn(500)});
	
$(".pic_big_bottom_in_search #searchform  #s").click(function() { $(".search_key_mod").slideDown(500)});
$(".pic_big_bottom_in_search").mouseleave(function() { $(".search_key_mod").slideUp(500);});	
	 
var gallery_xz = new Swiper('.gallery_xz',{
visibilityFullFit : true,
calculateHeight : true,
simulateTouch : false,
 pagination: '.galic_na',
 paginationClickable: true,
speed:1000
  });
$('.gallery_xz .galic_prve').click(function(){gallery_xz.swipePrev(); });
$('.gallery_xz .galic_next').click(function(){gallery_xz.swipeNext(); }); 
	 
	 
	var qiehuan = new Swiper('.qiehuan',{
visibilityFullFit : true,
calculateHeight : true,
simulateTouch : false,
speed:1000,
onSlideChangeStart: function(){
      $(".gallery_qiehuan_x  .swiper-wrapper .active").removeClass('active')
      $(".gallery_qiehuan_x  .swiper-wrapper a").eq(qiehuan.activeIndex).addClass('active')  
    }
  });

 $(".gallery_qiehuan_x  .swiper-wrapper a").on('touchstart mousedown',function(e){
    e.preventDefault()
    $(".gallery_qiehuan_x  .swiper-wrapper .active").removeClass('active')
    $(this).addClass('active');
	
     qiehuan.swipeTo( $(this).index() ,1000, false );
  });
  $(".gallery_qiehuan_x  .swiper-wrapper a").click(function(e){
    e.preventDefault()
  });


var gallery_qiehuan_x = new Swiper('.gallery_qiehuan_x',{
visibilityFullFit : true,
cssWidthAndHeight: 'width',
slidesPerView: 4,
speed:500
  });
$(".gallery_qiehuan_x").children(".swiper-wrapper").css("width", 80 * $(".gallery_qiehuan_x").children(".swiper-wrapper").children("a").length + "px");
  $('.gallery_qiehuan_x .galic_prve').click(function(){gallery_qiehuan_x.swipePrev();  });
$('.gallery_qiehuan_x .galic_next').click(function(){gallery_qiehuan_x.swipeNext(); });



$(".close_order").click(function() {
    $(".shop_form").fadeOut(500);
});

$(".buy_btn .btn").click(function() {
    $(".shop_form").fadeIn(500);
    var a = $(".shop_form").offset().top - 300;
    $("html,body").animate({
        scrollTop: a
    }, 1e3);
});

$("#content_shop_btn").click(function() {
    $(this).addClass("cutyes");
    $("#comment_shop_btn").removeClass("cutyes");
    $("#comment_shop").fadeOut(300);
    $("#content_shop").fadeIn(300);
});

$("#comment_shop_btn").click(function() {
    $(this).addClass("cutyes");
    $("#content_shop_btn").removeClass("cutyes");
    $("#content_shop").fadeOut(300);
    $("#comment_shop").fadeIn(300);
});




  
 });

