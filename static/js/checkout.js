$(document).ready(function() {
    $('.payWithRazorpay').click(function(e) {
        e.preventDefault();

        var fname = $("[name='contact_name']").val();
        var address = $("[name='street_address']").val();
        var phone = $("[name='phone_number']").val();
        var pincode = $("[name='postal_code']").val();
        var city = $("[name='city']").val();
        var state = $("[name='state']").val();
        var country = $("[name='country']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();

        $.ajax({
            method: "GET",
            url: "/proceed-to-pay",
            success: function(response) {
                var options = {
                    "key": "rzp_test_BzE6HdexQFvWsD",
                    "amount": response.total_price * 100,
                    "currency": "INR",
                    "name": "KanikaTeam",
                    "description": "Testing Transaction",
                    "image": "https://example.com/your_logo",
                    "handler": function(responseb) {
                        alert(responseb.razorpay_payment_id);
                        var data = {
                            "fname": fname,
                            "phone": phone,
                            "address": address,
                            "city": city,
                            "state": state,
                            "country": country,
                            "pincode": pincode,
                            "payment_method": "Razorpay",
                            "payment_id": responseb.razorpay_payment_id,
                            csrfmiddlewaretoken: token,
                        };
                        $.ajax({
                            method: "POST",
                            url: "/placeorder/",  // URL with trailing slash
                            data: data,
                            success: function(responsec) {
                                swal("Good job!", "Payment is successful!", "success").then((value) => {
                                    window.location.href = '/my-orders';
                                });
                            },
                            error: function(responsec) {
                                swal("Error!", "Something went wrong with placing the order!", "error");
                            }
                        });
                        
                    },
                    "prefill": {
                        "name": fname,
                        "contact": phone
                    },
                    "theme": {
                        "color": "#3399cc"
                    }
                };
                var rzp1 = new Razorpay(options);
                rzp1.open();
            }
        });
    });
});
