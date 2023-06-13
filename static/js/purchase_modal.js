$(document).ready(() => {
    $("#card").change(() => {
        selectedMethod = 2;
    })
    $("#cash").change(() => {
        selectedMethod = 1;
    })

    $("#openModal").click(() => {
        selectedMethod
    })

    $("#openModal").click((event) =>{
        let cardNumber = $("#cardNumber").val();
        let address= $("#address").val();

        $.ajax({
            url: '',
            method: '',
            data: {
                cardNumber: cardNumber,
                address: address,
            },

            success: (response) => {
                debugger
                $("#addmodal1").append(`ПРИШЕЛ ОТВЕТ: ${response.success}`)
            },
            error: (error) => {
                debugger
            }
        })
    })
});