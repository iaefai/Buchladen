
$(document).ready(function(e) {
    console.log("Run");
    $("#searchbox").focus(function(e) {
        $("#status").val("Search box is selected");
        console.log("selected");
    });

    $("#searchbox").blur(function(e) {
        console.log("unselected");
    });
});