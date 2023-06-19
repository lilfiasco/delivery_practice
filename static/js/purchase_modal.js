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
        let address = $("#cardAddress").val();
        let csrfToken = getCookie('csrftoken');
        let storedFranchiseId = parseInt(localStorage.getItem('franchiseId')); 
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
                franchise: storedFranchiseId,
            }),
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: (response) => {
                debugger
                $('#modal1').modal('hide');
                $('#successModal1').modal();
            },
            error: (error) => {
                alert('Не добавлена');
            }
        });
    });

    $("#purchase-btn").click((event) => {
        let address = $("#cashAddress").val();
        let csrfToken = getCookie('csrftoken');
        let storedFranchiseId = parseInt(localStorage.getItem('franchiseId'));  
        let payment = 1;

        $.ajax({
            url: '/purchase/',
            method: 'POST',
            contentType:"application/json; charset=utf-8",
            dataType:"json",
            data: JSON.stringify({
                address: address,
                payment: payment,
                franchise: storedFranchiseId,
            }),
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: (response) => {
                debugger
                $('#modal2').modal('hide');
                $('#successModal2').modal();
            },
            error: (error) => {
                debugger
                alert('Не добавлена');
            }
        });
    });

});
