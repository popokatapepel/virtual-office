document.querySelector("#createButton").onclick = function() {
    docId = document.querySelector("#createButton").getAttribute("docId")
    $.ajax({
        type: "GET",
        url: "/createTodo?id="+docId,
        success: function() {
            window.location.href = "/todoList";
        }
    })
}

function handleCBchange(cb, id) {

    $.ajax({
        type: "POST",
        url: "{{url_for(todoList)}}",
        data:{
            todoid: id,
            done: cb.checked
             }
}).then(function(data){
    console.log(data)
});

}