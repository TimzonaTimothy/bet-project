function payWithPayStack(){
        let currency = "NGN";
        let plan = "";
        let amount = 'deposit-amount'
        let ref = "{{ payment.ref }}";
        let obj = {
            key: "pk_test_14162cb89ec6e813cf664044d2cf5a44f5b40255",
            email: '{{ user.email }}',
            amount: 'amount',
            ref: ref,
            callback: function(response){
                window.location.href = "{% url 'verify-payment' payment.ref %}";
            }
        }
        if (Boolean(currency)){
            obj.currency = currency.toUpperCase()
        }
        if (Boolean(plan)){
            obj.plan - plan;
        }
        var handler = PaystackPop.setup(obj);
        handler.openIframe();
    }