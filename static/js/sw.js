self.addEventListener('install', function(event) {
  event.waitUntil(
      caches.open('biotools-sw').then(function(cache) {
          return cache.addAll([
              '/protein_reading',
              '/example',
              '/offline',
              '/webapp',
              '/css/main.css',
              '/css/ie8.css',
              '/css/ie9.css',
              '/css/font-awesome.min.css',
              '/css/SansPro.css',
              '/images/banner.jpg',
              '/js/production.js',
              '/js/webapp.operator.js',
              '/js/webapp.visual.js',
              '/js/ie/production.ie.js',
              '/js/ie/backgroundsize.min.htc',
              '/fonts/Light-300.woff2',
              '/fonts/SemiBold-300.woff2',
              '/config/manifest.json',
              '/config/browserconfig.xml'
          ]);
      })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(checkResponse(event.request).catch(function() {
    return returnFromCache(event.request)}
  ));
  event.waitUntil(addToCache(event.request));
});

var checkResponse = function(request){
  return new Promise(function(fulfill, reject) {
    fetch(request).then(function(response){
      if(response.status !== 404) {
        fulfill(response)
      } else {
        reject()
      }
    }, reject)
  });
};

var addToCache = function(request){
  return caches.open('biotools-sw').then(function(cache) {
    return fetch(request).then(function(response) {
      return cache.put(request, response);
    });
  });
};

var returnFromCache = function(request){
  return caches.open('biotools-sw').then(function(cache) {
    return cache.match(request).then(function(matching) {
     if(!matching || matching.status == 404) {
       return cache.match('/offline')
     } else {
       return matching;
     }
    });
  });
};

self.addEventListener('activate', function(event) {
  var cacheWhitelist = ['biotools-sw'];
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(cacheName) {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
