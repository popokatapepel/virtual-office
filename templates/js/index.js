function load_photo_screen(){
    $.ajax({
      type: "GET",
      url: "{{url_for('photo')}}",
      success: function(result) {
        document.getElementById("content").innerHTML=result;
      }
    });
    $.getScript( "{{url_for('render_js', jsname='photo.js')}}",
    function( data, textStatus, jqxhr ) {
      console.log( textStatus ); // Success
      console.log( jqxhr.status ); // 200
      console.log( "Load was performed." );
    });
}

function load_todo_screen(){
    $.ajax({
      type: "GET",
      url: "{{url_for('todoList')}}",
      success: function(result) {
        document.getElementById("content").innerHTML=result;
      }
    });
    $.getScript( "{{url_for('render_js', jsname='todos.js')}}",
    function( data, textStatus, jqxhr ) {
      console.log( textStatus ); // Success
      console.log( jqxhr.status ); // 200
      console.log( "Load was performed." );
    });
}

function load_upload_screen(){
    $.ajax({
      type: "GET",
      url: "{{url_for('upload')}}",
      success: function(result) {
        document.getElementById("content").innerHTML=result;
      }
    });
}




