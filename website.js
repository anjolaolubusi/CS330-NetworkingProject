"use strict";
//import $ from "jquery";


var Option1Count = 0;
var test;

window.onload = function init()
{
  console.log("PAGE LOADED");
}

function test(){
  console.log("Hello");
}
function clickMe()
{
    Option1Count+=1;
    console.log("YOU CLICKED IT");
    let clickLabel = document.getElementById("clickResult");
    console.log(clickLabel);
    clickLabel.innerHTML = "Selected x" + Option1Count;
    test = clickLabel.innerHTML;


// $.ajax({
//   type: "POST",
//   crossDomain: true,
//   url: "localhost:6789/echo",
//   data: test,
//   success: function(data, textStatus, jqHXR)
//   {
//     console.log("You succeeded");
//   },
//   error: function(jqHXR, textStatus, errorThrown)
//   {
//     console.log("You failed");
//   },
//   dataType: "html"
// });
}
