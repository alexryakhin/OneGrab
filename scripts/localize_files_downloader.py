#!/usr/bin/env python3
"""Generate localized Website index/support/terms for Files Downloader positioning."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP_ROOT = ROOT.parent

LOCALES = [
    "ar-SA", "ca", "cs", "da", "de-DE", "el", "en-AU", "en-CA", "en-GB", "es-ES", "es-MX",
    "fi", "fr-CA", "fr-FR", "he", "hi", "hr", "hu", "id", "it", "ja", "ko", "ms", "nl-NL",
    "no", "pl", "pt-BR", "pt-PT", "ro", "ru", "sk", "sv", "th", "tr", "uk", "vi", "zh-Hans", "zh-Hant",
]

LANG_ATTR = {
    "ar-SA": "ar", "ca": "ca", "cs": "cs", "da": "da", "de-DE": "de", "el": "el",
    "en-AU": "en-AU", "en-CA": "en-CA", "en-GB": "en-GB", "es-ES": "es", "es-MX": "es-MX",
    "fi": "fi", "fr-CA": "fr-CA", "fr-FR": "fr", "he": "he", "hi": "hi", "hr": "hr",
    "hu": "hu", "id": "id", "it": "it", "ja": "ja", "ko": "ko", "ms": "ms", "nl-NL": "nl",
    "no": "no", "pl": "pl", "pt-BR": "pt-BR", "pt-PT": "pt-PT", "ro": "ro", "ru": "ru",
    "sk": "sk", "sv": "sv", "th": "th", "tr": "tr", "uk": "uk", "vi": "vi",
    "zh-Hans": "zh-Hans", "zh-Hant": "zh-Hant",
}

# English source of truth for content
EN = {
    "meta_desc": "OneGrab — Files Downloader. Paste a direct file link, tap Save, and keep it on your device.",
    "title": "OneGrab — Files Downloader",
    "hero_label": "Files Downloader for iPhone, iPad & Mac",
    "hero_line1": "Paste a link.",
    "hero_accent": "Save the file.",
    "hero_desc": "OneGrab downloads open file URLs — documents, archives, media, and more. Paste a link that points to the file itself (not a webpage), tap Save, and keep it on your device.",
    "why": "Why OneGrab",
    "f1_title": "Direct file links",
    "f1_desc": "Paste a URL that points to the file itself — not a webpage — then tap Save.",
    "f2_title": "Progress you can see",
    "f2_desc": "Track the download, then open, share, or export when it’s done.",
    "f3_title": "On your device",
    "f3_desc": "Files stay organized in the app. Share or save images and videos to Photos when you want.",
    "cta_title": "Ready to download?",
    "cta_desc": "Get OneGrab on iPhone, iPad, or Mac. Free to try.",
    "support_meta_desc": "OneGrab Support — Help with downloads, subscriptions, and more.",
    "support_meta": "We’re here to help.",
    "contact_h2": "Contact us",
    "contact_p": "For questions about OneGrab, downloads, subscriptions, or anything else, reach out by email:",
    "contact_reply": "We’ll do our best to get back to you within a few business days.",
    "faq_h2": "Frequently asked questions",
    "q1": "How do I download a file?",
    "a1": "Copy a <strong>direct file URL</strong> (a link that points to the file itself — for example ending in <code>.pdf</code>, <code>.zip</code>, or <code>.mp4</code>), open OneGrab, and tap <strong>Save</strong> or <strong>Save from Clipboard</strong>. When it finishes, open, share, or export from your Saved list.",
    "q2": "What kinds of links work?",
    "a2": "OneGrab downloads open file links only — URLs that point to a file, not a webpage. Webpage links are refused. If a link isn’t a direct file, the app will tell you.",
    "q3": "How do I restore my subscription?",
    "a3": "Open OneGrab, tap the settings (gear) icon, then <strong>Restore purchase</strong>. Your subscription will be restored if it’s still active.",
    "q4": "Downloading isn’t working. What should I try?",
    "a4": "Make sure the URL is a direct file link (not an HTML page). Check your internet connection and try again. If it still fails, email us with the link and we’ll look into it.",
    "get_app": "Get the app",
    "agreement_h2": "Agreement",
    "agreement_p": "By downloading or using OneGrab, you agree to these Terms of Use.",
    "use_h2": "Use of the app",
    "use_p": "OneGrab is a download manager for direct file URLs. You may use it only in accordance with applicable laws. You are responsible for ensuring you have the right to download and store any files you save.",
    "sub_h2": "Subscriptions",
    "sub_p": "Paid features are governed by the subscription terms presented at purchase. Payments are processed by Apple. Refunds are subject to Apple&apos;s policy.",
    "disc_h2": "Disclaimer",
    "disc_p": "OneGrab is provided &quot;as is&quot;. We do not guarantee uninterrupted or error-free service. We are not responsible for third-party content or services.",
    "liab_h2": "Limitation of liability",
    "liab_p": "To the maximum extent permitted by law, we are not liable for any indirect, incidental, or consequential damages arising from your use of the app.",
    "chg_h2": "Changes",
    "chg_p": "We may update these terms. Continued use of the app after changes constitutes acceptance.",
}

# Locale-specific content overrides (full dict). Missing keys fall back to EN.
# Chrome (nav/footer/buttons) comes from git HEAD when available.


def show(path: str) -> str:
    try:
        return subprocess.check_output(
            ["git", "show", f"HEAD:{path}"],
            cwd=APP_ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        return ""


def extract_chrome(loc: str) -> dict:
    html = show(f"Website/{loc}/index.html")
    sh = show(f"Website/{loc}/support.html")
    th = show(f"Website/{loc}/terms.html")

    def g(src: str, pat: str):
        m = re.search(pat, src or "", re.S)
        return m.group(1).strip() if m else None

    c = {
        "lang": LANG_ATTR.get(loc, loc),
        "skip": g(html, r'class="skip-link">([^<]+)') or "Skip to main content",
        "home_aria": g(html, r'class="logo" aria-label="([^"]+)"') or "OneGrab home",
        "nav_aria": g(html, r'<nav class="nav" aria-label="([^"]+)"') or "Main",
        "features_nav": g(html, r'href="#features">([^<]+)') or "Features",
        "download_nav": g(html, r'href="#download">([^<]+)') or "Download",
        "support_nav": g(html, r'href="support.html">([^<]+)') or "Support",
        "privacy_nav": g(html, r'href="privacy.html">([^<]+)') or "Privacy",
        "terms_nav": g(html, r'href="terms.html">([^<]+)') or "Terms",
        "menu_aria": g(html, r'class="nav-toggle" aria-label="([^"]+)"') or "Toggle menu",
        "store": g(html, r'id="cta-download"[^>]*>\s*([^<]+)') or "Download on the App Store",
        "mac": g(html, r'id="cta-download-mac"[^>]*>\s*([^<]+)') or "Download for Mac",
        "made": g(html, r'class="footer-copy">([^<]+)') or "Made with care.",
        "support_title": g(sh, r"<title>([^<]+)") or "Support - OneGrab",
        "support_h1": g(sh, r'class="page-title">([^<]+)') or "Support",
        "back": g(sh, r'href="index.html">([^<]+)') or "← Back to OneGrab",
        "terms_title": g(th, r"<title>([^<]+)") or "Terms of Use - OneGrab",
        "terms_h1": g(th, r'class="page-title">([^<]+)') or "Terms of Use",
        "terms_meta": g(th, r'class="page-meta">([^<]+)') or "Last updated: 2026",
        "privacy_policy": g(html, r'href="privacy[^"]*">([^<]+)') or "Privacy Policy",
        "terms_of_use": g(html, r'href="terms[^"]*">([^<]+)') or "Terms of Use",
    }
    m = re.search(
        r'footer-legal.*?href="support.html">([^<]+).*?href="privacy[^"]*">([^<]+).*?href="terms[^"]*">([^<]+)',
        html or "",
        re.S,
    )
    if m:
        c["footer_support"], c["footer_privacy"], c["footer_terms"] = (
            m.group(1).strip(),
            m.group(2).strip(),
            m.group(3).strip(),
        )
    else:
        c["footer_support"] = c["support_nav"]
        c["footer_privacy"] = c["privacy_nav"]
        c["footer_terms"] = c["terms_nav"]
    # support page get-the-app nav
    c["get_app"] = g(sh, r'href="index.html#download">([^<]+)') or c["download_nav"]
    return c


# Load translations from sibling JSON written below
TRANS_PATH = Path(__file__).with_name("files_downloader_i18n.json")


def content_for(loc: str) -> dict:
    data = json.loads(TRANS_PATH.read_text(encoding="utf-8"))
    base = dict(EN)
    # english variants
    if loc.startswith("en"):
        base.update(data.get("en", {}))
        if loc == "en-GB" or loc == "en-AU":
            # minor spelling if present
            pass
        return base
    base.update(data.get(loc, data.get(loc.split("-")[0], {})))
    return base


def index_html(c: dict, t: dict) -> str:
    return f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0JNXZ901GN"></script>
  <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag('js', new Date()); gtag('config', 'G-0JNXZ901GN');</script>
  <meta name="description" content="{t['meta_desc']}">
  <title>{t['title']}</title>
  <link rel="icon" type="image/svg+xml" href="../favicon/favicon.svg">
  <link rel="manifest" href="../favicon/site.webmanifest">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/base.css">
  <link rel="stylesheet" href="../css/layout.css">
  <link rel="stylesheet" href="../css/components.css">
</head>
<body>
  <a href="#main" class="skip-link">{c['skip']}</a>
  <header class="site-header" role="banner">
    <div class="container header-inner">
      <a href="index.html" class="logo" aria-label="{c['home_aria']}"><img src="../assets/nameGlow.png" alt="OneGrab" class="logo-img"></a>
      <nav class="nav" aria-label="{c['nav_aria']}">
        <ul class="nav-list">
          <li><a href="#features">{c['features_nav']}</a></li>
          <li><a href="#download">{c['download_nav']}</a></li>
          <li><a href="support.html">{c['support_nav']}</a></li>
          <li><a href="privacy.html">{c['privacy_nav']}</a></li>
          <li><a href="terms.html">{c['terms_nav']}</a></li>
        </ul>
        <button type="button" class="nav-toggle" aria-label="{c['menu_aria']}" aria-expanded="false" hidden>
          <span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span>
        </button>
      </nav>
    </div>
  </header>
  <main id="main" class="main">
    <section class="hero" aria-labelledby="hero-heading">
      <div class="container hero-inner">
        <div class="hero-content">
          <p class="hero-label">{t['hero_label']}</p>
          <h1 id="hero-heading" class="hero-title">{t['hero_line1']}<br><span class="hero-title-accent">{t['hero_accent']}</span></h1>
          <p class="hero-desc">{t['hero_desc']}</p>
          <div class="hero-buttons">
            <a href="https://apps.apple.com/app/id6759439265" class="btn btn-primary btn-hero" id="cta-download">{c['store']}</a>
            <a href="https://github.com/alexryakhin/OneGrab/releases" class="btn btn-secondary btn-hero" id="cta-download-mac" rel="noopener noreferrer" target="_blank">{c['mac']}</a>
          </div>
        </div>
        <div class="hero-visual" aria-hidden="true"><img src="../assets/iPhone-Screenshot.png" alt="" class="hero-phone-img"></div>
      </div>
    </section>
    <section id="features" class="features" aria-labelledby="features-heading">
      <div class="container">
        <h2 id="features-heading" class="section-title">{t['why']}</h2>
        <ul class="feature-grid">
          <li class="feature-card"><span class="feature-icon" aria-hidden="true">⎘</span><h3 class="feature-title">{t['f1_title']}</h3><p class="feature-desc">{t['f1_desc']}</p></li>
          <li class="feature-card"><span class="feature-icon" aria-hidden="true">◇</span><h3 class="feature-title">{t['f2_title']}</h3><p class="feature-desc">{t['f2_desc']}</p></li>
          <li class="feature-card"><span class="feature-icon" aria-hidden="true">▷</span><h3 class="feature-title">{t['f3_title']}</h3><p class="feature-desc">{t['f3_desc']}</p></li>
        </ul>
      </div>
    </section>
    <section id="download" class="cta-section" aria-labelledby="cta-heading">
      <div class="container cta-inner">
        <h2 id="cta-heading" class="cta-title">{t['cta_title']}</h2>
        <p class="cta-desc">{t['cta_desc']}</p>
        <div class="cta-buttons">
          <a href="https://apps.apple.com/app/id6759439265" class="btn btn-primary btn-lg">{c['store']}</a>
          <a href="https://github.com/alexryakhin/OneGrab/releases" class="btn btn-secondary btn-lg" rel="noopener noreferrer" target="_blank">{c['mac']}</a>
        </div>
      </div>
    </section>
  </main>
  <footer class="site-footer" role="contentinfo">
    <div class="container footer-inner">
      <p class="footer-brand">OneGrab</p>
      <p class="footer-legal">
        <a href="support.html">{c['footer_support']}</a><span class="footer-sep">·</span>
        <a href="privacy.html">{c['footer_privacy']}</a><span class="footer-sep">·</span>
        <a href="terms.html">{c['footer_terms']}</a>
      </p>
      <p class="footer-copy">{c['made']}</p>
      <div class="lang-picker-wrap"><div id="lang-picker" class="lang-picker"></div></div>
    </div>
  </footer>
  <script src="../js/main.js"></script>
  <script src="../js/lang-picker.js"></script>
</body>
</html>
"""


def support_html(c: dict, t: dict) -> str:
    return f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0JNXZ901GN"></script>
  <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag('js', new Date()); gtag('config', 'G-0JNXZ901GN');</script>
  <meta name="description" content="{t['support_meta_desc']}">
  <title>{c['support_title']}</title>
  <link rel="icon" type="image/svg+xml" href="../favicon/favicon.svg">
  <link rel="manifest" href="../favicon/site.webmanifest">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/base.css">
  <link rel="stylesheet" href="../css/layout.css">
  <link rel="stylesheet" href="../css/components.css">
  <link rel="stylesheet" href="../css/pages.css">
</head>
<body>
  <header class="site-header" role="banner">
    <div class="container header-inner">
      <a href="index.html" class="logo" aria-label="{c['home_aria']}"><img src="../assets/nameGlow.png" alt="OneGrab" class="logo-img"></a>
      <nav class="nav" aria-label="{c['nav_aria']}">
        <button type="button" class="nav-toggle" aria-label="{c['menu_aria']}" aria-expanded="false" hidden>
          <span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span>
        </button>
        <ul class="nav-list">
          <li><a href="index.html#features">{c['features_nav']}</a></li>
          <li><a href="index.html#download">{c['get_app']}</a></li>
          <li><a href="support.html">{c['support_nav']}</a></li>
          <li><a href="privacy.html">{c['privacy_nav']}</a></li>
          <li><a href="terms.html">{c['terms_nav']}</a></li>
        </ul>
      </nav>
    </div>
  </header>
  <main id="main" class="main page-main">
    <article class="container page-content">
      <h1 class="page-title">{c['support_h1']}</h1>
      <p class="page-meta">{t['support_meta']}</p>
      <section class="prose">
        <h2>{t['contact_h2']}</h2>
        <p>{t['contact_p']}</p>
        <p><a href="mailto:bonney977@gmail.com">bonney977@gmail.com</a></p>
        <p>{t['contact_reply']}</p>
        <h2>{t['faq_h2']}</h2>
        <h3>{t['q1']}</h3>
        <p>{t['a1']}</p>
        <h3>{t['q2']}</h3>
        <p>{t['a2']}</p>
        <h3>{t['q3']}</h3>
        <p>{t['a3']}</p>
        <h3>{t['q4']}</h3>
        <p>{t['a4']}</p>
        <p><a href="index.html">{c['back']}</a></p>
      </section>
    </article>
  </main>
  <footer class="site-footer" role="contentinfo">
    <div class="container footer-inner">
      <p class="footer-brand">OneGrab</p>
      <p class="footer-legal">
        <a href="support.html">{c['footer_support']}</a><span class="footer-sep">·</span>
        <a href="privacy.html">{c['footer_privacy']}</a><span class="footer-sep">·</span>
        <a href="terms.html">{c['footer_terms']}</a>
      </p>
      <div class="lang-picker-wrap"><div id="lang-picker" class="lang-picker"></div></div>
    </div>
  </footer>
  <script src="../js/main.js"></script>
  <script src="../js/lang-picker.js"></script>
</body>
</html>
"""


def terms_html(c: dict, t: dict) -> str:
    return f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0JNXZ901GN"></script>
  <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag('js', new Date()); gtag('config', 'G-0JNXZ901GN');</script>
  <meta name="description" content="{c['terms_h1']} - OneGrab">
  <title>{c['terms_title']}</title>
  <link rel="icon" type="image/svg+xml" href="../favicon/favicon.svg">
  <link rel="manifest" href="../favicon/site.webmanifest">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/base.css">
  <link rel="stylesheet" href="../css/layout.css">
  <link rel="stylesheet" href="../css/components.css">
  <link rel="stylesheet" href="../css/pages.css">
</head>
<body>
  <header class="site-header" role="banner">
    <div class="container header-inner">
      <a href="index.html" class="logo" aria-label="{c['home_aria']}"><img src="../assets/nameGlow.png" alt="OneGrab" class="logo-img"></a>
      <nav class="nav" aria-label="{c['nav_aria']}">
        <button type="button" class="nav-toggle" aria-label="{c['menu_aria']}" aria-expanded="false" hidden>
          <span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span>
        </button>
        <ul class="nav-list">
          <li><a href="index.html#features">{c['features_nav']}</a></li>
          <li><a href="index.html#download">{c['download_nav']}</a></li>
          <li><a href="support.html">{c['support_nav']}</a></li>
          <li><a href="privacy.html">{c['privacy_nav']}</a></li>
          <li><a href="terms.html">{c['terms_nav']}</a></li>
        </ul>
      </nav>
    </div>
  </header>
  <main id="main" class="main page-main">
    <article class="container page-content">
      <h1 class="page-title">{c['terms_h1']}</h1>
      <p class="page-meta">{c['terms_meta']}</p>
      <section class="prose">
        <h2>{t['agreement_h2']}</h2>
        <p>{t['agreement_p']}</p>
        <h2>{t['use_h2']}</h2>
        <p>{t['use_p']}</p>
        <h2>{t['sub_h2']}</h2>
        <p>{t['sub_p']}</p>
        <h2>{t['disc_h2']}</h2>
        <p>{t['disc_p']}</p>
        <h2>{t['liab_h2']}</h2>
        <p>{t['liab_p']}</p>
        <h2>{t['chg_h2']}</h2>
        <p>{t['chg_p']}</p>
        <p><a href="index.html">{c['back']}</a></p>
      </section>
    </article>
  </main>
  <footer class="site-footer" role="contentinfo">
    <div class="container footer-inner">
      <p class="footer-brand">OneGrab</p>
      <p class="footer-legal">
        <a href="support.html">{c['footer_support']}</a><span class="footer-sep">·</span>
        <a href="privacy.html">{c['footer_privacy']}</a><span class="footer-sep">·</span>
        <a href="terms.html">{c['footer_terms']}</a>
      </p>
      <div class="lang-picker-wrap"><div id="lang-picker" class="lang-picker"></div></div>
    </div>
  </footer>
  <script src="../js/main.js"></script>
  <script src="../js/lang-picker.js"></script>
</body>
</html>
"""


def main() -> None:
    if not TRANS_PATH.exists():
        raise SystemExit(f"Missing {TRANS_PATH}")
    for loc in LOCALES:
        c = extract_chrome(loc)
        t = content_for(loc)
        dest = ROOT / loc
        dest.mkdir(exist_ok=True)
        (dest / "index.html").write_text(index_html(c, t), encoding="utf-8")
        (dest / "support.html").write_text(support_html(c, t), encoding="utf-8")
        (dest / "terms.html").write_text(terms_html(c, t), encoding="utf-8")
        print("ok", loc)


if __name__ == "__main__":
    main()
