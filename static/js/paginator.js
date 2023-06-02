function loadPage(pageNumber) {
  
    $.ajax({
      url: '/franchise/detail?page=' + pageNumber,
      type: 'GET',
      success: function(response) {
        $('franchise_detail').html(response);
      },
      error: function(error) {
        console.log(error);
      }
    });
  }
 