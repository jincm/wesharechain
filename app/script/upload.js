var policyText = {
    "expiration": "2020-01-01T12:00:00.000Z", //设置该Policy的失效时间，超过这个失效时间之后，就没有办法通过这个policy上传文件了
    "conditions": [
    ["content-length-range", 0, 1048576000] // 设置上传文件的大小限制
    ]
};

accessid= 'O4LzRirHOopmmAak';
accesskey= 'q5XcjfAbqcC91iFUEhoRFPjHrOXVPm';
host = 'http://xinsongkeji.oss-cn-beijing.aliyuncs.com';

var policyBase64 = Base64.encode(JSON.stringify(policyText))
message = policyBase64
var bytes = Crypto.HMAC(Crypto.SHA1, message, accesskey, { asBytes: true }) ;
var signature = Crypto.util.bytesToBase64(bytes);
var uploader = new plupload.Uploader({
	runtimes : 'html5,html4',
	browse_button : 'selectfiles', 
    //runtimes : 'flash',
	container: document.getElementById('container'),
	//flash_swf_url : 'lib/plupload-2.1.2/js/Moxie.swf',
	//silverlight_xap_url : 'lib/plupload-2.1.2/js/Moxie.xap',

    url : host,
    //url: "http://123.56.159.76/v1/ay/lost/" + "563ed050ce6a3d1f234f3eba" + "/upload_imgs?token=123",

	multipart_params: {
		'Filename': '${filename}', 
        'key' : 'zuohaoshi/10002/${filename}',
		'policy': policyBase64,
        'OSSAccessKeyId': accessid, 
        'success_action_status' : '200', //让服务端返回200,不然，默认会返回204
		'signature': signature,
	},

	init: {
		PostInit: function() {
			document.getElementById('ossfile').innerHTML = '';
			document.getElementById('postfiles').onclick = function() {
				uploader.start();
				return false;
			};
		},

		FilesAdded: function(up, files) {
			plupload.each(files, function(file) {
				document.getElementById('ossfile').innerHTML += '<div id="' + file.id + '">' + file.name + ' (' + plupload.formatSize(file.size) + ')<b></b>'
				+'<div class="progress"><div class="progress-bar" style="width: 0%"></div></div>'
				+'</div>';
			});
		},

		UploadProgress: function(up, file) {
			var d = document.getElementById(file.id);
			d.getElementsByTagName('b')[0].innerHTML = '<span>' + file.percent + "%</span>";
            
            var prog = d.getElementsByTagName('div')[0];
			var progBar = prog.getElementsByTagName('div')[0]
			progBar.style.width= 2*file.percent+'px';
			progBar.setAttribute('aria-valuenow', file.percent);
		},

		FileUploaded: function(up, file, info) {
            //alert(info.status)
            if (info.status >= 200 || info.status < 200)
            {
                document.getElementById(file.id).getElementsByTagName('b')[0].innerHTML = 'success';
            }
            else
            {
                document.getElementById(file.id).getElementsByTagName('b')[0].innerHTML = info.response;
            } 
		},

		Error: function(up, err) {
			document.getElementById('console').appendChild(document.createTextNode("\nError xml:" + err.response));
		}
	}
});

console.log("signature is " + signature);
uploader.init();





/*
//https://help.aliyun.com/document_detail/oss/api-reference/object/PostObject.html
//ali
var policyText = {
    "expiration": "2020-01-01T12:00:00.000Z", //设置该Policy的失效时间，超过这个失效时间之后，就没有办法通过这个policy上传文件了
    "conditions": [
    ["content-length-range", 0, 1048576000] // 设置上传文件的大小限制
    ]
};

accessid= 'O4LzRirHOopmmAak';
accesskey= 'q5XcjfAbqcC91iFUEhoRFPjHrOXVPm';
host = 'https://xinsongkeji.oss-cn-beijing.aliyuncs.com'; //https?

var policyBase64 = Base64.encode(JSON.stringify(policyText));
message = policyBase64;
var bytes = Crypto.HMAC(Crypto.SHA1, message, accesskey, { asBytes: true }) ;
var signature = Crypto.util.bytesToBase64(bytes);
*/

//参考：https://help.aliyun.com/document_detail/oss/practice/post_object_callback.html
// 上传图片
// url：上传的url地址
// filepath：上传的文件
// callback：上传成功返回地址
function myajax_upload_ali(path,filepath, callback) {
	post_id = $api.getStorage("user_id");
	token = $api.getStorage("token");
	http_url = host;

	//http_url = "http://123.56.159.76/v1/ay/lost/" + "563ed050ce6a3d1f234f3eba" + "/upload_imgs?token=" + token;

	console.log(http_url);
	console.log(filepath);
	console.log(signature);
	
	api.ajax({
		url : 'http://xinsongkeji.oss-cn-beijing.aliyuncs.com',
		method : 'post',
		timeout : 30,
		dataType : 'json',
		returnAll : true,
		//X-Requested-With: 'com.apicloud.apploader',
		
		//async: false,
		//cache: false,
		//processData: false,
		//contentType: false,
		data : {
			values: {
				'Filename': '${filename}', 
				'key' : 'zuohaoshi/10002/${filename}',
				'policy': policyBase64,
		        'OSSAccessKeyId': accessid, 
		        'success_action_status' : '200', 
				'Signature': signature
			},
			
			files: {
				'file': filepath
			}
		}
	}, function(ret, err) {
		if (ret) {
				console.log("bbbbbbbbbbbbbbbcccc");
	        	console.log(JSON.stringify(ret));
	        	console.log(JSON.stringify(ret.body))
				callback(ret.body.img_urls[0]);
	        	api.alert({
                			title: '上传成功',
                			msg: ret.body.img_urls,
                			buttons: ['确定']
            	});  
		} else {
			console.log("bbbbbbbbbbbbbbb");
			console.log(JSON.stringify(err));
			api.alert({msg : ('错误码：' + err.code + '；错误信息：' + err.msg + '；网络状态码：' + err.statusCode)});
		}
	});
}
