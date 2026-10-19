/**
 * Service Worker - EGEL Plus ISOFT PWA
 * Carga instantánea, caché resiliente y funcionamiento offline.
 */

const CACHE_NAME = 'egel-plus-v2.1.0';
const CORE_ASSETS = [
  '/',
  '/static/css/style.css?v=2.1',
  '/static/js/app.js?v=2.1',
  '/static/manifest.json',
  '/static/icons/logo.svg',
  '/static/icons/icon-192.png',
  '/static/icons/icon-512.png'
];

// Instalación: Precargar recursos esenciales del cascarón de la app
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(CORE_ASSETS);
    }).then(() => self.skipWaiting())
  );
});

// Activación: Limpieza agresiva de versiones antiguas de caché
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Estrategia de Fetch: Network-First con fallback a caché para funcionamiento offline
self.addEventListener('fetch', (event) => {
  const request = event.request;
  const url = new URL(request.url);

  // Peticiones de la API: Network First
  if (url.pathname.startsWith('/api/')) {
    event.respondWith(
      fetch(request).catch(() => {
        return new Response(JSON.stringify({
          error: "Sin conexión con el servidor. Verifica que 'python app.py' esté activo."
        }), {
          headers: { 'Content-Type': 'application/json' }
        });
      })
    );
    return;
  }

  // Network First para CSS, JS y Documentos HTML para reflejar cambios de inmediato
  event.respondWith(
    fetch(request)
      .then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(request, responseToCache));
        }
        return networkResponse;
      })
      .catch(() => {
        // Fallback a caché si no hay conexión
        return caches.match(request).then((cachedResponse) => {
          if (cachedResponse) return cachedResponse;
          if (request.mode === 'navigate') return caches.match('/');
        });
      })
  );
});
