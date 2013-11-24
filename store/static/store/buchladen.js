
$(document).ready(function(e) {
    console.log("Run");


    window.onpopstate = function(e) {
        //console.log("pop state " + location);
        var note = location.hash.split("#!/")[1];
        if (note !== '') {
      //      console.log("Hashed location: " + note);
            search(note);
            $("#searchbox").val(note);
        } else {
            recent(10);
        }
    }


    $("#searchbox").focus(function(e) {
        $("#status").val("Search box is selected");
       // console.log("selected");
    });

    $("#searchbox").blur(function(e) {
       // console.log("unselected");
    });

    $('input[type=text]').on('input', function(e) {
        if ($('#searchbox').val() !== '') {
            //console.log("not empty");
            $('#clearbutton').css('visibility', 'visible');
        } else $('#clearbutton').css('visibility', 'hidden');
        //console.log("empty");
    });

    $('#searchbox').on('keyup', function(e) {
        var search_string = $("#searchbox").val();

     //   console.log("Searching for " + search_string);
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
        //console.log("Hashed location: " + note);
        search(note);
        $("#searchbox").val(note);
    }

    $('#logout').on("click", function() {
        var post = $.post("/logout", {});
        post.done(function() {
            location.reload(true);
        });

        post.fail(function(jqXHR, textStatus, errorThrown) {
                        console.log("Failed request: " + textStatus);
                        console.log(jqXHR);
                    });
    });

    // register dialog
    $('#register-dialog').dialog({
            width: 640,
            height: 400,
            modal: true,
            resizable: false,
            autoOpen: false
        });


        $('#login_form').submit(function(event) {
            event.preventDefault();
            var form = $(this);
            var username = form.find("input[name='username']").val();
            var password = form.find("input[name='password']").val();
            var url = form.attr("action");

            var posting = $.post(url, {
                username: username,
                password: password
            });

            posting.done(function(data) {
                console.log(data);
                if (data === 'redirect') {
                    location.reload(true);
                }
            });

            posting.fail(function(jqXHR, textStatus, errorThrown) {
                console.log("Failed request: " + textStatus);
                console.log(jqXHR);
            });
        });
    
    $('#post-book-dialog').dialog({
        width: 640,
        height: 400,
        modal: true,
        resizable: false,
        autoOpen: false
    });

    $('#post_book').on("click", function() {
        $('#post-book-dialog').dialog("open");
    });

    $('#post_book_form').submit(function(event) {
        event.preventDefault();
        var form = $(this);
        var title = form.find("input[name='title']").val();
        var authors = form.find("input[name='authors']").val();
        var isbn = form.find("input[name='isbn']").val();
        var subjects = form.find("input[name='subjects']").val();
        var publisher = form.find("input[name='publisher']").val();
        var price = form.find("input[name='price']").val();
        var url = form.attr("action");

        var posting = $.post(url, {
            title : title,
            authors : authors,
            isbn : isbn,
            subjects : subjects,
            publisher : publisher,
            price : price
        });

        posting.done(function(data) {
            console.log(data);
            if (data === 'redirect') {
                location.reload(true);
            }
        });

        posting.fail(function(jqXHR, textStatus, errorThrown) {
            console.log("Failed request: " + textStatus);
            console.log(jqXHR);
        });
    });

         /*   var form = $.ajax({
            url: '/login',
            type: 'GET',
            dataType: 'html',
            cache: false,
            success: function(data, textStatus, jqXHR) {
                console.log("Open dialog");
                $('#register-dialog').html(data);

                $('#login_form').submit(function(event) {
                    event.preventDefault();
                    var form = $(this);
                    var username = form.find("input[name='username']").val();
                    var password = form.find("input[name='password']").val();
                    var url = form.attr("action");

                    var posting = $.post(url, {
                        username: username,
                        password: password
                    });

                    posting.done(function(data) {
                        console.log(data);
                        if (data === 'redirect') {
                            location.reload(true);
                        }
                    });

                    posting.fail(function(jqXHR, textStatus, errorThrown) {
                        console.log("Failed request: " + textStatus);
                        console.log(jqXHR);
                    });
                });
            },
            error: function(jqXHR, textStatus, errorThrown) {
               console.log("Error received: " + textStatus);
                console.log(errorThrown);
        }});

*/
    $('#register').on("click", function() {
        $('#register-dialog').dialog("open");
    });

    if (location.hash.split("#!/")[1] === "") {
        recent(10);
    }
});

function search(text) {
    if (text === "") recent(10);
    else {
    var result = $.ajax({
        url: '/search/' + text,
        type: 'GET',
        dataType: 'json',
        success: function(data, textStatus, jqXHR) {
            //console.log("Received request: " + textStatus);
            //console.log(data);

            var d = { books: data };
            //console.log(d);
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
}

function recent(n) {
    console.log("Recent numbers!")
    var result = $.ajax({
        url: '/recent/10',
        type: 'GET',
        dataType: 'json',
        success: function(data, textStatus, jqXHR) {
            //console.log("Received request: " + textStatus);
            //console.log(data);

            var d = { books: data };
            //console.log(d);
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