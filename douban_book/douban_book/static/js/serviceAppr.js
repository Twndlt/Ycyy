//banner图
$(function(){
	$.ajax({
	 	type: "post",
		data: "",
		url: yuming + '/banner/getBannerByBannerType?bannerType=07',
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


//动态切换
var ct;
$(function(){
   $(".apprRight:first").show();
   $(" .sort-item span").css("left",function(it){ return -it});
   $(" .sort-item span").on('click',function(){
       $(this).parent().addClass("on");
	   $(this).parent().siblings().removeClass("on");
	   ct =  $(this).parent().index();
	   $($(".rightAll .apprRight")[ct]).siblings().hide();
	   $($(".rightAll .apprRight")[ct]).fadeTo(200,1);
   });
});
var category = '00';
var dept = '';
//左侧数据
$(function(){
	$.ajax({
        type: "post",
        data: "",
        url: yuming + '/policy/getDeptList',
        dataType: "json",
        async: false,
        beforeSend: function(xhr) {

        },
        success: function(res) {
            console.log(res)
            if (res.code="200") {
                var data = res.data;
                var html = "";
                for (var i = 0; i < data.length; i++) {
                	html += '<li id='+ data[i].organizationid +' class="zhengce-list-li"><a>'+ data[i].organizationname +'</a></li>';
                };
                $('#fieldName-list').append(html);
                $('.zhengce-list-li').eq(0).addClass('active');
                 
                $('.zhengce-list-li').click(function(){
                	dept = $(this).attr('id');
                	$(this).addClass('active').siblings().removeClass('active');

                	$('#search-btn2').click();
                	 
                });          

            }                            
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {

            
        }
    });
   

    //======================
    $('#quxiao').click(function(){
    	var keyword = $.trim($('#service-search-input').val());
		category = '00';
		dept = '';
		$('.zhengce-list-li').eq(0).addClass('active').siblings().removeClass('active');
		search2(keyword);
	});
	$('#xiafang').click(function(){
		var keyword = $.trim($('#service-search-input').val());
		category = '01';
		dept = '';
		$('.zhengce-list-li').eq(0).addClass('active').siblings().removeClass('active');
		search2(keyword);
	});
	$('#search-btn2').click( function(){	 
		var keyword = $.trim($('#service-search-input').val());
		search2(keyword);
	});

    //=====初始化============================
    $('#search-btn2').click();
})

layui.use('laypage', function(){
	var laypage = layui.laypage;

    window.search2 = function(keyword){
    	 
    	 $.ajax({
		    type: "post",
		    data: {'category':category,'keyword':keyword,'dept':dept,'pageNum':1,'pageSize':10},
		    url: yuming + '/cancelDelegateMatter/getCancelDelegateMatterListByCondition',
		    dataType: "json",
		    beforeSend: function(xhr) {
		    	$('#zhengce-list').empty();
		    	$('#zhengce-list').append('<img src="images/huanchong.gif" id="huanchong" style="width: 30px;height: 30px;position: absolute;top: 50%;margin-top: -15px;left: 50%;margin-left: -15px;">');
		    	$('#page').show();
		    },
		    success: function(res) {
					console.log(res)
					if(res.code=="200"){
						var html = "";
						var data = res.data.list;
						if(data.length==0){
	                      $('#zhengce-list').append('<div style="text-align:center;margin-top:30px;padding-bottom:30px;"><img src="images/no_data_icon.png" style="display:inline-block;"></div>');
	                      $('#page').hide();
	                      return;
	                    }
						if (category=="01") {
							html = '<tr>'+
									'<th width="12%">序号</th>'+
									'<th width="40%">项目名称</th>'+
									'<th width="24%">审批部门</th>'+
									'<th width="24%">处理决定</th>'+
								'</tr>';
							$('#zhengce-list').append(html);
							for (var i = 0; i < data.length; i++) {							
								html =  '<tr>'+
											'<td>'+ (i+1) +'</td>'+
											'<td class="tl">'+ data[i].projectName +'</td>'+
											'<td>'+ data[i].approveDept +'</td>'+
											'<td>'+ data[i].decision +'</td>'+
										'</tr>';
								$('#zhengce-list').append(html);		
							}							
						}else{
							html = '<tr>'+
									'<th width="12%">序号</th>'+
									'<th width="56%">项目名称</th>'+
									'<th width="32%">审批部门</th>'+
								'</tr>';
							$('#zhengce-list').append(html);
							for (var i = 0; i < data.length; i++) {							
								html =  '<tr>'+
											'<td>'+ (i+1) +'</td>'+
											'<td class="tl">'+ data[i].projectName +'</td>'+
											'<td>'+ data[i].approveDept +'</td>'+
										'</tr>';
								$('#zhengce-list').append(html);		
							}
						}
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
									    data: {'category':category,'dept':dept,'keyword':keyword,'pageNum':obj.curr,'pageSize':obj.limit},
		                                url: yuming + '/cancelDelegateMatter/getCancelDelegateMatterListByCondition',
									    dataType: "json",
									    beforeSend: function(xhr) {
									    	$('#zhengce-list').empty();
									    	$('#zhengce-list').append('<img src="images/huanchong.gif" id="huanchong" style="width: 30px;height: 30px;position: absolute;top: 50%;margin-top: -15px;left: 50%;margin-left: -15px;">');
									    },
									    success: function(res) {
												console.log(res)
												var html = "";
						                        var data = res.data.list;
												if (category=="01") {
													html = '<tr>'+
															'<th width="12%">序号</th>'+
															'<th width="40%">项目名称</th>'+
															'<th width="24%">审批部门</th>'+
															'<th width="24%">处理决定</th>'+
														'</tr>';
													$('#zhengce-list').append(html);
													for (var i = 0; i < data.length; i++) {							
														html =  '<tr>'+
																	'<td>'+ (i+1) +'</td>'+
																	'<td class="tl">'+ data[i].projectName +'</td>'+
																	'<td>'+ data[i].approveDept +'</td>'+
																	'<td>'+ data[i].decision +'</td>'+
																'</tr>';
														$('#zhengce-list').append(html);		
													}							
												}else{
													html = '<tr>'+
															'<th width="12%">序号</th>'+
															'<th width="56%">项目名称</th>'+
															'<th width="32%">审批部门</th>'+
														'</tr>';
													$('#zhengce-list').append(html);
													for (var i = 0; i < data.length; i++) {							
														html =  '<tr>'+
																	'<td>'+ (i+1) +'</td>'+
																	'<td class="tl">'+ data[i].projectName +'</td>'+
																	'<td>'+ data[i].approveDept +'</td>'+
																'</tr>';
														$('#zhengce-list').append(html);		
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
		    },
		    error: function(xhr) {

		        
		    },
		    complete: function (xhr) {
		    	$('#huanchong').remove();		        
		    }
		});
    }
});