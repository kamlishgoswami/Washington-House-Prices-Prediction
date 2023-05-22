    function onPageLoad() {
        console.log("Doc loaded");
        // var url = "http://127.0.0.1:5000/get_location_names"; // use this url if you are not using nginx
        var url = "/api/get_location_names"  // use this url if you are using nginx 
        $.get(url, function(data,status){
            console.log("got response");
            if(data) {
                var locations = data.locations;
                var uilocations = document.getElementById("uilocations");
                $('#uilocations').empty();
                for (var i in locations){
                    var opt = new Option(locations[i]);
                    $('#uilocations').append(opt)
                }
            }
        });
    }


    function onClickEstimatedPrice() {
        console.log('EP Button clicked');
        var Sqft_living = document.getElementById('sqft_living');
        var Sqft_lot = document.getElementById('sqft_lot');
        var Floor= document.querySelector('input[name="uifloor"]:checked').value;
        var Condition = document.querySelector('input[name="uicondition"]:checked').value;
        var Bedroom = document.querySelector('input[name="uibedroom"]:checked').value;
        var Bathroom = document.querySelector('input[name="uibathroom"]:checked').value;
        var Waterfront = document.querySelector('input[name="uiwaterfront"]:checked').value;
        var Location = document.getElementById('uilocations');
        var estPrice = document.getElementById('uiEstimatedPrice');

        console.log("Working");
        // var url = "http://127.0.0.1:5000/predict_home_price"; // use this url if you are not using nginx
        var url = "/api/predict_home_price"  // use this url if you are using nginx
        console.log("got response");
        $.post({
            url: url,
            contentType: 'application/json',
            data: JSON.stringify({
                bedrooms : Bedroom,
                bathrooms : Bathroom,
                sqft_living : parseFloat(Sqft_living.value),
                sqft_lot : parseFloat(Sqft_lot.value),
                floors: Floor,
                waterfront: Waterfront,
                condition: Condition,
                location: Location.value,
            }),
            success: function(data, status) {
                console.log(data.estimated_price);
                estPrice.innerHTML = "<h2> $ "+ data.estimated_price.toString() + " </h2>"
                console.log(status);
            }
        });
    }    


    window.onload = onPageLoad;