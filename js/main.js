/**
 * OneGrab — Main script
 * Mobile nav toggle, no dependencies
 */

(function () {
  'use strict';

  const HEADER_SELECTOR = '.site-header';
  const NAV_SELECTOR = '.nav';
  const TOGGLE_SELECTOR = '.nav-toggle';

  function init() {
    const header = document.querySelector(HEADER_SELECTOR);
    const nav = header?.querySelector(NAV_SELECTOR);
    const toggle = header?.querySelector(TOGGLE_SELECTOR);

    if (!nav || !toggle) return;

    // Show toggle on small viewports
    function updateToggleVisibility() {
      const isNarrow = window.matchMedia('(max-width: 47.9375rem)').matches;
      toggle.hidden = !isNarrow;
      if (!isNarrow) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    }

    toggle.addEventListener('click', function () {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!expanded));
      nav.classList.toggle('is-open', !expanded);
    });

    // Close menu when a nav link is clicked (in-page anchor or same origin)
    nav.addEventListener('click', function (e) {
      const link = e.target.closest('a');
      if (link && window.matchMedia('(max-width: 47.9375rem)').matches) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });

    updateToggleVisibility();
    window.addEventListener('resize', updateToggleVisibility);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
