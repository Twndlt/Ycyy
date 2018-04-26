//专题-战新
var c;
$(function() {
	$(".AGcon ul:first").show();
	$(".AGtabs li a").css("left", function(i) {
		return -i;
	})
	$(".AGtabs li a").on('click', function() {
		$(this).addClass("AGcur");
		$(this).parent().siblings().children().removeClass("AGcur");
		c = $(this).parent().index();
		$($(".AGcon ul")[c]).siblings().hide();
		$($(".AGcon ul")[c]).fadeTo(200, 1);
	});
});

//banner图
$(function(){
$.ajax({
 	type: "post",
	data: "",
	url: yuming + '/banner/getBannerByBannerType?bannerType=02',
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
});

//  页码 分页  begin
layui.use('laypage', function(){
	var laypage = layui.laypage;
	window.leftRequest = function(category){
		$.ajax({
		    type: "post",
		    data: "",
		    url: yuming + '/newIndustry/getNewsList?pageNum=1&pageSize=9&category='+ category +'',
		    dataType: "json",
		    beforeSend: function(xhr) {
		    	$('#ztdt-list').empty();
		    	$('#page').show();
		    },
		    success: function(res) {
					console.log(res)
					if(res.code=="200"){															
						var data = res.data.list;
						for (var i = 0; i < data.length; i++) {
							var html = '<li><a href="zxxxq.html?id='+ data[i].id +'" target="_blank">'+ data[i].title +'</a><i>'+ data[i].pubTime +'</i></li>';
							$('#ztdt-list').append(html);
						}
						var pc = res.data.allCounts;
						if (pc > 9) {
							//执行一个laypage实例
							laypage.render({
							    elem: 'page', //注意，这里的 test1 是 ID，不用加 # 号
							    count: pc, //数据总数，从服务端得到
							    limit: 9,
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
									        url: yuming + '/newIndustry/getNewsList?pageNum='+ obj.curr +'&pageSize='+ obj.limit +'&category='+ category +'',
									        dataType: "json",
									        timeout: 10000,
									        beforeSend: function(xhr) {
									            $('#ztdt-list').empty();    
									            $('#zxx-index').append('<img src="images/huanchong.gif" id="huanchong">');
									        },
									        success: function(res) {
									            console.log(res)
									            if(res.code=="200"){
									                var data = res.data.list;
													for (var i = 0; i < data.length; i++) {
														var html = '<li><a href="zxxxq.html?id='+ data[i].id +'" target="_blank">'+ data[i].title +'</a><i>'+ data[i].pubTime +'</i></li>';
														$('#ztdt-list').append(html);
													}											
									            }
									        },
									        error: function(xhr) {

									            
									        },
									        complete: function (xhr) {
									            $('#huanchong').remove();
									        }
									    });
								    }
								}
							});
						}else{
							$('#page').hide();
						}
																
					}
		    },
		    error: function(xhr) {

		        
		    },
		    complete: function (xhr) {

		        
		    }
		});
	}
	
	leftRequest(2)
	
	$.ajax({
	    type: "post",
	    data: "",
	    url: yuming + '/newIndustry/getPolicyNewsList?pageNum=1&pageSize=10',
	    dataType: "json",
	    beforeSend: function(xhr) {

	    },
	    success: function(res) {
				console.log(res)
				if(res.code=="200"){															
					var data = res.data.list;
					for (var i = 0; i < data.length; i++) {
						var html = '<li><a href="zxxxq.html?id='+ data[i].id +'" target="_blank">'+ data[i].title +'</a><i>'+ data[i].pubTime +'</i></li>';
						$('#zczx-list').append(html);
					}
					var pc = res.data.allCounts;
					if (pc > 10) {
						//执行一个laypage实例
						laypage.render({
						    elem: 'page4', //注意，这里的 test1 是 ID，不用加 # 号
						    count: pc, //数据总数，从服务端得到
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
								        url: yuming + '/newIndustry/getPolicyNewsList?pageNum='+ obj.curr +'&pageSize='+ obj.limit +'',
								        dataType: "json",
								        timeout: 10000,
								        beforeSend: function(xhr) {
								            $('#zczx-list').empty();    
								            $('#zxx-index').append('<img src="images/huanchong.gif" id="huanchong">');
								        },
								        success: function(res) {
								            console.log(res)
								            if(res.code=="200"){
								                var data = res.data.list;
												for (var i = 0; i < data.length; i++) {
													var html = '<li><a href="zxxxq.html?id='+ data[i].id +'" target="_blank">'+ data[i].title +'</a><i>'+ data[i].pubTime +'</i></li>';
													$('#zczx-list').append(html);
												}											
								            }
								        },
								        error: function(xhr) {

								            
								        },
								        complete: function (xhr) {
								            $('#huanchong').remove();
								        }
								    });
							    }
							}
						});
					}
															
				}
	    },
	    error: function(xhr) {

	        
	    },
	    complete: function (xhr) {

	        
	    }
	});
	//中央快讯,部委讯息,地方报道
	$('#zykx,#bwxx,#dfbd').on('click',function(){
		$(this).children('a').addClass('AGcur');
		$(this).siblings().children('a').removeClass('AGcur');
		var category = $(this).attr('data-value');
		leftRequest(category);
	});	
});
