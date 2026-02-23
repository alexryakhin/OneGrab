/**
 * OneGrab - Language picker
 * Injects a <select> dropdown of all site locales and navigates on change.
 */
(function () {
  'use strict';

  var LOCALES = [
    { code: 'ar-SA', label: 'العربية' },
    { code: 'ca', label: 'Català' },
    { code: 'cs', label: 'Čeština' },
    { code: 'da', label: 'Dansk' },
    { code: 'de-DE', label: 'Deutsch' },
    { code: 'el', label: 'Ελληνικά' },
    { code: 'en-AU', label: 'English (Australia)' },
    { code: 'en-CA', label: 'English (Canada)' },
    { code: 'en-GB', label: 'English (UK)' },
    { code: '', label: 'English (US)' },
    { code: 'es-ES', label: 'Español (España)' },
    { code: 'es-MX', label: 'Español (México)' },
    { code: 'fi', label: 'Suomi' },
    { code: 'fr-CA', label: 'Français (Canada)' },
    { code: 'fr-FR', label: 'Français (France)' },
    { code: 'he', label: 'עברית' },
    { code: 'hi', label: 'हिन्दी' },
    { code: 'hr', label: 'Hrvatski' },
    { code: 'hu', label: 'Magyar' },
    { code: 'id', label: 'Bahasa Indonesia' },
    { code: 'it', label: 'Italiano' },
    { code: 'ja', label: '日本語' },
    { code: 'ko', label: '한국어' },
    { code: 'ms', label: 'Bahasa Melayu' },
    { code: 'nl-NL', label: 'Nederlands' },
    { code: 'no', label: 'Norsk' },
    { code: 'pl', label: 'Polski' },
    { code: 'pt-BR', label: 'Português (Brasil)' },
    { code: 'pt-PT', label: 'Português (Portugal)' },
    { code: 'ro', label: 'Română' },
    { code: 'ru', label: 'Русский' },
    { code: 'sk', label: 'Slovenčina' },
    { code: 'sv', label: 'Svenska' },
    { code: 'th', label: 'ไทย' },
    { code: 'tr', label: 'Türkçe' },
    { code: 'uk', label: 'Українська' },
    { code: 'vi', label: 'Tiếng Việt' },
    { code: 'zh-Hans', label: '简体中文' },
    { code: 'zh-Hant', label: '繁體中文' }
  ];

  var CODES = LOCALES.map(function (l) { return l.code; });

  function getPathInfo() {
    var path = window.location.pathname.replace(/^\/+|\/+$/g, '') || '';
    var segments = path ? path.split('/') : [];
    if (segments[0] === 'OneGrab') segments.shift();
    var page = 'index.html';
    var currentCode = '';
    if (segments.length && CODES.indexOf(segments[0]) !== -1) {
      currentCode = segments[0];
      page = segments[1] || 'index.html';
    } else if (segments.length && segments[0] !== '') {
      page = segments[0];
    }
    var inLocale = currentCode !== '';
    return { currentCode: currentCode, page: page, inLocale: inLocale };
  }

  function urlFor(code) {
    var info = getPathInfo();
    var page = info.page;
    if (info.inLocale) {
      return code === '' ? '../' + page : '../' + code + '/' + page;
    }
    return code === '' ? page : code + '/' + page;
  }

  function init() {
    var container = document.getElementById('lang-picker');
    if (!container) return;

    var info = getPathInfo();
    var select = document.createElement('select');
    select.setAttribute('aria-label', 'Select language');
    select.className = 'lang-picker-select';

    LOCALES.forEach(function (loc) {
      var opt = document.createElement('option');
      opt.value = urlFor(loc.code);
      opt.textContent = loc.label;
      if (loc.code === info.currentCode) opt.selected = true;
      select.appendChild(opt);
    });

    select.addEventListener('change', function () {
      var val = select.value;
      if (val) window.location.href = val;
    });

    container.appendChild(select);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
