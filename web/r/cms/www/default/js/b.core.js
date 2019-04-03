var B = {
	_set : {
		loginUrl : "", //session timeout
		debug : true
	},
	debug : function(msg) {
		if (this._set.debug) {
			if (typeof (console) != "undefined")
				console.log(msg);
			else
				alert(msg);
		}
	}
}

;
$(function() {
	
	caseCanvasAnimation();

	usedefaultAssetLogo();

	particles();

    $(window).scroll(function() {
    	var scrollTop = $(window).scrollTop();
    	var height = $(window).height();
    	if($(".header").hasClass('header-index')){
	    	var scrollTop = $(window).scrollTop();
	        if(scrollTop >= 30){
	            $(".header").addClass("fixed");
	            $('.logo').attr('src', resUrl + 'images/logo_bubi.png');
	        }else{
	            $(".header").removeClass("fixed");
	            $('.logo').attr('src', resUrl + 'images/logo.png');
	        }
    	}
    	if(scrollTop >= (height+1200)){
	        $(".to-top").show();
    	}else{
    		$(".to-top").hide();
    	}
    });
    
    
    /***** 首页 *****/
   //应用场景
	$('.scene-group .scene-item').mouseover(function(){
		$(this).addClass('active');
	});
	$('.scene-group .scene-item').mouseleave(function(){
		$('.scene-group .scene-item').removeClass('active');
	});
	
	// 技术优势
	$('.avt-item').mouseover(function(){
		$('.avt-item').removeClass('active');
		$(this).addClass('active');
		$(this).children('img').attr('src', resUrl + 'images/adv'+($(this).index()+1)+'.png');
	});
	$('.avt-item').mouseleave(function(){
		$('.avt-item').removeClass('active');
		$(this).children('img').attr('src', resUrl + 'images/adv'+($(this).index()+1)+'-active.png');
	});
	
	// 合作伙伴
	$('.partner-item').mouseover(function(){
		$(this).addClass('active');//children('img').attr('src', resUrl + 'images/partner_' + $(this).attr('data-img') + '.png');
	});
	$('.partner-item').mouseout(function(){
		$(this).removeClass('active');
	});
	
	// 更多应用场景
	var count = 0;
	$('.circle .box').eq(count++).addClass('active');
	setInterval(function () {			
		if (count == 5) {
			for(var i=0; i<4; i++){
				$('.circle .box').eq(i).removeClass('active');
			}
			setTimeout(function () {
				$('.circle .box').eq(4).removeClass('active');
				$('.circle .box').eq(5).removeClass('active');
			}, 3000);
		} else if (count == 6) {
			count = 0;
		}
		
		$('.circle .box').eq(count++).addClass('active');
	}, 2000);
	
	// 加入我们
    $('.J-viewJob').click(function(){
        $this = $(this);
		$this.addClass('active');
		if ($this.parent('.job-item').hasClass('active')) {
			$this.removeClass('active');
			$this.parent('.job-item').removeClass('active');
		} else {
			$this.addClass('active');
			$this.parent('.job-item').addClass('active');
		}
	});
	
	// 联系我们
	$('.address-item').click(function(){
		var index = $('.address-item').index(this);
		$('.iframe').removeClass('active');
		$('.address-item').removeClass('active');
		$(this).addClass('active');
		$('.iframe').eq(index).addClass('active');
	});
});

function canvasSupport() {
    return !!document.createElement('canvas').getContext;
}

function particles() {
	var particlesObtion = {
		particles: {
			color: "#69a591",
			shape: 'circle', // "circle", "edge" or "triangle"
			opacity: 1,
			size: 5,
			size_random: false,
			nb: 30,
			line_linked: {
				enable_auto: true,
				distance: 180,
				color: '#69a591',
				opacity: 1,
				width: 1,
				condensed_mode: {
					enable: false,
					rotateX: 100,
					rotateY: 600
				}
			},
			anim: {
				enable: true,
				speed: 0.5
			}
		},
		interactivity: {
			enable: true,
			mouse: {
				distance: 300
			},
			detect_on: 'window', // "canvas" or "window"
			mode: 'grab',
			line_linked: {
				opacity: .5
			},
			events: {
				onclick: {
					enable: false,
					mode: 'push', // "push" or "remove"
					nb: 4
				}
			}
		},
		retina_detect: true
	};
	
	if($('.particles-js').length && canvasSupport()) particlesJS('particles-js', particlesObtion);	
}

function usedefaultAssetLogo(){
	var browser={
	    versions:function(){
	        var u = navigator.userAgent, app = navigator.appVersion;
	        return {
	            trident: u.indexOf('Trident') > -1, //IE内核
	            presto: u.indexOf('Presto') > -1, //opera内核
	            webKit: u.indexOf('AppleWebKit') > -1, //苹果、谷歌内核
	            gecko: u.indexOf('Gecko') > -1 && u.indexOf('KHTML') == -1,//火狐内核
	            mobile: !!u.match(/AppleWebKit.*Mobile.*/), //是否为移动终端
	            ios: !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/), //ios终端
	            android: u.indexOf('Android') > -1 || u.indexOf('Linux') > -1, //android终端或者uc浏览器
	            iPhone: u.indexOf('iPhone') > -1 , //是否为iPhone或者QQHD浏览器
	            iPad: u.indexOf('iPad') > -1, //是否iPad
	            webApp: u.indexOf('Safari') == -1 //是否web应该程序，没有头部与底部
	        };
		}(),
		language:(navigator.language || navigator.browserLanguage || navigator.userLanguage).toLowerCase()
	};
	if(browser.versions.mobile || browser.versions.ios || browser.versions.android || browser.versions.iPhone || browser.versions.iPad){
	    $('body').addClass('wap');
	    $('.wap .swiper-banner').height($(window).height());
	    $('.wap .swiper-banner .swiper-container').height($(window).height());
	}else if(browser.versions.trident){
		// console.log("IE内核");
	}
}

function caseCanvasAnimation () {
	var mapId = $("map").attr("id");
	var imgId = 'img1';
	var dataId = 'mature';
	var obj = [];
	var canvasOpt = {
	    fillStyle: "#fbddc5",
	    strokeStyle: "#f4a58c",//"rgba(255,184,0,1)",
	    lineWidth: 2
	};
	var canvasCss = {
		left: '',
		top: '',
		zIndex: '',
	    position: "absolute",
	    zIndex: 11,
	    width: '',
	    height: ''
	};
	
	function initCanvas(t) {
	    var i = $("#" + imgId),
	    e = i.parent(),
	    s = "canvas" + Math.ceil(1e3 * Math.random());
	    e.append($('<canvas id="' + s + '"></canvas>'));
	    var n = $("#" + s);
	    canvasCss.left = i.position().left + "px",
	    canvasCss.top = i.position().top + "px",
	    canvasCss.width = i.width() + "px",
	    canvasCss.height = i.height() + "px",
	    canvasCss.zIndex && (canvasCss.zIndex += 1),
	    n.css(canvasCss).attr({
	        width: i.width()*2 + "px",
	        height: i.height()*2 + "px"
	    });
	    var a = n[0];
	    obj[t + "Canvas"] = a,
	    obj[t + "RenderArea"] = a.getContext("2d");
	    var o = canvasOpt;
	    for (var r in o) obj[t + "RenderArea"][r] = o[r]
	}
	
	function bindEvent() {
	    i = $("#" + mapId).find("area");
	    i.bind("mouseover", function() {
	    	var mouseoutCanvas = $(obj["hoverCanvas"]);
	        obj["hoverRenderArea"].clearRect(0, 0, 3000, 3000)
	     	$('.case-solution span').removeClass('active');
	    	var coords = $(this).attr("coords");
	        var point = coords.split(",");
	        var t = obj["hoverRenderArea"];
	        t.beginPath(),
	        t.moveTo(point[0]*2, point[1]*2);
	        for (var n = 2; n < point.length; n += 2){
	        	t.lineTo(point[n]*2, point[n + 1]*2);
	        }
	        t.lineTo(point[0]*2, point[1]*2);
	        t.fill();
	        t.stroke();
	        
	        t.closePath();
	        $('.case-solution span').eq($(this).attr('data-index')).addClass('active');
	    }),
	    i.bind("mouseout", function() {
	//  	var mouseoutCanvas = $(obj["hoverCanvas"]);
	//      obj["hoverRenderArea"].clearRect(0, 0, mouseoutCanvas.width(), mouseoutCanvas.height())
	    	// var i = $(obj["hoverCanvas"]);
	     //    obj["hoverRenderArea"].clearRect(0, 0, i.width(), i.height())
	    });
	//  i.bind("click", function() {
	//  	var coords = $(this).attr("coords");
	//      var point = coords.split(",");
	//      var t = obj["clickRenderArea"];
	//      t.beginPath(),
	//      t.moveTo(point[0], point[1]);
	//      for (var n = 2; n < point.length; n += 2){
	//      	t.lineTo(point[n], point[n + 1]);
	//      }
	//      t.lineTo(point[0], point[1]);
	//      t.stroke();
	//      t.fill();
	//      t.closePath();
	//  });
	}
	function hoverEvent() {
	    i = $("#" + mapId).find("area");
	    i.bind("mouseover", function() {
	     	$('.case-solution span').removeClass('active');
	        $('.case-solution span').eq($(this).attr('data-index')).addClass('active');
	    })
	}
	
	$('#img1').load(function() {
		flag = 1;
		if (canvasSupport()) {
			initCanvas("hover");
			bindEvent();
		} else {
			hoverEvent();
		}
	});
	
	$("#img1").one('load', function() {
		if (canvasSupport()) {
			initCanvas("hover");
			bindEvent();
		} else {
			hoverEvent();
		}
	}).each(function() {
		if (canvasSupport()) {
			initCanvas("hover");
			bindEvent();
		} else {
			hoverEvent();
		}
	});
}