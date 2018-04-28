var yuming = 'http://sccs.youedata.com';
$(function(){

//banner图
$.ajax({
 	type: "post",
	data: "",
	url: yuming + '/banner/getBannerByBannerType?bannerType=04',
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

//动态发布  tab切换	
var c;
$(function() {
	$(".conAll ul:first").show();
	$(".scz-dt-tab a").css("left", function(i) {
		return -i;
	});
	$(".scz-dt-tab a").on('click', function() {
		$(this).addClass("active");
		$(this).parent().siblings().children().removeClass("active");
		c = $(this).parent().index();
		$($(".conAll ul")[c]).siblings().hide();
		$($(".conAll ul")[c]).fadeTo(200, 1);
	});
});


//活动动态-主会场 
$.ajax({
    type: "post",
    data: '',
    url:yuming+'/activity/getSCZActivityListByType?pageNum=1&pageSize=5&category=0',
    dataType: "json",
    beforeSend: function(xhr) {},
    success: function(res) {
	//	console.log(res.data.list);
		if(res.code=="200"){			
			var data = res.data.list;
			var act = '';
      for (var i = 0; i < data.length; i++){
				act+='<li><a href="articleHD.html?id='+ data[i].id +'" target="_blank"><span>●&nbsp;</span>'+data[i].title+'</a><label>'+data[i].publishTime+'</label></li>';
			}	
			$('#act1').html(act);         						
		}
    },
    error: function(xhr) {},
    complete: function (xhr) {}
});
//活动动态-部委
$.ajax({
    type: "post",
    data: '',
    url:yuming+'/activity/getSCZActivityListByType?pageNum=1&pageSize=5&category=2',
    dataType: "json",
    beforeSend: function(xhr) {},
    success: function(res) {
	//	console.log(res.data[0].list);
		if(res.code=="200"){			
			var data = res.data.list;
			var act = '';
      for (var i = 0; i < data.length; i++){
				act+='<li><a href="articleHD.html?id='+ data[i].id +'" target="_blank"><span>●&nbsp;</span>'+data[i].title+'</a><label>'+data[i].publishTime+'</label></li>';
			}	
			$('#act2').html(act);         						
		}
    },
    error: function(xhr) {},
    complete: function (xhr) {}
});
//活动动态-分会场
$.ajax({
    type: "post",
    data: '',
    url:yuming+'/activity/getSCZActivityListByType?pageNum=1&pageSize=5&category=1',
    dataType: "json",
    beforeSend: function(xhr) {},
    success: function(res) {
	//	console.log(res.data[0].list);
		if(res.code=="200"){			
			var data = res.data.list;
			var act = '';
      for (var i = 0; i < data.length; i++){
				act+='<li><a href="articleHD.html?id='+ data[i].id +'" target="_blank"><span>●</span>'+data[i].title+'</a><label>'+data[i].publishTime+'</label></li>';
			}	
			$('#act3').html(act);         						
		}
    },
    error: function(xhr) {},
    complete: function (xhr) {}
});


});
