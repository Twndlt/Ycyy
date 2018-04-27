$(function(){
	function slider(m,y,tt){
        // 滑动特效
		var startX = 0, startY = 0; //触摸开始时手势横纵坐标 
        var temPos; //滚动元素当前位置
        var iCurr = 0; //当前滚动屏幕数
        var oPosition = {}; //触点位置
        var num = 2;
        var clone=m.children('li').first().clone();
        var ww =  parseInt(m.children('li').css('width')); 
        m.append(clone);
        var size =  m.children('li').size();
        //左滑
        function move_left(){
			iCurr++;
	        if(iCurr==size){
	           m.css({left:0});
	            iCurr=1;
	        }
	        m.stop().animate({left:-iCurr*ww},400);
	        if(iCurr==size-1){
	            y.eq(0).addClass("on").siblings().removeClass("on");
	            tt.eq(0).addClass("active").siblings().removeClass("active");
	        }
	        else{
	            y.eq(iCurr).addClass("on").siblings().removeClass("on");
	            tt.eq(iCurr).addClass("active").siblings().removeClass("active");
	        }
		}
		// 右滑
		function move_right(){
			iCurr--;
	        if(iCurr==-1){
	            m.css({left:-(size-1)*ww});
	            iCurr=size-2;
	        }
	        m.stop().animate({left:-iCurr*ww},400);
	        y.eq(iCurr).addClass("on").siblings().removeClass("on");
	        tt.eq(iCurr).addClass("active").siblings().removeClass("active");
		}
		var t = setInterval(move_left,3800);
		if (m.selector == '.erweima-wrap .list-wrap') {
			clearInterval(t);
		}
		m.hover(function(){
			clearInterval(t);
		},function(){
			t = setInterval(move_left,3800);
			if (m.selector == '.erweima-wrap .list-wrap') {
				clearInterval(t);
			}
		})
		// 划入小圆点
		y.hover(function(){
			m.stop().animate({left:-($(this).index())*ww},400);
			$(this).addClass('on').siblings().removeClass('on');
            tt.eq($(this).index()).addClass("active").siblings().removeClass("active");
			clearInterval(t);
		},function(){
			t = setInterval(move_left,3800);
			if (m.selector == '.erweima-wrap .list-wrap') {
				clearInterval(t);
			}
		})
		// 划入按钮
		$('#index-prev').hover(function(){
			clearInterval(t);
		},function(){
			t = setInterval(move_left,3800);
		})
		$('#index-next').hover(function(){
			clearInterval(t);
		},function(){
			t = setInterval(move_left,3800);
		})
		//按钮点击
		$('#index-prev').on('click',function(){			
			move_right();			
		})
		$('#index-next').on('click',function(){
			move_left();	
		})
    }
    // 双创服务选项卡
    $('#fuwu-tab .tab-btn').each(function(){
    	$(this).on('click',function(){
    		$(this).addClass('active').siblings().removeClass('active');
    		$('#fuwu-content>div').eq($(this).index()).addClass('active').siblings().removeClass('active');
    	})
    })
    // 双创活动选项卡
    $('#schd-tab .tab-btn').each(function(){
    	$(this).on('click',function(){
    		$(this).addClass('active').siblings().removeClass('active');
    	})
    })
    // 查询首页banner轮播图
    $.ajax({
        type: "post",
        data: "",
        url: yuming + '/homePage/getBanners?limit=4',
        dataType: "json",
        beforeSend: function(xhr) {

        },
        success: function(res) {
 			console.log(res,'lunbo');
 			if(res.code=="200"){
 				var html1 = '';
 				var html2 = '';
                var data = res.data;
                for (var i = 0; i < data.length; i++) {
                	var title = CF.ellipsis(data[i].title,36);
                    html1 += '<li><a href="dtxq.html?id='+ data[i].id +'" target="_blank"><img src='+yuming+"/"+data[i].imagePaths.split(";")[0]+' class="lunbotu" ></a></li>';
                    html2 += '<li><a href="dtxq.html?id='+ data[i].id +'" target="_blank">'+ title +'</a></li>'
                }
 				$('#index-slider-body').append(html1);
 				$('#index-title-ul').append(html2);
 				$('#index-title-ul li').eq(0).addClass('active');
                $('#index-title-ul li').each(function(){
                //    console.log($(this).height())                   
                //    $(this).css('margin-top',-$(this).height()/2);
                })
 				slider($('#index-slider-body'),$('#index-focus span'),$('#index-title-ul li'));
 				
 			}
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {

            
        }
    });
    // 查询网站收录各类资源总数
    $.ajax({
        type: "post",
        data: "",
        url: yuming + '/homePage/getResourcesTotalCounts',
        dataType: "json",
        beforeSend: function(xhr) {

        },
        success: function(res) {
 			console.log(res)
 			if(res.code=="200"){
 				$('#shoulu-item1').append('<label class="label1">'+ res.data[0].totalCount +'条</label><label class="label2">'+ res.data[0].resourcesName +'</label>');
 				$('#shoulu-item2').append('<label class="label1">'+ res.data[1].totalCount +'条</label><label class="label2">'+ res.data[1].resourcesName +'</label>');
 				$('#shoulu-item3').append('<label class="label1" style="margin-left:24px">'+ res.data[2].totalCount +'家</label><label class="label2">'+ res.data[2].resourcesName +'</label>');
 			}
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {

            
        }
    });
    //专题专栏 全面创新改革试验
    $.ajax({
        type: "post",
        data: "",
        url: yuming + '/homePage/getInnovationExperimentTopNews?limit=3',
        dataType: "json",
        beforeSend: function(xhr) {
            $('#qcg-index').append('<img src="images/huanchong.gif" id="huanchong">');
            $('#qcg-index').css('position','relative');
        },
        success: function(res) {
            console.log(res)
            if(res.code=="200"){
                var html = "";
                var data = res.data;
                for (var i = 0; i < data.length; i++) {
                    html += '<li><a href="qcgxq.html?id='+ data[i].id +'" target="_blank"><span>●</span> '+ data[i].title +'</a></li>'; 
                }
                $('#qcg-index').append(html);
            }
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {
            $('#huanchong').remove();           
        }
    });
    //专题专栏 战略性新兴产业
    $.ajax({
        type: "post",
        data: "",
        url: yuming + '/homePage/getNewIndustryTopNews?limit=3',
        dataType: "json",
        timeout: 10000,
        beforeSend: function(xhr) {            
            $('#zxx-index').append('<img src="images/huanchong.gif" id="huanchong">');
        },
        success: function(res) {
            console.log(res)
            if(res.code=="200"){
                var html = "";
                var data = res.data;
                for (var i = 0; i < data.length; i++) {
                    html += '<li><a href="zxxxq.html?id='+ data[i].id +'" target="_blank"><span>●</span> '+ data[i].title +'</a></li>'; 
                }
                $('#zxx-index').append(html);
            }
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {
            $('#huanchong').remove();
        }
    });
    $.ajax({
        type: "post",
        data: "",
        url: yuming + '/activity/getSCZActivityTops?limit=5',
        dataType: "json",
        beforeSend: function(xhr) {
            $('#schd-list').append('<img src="images/huanchong.gif" id="huanchong">');
        },
        success: function(res) {
            console.log(res,'scz')
            if(res.code=="200"){
                var html = '';
                var data = res.data;
                for (var i = 0; i < data.length; i++) {
                    var shortContent = CF.ellipsis(data[i].title,30);
                    html += '<li>'+
                               ' <a href="javascript:;">'+
                                    '<div class="img-wrapper"><a href="articleHD.html?id='+ data[i].id +'" class="detail" target="_blank"><img src="'+yuming+data[i].picPath.split(";")[0]+'"></a></div>'+
                                    '<a href="articleHD.html?id='+ data[i].id +'" class="detail" target="_blank"><p class="content">'+ shortContent +'</p></a>'+
                                '</a>'+
                            '</li>';
                };
                $('#schd-list').append(html);
            }
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {
            $('#huanchong').remove();
            
        }
    });
    //活动跟踪双创周
    $('#schd-scz').on('click',function(){
        $.ajax({
            type: "post",
            data: "",
            url: yuming + '/activity/getSCZActivityTops?limit=5',
            dataType: "json",
            beforeSend: function(xhr) {
                $('#schd-list').empty();
                $('#schd-list').append('<img src="images/huanchong.gif" id="huanchong">');
            },
            success: function(res) {
                console.log(res,'scz')
                if(res.code=="200"){
                    var html = '';
                    var data = res.data;
                    for (var i = 0; i < data.length; i++) {
                        var shortContent = CF.ellipsis(data[i].title,30);
                        html += '<li>'+
                                   ' <a href="javascript:;">'+
                                        '<div class="img-wrapper"><a href="articleHD.html?id='+ data[i].id +'" class="detail" target="_blank"><img src="'+yuming+data[i].picPath.split(";")[0]+'"></a></div>'+
                                        '<a href="articleHD.html?id='+ data[i].id +'" class="detail" target="_blank"><p class="content">'+ shortContent +'</p></a>'+
                                    '</a>'+
                                '</li>';
                    };
                    $('#schd-list').append(html);
                }
            },
            error: function(xhr) {

                
            },
            complete: function (xhr) {
                $('#huanchong').remove();
                
            }
        });
    });
    //活动跟踪创想中国
    $('#schd-cxzg').on('click',function(){
        $.ajax({
            type: "post",
            data: "",
            url: yuming + '/activity/getCXZGActivityTops?limit=5',
            dataType: "json",
            beforeSend: function(xhr) {
                $('#schd-list').empty();
                $('#schd-list').append('<img src="images/huanchong.gif" id="huanchong">');
            },
            success: function(res) {
                console.log(res,'scz')
                if(res.code=="200"){
                    var html = '';
                    var data = res.data;
                    for (var i = 0; i < data.length; i++) {
                        var shortContent = CF.ellipsis(data[i].title,30);
                        html += '<li>'+
                                   ' <a href="javascript:;">'+
                                        '<div class="img-wrapper"><a href="cxzgxq.html?id='+ data[i].id +'" class="detail" target="_blank"><img src="'+yuming+data[i].picPath.split(";")[0]+'"></a></div>'+
                                        '<a href="cxzgxq.html?id='+ data[i].id +'" class="detail" target="_blank"><p class="content">'+ shortContent +'</p></a>'+
                                    '</a>'+
                                '</li>';
                    };
                    $('#schd-list').append(html);
                }
            },
            error: function(xhr) {

                
            },
            complete: function (xhr) {
                $('#huanchong').remove();
                
            }
        });
    });
    var areaFlagId = '0';
    //最新政策部委点击
    $('#xinzheng-buwei').on('click',function(){
        $(this).addClass('active').siblings().removeClass('active');
        areaFlagId = '0';
        $.ajax({
            type: "post",
            data: "",
            url: yuming + '/policy/getNeastPolicys?areaFlagId=0&limit=2',
            dataType: "json",
            beforeSend: function(xhr) {
                $('#xinzheng-list').empty();
                $('#xinzheng-list').append('<img src="images/huanchong.gif" id="huanchong">');
            },
            success: function(res) {
                console.log(res,'zxzc');
                if(res.code=="200"){
                    var data = res.data;
                    var html = "";
                    for (var i = 0; i < data.length; i++) {
                        var shortContent = CF.ellipsis(data[i].shortContent,80);
                        html += '<li>'+
                                    '<a href="zhengcekuDetail.html?id='+ data[i].id +'" target="_blank">'+
                                        '<div class="right">'+
                                            '<p class="p1">'+ data[i].titile +'</p>'+
                                            '<p class="p2">'+ shortContent +'</p>'+
                                            '<p class="p3"><label class="label1">发布单位：'+ data[i].source +'</label><label class="label2">'+ data[i].pubTime +'</label></p>'+
                                        '</div>'+
                                    '</a>'+
                                '</li>';
                    }
                    $('#xinzheng-list').append(html);
                }
            },
            error: function(xhr) {
                console.log(xhr)
                
            },
            complete: function (xhr) {
                $('#huanchong').remove();
                
            }
        });  
    })
    //最新政策地方点击
    $('#xinzheng-difang').on('click',function(){
        $(this).addClass('active').siblings().removeClass('active');
        areaFlagId = '1';
        $.ajax({
            type: "post",
            data: "",
            url: yuming + '/policy/getNeastPolicys?areaFlagId=1&limit=2',
            dataType: "json",
            beforeSend: function(xhr) {
                $('#xinzheng-list').empty();
                $('#xinzheng-list').append('<img src="images/huanchong.gif" id="huanchong">');
            },
            success: function(res) {
                console.log(res,'zxzc');
                if(res.code=="200"){
                    var data = res.data;
                    var html = "";
                    for (var i = 0; i < data.length; i++) {
                        var shortContent = CF.ellipsis(data[i].shortContent,80);
                        html += '<li>'+
                                    '<a href="zhengcekuDetail.html?id='+ data[i].id +'" target="_blank">'+
                                        '<div class="right">'+
                                            '<p class="p1">'+ data[i].titile +'</p>'+
                                            '<p class="p2">'+ shortContent +'</p>'+
                                            '<p class="p3"><label class="label1">发布单位：'+ data[i].source +'</label><label class="label2">'+ data[i].pubTime +'</label></p>'+
                                        '</div>'+
                                    '</a>'+
                                '</li>';
                    }
                    $('#xinzheng-list').append(html);
                }
            },
            error: function(xhr) {
                console.log(xhr)
                
            },
            complete: function (xhr) {
                $('#huanchong').remove();
                
            }
        });  
    });
    //最新政策更多点击
    $('#zxzc-more-link').on('click',function(){
        window.location.href = 'zhengceku.html?areaFlagId='+ areaFlagId +'';
    })
})
//最新动态部委
$(function(){
    $.ajax({
        type: "post",
        data: "",
        url: yuming + '/dynamic/getDynamicTopsByCondition?type=0&limit=2',
        dataType: "json",
        beforeSend: function(xhr) {
            $('#buwei-list').append('<img src="images/huanchong.gif" id="huanchong">');
        },
        success: function(res) {
            console.log(res,'buwei');
            if(res.code=="200"){
                var data = res.data;
                var html = "";
                for (var i = 0; i < data.length; i++) {
                    var shortContent = CF.ellipsis(data[i].shortContent,60);
                    html += '<li>'+
                                '<a href="dtxq.html?id='+ data[i].id +'" target="_blank">'+
                                    '<div class="left"><img src="'+yuming+data[i].imagePaths.split(';')[0]+'"></div>'+
                                    '<div class="right">'+
                                        '<p class="p1">'+ data[i].title +'</p>'+
                                        '<p class="p2">'+ shortContent +'</p>'+
                                        '<p class="p3"><label class="label1">来源：'+ data[i].source +'</label><label class="label2">'+ data[i].pubtime +'</label></p>'+
                                    '</div>'+
                                '</a>'+
                            '</li>';
                }
                $('#buwei-list').append(html);
            }
        },
        error: function(xhr) {
            console.log(xhr)
            
        },
        complete: function (xhr) {
            $('#huanchong').remove();
            
        }
    });
})
//最新动态基地
$(function(){
   $.ajax({
        type: "post",
        data: "",
        url: yuming + '/dynamic/getDynamicTopsByCondition?type=2&limit=4',
        dataType: "json",
        beforeSend: function(xhr) {
            $('#jidi-list').append('<img src="images/huanchong.gif" id="huanchong">');
        },
        success: function(res) {
            console.log(res,'jidi');
            if(res.code=="200"){
                var html;
                var data = res.data;
                for (var i = 0; i < data.length; i++) {
                    if(i==0){
                        var shortContent = CF.ellipsis(data[i].title,25);
                        html = '<div class="detail">'+
                                    '<a href="dtxq.html?id='+ data[i].id +'" target="_blank">'+
                                        '<div class="left"><img src="'+yuming+data[i].imagePaths.split(";")[0]+'"></div>'+
                                        '<div class="right">'+
                                            '<p class="p1">'+ shortContent +'</p>'+
                                            '<p class="p2"><span>'+ data[i].pubtime +'</span></p>'+
                                        '</div>'+
                                    '</a>'+                
                                '</div>';
                        $('#jidi-list').append(html);
                    }else{
                        html = '<li>'+
                                    '<a href="dtxq.html?id='+ data[i].id +'" target="_blank">'+
                                        '<div class="img-wrapper"><img src="images/list_arrow_icon.png"></div>'+
                                        '<p class="content">'+ data[i].title +'</p>'+
                                        '<span class="date">'+ data[i].pubtime +'</span>'+
                                    '</a>'+
                                '</li>';
                        $('#jidi-list').append(html);
                    }
                };
            }
        },
        error: function(xhr) {
            console.log(xhr)
            
        },
        complete: function (xhr) {
            $('#huanchong').remove();
            
        }
    }); 
})
    
//最新动态社会团体
$(function(){
   $.ajax({
        type: "post",
        data: "",
        url: yuming + '/dynamic/getDynamicTopsByCondition?type=3&limit=4',
        dataType: "json",
        beforeSend: function(xhr) {
            $('#shtt-list').append('<img src="images/huanchong.gif" id="huanchong">');
        },
        success: function(res) {
            console.log(res,'jidi');
            if(res.code=="200"){
                var html;
                var data = res.data;
                for (var i = 0; i < data.length; i++) {
                    if(i==0){
                        var shortContent = CF.ellipsis(data[i].title,25);
                        html = '<div class="detail">'+
                                    '<a href="dtxq.html?id='+ data[i].id +'" target="_blank">'+
                                        '<div class="left"><img src="'+yuming+data[i].imagePaths.split(";")[0]+'"></div>'+
                                        '<div class="right">'+
                                            '<p class="p1">'+ shortContent +'</p>'+
                                            '<p class="p2"><span>'+ data[i].pubtime +'</span></p>'+
                                        '</div>'+
                                    '</a>'+                
                                '</div>';
                        $('#shtt-list').append(html);
                    }else{
                        html = '<li>'+
                                    '<a href="dtxq.html?id='+ data[i].id +'" target="_blank">'+
                                        '<div class="img-wrapper"><img src="images/list_arrow_icon.png"></div>'+
                                        '<p class="content">'+ data[i].title +'</p>'+
                                        '<span class="date">'+ data[i].pubtime +'</span>'+
                                    '</a>'+
                                '</li>';
                        $('#shtt-list').append(html);
                    }
                };
            }
        },
        error: function(xhr) {
            console.log(xhr)
            
        },
        complete: function (xhr) {
            $('#huanchong').remove();
            
        }
    }); 
})
//最新动态地方
$(function(){
   $.ajax({
        type: "post",
        data: "",
        url: yuming + '/dynamic/getDynamicTopsByCondition?type=1&limit=4',
        dataType: "json",
        beforeSend: function(xhr) {
            $('#difang-list').append('<img src="images/huanchong.gif" id="huanchong">');
        },
        success: function(res) {
            console.log(res,'difang');
            if(res.code=="200"){
                var html;
                var data = res.data;
                for (var i = 0; i < data.length; i++) {
                    if(i==0){
                        var shortContent = CF.ellipsis(data[i].title,25);
                        html = '<div class="detail">'+
                                    '<a href="dtxq.html?id='+ data[i].id +'" target="_blank">'+
                                        '<div class="left"><img src="'+yuming+data[i].imagePaths.split(";")[0]+'"></div>'+
                                        '<div class="right">'+
                                            '<p class="p1">'+ shortContent +'</p>'+
                                            '<p class="p2"><span>'+ data[i].pubtime +'</span></p>'+
                                        '</div>'+
                                    '</a>'+                
                                '</div>';
                        $('#difang-list').append(html);
                    }else{
                        html = '<li>'+
                                    '<a href="dtxq.html?id='+ data[i].id +'" target="_blank">'+
                                        '<div class="img-wrapper"><img src="images/list_arrow_icon.png"></div>'+
                                        '<p class="content">'+ data[i].title +'</p>'+
                                        '<span class="date">'+ data[i].pubtime +'</span>'+
                                    '</a>'+
                                '</li>';
                        $('#difang-list').append(html);
                    }
                };
            }
        },
        error: function(xhr) {
            console.log(xhr)
            
        },
        complete: function (xhr) {
            $('#huanchong').remove();
            
        }
    }); 
})
//最新政策部委
$(function(){
    $.ajax({
        type: "post",
        data: "",
        url: yuming + '/policy/getNeastPolicys?areaFlagId=0&limit=2',
        dataType: "json",
        beforeSend: function(xhr) {
            $('#xinzheng-list').append('<img src="images/huanchong.gif" id="huanchong">');
        },
        success: function(res) {
            console.log(res,'zxzc');
            if(res.code=="200"){
                var data = res.data;
                var html = "";
                for (var i = 0; i < data.length; i++) {
                    var shortContent = CF.ellipsis(data[i].shortContent,80);
                    html += '<li>'+
                                '<a href="zhengcekuDetail.html?id='+ data[i].id +'" target="_blank">'+
                                    '<div class="right">'+
                                        '<p class="p1">'+ data[i].titile +'</p>'+
                                        '<p class="p2">'+ shortContent +'</p>'+
                                        '<p class="p3"><label class="label1">发布单位：'+ data[i].source +'</label><label class="label2">'+ data[i].pubTime +'</label></p>'+
                                    '</div>'+
                                '</a>'+
                            '</li>';
                }
                $('#xinzheng-list').append(html);
            }
        },
        error: function(xhr) {
            console.log(xhr)
            
        },
        complete: function (xhr) {
            $('#huanchong').remove();
            
        }
    });  
})
//月度政策热点
$(function(){
    $.ajax({
        type: "post",
        data: "",
        url: yuming + '/policy/getHotsByCycle?limit=5&type=2',
        dataType: "json",
        beforeSend: function(xhr) {
            $('#zhengce-hot-list').append('<img src="images/huanchong.gif" id="huanchong">');
        },
        success: function(res) {
            console.log(res,'ydrd');
            if(res.code=="200"){
                var data = res.data;
                var html;
                for (var i = 0; i < data.length; i++) {
                    if (i==0) {
                        html = '<li>'+
                                    '<a href="zhengcekuDetail.html?id='+ data[i].businessId +'" target="_blank">'+
                                        '<div class="img-wrapper"><img src="images/hot1.png"></div>'+
                                        '<p class="content">'+ data[i].title +'</p>'+
                                    '</a>'+
                                '</li>';
                        $('#zhengce-hot-list').append(html);
                    }else if(i==1){
                        html = '<li>'+
                                    '<a href="zhengcekuDetail.html?id='+ data[i].businessId +'" target="_blank">'+
                                        '<div class="img-wrapper"><img src="images/hot2.png"></div>'+
                                        '<p class="content">'+ data[i].title +'</p>'+
                                    '</a>'+
                                '</li>';
                        $('#zhengce-hot-list').append(html);
                    }else if(i==2){
                        html = '<li>'+
                                    '<a href="zhengcekuDetail.html?id='+ data[i].businessId +'" target="_blank">'+
                                        '<div class="img-wrapper"><img src="images/hot3.png"></div>'+
                                        '<p class="content">'+ data[i].title +'</p>'+
                                    '</a>'+
                                '</li>';
                        $('#zhengce-hot-list').append(html);
                    }else{
                        html = '<li>'+
                                    '<a href="zhengcekuDetail.html?id='+ data[i].businessId +'" target="_blank">'+
                                        '<div class="img-text-wrapper">'+ (i+1) +'</div>'+
                                        '<p class="content">'+ data[i].title +'</p>'+
                                    '</a>'+
                                '</li>'
                        $('#zhengce-hot-list').append(html);
                    }
                }
               
            }
        },
        error: function(xhr) {
            console.log(xhr)
            
        },
        complete: function (xhr) {
             $('#huanchong').remove();
            
        }
    });
})
   