<script>
    let quantityValue = 0;

    function decreaseQuantity() {
        if (quantityValue > 0) {
            quantityValue--;
            document.querySelector('.quantity-value').textContent = quantityValue;
        }
    }

    function increaseQuantity() {
        quantityValue++;
        document.querySelector('.quantity-value').textContent = quantityValue;
    }
</script>


<script>
    document.addEventListener("DOMContentLoaded", function () {
        var cartItems = JSON.parse(localStorage.getItem("cart"));

        var cartItemsElement = document.getElementById("cartItems");
        for (var key in cartItems) {
            if (cartItems.hasOwnProperty(key)) {
                var item = cartItems[key];
                var title = item.title;
                var quantity = item.quantity;
                var image = item.image;
                var price = item.price;

                var container = document.createElement("div"); // Создаем контейнер для вывода данных в ряд
                container.classList.add("cartItemContainer"); // Добавляем CSS-класс контейнеру

                var img = document.createElement('img');
                img.src = "/media/" + image;
                img.width = 100;
                img.height = 100;
                img.classList.add("cartItemImage"); // Добавляем CSS-класс изображению

                var info = document.createElement("div"); // Создаем контейнер для информации
                info.classList.add("cartItemInfo"); // Добавляем CSS-класс контейнеру информации

                var titleElement = document.createElement("p");
                titleElement.textContent = title;

                var quantityElement = document.createElement("p");
                quantityElement.textContent = "Количество: " + quantity;

                var priceElement = document.createElement("p");
                priceElement.textContent = "Цена: " + price * quantity;
                

                info.appendChild(titleElement); // Добавляем заголовок в контейнер информации
                info.appendChild(quantityElement); // Добавляем количество в контейнер информации
                info.appendChild(priceElement); // Добавляем цену в контейнер информации

                container.appendChild(img); // Добавляем изображение в контейнер
                container.appendChild(info); // Добавляем контейнер информации в контейнер

                cartItemsElement.appendChild(container); // Добавляем контейнер в родительский контейнер

            }
        }
    });
</script>