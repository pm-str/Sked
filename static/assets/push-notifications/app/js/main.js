'use strict';

var reg;
var sub;
var isSubscribed = false;
var subscribeButton = document.querySelector("[id='push']");

function checkSubscribe() {
    navigator.serviceWorker.ready.then(function (serviceWorkerRegistration) {
        serviceWorkerRegistration.pushManager.getSubscription()
            .then(function (subscription) {
                // Enable any UI which subscribes / unsubscribes from
                if (!subscription) {
                    subscribeButton.textContent = 'Subscribe';
                    isSubscribed = false;
                }
                else {
                    subscribeButton.textContent = 'Unsubscribe';
                    isSubscribed = true;
                }
            });
    });
}

if ('serviceWorker' in navigator) {
    console.log('Service Worker is supported');
    navigator.serviceWorker.register('/sw.js').then(function () {
        return navigator.serviceWorker.ready;
    }).then(function (serviceWorkerRegistration) {
        reg = serviceWorkerRegistration;
        subscribeButton.disabled = false;
        console.log('Service Worker is ready', reg);
    }).catch(function (error) {
        console.log('Service Worker Error', error);
    });
    checkSubscribe();
}

subscribeButton.addEventListener('click', function () {
    if (isSubscribed) {
        unsubscribe();
    } else {
        subscribe();
    }
});

function subscribe() {
    reg.pushManager.subscribe({userVisibleOnly: true}).then(function (pushSubscription) {
        sub = pushSubscription;
        console.log(sub.endpoint.valueOf());
        $.ajax({
            type: "GET",
            url: "/home/api/push_token",
            data: {
                'endpoint': sub.endpoint.valueOf()
            },
            dataType: "HTML",
            cache: false,
            statusCode: {
                200: function () {
                    console.log('You have been subscribed');
                    checkSubscribe();
                },
                401: function () {
                    console.log('An error occurred downloading');
                    checkSubscribe();
                }
            }
        });
    });
}

function unsubscribe(){
    checkSubscribe();
    reg.pushManager.subscribe({userVisibleOnly: true}).then(function (pushSubscription) {
        sub = pushSubscription;
        sub.unsubscribe().then(function (event) {
            console.log('Unsubscribed!', event);
            checkSubscribe();
        }).catch(function (error) {
            console.log('Error unsubscribing', error);
            checkSubscribe();
        });

        $.ajax({
            type: "GET",
            url: "/home/api/del_token",
            data: {
                'endpoint': sub.endpoint.valueOf()
            },
            dataType: "HTML",
            cache: false,
            statusCode: {
                200: function () {
                    console.log('You have been UnSubscribed');
                },
                401: function () {
                    console.log('An error occurred downloading');
                }
            }
        });
    });
}