document.getElementById("openModal").addEventListener("click", function() {
    document.getElementById("modal").style.display = "block";
  });
  debugger
  document.getElementById("modal").addEventListener("click", function(event) {
    if (event.target === this) {
      document.getElementById("modal").style.display = "none";
    }
  });
  
  document.querySelector(".close").addEventListener("click", function() {
    document.getElementById("modal").style.display = "none";
  });
  