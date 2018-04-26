 function imgCenter(obj,w,h){
    var pw = $(obj).width();
    var ph = $(obj).height();
    var w = $(obj).parent().width();
    var h = $(obj).parent().height();

    if (pw<w||ph<h) {
        if (pw/ph>w/h) {
            $(obj).css('height','100%');
            pw = $(obj).width();
            $(obj).css({'left':'50%','margin-left':-pw/2});
        }else{
            $(obj).css('width','100%');
            ph = $(obj).height();
            $(obj).css({'top':'50%','margin-top':-ph/2});
        };
    }else{     
        $(obj).css({'top':'50%','margin-top':-ph/2});
        $(obj).css({'left':'50%','margin-left':-pw/2});
    } 
}
