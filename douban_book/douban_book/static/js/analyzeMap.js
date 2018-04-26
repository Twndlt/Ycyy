$(function(){
//北京最热政策Top5   政策关注度/政策分布
$.ajax({
 	type: "post",
	data: {'area':'北京'},
	url: yuming + '/policy/getHotsByArea?limit=5',
	dataType: "json",
	success: function(res) {
	//	console.log(res);
		if(res.code == "200") {			
			var data = res.data;									
			var topFive = '';
			for(var i = 0; i < data.length; i++) {
				topFive+='<li><a href="zhengcekuDetail.html?id='+ data[i].businessId +'" target="_blank">'+ data[i].title +'</a></li>'	
		  	}
		  	$("#hotTop5Content").html(topFive);			    
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

//北京最热政策Top5   双创活跃度
$.ajax({
 	type: "post",
	data: {'area':'北京'},
	url: yuming + '/activity/getHotsByArea?limit=5',
	dataType: "json",
	success: function(res) {
		console.log(res);
		if(res.code == "200") {			
			var data = res.data;									
			var topAct = '';
			for(var i = 0; i < data.length; i++) {
				topAct+='<li><a href="articleHD.html?id='+ data[i].businessId +'" target="_blank">'+ data[i].title +'</a></li>'	
		  	}
		  	$("#hotTop5Act").html(topAct);			    
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

//点击按钮切换最热政策Top5
$('.tabTit2').on('click',function(){
	$("#hotTop5Act").removeClass("none");
	$("#hotTop5Content").addClass("none");
	$(".topTitle").text("全国最热活动Top5");
});
$('.tabTit1,.tabTit3').on('click',function(){
	$("#hotTop5Content").removeClass("none");
	$("#hotTop5Act").addClass("none");
	$(".topTitle").text("全国最热政策Top5");
});



//年度最热政策
$.ajax({
 	type: "post",
	data: "",
	url: yuming + '/policy/getHotsByCycle?limit=3&type=0',
	dataType: "json",
	success: function(res) {
	//	console.log(res);
		if(res.code == "200") {			
			var data = res.data;									
			var year = '';
			for(var i = 0; i < data.length; i++) {
				year+='<li><i></i><p><a href="zhengcekuDetail.html?id='+ data[i].businessId +'" target="_blank">'+ data[i].title +'</a></p></li>'	
		  	}
		  	$("#yearHotPolicyList").html(year);			    
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

//季度最热政策
$.ajax({
 	type: "post",
	data: "",
	url: yuming + '/policy/getHotsByCycle?limit=3&type=1',
	dataType: "json",
	success: function(res) {
	//	console.log(res);
		if(res.code == "200") {			
			var data = res.data;									
			var quarter = '';			
			for(var i = 0; i < data.length; i++) {
				var title = CF.ellipsis(data[i].title,10);	
				quarter+='<li><i></i><p><a href="zhengcekuDetail.html?id='+ data[i].businessId +'" target="_blank">'+ data[i].title +'</a></p></li>'	
		  	}
		  	$("#quarterHotPolicyList").html(quarter);			    
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

//月度最热政策
$.ajax({
 	type: "post",
	data: "",
	url: yuming + '/policy/getHotsByCycle?limit=3&type=2',
	dataType: "json",
	success: function(res) {
	//	console.log(res);
		if(res.code == "200") {			
			var data = res.data;									
			var mon = '';
			for(var i = 0; i < data.length; i++) {
				mon+='<li><i></i><p><a href="zhengcekuDetail.html?id='+ data[i].businessId +'" target="_blank">'+ data[i].title +'</a></p></li>'	
		  	}
		  	$("#monthHotPolicyList").html(mon);			    
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

//周度最热政策
$.ajax({
 	type: "post",
	data: "",
	url: yuming + '/policy/getHotsByCycle?limit=3&type=3',
	dataType: "json",
	success: function(res) {
	//	console.log(res);
		if(res.code == "200") {			
			var data = res.data;									
			var week = '';
			for(var i = 0; i < data.length; i++) {
				week+='<li><i></i><p><a href="zhengcekuDetail.html?id='+ data[i].businessId +'" target="_blank">'+ data[i].title +'</a></p></li>'	
		  	}
		  	$("#weekHotPolicyList").html(week);			    
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

});



 