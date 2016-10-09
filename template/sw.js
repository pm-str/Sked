/*
*
*  Push Notifications codelab
*  Copyright 2015 Google Inc. All rights reserved.
*
*  Licensed under the Apache License, Version 2.0 (the "License");
*  you may not use this file except in compliance with the License.
*  You may obtain a copy of the License at
*
*      https://www.apache.org/licenses/LICENSE-2.0
*
*  Unless required by applicable law or agreed to in writing, software
*  distributed under the License is distributed on an "AS IS" BASIS,
*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*  See the License for the specific language governing permissions and
*  limitations under the License
*
*/

// Version 0.1

'use strict';

var config = {
  'api_url': '/home/api/',
  'static_url': '/static/assets/push-notifications/app/images/',
  'is_broadcast': true
};

console.log('Started', self);

self.addEventListener('install', function(event) {
  self.skipWaiting();
  console.log('Installed', event);
});

self.addEventListener('activate', function(event) {
  console.log('Activated', event);
});

self.addEventListener('push', function(event) {
  console.log('Push', event);

event.waitUntil(
    // получаем id устройства
    self.registration.pushManager.getSubscription().then(function(subscription) {
        var registration_id = subscription.endpoint.split("/").slice(-1)[0];
        // получаем payload по id устройства
        fetch(config.api_url + 'data_by_reg_id?registration_id=' + registration_id, {
          'headers': {'Content-type': 'application/json'}
        }).then(function(response) {
          if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' + response.status);
            throw new Error('Looks like there was a problem. Status Code: ' + response.status);
          }

          return response.json().then(function (data) {
            var title = data.title;
            var body = data.body;
            var url = data.url;
            var icon = config.static_url + data.icon;

            return self.registration.showNotification(title, {
              body: body,
              icon: icon,
              vibrate: [200, 100, 200, 100, 200, 100, 200],
              tag: 'MySked',
              data: {
                url: url
              }
              
            });
          }).catch(function (err) {
            console.error('Unable to retrieve data', err);
          });
        });
    })
  );
// ############
});

self.addEventListener('notificationclick', function(event) {
  console.log('Notification click: tag', event.notification.tag);
  // Android doesn't close the notification when you click it
  // See http://crbug.com/463146
  event.notification.close();
  var url = event.notification.data.url;
  // Check if there's already a tab open with this URL.
  // If yes: focus on the tab.
  // If no: open a tab with the URL.
  event.waitUntil(
    clients.matchAll({
      type: 'window'
    })
    .then(function(windowClients) {
      console.log('WindowClients', windowClients);
      for (var i = 0; i < windowClients.length; i++) {
        var client = windowClients[i];
        console.log('WindowClient', client);
        if (client.url === url && 'focus' in client) {
          return client.focus();
        }
      }
      if (clients.openWindow) {
        return clients.openWindow(url);
      }
    })
  );
});
