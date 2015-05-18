function save_page(info, tab){
    console.log(info);
    chrome.tabs.executeScript(null, {code:"document.body.bgColor='red'"});
}

function save_image(info, tab){
    console.log(info);
}

var parent = chrome.contextMenus.create({"title": "Save", "onclick":save_page});
var id = chrome.contextMenus.create({"title": "Save Image", "contexts":["image"], "onclick":save_image});
