(function ($) {

  // preload object array to gain performance
  var $headers = $('.header')
  
  // run at resize
  $( window ).resize(function() {
    $.fn.setHeaderHeight(0);   
  });  

  $.fn.setHeaderHeight = function(height) {

    // reset to auto or else we can't check height
    $($headers).css({ 'height': 'auto' });
    
    // get highest value
    $($headers).each(function(i, obj) {    
      height = Math.max(height, $(obj).outerHeight()) 
    });

    // set new height
    $($headers).css({ 'height': height + 'px' });    
  }

  // run at load
  $.fn.setHeaderHeight(0);
  
}(jQuery));