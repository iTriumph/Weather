
var baseURL = 'http://127.0.0.1:8080';
var ResourceCreateURL = baseURL + '/ResourceCreate';//添加资源
var ResourceListURL = baseURL + '/ResourceList';//获取资源列表

/**
 * 获取参数，主要是添加上userId和SSID
 */
function getParameter(parameter){
    if (!parameter) {
        parameter = {};
    }
    return json2one(parameter, storage().get('user_info'));

}
/**
 合并两个json
 */
function json2one(des, src, override){
    if (src instanceof Array) {
        for (var i = 0, len = src.length; i < len; i++)
            json2one(des, src[i], override);
    }
    for (var i in src) {
        if (override || !(i in des)) {
            des[i] = src[i];
        }
    }
    return des;
}
