function handleCBchange(cb, id) {

    $.ajax({
        type: "POST",
        url: window.location,
        data:{
            todoid: id,
            done: cb.checked
             }
}).then(function(data){
    console.log(data)
});

}