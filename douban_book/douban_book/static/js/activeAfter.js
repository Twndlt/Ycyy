var yuming = 'http://127.0.0.1:5000';
$(function(){
//banner图
$.ajax({
 	type: "post",
	data: "",
	url: yuming + '/banner/getBannerByBannerType?bannerType=00',
	dataType: "json",
	success: function(result) {
	//	console.log(result);
		if(result.code == "200") {			
			var list = result.data[0];									
			$("#banner").html('<img src='+yuming+"/"+list.picPath+'>');			    
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

//主要活动-创想中国  
  $.ajax({
 	type: "post",
	data: "",
	url: yuming + '/activity/getCXZGActivityTops?limit=3',
	dataType: "json",
	success: function(result) {
		console.log(result);
		if(result.code == "200") {			
			var list = result.data;									
			var ccn = '';
			for(var i = 0; i < list.length; i++) {
				ccn+='<li><a href="cxzgxq.html?id='+ list[i].id +'" target="_blank">'+ list[i].title +'</a><p><em style="color:#6a6566">来源：<b>'+ list[i].source +'</b></em><i style="color:rgb(140,140,140)">'+ list[i].publishTime +'</i></p></li>'	
		  	}
		  	$("#ccn").html(ccn);			    
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

//主要活动-双创活动周
  $.ajax({
 	type: "post",
	data: "",
	url: yuming + '/activity/getSCZActivityTops?limit=3',
	dataType: "json",
	success: function(result) {
		console.log(result);
		if(result.code == "200") {			
			var list = result.data;
			var scz = '';		
			for(var i = 0; i < list.length; i++) {
				scz+='<li><a href="articleHD.html?id='+ list[i].id +'" target="_blank">'+ list[i].title +'</a><p><em style="color:#6a6566">来源：<b>'+ list[i].source +'</b></em><i style="color:rgb(140,140,140)">'+ list[i].publishTime +'</i></p></li>'	
		  	} 			 
		  	$("#scz").html(scz);		     		    	    
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
//部委
  $.ajax({
 	type: "post",
	data: "",
	url: yuming + '/activity/getActivityTypeDetailList?category=0',
	dataType: "json",
	success: function(result) {
		console.log(result);
		if(result.code == "200") {				
			var list = result.data;
			var buwei = '';	
			for(var i = 0; i < list.length; i++) {
	//		$.each(list,function(item,name){	
				buwei+='<a href="hdxq.html?id='+ list[i].id +'" target="_blank"><img src='+yuming+"/"+list[i].previewPicPath+'><p>'+list[i].title+'</p><em>'+ list[i].area +'</em></a>'
			};    			 
		    $("#buwei .ConBoxDet").html(buwei);		     		    	    
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

//地方
  $.ajax({
 	type: "post",
	data: "",
	url: yuming + '/activity/getActivityTypeDetailList?category=1',
	dataType: "json",
	success: function(result) {
	//	console.log(result);
		if(result.code == "200") {				
			var list = result.data;
			var diqu = '';	
			for(var i = 0; i < list.length; i++) {
	//		$.each(list,function(item,name){	
				diqu+='<a href="hdxq.html?id='+ list[i].id +'" target="_blank"><img src='+yuming+"/"+list[i].previewPicPath+'><p>'+list[i].title+'</p><em>'+list[i].area+'</em></a>';
			};   			 
		    $("#diqu .ConBoxDet").html(diqu);		     		    	    
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

//基地
  $.ajax({
 	type: "post",
	data: "",
	url: yuming + '/activity/getActivityTypeDetailList?category=2',
	dataType: "json",
	success: function(result) {
	//	console.log(result);
		if(result.code == "200") {				
			var list = result.data;
			var jidi = '';		
			for(var i = 0; i < list.length; i++) {
	//		$.each(list,function(item,name){	
				jidi+='<a href="hdxq.html?id='+ list[i].id +'" target="_blank"><img src='+yuming+"/"+list[i].previewPicPath+'><p>'+list[i].title+'</p><em>'+ list[i].area +'</em></a>'
			};   			 
		    $("#jidi .ConBoxDet").html(jidi);		     		    	    
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

//社会团体
  $.ajax({
 	type: "post",
	data: "",
	url: yuming + '/activity/getActivityTypeDetailList?category=3',
	dataType: "json",
	success: function(result) {
	//	console.log(result);
		if(result.code == "200") {				
			var list = result.data;
			var tuanti = '';		
			for(var i = 0; i < list.length; i++) {
	//		$.each(list,function(item,name){	
				tuanti+='<a href="hdxq.html?id='+ list[i].id +'" target="_blank"><img src='+yuming+"/"+list[i].previewPicPath+'><p>'+list[i].title+'</p><em>'+ list[i].area +'</em></a>'
			};    			 
		    $("#tuanti .ConBoxDet").html(tuanti);		     		    	    
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
