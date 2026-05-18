(function () {
  var KEY = 'bib_cookie_consent';
  if (localStorage.getItem(KEY)) return;

  var style = document.createElement('style');
  style.textContent = [
    '#cc-banner{',
      'position:fixed;bottom:0;left:0;right:0;z-index:9999;',
      'background:#111111;color:#ccc;',
      'padding:14px 48px;',
      'display:flex;align-items:center;justify-content:space-between;gap:24px;',
      'font-family:"DM Sans",sans-serif;font-size:13px;line-height:1.5;',
      'border-top:1px solid #2a2a2a;',
    '}',
    '#cc-banner a{color:#1D9E75;text-decoration:underline;}',
    '#cc-banner a:hover{color:#25c490;}',
    '#cc-actions{display:flex;gap:10px;flex-shrink:0;}',
    '#cc-accept{',
      'background:#1D9E75;color:#fff;border:none;border-radius:4px;',
      'padding:8px 20px;font-size:13px;font-weight:500;cursor:pointer;white-space:nowrap;',
      'font-family:inherit;',
    '}',
    '#cc-accept:hover{background:#0F6E56;}',
    '#cc-decline{',
      'background:transparent;color:#888;border:0.5px solid #444;border-radius:4px;',
      'padding:8px 20px;font-size:13px;cursor:pointer;white-space:nowrap;',
      'font-family:inherit;',
    '}',
    '#cc-decline:hover{color:#ccc;border-color:#666;}',
    '@media(max-width:700px){',
      '#cc-banner{flex-direction:column;align-items:flex-start;padding:20px 24px;gap:14px;}',
      '#cc-actions{width:100%;justify-content:flex-end;}',
    '}'
  ].join('');
  document.head.appendChild(style);

  var banner = document.createElement('div');
  banner.id = 'cc-banner';
  banner.setAttribute('role', 'dialog');
  banner.setAttribute('aria-label', 'Cookie consent');
  banner.innerHTML =
    '<p>We use cookies to ensure the proper functioning of this website. ' +
    'By clicking "Accept" you consent to their use. ' +
    '<a href="/en/cookies/">Cookie Policy</a></p>' +
    '<div id="cc-actions">' +
      '<button id="cc-decline">Decline</button>' +
      '<button id="cc-accept">Accept</button>' +
    '</div>';
  document.body.appendChild(banner);

  document.getElementById('cc-accept').addEventListener('click', function () {
    localStorage.setItem(KEY, 'accepted');
    banner.remove();
  });
  document.getElementById('cc-decline').addEventListener('click', function () {
    localStorage.setItem(KEY, 'declined');
    banner.remove();
  });
})();
