if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('/sw.js', {
    scope: './'
  }).then(function() {
      console.log('ServiceWorker registration complete.');
    }, function() {
      console.log('ServiceWorker registration failure.');
    });
  });
} else {
  console.log('ServiceWorker is not supported.');
}