//pf[ezh.

$(document).ready(() => {
    let selectedMethod;

    $("#card").change(() => {
        selectedMethod = 2;
    });

    $("#cash").change(() => {
        selectedMethod = 1;
    });

    function getCookie(name) {
        const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
        return cookieValue ? cookieValue.pop() : '';
    }

    $("#purchase-button").click((event) => {
        let cardNumber = $("#cardNumber").val();
        let address = $("#address").val();
        let csrfToken = getCookie('csrftoken');
        debugger
        let payment = 2;

        $.ajax({
            url: '/purchase/',
            method: 'POST',
            contentType:"application/json; charset=utf-8",
            dataType:"json",
            data: JSON.stringify({
                cardNumber: cardNumber,
                address: address,
                payment: payment,
            }),
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: (response) => {
                debugger;
                alert("ну работает");
                // $("#successModal").append(`ПРИШЕЛ ОТВЕТ: ${response.success}`);
            },
            error: (error) => {
                debugger;
                alert('Не добавлена');
            }
        });
    });
});
