/*
 * app JavaScript Library
 * Copyright (c) 2015-2018 xinsongkeji
 */
// 上传图片
// url：上传的url地址
// method: GET/POST/DELETE/PUT
// payload:post body
function myajax(path, method, payload, callback){
	//user_id = $api.getStorage("user_id");
	
	token = $api.getStorage("token");
	console.log("token is " + token);
	
	if(method == 'GET'){
		if(token == null || token == undefined || token == ''){
			url = 'http://123.56.159.76/v1' + path;
		} else if(path.indexOf("?") > -1) {
			url = 'http://123.56.159.76/v1' + path + '&' + 'token=' + token;
			//url = 'http://123.56.159.76/v1' + path
		} else {
			url = 'http://123.56.159.76/v1' + path + '?' + 'token=' + token;
		}
	}else{
		url = 'http://123.56.159.76/v1' + path
	}
	if(method == 'GET'){
		console.log(url + ' ' + method + ' ');
		
		api.ajax({
			url : url,
			method : 'get',
			timeout : 30,
			dataType : 'json',
			returnAll : true
		}, function(ret, err) {
			//if token is timeout,login again
			callback(ret,err);
		});
	} else if(method == "POST"){
		mybody = JSON.stringify(payload);
		console.log(url + ' ' + method + ' ' + mybody);
		
    	api.ajax({
	        url:url,
	        method: 'post',
		    timeout: 30,
		    dataType: 'json',
		    returnAll:true,
		    headers:{
		    	'Content-Type': 'application/json',
		    	'token': token
		    },
		    data:{
		    	body: mybody
		    }
        }, function(ret, err) {
            //api.hideProgress();
            callback(ret, err);
        });
	}
}


// 上传图片
// url：上传的url地址
// filepath：上传的文件
// callback：上传成功返回地址
function myajax_upload(path,myfiles, callback) {
	post_id = $api.getStorage("user_id");
	token = $api.getStorage("token");
	//http_url = "http://123.56.159.76/v1/ay/lost/" + post_id + "/upload_imgs" ;
	http_url = "http://123.56.159.76/v1/ay/upload_imgs?token=" + token;
	api.ajax({
		url : http_url,
		method : 'post',
		timeout : 30,
		dataType : 'json',
		returnAll : true,
		data : {
			files : {"file": myfiles}
		}
	}, function(ret, err) {
		callback(ret, err);
		/*if (ret) {
	        	console.log(JSON.stringify(ret));
	        	console.log(JSON.stringify(ret.body))
				callback(ret.body.img_urls);
	        	
		} else {
			api.alert({msg : ('错误码：' + err.code + '；错误信息：' + err.msg + '；网络状态码：' + err.statusCode)});
		}*/
	});
}



// 时间戳转时间
function _formatDate(timespan) {
	var now = new Date(timespan);
	var year = now.getFullYear();
	var month = now.getMonth() + 1;
	var date = now.getDate();
	var hour = now.getHours();
	var minute = now.getMinutes();
	var second = now.getSeconds();
	return year + "-" + month + "-" + date + "   " + hour + ":" + minute + ":" + second;
}

// 滚动到底部
function _scrollToEnd() {
	document.getElementsByTagName('body')[0].scrollTop = document.getElementsByTagName('body')[0].scrollHeight;
}

// 广播事件
function _sendEvent(eventName, extra) {
	var _extra = ( typeof arguments[1] == "undefined" || arguments[1] == null) ? {} : arguments[1];
	api.sendEvent({
		name : eventName,
		extra : _extra
	});
}

// 监听事件
function _addEventListener(eventName, _call, extra) {
	var _extra = ( typeof arguments[2] == "undefined" || arguments[2] == null) ? {} : arguments[2];
	api.addEventListener({
		name : eventName,
		extra : _extra
	}, function(ret, err) {
		if ( typeof _call == "function") {
			_call(ret);
		}
	});
}

// 打开相册或相机
//library            //图片库
//camera            //相机
//album            //相册
//pic            //图片
//video        //视频
function _getPicture(_call, encodingType, mediaValue, destinationType, quality, targetWidth, targetHeight, saveToPhotoAlbum, allowEdit) {
	var _encodingType = ( typeof arguments[1] == "undefined" || arguments[1] == null) ? "jpg" : arguments[1];
	var _mediaValue = ( typeof arguments[2] == "undefined" || arguments[2] == null) ? "pic" : arguments[2];
	var _destinationType = ( typeof arguments[3] == "undefined" || arguments[3] == null) ? "url" : arguments[3];
	var _quality = ( typeof arguments[4] == "undefined" || arguments[4] == null) ? 50 : arguments[4];
	var _targetWidth = ( typeof arguments[5] == "undefined" || arguments[5] == null) ? 320 : arguments[5];
	var _targetHeight = ( typeof arguments[6] == "undefined" || arguments[6] == null) ? 320 : arguments[6];
	var _saveToPhotoAlbum = ( typeof arguments[7] == "undefined" || arguments[7] == null) ? true : arguments[7];

	api.actionSheet({
		title : '您想要从哪里选取图片？',
		cancelTitle : '取消',
		buttons : ["优雅自拍", "相册收藏"]
	}, function(ret, err) {
		if (ret.buttonIndex == 3) {
			return;
		}
		var sourceType = "album";
		if (ret.buttonIndex == 1) {
			sourceType = "camera";
		}

		api.getPicture({
			sourceType : sourceType,
			encodingType : _encodingType,
			destinationType : _destinationType,
			mediaValue : _mediaValue,
			quality : _quality,
			targetWidth : _targetWidth,
			targetHeight : _targetHeight,
			saveToPhotoAlbum : _saveToPhotoAlbum
		}, function(ret, err) {
			if (ret) {
				if ( typeof _call == "function") {
					_call(ret.data);
				}
			} else {
				api.alert({
					msg : err.msg
				});
			}
		});
	});

}
// 根据出生日期算年龄
function ages(str) {
	var r = str.match(/^(\d{1,4})(-|\/)(\d{1,2})\2(\d{1,2})$/);
	if (r == null)
		return false;
	var d = new Date(r[1], r[3] - 1, r[4]);
	if (d.getFullYear() == r[1] && (d.getMonth() + 1) == r[3] && d.getDate() == r[4]) {
		var Y = new Date().getFullYear();
		return (Y - r[1]);
	}
	return 0;
}

// 获取文件拓展名
function _getExt(fileName) {
	return fileName.substring(fileName.lastIndexOf('.') + 1);
}

// PHP时间戳转时间
function _trans_php_time_to_str(timestamp, n) {
	update = new Date(timestamp * 1000);
	//时间戳要乘1000
	year = update.getFullYear();
	month = (update.getMonth() + 1 < 10) ? ('0' + (update.getMonth() + 1)) : (update.getMonth() + 1);
	day = (update.getDate() < 10) ? ('0' + update.getDate()) : (update.getDate());
	hour = (update.getHours() < 10) ? ('0' + update.getHours()) : (update.getHours());
	minute = (update.getMinutes() < 10) ? ('0' + update.getMinutes()) : (update.getMinutes());
	second = (update.getSeconds() < 10) ? ('0' + update.getSeconds()) : (update.getSeconds());
	if (n == 1) {
		return (year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second);
	} else if (n == 2) {
		return (year + '-' + month + '-' + day);
	} else {
		return 0;
	}
}

function _uuid() {
    var s = [];
    var hexDigits = "0123456789abcdef";
    for (var i = 0; i < 32; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    //s[14] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
    //s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01
    //s[8] = s[13] = s[18] = s[23] = "-";

    var uuid = s.join("");
    return uuid;
}

// 生成guid,主要用于生成随机文件名
function _newGuid() {
	function S4() {
		return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
	}

	return (S4() + S4() + "-" + S4() + "-" + S4() + "-" + S4() + "-" + S4() + S4() + S4());
}

// 获取当前的时间，拼接成2015-11-09这样的格式，主要用于对图片进行时间分类
function _getNowFormatDate() {
	var date = new Date();
	var seperator1 = "-";
	var year = date.getFullYear();
	var month = date.getMonth() + 1;
	var strDate = date.getDate();
	if (month >= 1 && month <= 9) {
		month = "0" + month;
	}
	if (strDate >= 0 && strDate <= 9) {
		strDate = "0" + strDate;
	}
	var currentdate = year + seperator1 + month + seperator1 + strDate
	return currentdate;
}

// 判断是否是IOS
function _isIOS() {
	return api.systemType == "ios" ? true : false;
}

// 图片压缩
// imageFilter:压缩对象
// imgsrc：源图片的路径
// quality：图片压缩质量，一般建议0.5
// scale：图片压缩比例，也是建议0.5
// ext：源图片拓展名
// callback：转换成功之后回调函数
function _imgCompress(imageFilter, imgsrc, quality, scale, ext, callback) {
	// 压缩文件的保存目录
	var savePath = api.cacheDir + "/" + _getNowFormatDate() + "/";
	// 压缩文件生成的随机文件名称
	var savename = _newGuid() + "." + ext;
	imageFilter.compress({
		img : imgsrc,
		quality : quality,
		scale : quality,
		save : {
			album : false,
			imgPath : savePath,
			imgName : savename
		}
	}, function(ret, err) {
		if (ret) {
			callback(savePath + savename);
		} else {
			alert(JSON.stringify(err));
		}
	});
}		
// 解决状态栏重合
function _fixStatusBar(headerid, callback) {
	var header = $api.byId(headerid);
	var systemType = api.systemType;
	var systemVersion = parseFloat(api.systemVersion);
	if (systemType == "ios" || (systemType == "android" && systemVersion >= 4.4)) {
		if (systemType == "android") {
			header.style.paddingTop = '25px';
		}
		$api.fixStatusBar(header);
	} else {
		$api.fixIos7Bar(header);
	}
	var headerPos = $api.offset(header);
	if ( typeof callback == "function") {
		callback(headerPos);
	}
}



// 下拉刷新
function _setRefreshHeaderInfo(_call, bgColor, textColor) {
	var _bgColor = ( typeof arguments[1] == "undefined" || arguments[1] == null) ? '#f1f1f1' : arguments[1];
	var _textColor = ( typeof arguments[2] == "undefined" || arguments[2] == null) ? '#999' : arguments[2];
	api.setRefreshHeaderInfo({
		visible : true,
		loadingImg : 'widget://image/refresh.png',
		bgColor : _bgColor,
		textColor : _textColor,
		textDown : '下拉刷新...',
		textUp : '松开刷新...',
		showTime : true
	}, function(ret, err) {
		if ( typeof _call == "function") {
			_call();
		}
	});
}

// 上拉加载
function _scrolltobottom(_call, threshold) {
	var _threshold = ( typeof arguments[1] == "undefined" || arguments[1] == null) ? 0 : arguments[1];
	_addEventListener('scrolltobottom', _call, {
		threshold : _threshold
	});
}


// 打开新框架
function _openFrame(name, url, rect, pageParam, bgColor, bounces, reload, showProgress) {
	var __rect = {
		x : 0,
		y : 0,
		w : api.winWidth,
		y : api.winHeight,
		l : 0,
		t : 0,
		b : 0,
		r : 0
	};
	var _rect = ( typeof arguments[2] == "undefined" || arguments[2] == null || typeof arguments[2] != "object") ? __rect : arguments[2];
	var _pageParam = ( typeof arguments[3] == "undefined" || arguments[3] == null) ? api.pageParam : arguments[3];
	var _bgColor = ( typeof arguments[4] == "undefined" || arguments[4] == null) ? 'rgba(0,0,0,0)' : arguments[4];
	var _bounces = ( typeof arguments[5] == "undefined" || arguments[5] == null) ? false : arguments[5];
	var _reload = ( typeof arguments[6] == "undefined" || arguments[6] == null) ? false : arguments[6];
	var _showProgress = ( typeof arguments[7] == "undefined" || arguments[7] == null) ? false : arguments[7];
	api.openFrame({
		name : name,
		url : url,
		rect : {
			x : typeof _rect.x != "number" ? __rect.x : _rect.x,
			y : typeof _rect.y != "number" ? __rect.y : _rect.y,
			w : typeof _rect.w != "number" ? __rect.w : _rect.w,
			h : typeof _rect.h != "number" ? __rect.h : _rect.h,
			marginLeft : typeof _rect.l != "number" ? __rect.l : _rect.l,
			marginTop : typeof _rect.t != "number" ? __rect.t : _rect.t,
			marginBottom : typeof _rect.b != "number" ? __rect.b : _rect.b,
			marginRight : typeof _rect.r != "number" ? __rect.r : _rect.r
		},
		bgColor : _bgColor,
		pageParam : _pageParam,
		scrollToTop : true,
		bounces : _bounces,
		showProgress : _showProgress,
		reload : _reload,
		vScrollBarEnabled : false,
		hScrollBarEnabled : false,
		allowEdit : true
	});
}
// 小提示
function _toast(msg, duration, location, _call) {
	var _duration = ( typeof arguments[1] == "undefined" || arguments[1] == null) ? window.toastDuration : arguments[1];
	var _location = ( typeof arguments[2] == "undefined" || arguments[2] == null) ? window.toastLocation : arguments[2];
	api.toast({
		msg : msg,
		duration : _duration,
		location : _location
	});
	if ( typeof _call == "function") {
		setTimeout(_call, duration);
	}
}

// 加载框
function _showProgress(title, text, modal, animationType) {
	var _title = ( typeof arguments[0] == "undefined" || arguments[0] == null) ? window.showProgressTitle : arguments[0];
	var _text = ( typeof arguments[1] == "undefined" || arguments[1] == null) ? window.showProgressText : arguments[1];
	var _modal = ( typeof arguments[2] == "undefined" || arguments[2] == null) ? true : arguments[2];
	var _animationType = ( typeof arguments[3] == "undefined" || arguments[3] == null) ? window.showProgressAnimationType : arguments[3];
	api.showProgress({
		style : 'default',
		animationType : _animationType,
		title : _title,
		text : _text,
		modal : _modal
	});
}
