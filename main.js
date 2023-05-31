"use strict";
var Rotas = /** @class */ (function () {
    function Rotas() {
    }
    Rotas.getNextPage = function () {
        return '/getNextPageUrl';
    };
    return Rotas;
}());
function sendUrlToScrapApplication(event) {
    event.preventDefault();
    console.log('teste');
    var target = event.target;
    if (target instanceof HTMLAnchorElement) {
        var apiUrl = process.env.API_URL;
        console.log(apiUrl);
        var link = target.href;
        var request = { link: link };
        var requestOptions = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(request),
        };
        var prox_1 = function (data) {
            console.log(data);
        };
        fetch(apiUrl + Rotas.getNextPage(), requestOptions)
            .then(function (response) { return response.json(); })
            .then(function (response) { return prox_1(response); });
    }
}
