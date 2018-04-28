//banner图
$(function(){
	$.ajax({
	 	type: "post",
		data: "",
		url: yuming + '/banner/getBannerByBannerType?bannerType=05',
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
 //请求详情
function rightDetail(id,obj){
    $.ajax({
        type: "post",
        data: "",
        url: yuming + '/taxPolicy/getTaxPolicyDetail?id='+ id +'',
        dataType: "json",
        beforeSend: function(xhr) {
            obj.empty();
            obj.append('<img src="images/huanchong.gif" id="huanchong">');
        },
        success: function(res) {
            console.log(res)
            if (res.code == '200') {
                var data = res.data;
                if(data.length==0){
                 obj.append('<div style="text-align:center;margin-top:30px;padding-bottom:30px;"><img src="images/no_data_icon.png" style="display:inline-block;"></div>');
                  return;
                }
                var html =  '<tr>'+
                                '<th class="th1">优惠政策</th>'+
                                '<th class="th2">'+ data.title +'</th>'+
                            '</tr>';
                obj.append(html);
                var num = 1;
                while(data['fieldName'+num] != undefined && data['fieldName'+num] != ""){                            
                    if (num%2 == 0) {
                        html = '<tr>'+
                                       ' <td>'+ data['fieldName'+num] +'</td>'+
                                        '<td class="pl">'+ data['fieldValue'+num] +'</td>'+
                                    '</tr>';
                        obj.append(html);
                    }else{
                         html = '<tr class="bg">'+
                                       ' <td>'+ data['fieldName'+num] +'</td>'+
                                        '<td class="pl">'+ data['fieldValue'+num] +'</td>'+
                                    '</tr>';
                        obj.append(html);
                    }
                    num++;                         
                };
            }
            
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {
            $('#huanchong').remove();
        }
    });
}




//请求左侧标题
    function leftTitle(category,type,obj){
        console.log(category,type);
        $.ajax({
            type: "post",
            data: "",
            url: yuming + '/taxPolicy/getTaxPolicyList?category='+ category +'&type='+ type +'',
            dataType: "json",
            beforeSend: function(xhr) {
                obj.siblings('.subnav').empty();
                
            },
            success: function(res) {
                console.log(res)
                if (res.code == '200') {
                    var data = res.data;
                    var html = "";
                    for (var i = 0; i < data.length; i++) {
                        html += '<li><a href="javascript:;" id="'+ data[i].id +'" class="sub-title">'+ data[i].title +'</a></li>'
                    }
                    obj.siblings('.subnav').append(html);
                }
                $('.sub-title').click(function(){
                    var id = $(this).attr('id');
                    $(this).parent().addClass('active').siblings().removeClass('active');
                    rightDetail(id,$('#detail-table'))
                })
                
            },
            error: function(xhr) {

                
            },
            complete: function (xhr) {

            }
        });
    }
//交互效果
$(function(){
     
	$('.yhzccx-shoufengqin-list .link').each(function(){
    	$(this).on('click',function(){
    		$(this).parent().siblings().find('.subnav').slideUp();
			$(this).siblings('.subnav').slideToggle();
            $(this).parent().siblings().find('.link').removeClass('active');
            $(this).toggleClass('active');
            var category = $(this).attr('data-category');
            var type = $(this).attr('data-type');
            leftTitle(category,type,$(this));
    	})
    });
    $('#yhzccx-sort .sort-item').each(function(){
    	$(this).on('click',function(){
    		$(this).addClass('on').siblings().removeClass('on');
            $('.yhzccx-shoufengqin-list').eq($(this).index()).addClass('active').siblings().removeClass('active');
    	})
    });
    $('#zck-search').on('focus',function(){
        if ($(this).val()=="") {
    		$('#ph-span').show();
    	}else{
    		$('#ph-span').hide();
    	}
    });
    $('#zck-search').on('blur',function(){
    	if ($(this).val()=="") {
    		$('#ph-span').show();
    	}		    	
    });
    $('#zck-search').on('keydown',function(){		    	
    	$('#ph-span').hide();		    		    	
    });
    $('#ph-span').on('click',function(){
    	$('#zck-search').focus();
    });
   
    //点击初创期
    $('#chuchuang').on('click',function(){
        $.ajax({
            type: "post",
            data: "",
            url: yuming + '/taxPolicy/getTaxPolicyList?category=00&type=00',
            dataType: "json",
            beforeSend: function(xhr) {
                $('#chuchuang-tl1').empty();
            },
            success: function(res) {
                console.log(res)
                if (res.code="200") {
                    var id = res.data[0].id;
                    rightDetail(id,$('#detail-table'));
                    var data = res.data;
                    var html = "";
                    for (var i = 0; i < data.length; i++) {
                        html += '<li><a href="javascript:;" id="'+ data[i].id +'">'+ data[i].title +'</a></li>'
                    };
                    $('#chuchuang-tl1').append(html);
                    $('#chuchuang-tl1').siblings('.link').addClass('active');
                    $('#chuchuang-tl1 li').eq(0).addClass('active');
                }                            
            },
            error: function(xhr) {

                
            },
            complete: function (xhr) {

                
            }
        });
    });
    //点击成长期
    $('#chengzhang').on('click',function(){
        $.ajax({
            type: "post",
            data: "",
            url: yuming + '/taxPolicy/getTaxPolicyList?category=01&type=10',
            dataType: "json",
            beforeSend: function(xhr) {
                $('#chengzhang-tl1').empty();
            },
            success: function(res) {
                console.log(res);
                if (res.code=="200") {
                    var id = res.data[0].id;
                    rightDetail(id,$('#detail-table'));
                    var data = res.data;
                    var html = "";
                    for (var i = 0; i < data.length; i++) {
                        html += '<li><a href="javascript:;" id="'+ data[i].id +'">'+ data[i].title +'</a></li>'
                    };
                    $('#chengzhang-tl1').append(html);
                    $('#chengzhang-tl1').siblings('.link').addClass('active');
                    $('#chengzhang-tl1 li').eq(0).addClass('active');
                }
            },
            error: function(xhr) {

                
            },
            complete: function (xhr) {

                
            }
        });
    });
    //点击成熟期
    $('#chengshu').on('click',function(){
        $.ajax({
            type: "post",
            data: "",
            url: yuming + '/taxPolicy/getTaxPolicyList?category=02&type=20',
            dataType: "json",
            beforeSend: function(xhr) {
                $('#chengshu-tl1').empty();
            },
            success: function(res) {
                console.log(res);
                if (res.code=="200") {
                    var id = res.data[0].id;
                    rightDetail(id,$('#detail-table'));
                    var data = res.data;
                    var html = "";
                    for (var i = 0; i < data.length; i++) {
                        html += '<li><a href="javascript:;" id="'+ data[i].id +'" class="sub-title">'+ data[i].title +'</a></li>'
                    };
                   
                    $('#chengshu-tl1').append(html);
                    $('#chengshu-tl1').siblings('.link').addClass('active');
                    $('#chengshu-tl1 li').eq(0).addClass('active');
                    $('.sub-title').click(function(){
                        var id = $(this).attr('id');
                        rightDetail(id,$('#detail-table'))
                    });
                }                            
            },
            error: function(xhr) {

                
            },
            complete: function (xhr) {

                
            }
        });
    });
})
//页面加载时默认加载初创期-小微企业税收优惠-第一个标题的数据
$(function(){
    $.ajax({
        type: "post",
        data: "",
        url: yuming + '/taxPolicy/getTaxPolicyList?category=00&type=00',
        dataType: "json",
        beforeSend: function(xhr) {
           
        },
        success: function(res) {
            console.log(res,'1111')         
            if (res.code == '200') {
                var id = res.data[0].id;
                rightDetail(id,$('#detail-table'));
                var data = res.data;
                var html = "";
                for (var i = 0; i < data.length; i++) {
                    html += '<li><a href="javascript:;" id="'+ data[i].id +'" class="sub-title">'+ data[i].title +'</a></li>'
                };
                
                $('#chuchuang-tl1').append(html).show();
                $('#chuchuang-tl1').siblings('.link').addClass('active');
                $('#chuchuang-tl1 li').eq(0).addClass('active');
                $('.sub-title').click(function(){
                    $(this).parent().addClass('active').siblings().removeClass('active');
                    var id = $(this).attr('id');
                    rightDetail(id,$('#detail-table'));
                });
            }           
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {
            
            
        }
    });
});

