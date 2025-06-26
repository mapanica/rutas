var modal = (function(){
  var
  method = {},
  $modal,
  $content,
  $close;

  // Open the modal
  method.open = function (settings) {
      $content.empty().append(settings.content);
      if(!$("#modal").hasClass("expanded")){
         $("#modal").addClass("expanded");
      }

  };

  // Close the modal
  method.close = function () {
    if($("#modal").hasClass("expanded")){
       $("#modal").removeClass("expanded");
    }
    $content.empty();
  };

  $modal = $('<div id="modal"></div>');
  $content = $('<div id="modal-content"></div>');
  $close = $('<a id="modal-close" href="#">close</a>');

  $modal.append($content);

  $(document).ready(function(){
    $('body').append($modal);
  });

  $close.click(function(e){
    e.preventDefault();
    method.close();
  });

  return method;
}());
