$(document).ready(function () {

    $("body").append('<div id="loading_indicator">Loading...</div>');

    $("#loading_indicator").css({
        display: "none",
        margin: "0px",
        paddingLeft: "0px",
        paddingRight: "0px",
        paddingTop: "0px",
        paddingBottom: "0px",
        position: "absolute",
        right: "50%",
        top: "3px",
        width: "200px",
        height: "30px",
        border: "1px dotted #E6E65C",
        background: "#FFFF66"
    });

    $(document).ajaxStart(function () {
        $("#loading_indicator").show();
    }).ajaxStop(function () {
        $("#loading_indicator").hide();
    });

    $("#runbtn").click(function (event) {
        $.post("/report/", $("#qbeform").serialize())
        .done(function (data) {
            var report_data = $(data).find("#reporttbl");
            var errors = $(data).find("#reportfor");

            $("#reporttbl").empty().append(report_data);
            $("#reportfor").empty().append(errors);
        })
        .fail(function (xhr, errmsg, err) {
            $("#reportfor_err").html("<div class='errorlist'>" + err + "</div>");
            console.log(xhr.status + ": " + xhr.responseText);
        });
    });
})
