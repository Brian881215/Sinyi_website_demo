$(document).ready(function () {
    //tab
    $("#article-flters li").on("click", function (event) {
        $("#article-flters li").removeClass("filter-active");
        $("#article-container").children(".article-item").removeClass("show animate__animated animate__fadeInRight");
        $("#article-container").children(".article-item").removeClass("hidden animate__animated animate__fadeOutRight");
        var containerpos = parseInt($("#article-flters").offset().left);
        var position1 = parseInt($("#article-flters li:first-child").offset().left) -
            containerpos;
        var position2 = parseInt($("#article-flters li:nth-child(2)").offset().left) -
            containerpos;
        var position3 = parseInt($("#article-flters li:nth-child(3)").offset().left) -
            containerpos;
        var position4 = parseInt($("#article-flters li:last-child").offset().left) -
            containerpos;
        var index = $("#article-flters li").index(this);
        console.log("this" + index);
        // console.log("container left" + containerpos);
        // console.log("position4 left" + position1);
        var thisfilter=$(this).attr("data-filter");
        switch (index) {
            case 0:
            $(this).parents("ul").siblings("span.tabitemmark").css("margin-left", position1 - 10 + "px");
            $("#article-container .article-item").addClass("show animate__animated animate__fadeInRight");
                break;
            case 1:
            $(this).parents("ul").siblings("span.tabitemmark").css("margin-left", position2 + "px");
            $("#article-container .article-item:not("+thisfilter+")").addClass("hidden animate__animated animate__fadeOutRight");
            $("#article-container .article-item"+thisfilter).addClass("show animate__animated animate__fadeInRight");;
                break;
            case 2:
            $(this).parents("ul").siblings("span.tabitemmark").css("margin-left", position3 + "px");
            $("#article-container .article-item:not("+thisfilter+")").addClass("hidden animate__animated animate__fadeOutRight");
            $("#article-container .article-item"+thisfilter).addClass("show animate__animated animate__fadeInRight");;
                break;
            case 3:
            $(this).parents("ul").siblings("span.tabitemmark").css("margin-left", position4 + "px");
            $("#article-container .article-item:not("+thisfilter+")").addClass("hidden animate__animated animate__fadeOutRight");
            $("#article-container .article-item"+thisfilter).addClass("show animate__animated animate__fadeInRight");;
                break;
            default:
            $(this).parents("ul").siblings("span.tabitemmark").css("margin-left", position1 + "px");
            // $("#article-container .article-item:not("+thisfilter+")").addClass("animate__animated animate__fadeOutRight");
            $("#article-container .article-item").addClass("show animate__animated animate__fadeInRight");;
                break;
        }
        $(this).addClass("filter-active");

        console.log("thisfilter"+thisfilter);
       
    });
});