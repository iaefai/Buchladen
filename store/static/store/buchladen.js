
$(document).ready(function(e) {
    console.log("Run");
    $("#searchbox").focus(function(e) {
        $("#status").val("Search box is selected");
        console.log("selected");
    });

    $("#searchbox").blur(function(e) {
        console.log("unselected");
    });

    $('input[type=text]').on('input', function(e) {
        if ($('#searchbox').val() !== '') {
            //console.log("not empty");
            $('#clearbutton').css('visibility', 'visible');
        } else $('#clearbutton').css('visibility', 'hidden');
        //console.log("empty");
    });

    $('input[type=text]').on('keyup', function(e) {
        // if (e.which == 13) {
        {   e.preventDefault();
            console.log("Send request: " + $("#searchbox").val());

            var result = $.ajax({
                url: '/search/' + $("#searchbox").val(),
                type: 'GET',
                dataType: 'json',
                success: function(data, textStatus, jqXHR) {
                    console.log("Received request: " + textStatus);
                    console.log(data);

                    var d = { books: data };
                    console.log(d);
                    var template = $('#search_template').html();
                    var output = Mustache.render(template, d);
                    console.log(output);
                    $('#main_content').html(output);

                },
                error: function(jqXHR, textStatus, errorThrown) {
                    console.log("Error received: " + textStatus);
                    console.log(errorThrown);
                }});
        };
    });

    $('#clearbutton').click(function() {
        $('#searchbox').val('');
        $('#searchbox').trigger('input');
    });


});

function search(text) {


}