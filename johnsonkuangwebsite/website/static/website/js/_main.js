/*! viewportSize | Author: Tyson Matanich, 2013 | License: MIT */
(function(n){n.viewportSize={},n.viewportSize.getHeight=function(){return t("Height")},n.viewportSize.getWidth=function(){return t("Width")};var t=function(t){var f,o=t.toLowerCase(),e=n.document,i=e.documentElement,r,u;return n["inner"+t]===undefined?f=i["client"+t]:n["inner"+t]!=i["client"+t]?(r=e.createElement("body"),r.id="vpw-embeds-b",r.style.cssText="overflow:scroll",u=e.createElement("div"),u.id="vpw-embeds-d",u.style.cssText="position:absolute;top:-1000px",u.innerHTML="<style>@media("+o+":"+i["client"+t]+"px){body#vpw-embeds-b div#vpw-embeds-d{"+o+":7px!important}}<\/style>",r.appendChild(u),i.insertBefore(r,e.head),f=u["offset"+t]==7?i["client"+t]:n["inner"+t],i.removeChild(r)):f=n["inner"+t],f}})(this);

$(document).ready(function () {
	console.log("reached");
	var $heightDiv = $('.about-slide-img');
	$('.about-displacer-div').height($('.about-slide-img').scrollHeight);
	console.log($heightDiv.height());
});
$(document).ready(function () {
	var height = document.getElementById('#about-image').offsetHeight;
	console.log(height);
})

$(function(){
		skrollr.init({
		forceHeight: false
	});
});