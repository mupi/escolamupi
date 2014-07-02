jQuery(document).ready(function (){
	jQuery('.lnk-webdesign').click(function (e) {
	  e.preventDefault();
	  /*$(this).tab('show');*/
	  jQuery("#web-design-tab").trigger("click");
	})
})