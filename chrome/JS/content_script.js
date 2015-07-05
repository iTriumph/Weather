function alert_result(){
    alert("ok");
    var bodyEle = document.getElementsByTagName("body")[0];
    var boxEle = document.createElement("div");
    boxEle.id = "smile_insert_box";
    var innerHtml = '<div id="result">'
        + 'ok'
        + '</div>';
    boxEle.innerHTML = innerHtml;
    bodyEle.appendChild(boxEle);
}
