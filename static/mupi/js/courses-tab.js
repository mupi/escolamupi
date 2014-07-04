$(document).ready(function (){
	$('.lnk-webdesign').click(function (e) {
	  e.preventDefault();
	  /*$(this).tab('show');*/
	  $("#web-design-link").trigger("click");
	})
})