function initMap() {
    // Use your own latitude and longitude values
    var myLatLng = { lat: 44.69464, lng: -0.44679 };

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: "Wine O'Clock Location"
    });
}