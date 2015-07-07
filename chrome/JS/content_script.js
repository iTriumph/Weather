function alert_result(){
    var bodyEle = document.getElementsByTagName("body")[0];
    var boxEle = document.createElement("div");
    boxEle.id = "smile_insert_box";
    var loadingHtml = '<div id="loading">'
        + '<div class="rect1"></div>'
        + '<div class="rect2"></div>'
        + '<div class="rect3"></div>'
        + '<div class="rect4"></div>'
        + '<div class="rect5"></div>'
        + '<div class="rect6"></div>'
        + '</div>';

    var innerHtml = '<div id="close" >✖</div><div id="result">'
        + 'Page Saved'
        + '</div>'
        + '<div id="option">'
        + '<a class="" href="laoma.im" target="_blank" >Open Smile</a> | <a href="#" class="" onclick="alert(0);">Remove Page</a>'
        + '</div>';
    boxEle.innerHTML = innerHtml;
    bodyEle.appendChild(boxEle);
    document.smile_time_id = setTimeout("remove_box();", 5000);
    boxEle.onmouseover = function(){
        console.log("over");
        clearTimeout(document.smile_time_id);
        boxEle.onmouseout = function(e){
            console.log(e);
            document.smile_time_id = setTimeout("remove_box();", 5000);
        }
    }
}

function mouse_over_def(ele,timeid){
    console.log("over");
    ele.onmouseover = false;
    clearTimeout(removetime);
    ele.onmouseout = mouse_out_def

}
function mouse_out_def(timeid){
    console.log("out");
    var removetime = setTimeout("remove_box();", 5000);
}

function remove_box(){
    document.body.removeChild(document.getElementById("smile_insert_box"));
}
