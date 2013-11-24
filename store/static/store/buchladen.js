
$(document).ready(function(e) {
    console.log("Run");

    window.onpopstate = function(e) {
        //console.log("pop state " + location);
        var note = location.hash.split("#!/")[1];
        if (note !== '') {
            console.log("Hashed location: " + note);
            search(note);
            $("#searchbox").val(note);
        }
    }


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
        var search_string = $("#searchbox").val();

        console.log("Searching for " + search_string);
        // from http://stackoverflow.com/questions/5817505/is-there-any-method-to-get-url-without-query-string-in-java-script
        // get current location without query parameters
        var url = [location.protocol, '//', location.host, location.pathname].join('');
        history.pushState(null, "", [url, '#!/', search_string].join(''));
        search(search_string);
    });

    $('#clearbutton').click(function() {
        $('#searchbox').val('');
        $('#searchbox').trigger('input');
    });

    var note = location.hash.split("#!/")[1];
    if (note !== '') {
        console.log("Hashed location: " + note);
        search(note);
        $("#searchbox").val(note);
    }


});

function search(text) {
    var result = $.ajax({
        url: '/search/' + text,
        type: 'GET',
        dataType: 'json',
        success: function(data, textStatus, jqXHR) {
            console.log("Received request: " + textStatus);
            console.log(data);

            var d = { books: data };
            console.log(d);
            var template = $('#search_template').html();
            var output = Mustache.render(template, d);
            //console.log(output);
            $('#main_content').html(output);

        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log("Error received: " + textStatus);
            console.log(errorThrown);
        }});
}