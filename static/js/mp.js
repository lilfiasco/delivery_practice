var cart = JSON.parse(localStorage.getItem("cart")) || {};
    
        function addToCart(button) {
            var foodId = button.getAttribute("data-food-id");
            var foodTitle = button.getAttribute("data-food-title");
            var foodPrice = parseFloat(button.getAttribute("data-food-price"));
            var foodQuantity = parseInt(button.getAttribute("data-food-quantity"));
            var foodImage = button.getAttribute("data-food-image");

            var quantityInput = button.parentNode.previousElementSibling.querySelector(".quantity");
            var quantity = parseInt(quantityInput.value);

            if (quantity > 0) {
                cart[foodId] = {
                    title: foodTitle,
                    price: foodPrice,
                    quantity: quantity,
                    image: foodImage
                };
                saveCartToLocalStorage();
                updateCartDisplay();
            }else {
        
                var foodId = button.getAttribute("data-food-id");
                delete cart[foodId];
                saveCartToLocalStorage();
                updateCartDisplay();
    }
            
        }
    
        function changeQuantity(button, increment) {
            var quantityInput = button.parentNode.querySelector(".quantity");
            var currentQuantity = parseInt(quantityInput.value);
            var newQuantity = currentQuantity + increment;
    
            if (newQuantity >= 0) {
                quantityInput.value = newQuantity;
                saveCartToLocalStorage();
            }
            
        }

        function updateCartDisplay() {
            var cartItemsDiv = document.getElementById("cart-items");
            cartItemsDiv.innerHTML = "";
    
            for (var foodId in cart) {
                var item = cart[foodId];
                var itemElement = document.createElement("div");
                itemElement.innerText = item.title + " - " + item.quantity + item.price;
                cartItemsDiv.appendChild(itemElement);
            }
        }
        
        function saveCartToLocalStorage() {
            localStorage.setItem("cart", JSON.stringify(cart));
        }
    
        function checkout() {
            console.log(cart);
            localStorage.removeItem("cart");
        }