/**
* CF 命名空间，以项目名字开头字母大写命名的
*/
var yuming = 'http://127.0.0.1:5000';
var CF = {
    /**
     * 没有数据的情况合并td
     * @param colspanNum
     * @returns {String}
     */
    getNoDataHtml : function (colspanNum) {
        var html='<tr><td colspan="'+colspanNum+'">暂无数据</td></tr>';
        return html;
    },
    /**
     * 判断是否为ie8
     * @returns {Boolean}
     */
    isIe8 : function () {
        return navigator.appName == "Microsoft Internet Explorer" && navigator.appVersion .split(";")[1].replace(/[ ]/g,"")=="MSIE8.0";
    },
    /**
    * 获取地址栏参数
    * @param name 参数名称
    * @result 参数值
    */
    getUrlParam : function (name) {
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); // 构造一个含有目标参数的正则表达式对象
        var r = window.location.search.substr(1).match(reg); // 匹配目标参数
        if(r != null)
            return decodeURIComponent(r[2]);
        return null; // 返回参数值
    },
    /**
    * 公共的错误处理方法
    */
    errorAlert : function (code, msg) {
        switch(Number(code)) {
            case 3018:
                //dropOut();
                break;
            default:
                $.zmAlert(msg, 2000, null, "rgba(95,189,211,0.7)");
                break;
        }
    },
    /**
    * 字符截取，添加点点点
    * @param num 字符长度
    * @result {String} 截取后的字符
    */
    ellipsis : function (str, length) {
        return str.length <= length ? str : (str.substr(0, length) + '...');
    },
    /**
    * 字符截取，添加点点点
    * @param num 字符长度
    * @result {String} 截取后的字符
    */
    formatTime : function (time) {
        var date =  new Date(time);
        var y = 1900+date.getYear();
        var m = "0"+(date.getMonth()+1);
        var d = "0"+date.getDate();
        return y+"-"+m.substring(m.length-2,m.length)+"-"+d.substring(d.length-2,d.length);
    }
}

/**
 * ajax封装
 * @param params.url 发送请求的地址 /a/b.do
 * @param params.data 发送到服务器的数据，数组存储，如：{a:a,b:b} 或者 null
 * @param params.success 成功回调函数 
 * @param params.error 请求错误
 * @param params.beforeSend 请求前
 */
$.axsJson = function(params) {

    params.data = $.extend( {orgCode: '23'}, params.data|| {} );
    //params.data = params.data|| {} ;
    console.log(params.url)
    $.ajax({
        type: "get",
        data: params.data,
        url: 'http://dev.api.puxin.com' + params.url,
        dataType: "jsonp",
        timeout : 1000,
        beforeSend: function(xhr) {

            params.beforeSend && params.beforeSend(xhr);
        },
        success: function(res) {

            params.success && params.success(res);
        },
        error: function(xhr) {

            params.error && params.error(xhr);
        },
        complete: function (xhr) {

            params.complete && params.complete(xhr);
        }
    });
};



/**
 * 弹出框、确认框
 */
(function($) {
    $.extend({
        "zmAlert": function(con, time, urls) { //三个参数 内容、时间、跳转地址（如果有的话）
            if($(".zmAlert").size() == 0) {
                var box = $("<div>");
                var close = $("<button>");
                var bg = $("<div>");
                var p = $("<p>");
                box.attr("class", "zmAlert");
                bg.attr("class", "zmBg");
                close.attr("class", "zmClose");
                box.append(close);
                box.append(p);
                $("body").append(box).append(bg);
                close.unbind("click");
                close.bind("click",
                    function() {
                        box.fadeOut();
                        bg.fadeOut();
                    });
                bg.unbind("click");
                bg.bind("click",
                    function() {
                        box.fadeOut();
                        bg.fadeOut();
                    });
            }
            time == undefined ? time = 1500 : null;
            time < 1000 ? time = 1000 : null;
            time > 5000 ? time = 5000 : null;
            $(".zmAlert").show();
            $(".zmBg").first().show();
            $(".zmAlert p").html(con);
            alertBack(time, urls);
        },
        "zmConfirm": function(val, titleText, f1, f2) { //内容、标题、确认回调、取消回调
            if($(".zmConfirm").size() == 0) {
                var bg = $("<div class='zmBg'>");
                var box = $("<div class='zmConfirm'>");
                var zcTop = $("<div class='zcTop'>");
                var zcContent = $("<div class='zcContent'>");
                var zcBottom = $("<div class='zcBottom'>");
                var title = $("<p class='title'>");
                var close = $("<button class='zmclose'>");
                var sure = $("<button class='zcBtn'>确 定</button>");
                var cancel = $("<button class='zcBtn'>取 消</button>");
                bg.off("click");
                bg.on("click", function() {
                    box.fadeOut();
                    bg.fadeOut();
                });
                close.on("click", function() {
                    box.fadeOut();
                    bg.fadeOut();
                });
                zcTop.append(title).append(close);
                zcBottom.append(sure).append(cancel);
                box.append(zcTop).append(zcContent).append(zcBottom);
                $("body").append(box).append(bg);
            }
            $(".zmConfirm").show();
            $(".zmBg").first().show();
            $(".zcBottom .zcBtn").off("click");
            $(".zcContent").text(val);
            $(".zcTop .title").text(titleText);
            if(typeof(f1) == "function") {
                $(".zcBottom .zcBtn").eq(0).on("click",
                    function() {
                        $(".zmConfirm").fadeOut();
                        $(".zmBg").fadeOut();
                        f1();
                    });
            }

            $(".zcBottom .zcBtn").eq(1).on("click",
                function() {
                    if(f2 != false && typeof(f2) == "function") {
                        $(".zmConfirm").fadeOut();
                        $(".zmBg").fadeOut();
                        f2();
                    } else {
                        $(".zmConfirm").fadeOut();
                        $(".zmBg").fadeOut();
                    }
                });
        }
    });

    function alertBack(time, urls) {
        setTimeout(showAlert(urls), time);

    }

    function showAlert(urls) {
        return function() {
            showAlert(urls);
            $(".zmAlert").fadeOut();
            $(".zmBg").fadeOut();
            if(urls != undefined && urls != "") {
                window.location.href = urls;
            }

        }
    }
})(window.jQuery);
