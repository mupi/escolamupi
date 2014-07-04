$(document).ready(function (){
	$('.lnk-webdesign').click(function (e) {
	  e.preventDefault();
	  /*$(this).tab('show');*/
	  $("#web-design-link").trigger("click");
	});

    var url = document.location.toString();
    if (url.match('#')) {
        jQuery('.tablist li a[href=#'+url.split('#')[1]+']').tab('show') ;
    } 

    jQuery('.tablist li a').on('shown.bs.tab', function (e) {
        window.location.hash = e.target.hash;
        window.scrollTo(0, 0);
    });
});
