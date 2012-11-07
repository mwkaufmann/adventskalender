$(window).load(function(){

  // make the opened doors clickable
  $(".day").each(function() {
    id = $(this).attr("id").replace(/d/, "");
    if (parseInt(id) <= today) {
      $(this).css("cursor","pointer");   
    }
  });


  // handle the clicks 
  $(".day").click(function(){
    // only allow clicks if door is already opened
    id = $(this).attr("id").replace(/d/, "");
    if (parseInt(id) <= today) {
      window.location = "static/images/" + id + ".png";
    }
  });
});

// create an array with a specific range
function range(start, end) {
  var foo = [];
  for (var i = start; i <= end; i++)
    foo.push(i);
  return foo;
}


// the main angular.js controller
function MainCtrl($scope) {
  $scope.days = range(1,24);
}
