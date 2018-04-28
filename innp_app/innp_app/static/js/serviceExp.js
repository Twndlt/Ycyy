//banner图
$(function(){
	$.ajax({
	 	type: "post",
		data: "",
		url: yuming + '/banner/getBannerByBannerType?bannerType=06',
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
//中央设立政府性基金和行政事业性收费目录清单
$(function(){
	$.ajax({
        type: "post",
        data: "",
        url: yuming + '/fundsFees/getFundsFeesList?category=00',
        dataType: "json",
        beforeSend: function(xhr) {

        },
        success: function(res) {
            console.log(res)
            if (res.code="200") {
                var data = res.data;
                var html = "";
                for (var i = 0; i < data.length; i++) {
               	    var dowurl = yuming + '/fundsFees/downloadFile?id=' + data[i].id
               	    html += '<li><b>'+ data[i].title +'</b><a href="'+ dowurl +'">附件下载</a></li>';
                };
                $('#category-00-list').append(html);
            }                            
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {

            
        }
    });
});
//省（区、市）设立行政事业性收费目录清单
$(function(){
	$.ajax({
        type: "post",
        data: "",
        url: yuming + '/fundsFees/getFundsFeesList?category=01',
        dataType: "json",
        beforeSend: function(xhr) {

        },
        success: function(res) {
            console.log(res)
            if (res.code="200") {
                var data = res.data;
                var html = "";
                for (var i = 0; i < data.length; i++) {
               	    var dowurl = yuming + '/fundsFees/downloadFile?id=' + data[i].id
               	    html += '<li><b>'+ data[i].title +'</b><a href="'+ dowurl +'">附件下载</a></li>';
                };
                $('#category-01-list').append(html);
            }                            
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {

            
        }
    });
});
//省（区、市）设立涉企行政事业性收费目录清单
$(function(){
	$.ajax({
        type: "post",
        data: "",
        url: yuming + '/fundsFees/getFundsFeesList?category=02',
        dataType: "json",
        beforeSend: function(xhr) {

        },
        success: function(res) {
            console.log(res)
            if (res.code="200") {
                var data = res.data;
                var html = "";
                for (var i = 0; i < data.length; i++) {
               	    var dowurl = yuming + '/fundsFees/downloadFile?id=' + data[i].id
               	    html += '<li><b>'+ data[i].title +'</b><a href="'+ dowurl +'">附件下载</a></li>';
                };
                $('#category-02-list').append(html);
            }                            
        },
        error: function(xhr) {

            
        },
        complete: function (xhr) {

            
        }
    });
});