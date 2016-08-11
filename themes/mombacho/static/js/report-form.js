$(document).ready(function (){

  var url_params = get_params();

  if (typeof url_params['message'] == 'string') {
    modal.open({content: '<img src="/theme/img/loading.gif" alt="Cargando"/>'});
    $('#modal-content').empty();
    $('#modal-content').html('<div class="message">' + url_params['message'] + '</div>');
  }

  // Search callback
  $('#report').bind('click',function(e){

    // Avoiding reload of page after form submit
    e.preventDefault();

    if(!$("#searchlink").hasClass("open")){
       $("#searchlink").addClass("open");
       $('#searchlink .fa-search').addClass('fa-times');
       $('#searchlink .fa-search').removeClass('fa-search');
       $('#report').hide();
    }

    // Define modal
    modal.open({content: '<img src="/theme/img/loading.gif" alt="Cargando"/>'});
    $('#modal-content').html(
      $('#modal-content').load('contact.html')
    )

    $.get('/contact.html', function(result) {
        $('#modal-content').val(result);
        // Obtain parameters from url
        var url_params = get_params();
        if (typeof url_params.ruta !== 'undefined') {
          bus_number = 'la ruta ' + url_params.ruta;
        }
        else {
          bus_number = "ninguna ruta";
        }
        $('#route-number').val(bus_number);
        $('#route-number-text').html(bus_number);
    });
  });
});
