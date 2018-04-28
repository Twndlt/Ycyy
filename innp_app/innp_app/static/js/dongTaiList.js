
//右侧分类
$(function(){
	$('.rightMenu a').on('click',function(){
		$(this).addClass('condCur');
		$('.rightMenu h3').removeClass("condCur");
	});
	$('.rightMenu h3 , .rightMenu b , .rightMenu em').on('click',function(){
		$(".rightMenu h3").addClass('condCur');
		$('.rightMenu a').removeClass("condCur");
	});
})

function getQueryVariable(variable){
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i=0;i<vars.length;i++) {
           var pair = vars[i].split("=");
           if(pair[0] == variable){return pair[1];}
    }
    return('');
};

var type = $.trim(getQueryVariable('type'));
 
var category = '';
var areaId = '';
var socialGroup = '';
$(function(){
     switch(type){

     	case '0':
     	  $('#buwei-dt').children('a').addClass('current');
     	  $('#leixing-all').children('a').removeClass('current');
     	  break;
     	case '1':
     	  $('#difang-dt').children('a').addClass('current');
     	  $('#leixing-all').children('a').removeClass('current');
     	  break;
     	case '2':
     	  $('#jidi-dt').children('a').addClass('current');
     	  $('#leixing-all').children('a').removeClass('current');
     	  break;
     	case '3':
     	  $('#shtt-dt').children('a').addClass('current');
     	  $('#leixing-all').children('a').removeClass('current');
     	  break;

     	 // default:
     	 //    type = "";
     	 //     break;
          
     }
});



layui.use('laypage', function(){
    var laypage = layui.laypage;	
	
    window.dongtaiList = function(areaId,type){
    	$.ajax({
            type: "post",
            data: "",
            url: yuming + '/dynamic/getDynamicListByCondition?type='+ type +'&category='+ category +'&pageNum=1&pageSize=10&areaId='+ areaId +'&socialGroup='+ socialGroup +'',
            dataType: "json",
            beforeSend: function(xhr) {
                $('#dtlist').empty();
                $('#dtlist').append('<img src="images/huanchong.gif" id="huanchong" style="width: 30px;height: 30px;position: absolute;top: 50%;margin-top: -15px;left: 50%;margin-left: -15px;">');
                $('#page').show();
            },
            success: function(res) {
                console.log(res);
                if (res.code=="200") {
                    var data = res.data.list;
                    if(data.length==0){
                      $('#dtlist').append('<div style="text-align:center;margin-top:30px;padding-bottom:30px;"><img src="images/no_data_icon.png" style="display:inline-block;"></div>');
                      $('#page').hide();
                      return;
                    }
                    var html;
                    var shortContent;
                    var flag;
                    for (var i = 0; i < data.length; i++) {
                    	shortContent = CF.ellipsis(data[i].shortContent,150);                       
						if(data[i].imagePaths==null || data[i].imagePaths==""){
					        flag = "";
						}else{
							flag = '<a href="dtxq.html?id='+ data[i].id +'" target="_blank" style="float:left;padding:0;"><img src="'+yuming+ data[i].imagePaths.split(";")[0] +'"></a>';
						}
 						html = '<div class="listBox">'+
										'<a href="dtxq.html?id='+ data[i].id +'" target="_blank">'+ data[i].title +'</a>'+
										'<div class="detailAll">'+
											''+ flag +''+
											'<div class="listDetail">'+
												'<p>'+ shortContent +'</p>'+
												'<em>发布时间：'+ data[i].pubtime +'</em><span>来源：<i>'+ data[i].source +'</i></span>'+
											'</div>'+
										'</div>'+
									'</div>';
						$('#dtlist').append(html);
                    };
                    var allCounts = res.data.allCounts;
                    //调用分页
				    laypage.render({
					    elem: 'page', //注意，这里的 test1 是 ID，不用加 # 号
					    count: allCounts, //数据总数，从服务端得到
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
							        url: yuming + '/dynamic/getDynamicListByCondition?type='+ type +'&category='+ category +'&pageNum='+ obj.curr +'&pageSize='+ obj.limit +'&areaId='+ areaId +'&socialGroup='+ socialGroup +'',
							        dataType: "json",
							        beforeSend: function(xhr) {
							        	$('#dtlist').empty();
							        	$('#dtlist').append('<img src="images/huanchong.gif" id="huanchong" style="width: 30px;height: 30px;position: absolute;top: 50%;margin-top: -15px;left: 50%;margin-left: -15px;">');
							        },
							        success: function(res) {
							 			console.log(res)
							 			if(res.code=="200"){
							 				var data = res.data.list;
						                    var html;
						                    var shortContent;
						                    var flag;
						                    for (var i = 0; i < data.length; i++) {
						                    	shortContent = CF.ellipsis(data[i].shortContent,150);                       
												if(data[i].imagePaths==null || data[i].imagePaths==""){
											        flag = "";
												}else{
													flag = '<a href="dtxq.html?id='+ data[i].id +'" target="_blank" style="float:left;padding:0;"><img src="'+yuming+data[i].imagePaths.split(";")[0] +'"></a>';
												}
						 						html = '<div class="listBox">'+
																'<a href="dtxq.html?id='+ data[i].id +'" target="_blank">'+ data[i].title +'</a>'+
																'<div class="detailAll">'+
																	''+ flag +''+
																	'<div class="listDetail">'+
																		'<p>'+ shortContent +'</p>'+
																		'<em>发布时间：'+ data[i].pubtime +'</em><span>来源：<i>'+ data[i].source +'</i></span>'+
																	'</div>'+
																'</div>'+
															'</div>';
												$('#dtlist').append(html);
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
//页面初始化
$(function(){
	dongtaiList(areaId,type);
});
//加载地方动态列表
$(function(){
	//汉语拼音首字母排序的方法
	function pySegSort(arr,empty) {
	    if(!String.prototype.localeCompare)
	        return null;
	     
	     var letters ="*ABCDEFGHJKLMNOPQRSTWXYZ".split('');
         var zh ="阿把苍大峨发噶哈级喀啦吗那哦爬祁然三他哇西呀咋".split('');
	     
	    var segs = [];
	    var curr;
	    $.each(letters, function(i){
	        curr = {letter: this, data:[],letter_index: i};
	        $.each(arr, function() {

	            if((!zh[i-1] || zh[i-1].localeCompare(this.areaName,'zh') <= 0) && this.areaName.localeCompare(zh[i],'zh') == -1) {
	                curr.data.push(this);
	                // console.log(this)
	            }else{
	            	if(i==23){
	            		if((!zh[i-1] || zh[i-1].localeCompare(this.areaName,'zh') <= 0) && (this.areaName.localeCompare(zh[i],'zh') == -1 || this.areaName.localeCompare(zh[i],'zh') == 1)) {
			                curr.data.push(this);
			            }
	            	}
	            }
	        });
	        if(empty || curr.data.length) {
	            segs.push(curr);
	            curr.data.sort(function(a,b){ 
	                return a.areaName.localeCompare(b.areaName,'zh');
	            });
	        }
	    });
	    return segs;

	};
	$.ajax({
	    type: "post",
	    data: "",
	    url: yuming + '/policy/getFilterDictData',
	    dataType: "json",
	    beforeSend: function(xhr) {

	    },
	    success: function(res) {
				console.log(res)
				if(res.code=="200"){
					data = res.data.areaList;
					var areaArray = [];
					for (var i = 0; i < data.length; i++) {
						areaArray.push(data[i]);
					};
					var newAreaArray = pySegSort(areaArray);					
					for (var i = 0; i < newAreaArray.length; i++) {
				    	$('#city-list').append('<li style="position:relative;padding-left:10px;text-align:left;"><label style="position:absolute;left:0;top:7px;">'+ newAreaArray[i].letter +'</label></li>');
				    	for (var j = 0; j < newAreaArray[i].data.length; j++) {				
				    		$('#city-list li').eq(i).append('<b id="'+ newAreaArray[i].data[j].id +'" class="filter-item-a">'+ newAreaArray[i].data[j].areaName +'</b>');				    		;
				    	}
				    };
					$('#city-list b').click(function(){
						var areaId0 = $(this).attr('id');
						socialGroup = '';
						type = 1;
						$('#city-list').css('color','#2b2b2b');
						$('#city-list b').removeClass('on');
						$(this).addClass('on');
						$('#shtt-text').text('社会团体');
						$('#dfdt-text').text($(this).text());
						dongtaiList(areaId0,'1');
					})
				}
	    },
	    error: function(xhr) {

	        
	    },
	    complete: function (xhr) {

	        
	    }
	});
})

$(function(){
	//全部点击
	$('#leixing-all').click(function(){
		type = '';
		areaId = '';
        socialGroup = '';
        $('#dfdt-text').text('地方动态');
        $('#shtt-text').text('社会团体');
		dongtaiList(areaId,type);
	})
	//社会团体点击
	$('.group-item').click(function(){
		type = 3;
		areaId = '';
		socialGroup = $(this).attr('data-value');
		$('#shtt-text').text($(this).text());
		$('#dfdt-text').text('地方动态');
		$(this).addClass('on').siblings().removeClass('on');
		dongtaiList(areaId,type);
	});
	//部委动态点击
	$('#buwei-dt').click(function(){
		type = 0;
		areaId = '';
        socialGroup = '';
        $('#dfdt-text').text('地方动态');
        $('#shtt-text').text('社会团体');
		dongtaiList(areaId,type);
	});
	//基地动态点击
	$('#jidi-dt').click(function(){
		type = 2;
		areaId = '';
        socialGroup = '';
        $('#dfdt-text').text('地方动态');
        $('#shtt-text').text('社会团体');
		dongtaiList(areaId,type);
	});
	//全部分类
	$('#fenlei,#fenlei-all').click(function(){
		category = '';
		dongtaiList(areaId,type);
	});
	//动态咨询
	$('#dtzx').click(function(){
		category = 0;
		dongtaiList(areaId,type);
	});
	//政策动态
	$('#zcdt').click(function(){
		category = 1;
		dongtaiList(areaId,type);
	});

	$(".dt-tab-ul li").click(function(){

       $(this).children('a').addClass("current");
       $(this).siblings().children('a').removeClass("current");
    });
	

	
})





