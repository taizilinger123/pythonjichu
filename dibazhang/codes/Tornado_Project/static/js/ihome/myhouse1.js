$(document).ready(function(){
    $(".auth-warn").show();

    $.get("/api/house/my", function(data){
         if("4101" == data.errno){
         	location.href="/login.html";
         }else if("0" == data.errno){
         	//console.log(template("house-list-tmpl",{houses:data.houses}));
            $("#house-list").html(template("house-list-tmpl",{houses:data.houses}));
         }
    })

})     