(function($){
    $(function(){
        $(".price-box").click(function(){
            $(".price-box.selected").removeClass("selected");
            $(this).addClass("selected");
            var idplan = $(this).attr("id").split("plan");

            $("#id_plan").val(idplan[1]).change();

        });
    });
})(jQuery);