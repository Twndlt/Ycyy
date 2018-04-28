
$(function(){
//banner图
$.ajax({
 	type: "post",
	data: "",
	url: yuming + '/banner/getBannerByBannerType?bannerType=03',
	dataType: "json",
	success: function(result) {
		console.log(result);
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

//视频
	$.ajax({
    type: "post",
    data:'',
    url: yuming + '/activity/getActivityVideo',
    dataType: "json",
    beforeSend: function(xhr) {
    },
    success: function(res) {
			if(res.code=="200"){
				$('#my-video').prepend('<source src='+ res.data[0].linkUrl +' type="video/mp4" id="mp4">');
			}
    },
    error: function(xhr) {        
    },
    complete: function (xhr) {   
    }
	});



    layui.use('laypage', function(){
	    var laypage = layui.laypage;
        //活动动态  的列表
		$.ajax({
		    type: "post",
		    data: '',
		    url:yuming+'/activity/getCXZGActivityList?pageNum=1&pageSize=10',
		    dataType: "json",
		    beforeSend: function(xhr) {},
		    success: function(res) {
				console.log(res);
				if(res.code=="200"){	
					var data = res.data.list;
					var act = '';
					for (var i = 0; i < data.length; i++){
		            	var shortContent = CF.ellipsis(data[i].shortContent,170);	
		            	act+='<li><a href="cxzgxq.html?id='+ data[i].id +'" target="_blank" class="title">'+data[i].title+'</a><div class="content"><div class="img-wrapper">';
						act+='<a href="cxzgxq.html?id='+ data[i].id +'" target="_blank"><img src="'+yuming+"/"+data[i].previewPicPath+'"></a></div>';
						act+='<div class="detail"><p class="p1">'+shortContent+'</p>';
						act+='<p class="p2"><img src="images/list-time.png">';
						act+='<em>发布时间：<span>'+data[i].publishTime+'</span></em>';
				//		act+='<span>来源：<i>'+data[i].source+'</i></span>';
						act+='<p></div></div></li>';
		            }	
					$('#act').html(act);
					pageCounts = res.data.allCounts;	
						//执行一个laypage实例
						laypage.render({
						    elem: 'page', //注意，这里的 test1 是 ID，不用加 # 号
						    count: pageCounts, //数据总数，从服务端得到
						    limit: 10,
						    theme: '#2d6393',
						    jump: function(obj, first){
							    //obj包含了当前分页的所有参数，比如：
							    console.log(obj.curr); //得到当前页，以便向服务端请求对应页的数据。
							    console.log(obj.limit); //得到每页显示的条数							   
							    //首次不执行
							    if(!first){
							        $.ajax({
									    type: "post",
									    data: "",
									    url: yuming + '/activity/getCXZGActivityList?pageNum='+ obj.curr +'&pageSize='+ obj.limit +'',
									    dataType: "json",									    
									    beforeSend: function(xhr) {
									    	$('#act').empty();
									    	$('#act').append('<div class="Sdownload"><img src="images/huanchong.gif" id="huanchong"></div>');
									    	$('#page').show();
									    },
									    success: function(res) {
												console.log(res)
												if(res.code=="200"){											
													var data = res.data.list;
													var act = '';
										            for (var i = 0; i < data.length; i++){
										            	var shortContent = CF.ellipsis(data[i].shortContent,60);	
										            	act+='<li><a href="cxzgxq.html?id='+ data[i].id +'" target="_blank" class="title">'+data[i].title+'</a><div class="content"><div class="img-wrapper">';
														act+='<a href="cxzgxq.html?id='+ data[i].id +'" target="_blank"><img src="'+yuming+"/"+data[i].previewPicPath+'"></a></div>';
														act+='<div class="detail"><p class="p1">'+data[i].shortContent+'</p>';
														act+='<p class="p2"><img src="images/list-time.png">';
														act+='<em>发布时间：<span>'+data[i].publishTime+'</span></em>';
												//		act+='<span>来源：<i>'+data[i].source+'</i></span>';
														act+='<p></div></div></li>';
										            }	
													$('#act').html(act);											
												}
									    },
									    error: function(xhr) {
									    		
									        
									    },
									    complete: function (xhr) {

									        
									    }
									});
							    }
							}
						});        						
				}
		    },
		    error: function(xhr) {},
		    complete: function (xhr) {}
		});
    })


}); 