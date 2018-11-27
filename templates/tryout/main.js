setTimeout("main()", 5000);

function main(){
console.log("hallo janniklas");
var str="<h2>London</h2><p>London is the capital city of England.</p><p>It is the most populous city in the United Kingdom, with a metropolitan area of over 13 million inhabitants.</p>"
london_div=document.getElementById("london");
london_div.innerHTML=str;
}
