$(document).ready(function() {
    M.AutoInit();    

    $('.sidenav').sidenav();
    // Resize Screen 
    window.onload = function(){
        
        if($(window).width() <= 900){
            $("#grid").removeClass('row').addClass('column');
        }else{
            $("#grid").removeClass('column').addClass('row');            
        }

    }

    window.onresize = function(event) {
        
        if($(window).width() <= 900){
            $("#grid").removeClass('row').addClass('column');         
        }
        else{
            $("#grid").removeClass('column').addClass('row');                    
        }
    };

});