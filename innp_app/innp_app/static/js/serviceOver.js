//查询双创时间轴列表
$(function(){
	$.ajax({
        type: "post",
        data: "",
        url: yuming + '/policy/getTimeStageList',
        dataType: "json",
        beforeSend: function(xhr) {

        },
        success: function(res) {
            console.log(res)
            if (res.code == "200") {
            	var data = res.data;
            	var html = "";
            	for (var i = 0; i < data.length; i++) {
            		html += '<a href="zhengceku.html?timeStageId='+ data[i].id +'" class="soBanner'+ (i+1) +'" >'+ data[i].timestagename +'</a>';
            	}
            	$('#soBanner').append(html);
            }
            
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {

            
        }
    });
});
//查询办事指南列表
$(function(){
	$.ajax({
        type: "post",
        data: "",
        url: yuming + '/guidance/getGuidanceList',
        dataType: "json",
        beforeSend: function(xhr) {

        },
        success: function(res) {
            console.log(res)
            if (res.code == "200") {
            	var data = res.data;
                var html = "";
                for (var i = 0; i < data.length; i++) {
                    var shortContent = CF.ellipsis(data[i].shortContent,220);
                    html += '<li class="listCon">'+
                                '<div class="listBox">'+
                                    '<a href="bsznxq.html?id='+ data[i].id +'">'+ data[i].title +'</a>'+
                                    '<div class="detailAll">'+
                                        '<div class="listDetail">'+
                                            '<p>'+ shortContent +'</p>'+
                                            '<em>发布时间：'+ data[i].pubtime +'</em><span>来源：<i>'+ data[i].source +'</i></span>'+
                                        '</div>'+
                                    '</div>'+
                                '</div>'+                  
                           ' </li>';
                };
                $('#banshizhinan').append(html);
            }
            
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {

            
        }
    });
});
//查询小微企业扶持政策id
$(function(){
    $.ajax({
        type: "post",
        data: "",
        url: yuming + '/policy/getSmallCompanyInfo',
        dataType: "json",
        beforeSend: function(xhr) {

        },
        success: function(res) {
            console.log(res)
            if (res.code == "200") {
                $('#xiaoweiqiye').click(function(){
                    window.location.href = 'zhengceku.html?businessPeopleId='+ res.data.id +''
                })
            }
            
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {

            
        }
    });
});