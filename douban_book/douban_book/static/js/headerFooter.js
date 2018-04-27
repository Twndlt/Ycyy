var yuming = 'http://sccs.youedata.com';
$(function(){

//----头部----------------------------
var header = '<div class="headAll"><div class="header">'
	+'<a class="iBlock" href="index.html"><img src="/static/images/logo.png"></a>'
	+'<div class="searchBox fr">'
		+'<form class="search" action="" method="post">'
			+'<input class="sWord" type="text" placeholder="站内搜索" id="search-input"/>'
			+'<input class="sBtn" name="Submit" value="" id="search-btn"/>' 
		+'</form>'
		+'<ul class="fix">'
			+'<li class="mobile"><img src="images/mobileMa.png"></li>'
			+'<li class="weixin"></li>'
			+'<li class="sina"></li>'
		+'</ul>'
	+'</div>'
+'</div>'
+'</div>'
+'<div class="headNav">'
	+'<div>'
		+'<a href="index.html">首页</a>'
		+'<a href="policyKu.html">政策库<i id="gozcdt">政策动态</i><i class="navindex2" id="gozck">政策查询</i></a>'
		+'<a href="analyzeMap.html">政策分析</a>'
		+'<a href="baseExp.html">示范基地<i id="gojddt">基地动态</i><i class="navindex2" id="jdk">基地库</i></a>'
		+'<a href="activeAfter.html">活动跟踪</a>'
		+'<a href="serviceOver.html">服务拓展</a>'
		+'<a class="navLineNo" href="word.html">建言献策</a>'		
	+'</div>'
+'</div>';
$('body').prepend(header);
$('#gozcdt').click(function(e){
	e = e || window.event;
    if(e.preventDefault) {
      e.preventDefault();
    }else{
      e.returnValue = false;
    }
	window.location.href = 'policyKu.html';
});
$('#gozck').click(function(e){
	e = e || window.event;
    if(e.preventDefault) {
      e.preventDefault();
    }else{
      e.returnValue = false;
    }
	window.location.href = 'zhengceku.html';
});
$('#gojddt').click(function(e){
	e = e || window.event;
    if(e.preventDefault) {
      e.preventDefault();
    }else{
      e.returnValue = false;
    }
	window.location.href = 'baseExp.html';
});
$('#jdk').click(function(e){
	e = e || window.event;
    if(e.preventDefault) {
      e.preventDefault();
    }else{
      e.returnValue = false;
    }
	window.location.href = 'jidiku.html';
});
//---底部---------------------------------------
var  foot='<div class="footAbout">'
	+'<div>'
		+'<img src="/static/images/party.png">'
		+'<ul>'
			+'<li><a href="aboutWebsite.html">关于本站</a></li>'
			+'<li><a href="websiteState.html">网站声明</a></li>'
			+'<li><a href="zddt.html">网站地图</a></li>'
			+'<li><a href="aboutUs.html">联系我们</a></li>'
		+'</ul>'
		+'<b style="font-weight:normal;">版权所有：国家信息中心</b>'
		+'<p style="left:241px;"><a href="http://www.youedata.cn/" style="color:#fff;">技术支持：国信优易数据有限公司</a></p>'
	+'</div>'
+'</div>';
$('body').append(foot); 

	
//页头ajax   begin   
  $.ajax({
 	type: "post",
    data: "",
    url: yuming + '/homePage/getQRCode',
    dataType: "json",
 	success: function(result) {
 		if(result.code == "200") {			
 			var list = result.data;
 			var weixin = '<img src="'+list.wechatPath+'">';					 
 		    $(".weixin").append(weixin);
 		    
 		    var weibo = '<img src="'+list.weiboPath+'">';					 
 		    $(".sina").append(weibo);
 		}else{
 			//加载异常 xhj
 		}
 	},
 	beforeSend:function(){
 		//加载中 xhj
 	},
 	error:function(){
 		//加载异常 xhj
 	}
 });     
//页头ajax   end
  function getValue(){
  	var value = $.trim($('#search-input').val());
    if (value=='') {
    	alert("请输入搜索内容");
    	return;
    }
 //    _encode = encodeURI('search.html?keyword='+ value +'');
 //    _encode = encodeURI(_encode);
	// window.location.href = _encode;
	

	window.location.href = 'search.html?keyword='+ value +'';
  }
  $('#search-btn').click(function(e){
  		e = e || window.event;
	    if(e.preventDefault) {
	      e.preventDefault();
	    }else{
	      e.returnValue = false;
	    };
	    getValue();
  })
  //回车事件
  $('#search-input').keyup(function(e){
  	  e = e || window.event;  	  
	  if(e.keyCode ==13){
	    getValue();	   
	  }
	});
   
	function getQueryVariable(variable){
        var query = window.location.search.substring(1);
        var vars = query.split("&");
        for (var i=0;i<vars.length;i++) {
            var pair = vars[i].split("=");
            if(pair[0] == variable){return pair[1];}
        }
       return('');
	};
	var keyword = decodeURI(getQueryVariable('keyword'));
	$('#search-input').val(keyword);
});
