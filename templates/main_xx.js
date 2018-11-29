function load_photo_screen(){
    $.ajax({
      type: "GET",
      url: "{{url_for('photo')}}",
      success: function(result) {
        document.getElementById("content").innerHTML=result;
      }
    });
    $.getScript( "{{url_for('static', filename='main.js')}}",
    function( data, textStatus, jqxhr ) {
      console.log( data ); // Data returned
      console.log( textStatus ); // Success
      console.log( jqxhr.status ); // 200
      console.log( "Load was performed." );
    });
}



