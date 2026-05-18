const DE_COUNTRIES = new Set(['DE','AT','CH','LI','LU']);
const ES_COUNTRIES = new Set(['ES','MX','AR','CO','CL','PE','VE','EC','BO','PY','UY','CR','PA','GT','HN','SV','NI','DO','CU','PR']);

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // www redirect
    if (url.hostname === 'www.bibparts.com') {
      url.hostname = 'bibparts.com';
      return Response.redirect(url.toString(), 301);
    }

    // Geo redirect on root
    if (url.pathname === '/') {
      const country = request.cf?.country || '';
      let target = '/en/';
      if (DE_COUNTRIES.has(country)) target = '/de/';
      else if (ES_COUNTRIES.has(country)) target = '/es/';
      return Response.redirect(new URL(target, url).toString(), 307);
    }

    // Serve static asset
    let response;
    try {
      response = await env.ASSETS.fetch(request);
    } catch {
      return new Response('Not found', { status: 404 });
    }
    if (response.status === 500) {
      return new Response('Not found', { status: 404 });
    }

    const isHtml = response.headers.get('content-type')?.includes('text/html');
    const isStatic = /\.(svg|png|jpg|jpeg|gif|webp|ico|js|css|woff2?)$/.test(url.pathname);

    const headers = new Headers(response.headers);
    headers.set('X-Frame-Options', 'SAMEORIGIN');
    headers.set('X-Content-Type-Options', 'nosniff');
    headers.set('Referrer-Policy', 'strict-origin-when-cross-origin');
    headers.set('Permissions-Policy', 'camera=(), microphone=(), geolocation=()');

    if (isStatic) {
      headers.set('Cache-Control', 'public, max-age=31536000, immutable');
    } else if (isHtml) {
      headers.set('Cache-Control', 'no-cache');
    }

    return new Response(response.body, {
      status: response.status,
      headers,
    });
  },
};
