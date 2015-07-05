function save_page(info, tab){
    console.log(info);
    chrome.tabs.executeScript(null, {code:"document.body.bgColor='red'"});
}

function save_image(info, tab){
    console.log(info);
}

<<<<<<< HEAD
function save_video(info, tab){
    console.log(info);
}

var contextMenusText = chrome.contextMenus.create({"title": "Save",
    "contexts":["page", "frame", "selection", "link", "editable"],
    "onclick":save_page});

var contextMenusImage = chrome.contextMenus.create({"title": "Save Image",
    "contexts":["image"], "onclick":save_image});

var contextMenusVedio = chrome.contextMenus.create({"title": "Save Vedio",
    "contexts":["video"], "onclick": save_video});

chrome.browserAction.onClicked.addListener(function(tab){
    chrome.tabs.insertCSS(null, {file: "/Static/content_css.css"});
    chrome.tabs.executeScript(null, {file: "/JS/content_script.js"});
    chrome.tabs.executeScript(null, {code: "alert_result();"});
});
=======
var parent = chrome.contextMenus.create({"title": "Save", "onclick":save_page});
var id = chrome.contextMenus.create({"title": "Save Image", "contexts":["image"], "onclick":save_image});
>>>>>>> 7710d9b27fe9d8cc98e3ad5d1494c5159ae4a4f1
