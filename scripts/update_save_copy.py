#!/usr/bin/env python3
"""Rewrite Website marketing copy to save-for-later (App Review-safe) messaging."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path("/Users/alexriakhin/Developer/OneGrabApp/Website")

# Per-locale marketing strings. App Store CTA buttons stay as-is (get the app).
COPY: dict[str, dict[str, str]] = {
    "en": {
        "meta": "OneGrab — Save your favorite TikToks, Threads, and clips for later. Copy a link, tap Save, keep it in Photos.",
        "title": "OneGrab — Save clips for later",
        "label": "Save TikToks, Threads & clips for later",
        "desc": "Copy a link from TikTok, Instagram, YouTube Shorts, or 20+ other apps. Open OneGrab and tap Save — then keep it in Photos so you can come back anytime.",
        "f1t": "One tap from clipboard",
        "f1d": "Copy a link, open the app, tap Save. No pasting into fields.",
        "f2t": "All your platforms",
        "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch and more.",
        "f3t": "Save to Photos",
        "f3d": "Keep your saves in the Photo Library. Come back anytime.",
        "cta": "Ready to save?",
        "cta_desc": "Get OneGrab on iPhone, iPad, or Mac. Free to try.",
    },
    "en-GB": {
        "meta": "OneGrab — Save your favourite TikToks, Threads, and clips for later. Copy a link, tap Save, keep it in Photos.",
        "title": "OneGrab — Save clips for later",
        "label": "Save TikToks, Threads & clips for later",
        "desc": "Copy a link from TikTok, Instagram, YouTube Shorts, or 20+ other apps. Open OneGrab and tap Save — then keep it in Photos so you can come back anytime.",
        "f1t": "One tap from clipboard",
        "f1d": "Copy a link, open the app, tap Save. No pasting into fields.",
        "f2t": "All your platforms",
        "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch and more.",
        "f3t": "Save to Photos",
        "f3d": "Keep your saves in the Photo Library. Come back anytime.",
        "cta": "Ready to save?",
        "cta_desc": "Get OneGrab on iPhone, iPad, or Mac. Free to try.",
    },
}

# British English variants share en-GB
for loc in ("en-AU", "en-CA"):
    COPY[loc] = COPY["en-GB"]

COPY.update(
    {
        "de-DE": {
            "meta": "OneGrab — Speichere TikToks, Threads und Clips für später. Link kopieren, Speichern tippen, in Fotos behalten.",
            "title": "OneGrab — Clips für später speichern",
            "label": "TikToks, Threads & Clips für später speichern",
            "desc": "Kopiere einen Link von TikTok, Instagram, YouTube Shorts oder 20+ anderen Apps. Öffne OneGrab und tippe auf Speichern — dann behalte ihn in Fotos, um jederzeit zurückzukommen.",
            "f1t": "Ein Tipp aus der Zwischenablage",
            "f1d": "Link kopieren, App öffnen, Speichern tippen. Kein Einfügen in Felder.",
            "f2t": "Alle deine Plattformen",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch und mehr.",
            "f3t": "In Fotos speichern",
            "f3d": "Speicherungen in der Mediathek behalten. Jederzeit zurückkommen.",
            "cta": "Bereit zum Speichern?",
            "cta_desc": "OneGrab für iPhone, iPad oder Mac. Kostenlos testen.",
        },
        "fr-FR": {
            "meta": "OneGrab — Enregistrez vos TikToks, Threads et clips pour plus tard. Copiez un lien, touchez Enregistrer, gardez-le dans Photos.",
            "title": "OneGrab — Enregistrer des clips pour plus tard",
            "label": "Enregistrez TikToks, Threads et clips pour plus tard",
            "desc": "Copiez un lien depuis TikTok, Instagram, YouTube Shorts ou 20+ autres apps. Ouvrez OneGrab et touchez Enregistrer — puis gardez-le dans Photos pour y revenir quand vous voulez.",
            "f1t": "Un tap depuis le presse-papiers",
            "f1d": "Copiez un lien, ouvrez l’app, touchez Enregistrer. Pas de collage dans des champs.",
            "f2t": "Toutes vos plateformes",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch et plus.",
            "f3t": "Enregistrer dans Photos",
            "f3d": "Gardez vos enregistrements dans la photothèque. Revenez quand vous voulez.",
            "cta": "Prêt à enregistrer ?",
            "cta_desc": "OneGrab sur iPhone, iPad ou Mac. Essai gratuit.",
        },
        "es-ES": {
            "meta": "OneGrab — Guarda tus TikToks, Threads y clips para más tarde. Copia un enlace, toca Guardar, guárdalo en Fotos.",
            "title": "OneGrab — Guardar clips para más tarde",
            "label": "Guarda TikToks, Threads y clips para más tarde",
            "desc": "Copia un enlace de TikTok, Instagram, YouTube Shorts u otras 20+ apps. Abre OneGrab y toca Guardar — luego guárdalo en Fotos para volver cuando quieras.",
            "f1t": "Un toque desde el portapapeles",
            "f1d": "Copia un enlace, abre la app, toca Guardar. Sin pegar en campos.",
            "f2t": "Todas tus plataformas",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch y más.",
            "f3t": "Guardar en Fotos",
            "f3d": "Mantén tus guardados en la fototeca. Vuelve cuando quieras.",
            "cta": "¿Listo para guardar?",
            "cta_desc": "OneGrab en iPhone, iPad o Mac. Prueba gratis.",
        },
        "it": {
            "meta": "OneGrab — Salva i tuoi TikTok, Threads e clip per dopo. Copia un link, tocca Salva, tienilo in Foto.",
            "title": "OneGrab — Salva clip per dopo",
            "label": "Salva TikTok, Threads e clip per dopo",
            "desc": "Copia un link da TikTok, Instagram, YouTube Shorts o altre 20+ app. Apri OneGrab e tocca Salva — poi tienilo in Foto per tornarci quando vuoi.",
            "f1t": "Un tocco dagli appunti",
            "f1d": "Copia un link, apri l’app, tocca Salva. Niente incolla nei campi.",
            "f2t": "Tutte le tue piattaforme",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch e altro.",
            "f3t": "Salva in Foto",
            "f3d": "Tieni i salvataggi nella Fototeca. Torna quando vuoi.",
            "cta": "Pronto a salvare?",
            "cta_desc": "OneGrab su iPhone, iPad o Mac. Prova gratis.",
        },
        "pt-BR": {
            "meta": "OneGrab — Salve seus TikToks, Threads e clips para depois. Copie um link, toque em Salvar, guarde em Fotos.",
            "title": "OneGrab — Salvar clips para depois",
            "label": "Salve TikToks, Threads e clips para depois",
            "desc": "Copie um link do TikTok, Instagram, YouTube Shorts ou mais de 20 apps. Abra o OneGrab e toque em Salvar — depois guarde em Fotos para voltar quando quiser.",
            "f1t": "Um toque da área de transferência",
            "f1d": "Copie um link, abra o app, toque em Salvar. Sem colar em campos.",
            "f2t": "Todas as suas plataformas",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch e mais.",
            "f3t": "Salvar em Fotos",
            "f3d": "Mantenha seus saves na biblioteca de Fotos. Volte quando quiser.",
            "cta": "Pronto para salvar?",
            "cta_desc": "OneGrab no iPhone, iPad ou Mac. Teste grátis.",
        },
        "pt-PT": {
            "meta": "OneGrab — Guarde os seus TikToks, Threads e clips para mais tarde. Copie uma ligação, toque em Guardar, mantenha em Fotografias.",
            "title": "OneGrab — Guardar clips para mais tarde",
            "label": "Guarde TikToks, Threads e clips para mais tarde",
            "desc": "Copie uma ligação do TikTok, Instagram, YouTube Shorts ou mais de 20 apps. Abra o OneGrab e toque em Guardar — depois mantenha em Fotografias para voltar quando quiser.",
            "f1t": "Um toque da área de transferência",
            "f1d": "Copie uma ligação, abra a app, toque em Guardar. Sem colar em campos.",
            "f2t": "Todas as suas plataformas",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch e mais.",
            "f3t": "Guardar em Fotografias",
            "f3d": "Mantenha os guardados na fototeca. Volte quando quiser.",
            "cta": "Pronto para guardar?",
            "cta_desc": "OneGrab no iPhone, iPad ou Mac. Experimente grátis.",
        },
        "nl-NL": {
            "meta": "OneGrab — Bewaar je TikToks, Threads en clips voor later. Kopieer een link, tik op Bewaar, houd het in Foto’s.",
            "title": "OneGrab — Clips bewaren voor later",
            "label": "Bewaar TikToks, Threads & clips voor later",
            "desc": "Kopieer een link van TikTok, Instagram, YouTube Shorts of 20+ andere apps. Open OneGrab en tik op Bewaar — bewaar het daarna in Foto’s zodat je later terug kunt.",
            "f1t": "Eén tik vanaf het klembord",
            "f1d": "Kopieer een link, open de app, tik op Bewaar. Geen plakken in velden.",
            "f2t": "Al je platforms",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch en meer.",
            "f3t": "Bewaar in Foto’s",
            "f3d": "Houd je saves in de Fotobibliotheek. Kom wanneer je wilt terug.",
            "cta": "Klaar om te bewaren?",
            "cta_desc": "OneGrab op iPhone, iPad of Mac. Gratis proberen.",
        },
        "pl": {
            "meta": "OneGrab — Zapisuj TikToki, Threads i klipy na później. Skopiuj link, stuknij Zapisz, trzymaj w Zdjęciach.",
            "title": "OneGrab — Zapisuj klipy na później",
            "label": "Zapisuj TikToki, Threads i klipy na później",
            "desc": "Skopiuj link z TikToka, Instagrama, YouTube Shorts lub 20+ innych aplikacji. Otwórz OneGrab i stuknij Zapisz — potem trzymaj w Zdjęciach, by wrócić kiedy chcesz.",
            "f1t": "Jedno stuknięcie ze schowka",
            "f1d": "Skopiuj link, otwórz aplikację, stuknij Zapisz. Bez wklejania w pola.",
            "f2t": "Wszystkie Twoje platformy",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch i inne.",
            "f3t": "Zapisz w Zdjęciach",
            "f3d": "Trzymaj zapisane w bibliotece Zdjęć. Wróć kiedy chcesz.",
            "cta": "Gotowy, by zapisać?",
            "cta_desc": "OneGrab na iPhonie, iPadzie lub Macu. Wypróbuj za darmo.",
        },
        "ru": {
            "meta": "OneGrab — Сохраняйте TikTok, Threads и клипы на потом. Скопируйте ссылку, нажмите «Сохранить», оставьте в Фото.",
            "title": "OneGrab — Сохраняйте клипы на потом",
            "label": "Сохраняйте TikTok, Threads и клипы на потом",
            "desc": "Скопируйте ссылку из TikTok, Instagram, YouTube Shorts или 20+ других приложений. Откройте OneGrab и нажмите «Сохранить» — затем оставьте в Фото, чтобы вернуться в любой момент.",
            "f1t": "Один тап из буфера",
            "f1d": "Скопируйте ссылку, откройте приложение, нажмите «Сохранить». Без вставки в поля.",
            "f2t": "Все ваши платформы",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch и другие.",
            "f3t": "Сохранить в Фото",
            "f3d": "Храните сохранения в медиатеке. Возвращайтесь когда угодно.",
            "cta": "Готовы сохранить?",
            "cta_desc": "OneGrab на iPhone, iPad или Mac. Попробуйте бесплатно.",
        },
        "uk": {
            "meta": "OneGrab — Зберігайте TikTok, Threads і кліпи на потім. Скопіюйте посилання, натисніть «Зберегти», тримайте у Фото.",
            "title": "OneGrab — Зберігайте кліпи на потім",
            "label": "Зберігайте TikTok, Threads і кліпи на потім",
            "desc": "Скопіюйте посилання з TikTok, Instagram, YouTube Shorts або 20+ інших застосунків. Відкрийте OneGrab і натисніть «Зберегти» — потім тримайте у Фото, щоб повернутися будь-коли.",
            "f1t": "Один дотик з буфера",
            "f1d": "Скопіюйте посилання, відкрийте застосунок, натисніть «Зберегти». Без вставки в поля.",
            "f2t": "Усі ваші платформи",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch та інші.",
            "f3t": "Зберегти у Фото",
            "f3d": "Тримайте збереження в медіатеці. Повертайтеся будь-коли.",
            "cta": "Готові зберегти?",
            "cta_desc": "OneGrab на iPhone, iPad або Mac. Спробуйте безкоштовно.",
        },
        "ja": {
            "meta": "OneGrab — TikTokやThreads、クリップをあとで見返せるように保存。リンクをコピーして保存をタップ、写真に残そう。",
            "title": "OneGrab — クリップをあとで保存",
            "label": "TikTok・Threads・クリップをあとで保存",
            "desc": "TikTok、Instagram、YouTube Shortsなど20以上のアプリからリンクをコピー。OneGrabを開いて「保存」をタップ — 写真に残していつでも見返せます。",
            "f1t": "クリップボードからワンタップ",
            "f1d": "リンクをコピーしてアプリを開き、「保存」をタップ。欄への貼り付け不要。",
            "f2t": "好きなプラットフォーム",
            "f2d": "TikTok、Instagram、YouTube Shorts、X、Facebook、Reddit、Twitchなど。",
            "f3t": "写真に保存",
            "f3d": "保存した内容を写真ライブラリに。いつでも戻ってこれます。",
            "cta": "保存する準備はできた？",
            "cta_desc": "iPhone・iPad・MacでOneGrab。無料で試せます。",
        },
        "ko": {
            "meta": "OneGrab — TikTok, Threads, 클립을 나중에 보려고 저장하세요. 링크 복사, 저장 탭, 사진에 보관.",
            "title": "OneGrab — 클립을 나중에 저장",
            "label": "TikTok, Threads, 클립을 나중에 저장",
            "desc": "TikTok, Instagram, YouTube Shorts 등 20개 이상 앱에서 링크를 복사하세요. OneGrab을 열고 저장을 탭한 뒤 — 사진에 남겨 언제든 다시 볼 수 있어요.",
            "f1t": "클립보드에서 한 번 탭",
            "f1d": "링크를 복사하고 앱을 연 뒤 저장을 탭하세요. 필드에 붙여넣을 필요 없어요.",
            "f2t": "모든 플랫폼",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch 등.",
            "f3t": "사진에 저장",
            "f3d": "사진 보관함에 저장해 두세요. 언제든 다시 오세요.",
            "cta": "저장할 준비됐나요?",
            "cta_desc": "iPhone, iPad, Mac용 OneGrab. 무료로 시작해 보세요.",
        },
        "zh-Hans": {
            "meta": "OneGrab — 把 TikTok、Threads 和精彩片段留到以后看。复制链接，点储存，保存在照片。",
            "title": "OneGrab — 把片段留到以后",
            "label": "把 TikTok、Threads 和片段留到以后",
            "desc": "从 TikTok、Instagram、YouTube Shorts 或 20+ 款应用复制链接。打开 OneGrab，点按“储存”——再保存在照片，随时回来看。",
            "f1t": "剪贴板一键储存",
            "f1d": "复制链接，打开应用，点按储存。无需粘贴到输入框。",
            "f2t": "你常用的平台",
            "f2d": "TikTok、Instagram、YouTube Shorts、X、Facebook、Reddit、Twitch 等。",
            "f3t": "储存到照片",
            "f3d": "把储存内容留在照片图库。随时回来。",
            "cta": "准备好储存了吗？",
            "cta_desc": "在 iPhone、iPad 或 Mac 上使用 OneGrab。免费试用。",
        },
        "zh-Hant": {
            "meta": "OneGrab — 把 TikTok、Threads 和精彩片段留到以後看。複製連結，點儲存，保存在照片。",
            "title": "OneGrab — 把片段留到以後",
            "label": "把 TikTok、Threads 和片段留到以後",
            "desc": "從 TikTok、Instagram、YouTube Shorts 或 20 多個 app 複製連結。打開 OneGrab，點一下「儲存」— 再保存在照片，隨時回來看。",
            "f1t": "剪貼簿一鍵儲存",
            "f1d": "複製連結，打開 app，點儲存。無需貼到欄位。",
            "f2t": "你常用的平台",
            "f2d": "TikTok、Instagram、YouTube Shorts、X、Facebook、Reddit、Twitch 等。",
            "f3t": "儲存到照片",
            "f3d": "把儲存內容留在照片圖庫。隨時回來。",
            "cta": "準備好儲存了嗎？",
            "cta_desc": "在 iPhone、iPad 或 Mac 上使用 OneGrab。免費試用。",
        },
        "ar-SA": {
            "meta": "OneGrab — احفظ مقاطع TikTok وThreads لمشاهدتها لاحقًا. انسخ رابطًا، اضغط حفظ، واحتفظ به في الصور.",
            "title": "OneGrab — احفظ المقاطع لوقت لاحق",
            "label": "احفظ TikTok وThreads والمقاطع لوقت لاحق",
            "desc": "انسخ رابطًا من TikTok أو Instagram أو YouTube Shorts أو أكثر من 20 تطبيقًا. افتح OneGrab واضغط حفظ — ثم احتفظ به في الصور لتعود إليه في أي وقت.",
            "f1t": "ضغطة واحدة من الحافظة",
            "f1d": "انسخ رابطًا، افتح التطبيق، اضغط حفظ. بلا لصق في الحقول.",
            "f2t": "كل منصاتك",
            "f2d": "TikTok وInstagram وYouTube Shorts وX وFacebook وReddit وTwitch والمزيد.",
            "f3t": "حفظ في الصور",
            "f3d": "احتفظ بحفظاتك في مكتبة الصور. عُد في أي وقت.",
            "cta": "جاهز للحفظ؟",
            "cta_desc": "OneGrab على iPhone أو iPad أو Mac. جرّبه مجانًا.",
        },
        "he": {
            "meta": "OneGrab — שמרו TikTok, Threads וקליפים להמשך. העתיקו קישור, הקישו שמירה, שמרו בתמונות.",
            "title": "OneGrab — שמרו קליפים להמשך",
            "label": "שמרו TikTok, Threads וקליפים להמשך",
            "desc": "העתיקו קישור מ-TikTok, Instagram, YouTube Shorts או 20+ אפליקציות. פתחו את OneGrab והקישו שמירה — ואז שמרו בתמונות כדי לחזור בכל רגע.",
            "f1t": "מגע אחד מהלוח",
            "f1d": "העתיקו קישור, פתחו את האפליקציה, הקישו שמירה. בלי להדביק בשדות.",
            "f2t": "כל הפלטפורמות שלכם",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch ועוד.",
            "f3t": "שמירה בתמונות",
            "f3d": "שמרו בספריית התמונות. חזרו מתי שתרצו.",
            "cta": "מוכנים לשמור?",
            "cta_desc": "OneGrab ב-iPhone, iPad או Mac. נסו בחינם.",
        },
        "tr": {
            "meta": "OneGrab — TikTok, Threads ve klipleri sonraya kaydedin. Bağlantı kopyalayın, Kaydet’e dokunun, Fotoğraflar’da tutun.",
            "title": "OneGrab — Klipleri sonraya kaydedin",
            "label": "TikTok, Threads ve klipleri sonraya kaydedin",
            "desc": "TikTok, Instagram, YouTube Shorts veya 20+ uygulamadan bir bağlantı kopyalayın. OneGrab’ı açın ve Kaydet’e dokunun — sonra Fotoğraflar’da tutun, istediğiniz zaman geri dönün.",
            "f1t": "Panodan tek dokunuş",
            "f1d": "Bağlantıyı kopyalayın, uygulamayı açın, Kaydet’e dokunun. Alana yapıştırmaya gerek yok.",
            "f2t": "Tüm platformlarınız",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch ve daha fazlası.",
            "f3t": "Fotoğraflar’a kaydet",
            "f3d": "Kayıtlarınızı Fotoğraf Kitaplığı’nda tutun. İstediğiniz zaman geri dönün.",
            "cta": "Kaydetmeye hazır mısınız?",
            "cta_desc": "iPhone, iPad veya Mac’te OneGrab. Ücretsiz deneyin.",
        },
        "vi": {
            "meta": "OneGrab — Lưu TikTok, Threads và clip để xem sau. Sao chép liên kết, chạm Lưu, giữ trong Ảnh.",
            "title": "OneGrab — Lưu clip để xem sau",
            "label": "Lưu TikTok, Threads & clip để xem sau",
            "desc": "Sao chép liên kết từ TikTok, Instagram, YouTube Shorts hoặc hơn 20 ứng dụng khác. Mở OneGrab và chạm Lưu — rồi giữ trong Ảnh để quay lại bất cứ lúc nào.",
            "f1t": "Một chạm từ clipboard",
            "f1d": "Sao chép liên kết, mở app, chạm Lưu. Không cần dán vào ô.",
            "f2t": "Mọi nền tảng của bạn",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch và hơn thế.",
            "f3t": "Lưu vào Ảnh",
            "f3d": "Giữ bản lưu trong Thư viện ảnh. Quay lại bất cứ lúc nào.",
            "cta": "Sẵn sàng lưu?",
            "cta_desc": "OneGrab trên iPhone, iPad hoặc Mac. Dùng thử miễn phí.",
        },
        "th": {
            "meta": "OneGrab — บันทึก TikTok, Threads และคลิปไว้ดูทีหลัง คัดลอกลิงก์ แตะบันทึก เก็บในรูปภาพ",
            "title": "OneGrab — บันทึกคลิปไว้ดูทีหลัง",
            "label": "บันทึก TikTok, Threads และคลิปไว้ดูทีหลัง",
            "desc": "คัดลอกลิงก์จาก TikTok, Instagram, YouTube Shorts หรือแอปอื่นอีก 20+ เปิด OneGrab แล้วแตะบันทึก — จากนั้นเก็บในรูปภาพเพื่อกลับมาดูได้ทุกเมื่อ",
            "f1t": "แตะครั้งเดียวจากคลิปบอร์ด",
            "f1d": "คัดลอกลิงก์ เปิดแอป แตะบันทึก ไม่ต้องวางในช่อง",
            "f2t": "ทุกแพลตฟอร์มของคุณ",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch และอื่น ๆ",
            "f3t": "บันทึกลงรูปภาพ",
            "f3d": "เก็บรายการที่บันทึกไว้ในคลังรูปภาพ กลับมาได้ทุกเมื่อ",
            "cta": "พร้อมบันทึกหรือยัง?",
            "cta_desc": "OneGrab บน iPhone, iPad หรือ Mac ทดลองใช้ฟรี",
        },
        "id": {
            "meta": "OneGrab — Simpan TikTok, Threads, dan klip untuk nanti. Salin tautan, ketuk Simpan, simpan di Foto.",
            "title": "OneGrab — Simpan klip untuk nanti",
            "label": "Simpan TikTok, Threads & klip untuk nanti",
            "desc": "Salin tautan dari TikTok, Instagram, YouTube Shorts, atau 20+ aplikasi lain. Buka OneGrab dan ketuk Simpan — lalu simpan di Foto agar bisa kembali kapan saja.",
            "f1t": "Satu ketuk dari clipboard",
            "f1d": "Salin tautan, buka app, ketuk Simpan. Tanpa menempel di kolom.",
            "f2t": "Semua platform Anda",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch, dan lainnya.",
            "f3t": "Simpan ke Foto",
            "f3d": "Simpan di Perpustakaan Foto. Kembali kapan saja.",
            "cta": "Siap menyimpan?",
            "cta_desc": "OneGrab di iPhone, iPad, atau Mac. Coba gratis.",
        },
        "ms": {
            "meta": "OneGrab — Simpan TikTok, Threads dan klip untuk kemudian. Salin pautan, ketik Simpan, simpan dalam Foto.",
            "title": "OneGrab — Simpan klip untuk kemudian",
            "label": "Simpan TikTok, Threads & klip untuk kemudian",
            "desc": "Salin pautan dari TikTok, Instagram, YouTube Shorts atau 20+ app lain. Buka OneGrab dan ketik Simpan — kemudian simpan dalam Foto supaya anda boleh kembali bila-bila masa.",
            "f1t": "Satu ketikan dari papan klip",
            "f1d": "Salin pautan, buka app, ketik Simpan. Tiada tampal dalam medan.",
            "f2t": "Semua platform anda",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch dan lagi.",
            "f3t": "Simpan ke Foto",
            "f3d": "Simpan dalam Perpustakaan Foto. Kembali bila-bila masa.",
            "cta": "Sedia untuk simpan?",
            "cta_desc": "OneGrab pada iPhone, iPad atau Mac. Cuba percuma.",
        },
        "hi": {
            "meta": "OneGrab — अपने TikTok, Threads और क्लिप बाद के लिए सेव करें। लिंक कॉपी करें, सेव टैप करें, फ़ोटो में रखें।",
            "title": "OneGrab — क्लिप बाद के लिए सेव करें",
            "label": "TikTok, Threads और क्लिप बाद के लिए सेव करें",
            "desc": "TikTok, Instagram, YouTube Shorts या 20+ ऐप्स से लिंक कॉपी करें। OneGrab खोलें और सेव टैप करें — फिर फ़ोटो में रखें ताकि कभी भी वापस आ सकें।",
            "f1t": "क्लिपबोर्ड से एक टैप",
            "f1d": "लिंक कॉपी करें, ऐप खोलें, सेव टैप करें। फ़ील्ड में पेस्ट नहीं।",
            "f2t": "आपके सभी प्लेटफ़ॉर्म",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch और ज़्यादा।",
            "f3t": "फ़ोटो में सेव करें",
            "f3d": "सेव फ़ोटो लाइब्रेरी में रखें। जब चाहें वापस आएँ।",
            "cta": "सेव करने के लिए तैयार?",
            "cta_desc": "iPhone, iPad या Mac पर OneGrab। मुफ़्त आज़माएँ।",
        },
        "sv": {
            "meta": "OneGrab — Spara TikToks, Threads och klipp till senare. Kopiera en länk, tryck Spara, behåll i Bilder.",
            "title": "OneGrab — Spara klipp till senare",
            "label": "Spara TikToks, Threads & klipp till senare",
            "desc": "Kopiera en länk från TikTok, Instagram, YouTube Shorts eller 20+ andra appar. Öppna OneGrab och tryck på Spara — behåll sedan i Bilder så du kan komma tillbaka när som helst.",
            "f1t": "Ett tryck från urklipp",
            "f1d": "Kopiera en länk, öppna appen, tryck Spara. Ingen inklistring i fält.",
            "f2t": "Alla dina plattformar",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch med mera.",
            "f3t": "Spara till Bilder",
            "f3d": "Behåll sparade i fotobiblioteket. Kom tillbaka när du vill.",
            "cta": "Redo att spara?",
            "cta_desc": "OneGrab på iPhone, iPad eller Mac. Prova gratis.",
        },
        "da": {
            "meta": "OneGrab — Gem TikToks, Threads og klip til senere. Kopiér et link, tryk Gem, behold det i Fotos.",
            "title": "OneGrab — Gem klip til senere",
            "label": "Gem TikToks, Threads & klip til senere",
            "desc": "Kopiér et link fra TikTok, Instagram, YouTube Shorts eller 20+ andre apps. Åbn OneGrab og tryk Gem — behold det derefter i Fotos, så du kan vende tilbage når som helst.",
            "f1t": "Et tryk fra udklipsholderen",
            "f1d": "Kopiér et link, åbn appen, tryk Gem. Ingen indsættelse i felter.",
            "f2t": "Alle dine platforme",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch og mere.",
            "f3t": "Gem i Fotos",
            "f3d": "Behold gemte i fotobiblioteket. Vend tilbage når du vil.",
            "cta": "Klar til at gemme?",
            "cta_desc": "OneGrab på iPhone, iPad eller Mac. Prøv gratis.",
        },
        "no": {
            "meta": "OneGrab — Lagre TikToks, Threads og klipp til senere. Kopier en lenke, trykk Lagre, behold i Bilder.",
            "title": "OneGrab — Lagre klipp til senere",
            "label": "Lagre TikToks, Threads & klipp til senere",
            "desc": "Kopier en lenke fra TikTok, Instagram, YouTube Shorts eller 20+ andre apper. Åpne OneGrab og trykk Lagre — behold den deretter i Bilder så du kan komme tilbake når som helst.",
            "f1t": "Ett trykk fra utklippstavlen",
            "f1d": "Kopier en lenke, åpne appen, trykk Lagre. Ingen liming i felt.",
            "f2t": "Alle plattformene dine",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch og mer.",
            "f3t": "Lagre til Bilder",
            "f3d": "Behold lagrede i bildebiblioteket. Kom tilbake når du vil.",
            "cta": "Klar til å lagre?",
            "cta_desc": "OneGrab på iPhone, iPad eller Mac. Prøv gratis.",
        },
        "fi": {
            "meta": "OneGrab — Tallenna TikTokit, Threadsit ja klipit myöhemmäksi. Kopioi linkki, napauta Tallenna, pidä Kuvissa.",
            "title": "OneGrab — Tallenna klipit myöhemmäksi",
            "label": "Tallenna TikTokit, Threadsit & klipit myöhemmäksi",
            "desc": "Kopioi linkki TikTokista, Instagramista, YouTube Shortsista tai 20+ muusta sovelluksesta. Avaa OneGrab ja napauta Tallenna — pidä se sitten Kuvissa, jotta voit palata milloin tahansa.",
            "f1t": "Yksi napautus leikepöydältä",
            "f1d": "Kopioi linkki, avaa sovellus, napauta Tallenna. Ei liittämistä kenttiin.",
            "f2t": "Kaikki alustasi",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch ja muut.",
            "f3t": "Tallenna Kuviin",
            "f3d": "Pidä tallennukset kuvakirjastossa. Palaa milloin tahansa.",
            "cta": "Valmis tallentamaan?",
            "cta_desc": "OneGrab iPhonella, iPadilla tai Macilla. Kokeile ilmaiseksi.",
        },
        "cs": {
            "meta": "OneGrab — Ukládejte TikToky, Threads a klipy na později. Zkopírujte odkaz, klepněte na Uložit, nechte ve Fotkách.",
            "title": "OneGrab — Ukládejte klipy na později",
            "label": "Ukládejte TikToky, Threads a klipy na později",
            "desc": "Zkopírujte odkaz z TikToku, Instagramu, YouTube Shorts nebo 20+ dalších aplikací. Otevřete OneGrab a klepněte na Uložit — pak nechte ve Fotkách, abyste se mohli kdykoli vrátit.",
            "f1t": "Jedno klepnutí ze schránky",
            "f1d": "Zkopírujte odkaz, otevřete aplikaci, klepněte na Uložit. Bez vkládání do polí.",
            "f2t": "Všechny vaše platformy",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch a další.",
            "f3t": "Uložit do Fotek",
            "f3d": "Uložte si je do knihovny Fotky. Vraťte se kdykoli.",
            "cta": "Připraveni uložit?",
            "cta_desc": "OneGrab na iPhonu, iPadu nebo Macu. Vyzkoušejte zdarma.",
        },
        "sk": {
            "meta": "OneGrab — Ukladajte TikToky, Threads a klipy na neskôr. Skopírujte odkaz, klepnite na Uložiť, nechajte vo Fotkách.",
            "title": "OneGrab — Ukladajte klipy na neskôr",
            "label": "Ukladajte TikToky, Threads a klipy na neskôr",
            "desc": "Skopírujte odkaz z TikToku, Instagramu, YouTube Shorts alebo 20+ ďalších aplikácií. Otvorte OneGrab a klepnite na Uložiť — potom nechajte vo Fotkách, aby ste sa mohli kedykoľvek vrátiť.",
            "f1t": "Jedno klepnutie zo schránky",
            "f1d": "Skopírujte odkaz, otvorte aplikáciu, klepnite na Uložiť. Bez vkladania do polí.",
            "f2t": "Všetky vaše platformy",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch a ďalšie.",
            "f3t": "Uložiť do Fotiek",
            "f3d": "Uložte si ich do knižnice Fotky. Vráťte sa kedykoľvek.",
            "cta": "Pripravení uložiť?",
            "cta_desc": "OneGrab na iPhone, iPade alebo Macu. Vyskúšajte zadarmo.",
        },
        "hu": {
            "meta": "OneGrab — Mentse el a TikTokokat, Threadseket és klipeket későbbre. Másoljon egy linket, koppintson a Mentés gombra, tartsa a Fotókban.",
            "title": "OneGrab — Klipek mentése későbbre",
            "label": "Mentse el a TikTokokat, Threadseket és klipeket későbbre",
            "desc": "Másoljon egy linket a TikTokról, Instagramról, YouTube Shortsról vagy 20+ más alkalmazásból. Nyissa meg az OneGrabot, és koppintson a Mentés gombra — majd tartsa a Fotókban, hogy bármikor visszatérhessen.",
            "f1t": "Egy koppintás a vágólapról",
            "f1d": "Másoljon egy linket, nyissa meg az appot, koppintson a Mentés gombra. Nincs beillesztés mezőkbe.",
            "f2t": "Minden platformja",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch és még több.",
            "f3t": "Mentés a Fotókba",
            "f3d": "Tartsa a mentéseket a Fotókönyvtárban. Térjen vissza bármikor.",
            "cta": "Készen áll a mentésre?",
            "cta_desc": "OneGrab iPhone-on, iPaden vagy Macen. Próbálja ki ingyen.",
        },
        "ro": {
            "meta": "OneGrab — Salvează TikTok-uri, Threads și clipuri pentru mai târziu. Copiază un link, atinge Salvare, păstrează în Poze.",
            "title": "OneGrab — Salvează clipuri pentru mai târziu",
            "label": "Salvează TikTok-uri, Threads și clipuri pentru mai târziu",
            "desc": "Copiază un link din TikTok, Instagram, YouTube Shorts sau peste 20 de alte aplicații. Deschide OneGrab și atinge Salvare — apoi păstrează-l în Poze ca să te întorci oricând.",
            "f1t": "O atingere din clipboard",
            "f1d": "Copiază un link, deschide aplicația, atinge Salvare. Fără lipire în câmpuri.",
            "f2t": "Toate platformele tale",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch și altele.",
            "f3t": "Salvare în Poze",
            "f3d": "Păstrează salvările în biblioteca Foto. Întoarce-te oricând.",
            "cta": "Gata de salvat?",
            "cta_desc": "OneGrab pe iPhone, iPad sau Mac. Încearcă gratuit.",
        },
        "el": {
            "meta": "OneGrab — Αποθηκεύστε TikTok, Threads και κλιπ για αργότερα. Αντιγράψτε έναν σύνδεσμο, πατήστε Αποθήκευση, κρατήστε το στις Φωτογραφίες.",
            "title": "OneGrab — Αποθηκεύστε κλιπ για αργότερα",
            "label": "Αποθηκεύστε TikTok, Threads και κλιπ για αργότερα",
            "desc": "Αντιγράψτε έναν σύνδεσμο από TikTok, Instagram, YouTube Shorts ή 20+ άλλες εφαρμογές. Ανοίξτε το OneGrab και πατήστε Αποθήκευση — μετά κρατήστε το στις Φωτογραφίες για να επιστρέψετε όποτε θέλετε.",
            "f1t": "Ένα πάτημα από το πρόχειρο",
            "f1d": "Αντιγράψτε έναν σύνδεσμο, ανοίξτε την εφαρμογή, πατήστε Αποθήκευση. Χωρίς επικόλληση σε πεδία.",
            "f2t": "Όλες οι πλατφόρμες σας",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch και άλλα.",
            "f3t": "Αποθήκευση στις Φωτογραφίες",
            "f3d": "Κρατήστε τις αποθηκεύσεις στη βιβλιοθήκη Φωτογραφιών. Επιστρέψτε όποτε θέλετε.",
            "cta": "Έτοιμοι να αποθηκεύσετε;",
            "cta_desc": "OneGrab σε iPhone, iPad ή Mac. Δοκιμάστε δωρεάν.",
        },
        "hr": {
            "meta": "OneGrab — Spremite TikTokove, Threads i isječke za kasnije. Kopirajte poveznicu, dodirnite Spremi, držite u Fotografijama.",
            "title": "OneGrab — Spremite isječke za kasnije",
            "label": "Spremite TikTokove, Threads i isječke za kasnije",
            "desc": "Kopirajte poveznicu s TikToka, Instagrama, YouTube Shortsa ili 20+ drugih aplikacija. Otvorite OneGrab i dodirnite Spremi — zatim držite u Fotografijama da se možete vratiti kad god poželite.",
            "f1t": "Jedan dodir s međuspremnika",
            "f1d": "Kopirajte poveznicu, otvorite aplikaciju, dodirnite Spremi. Bez lijepljenja u polja.",
            "f2t": "Sve vaše platforme",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch i više.",
            "f3t": "Spremi u Fotografije",
            "f3d": "Držite spremljeno u biblioteci Fotografija. Vratite se kad god poželite.",
            "cta": "Spremni za spremanje?",
            "cta_desc": "OneGrab na iPhoneu, iPadu ili Macu. Isprobajte besplatno.",
        },
        "ca": {
            "meta": "OneGrab — Desa els teus TikToks, Threads i clips per més tard. Copia un enllaç, toca Desa, guarda’l a Fotos.",
            "title": "OneGrab — Desa clips per més tard",
            "label": "Desa TikToks, Threads i clips per més tard",
            "desc": "Copia un enllaç de TikTok, Instagram, YouTube Shorts o més de 20 apps. Obre OneGrab i toca Desa — després guarda’l a Fotos per tornar-hi quan vulguis.",
            "f1t": "Un toc des del porta-retalls",
            "f1d": "Copia un enllaç, obre l’app, toca Desa. Sense enganxar en camps.",
            "f2t": "Totes les teves plataformes",
            "f2d": "TikTok, Instagram, YouTube Shorts, X, Facebook, Reddit, Twitch i més.",
            "f3t": "Desar a Fotos",
            "f3d": "Mantén els desats a la fototeca. Torna-hi quan vulguis.",
            "cta": "Preparat per desar?",
            "cta_desc": "OneGrab a l’iPhone, l’iPad o el Mac. Prova’l gratis.",
        },
    }
)

COPY["fr-CA"] = COPY["fr-FR"]
COPY["es-MX"] = {
    **COPY["es-ES"],
    "desc": "Copia un enlace de TikTok, Instagram, YouTube Shorts u otras 20+ apps. Abre OneGrab y toca Guardar — luego guárdalo en Fotos para volver cuando quieras.",
}


def locale_key(path: Path) -> str:
    if path.parent.name == "Website":
        return "en"
    return path.parent.name


def replace_once(html: str, pattern: str, repl: str, flags: int = 0) -> str:
    new, n = re.subn(pattern, repl, html, count=1, flags=flags)
    if n != 1:
        raise RuntimeError(f"Expected 1 match for {pattern!r}, got {n}")
    return new


def patch_index(html: str, c: dict[str, str]) -> str:
    html = replace_once(
        html,
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{c["meta"]}">',
    )
    html = replace_once(html, r"<title>[^<]*</title>", f"<title>{c['title']}</title>")
    html = replace_once(
        html,
        r'<p class="hero-label">[^<]*</p>',
        f'<p class="hero-label">{c["label"]}</p>',
    )
    # hero-desc may be single-line or multi-line
    html = replace_once(
        html,
        r'<p class="hero-desc">.*?</p>',
        f'<p class="hero-desc">{c["desc"]}</p>',
        flags=re.S,
    )
    # feature cards: three feature-desc blocks — replace by title+desc pairs more carefully
    # Match feature blocks in order
    feature_pattern = re.compile(
        r'(<h3 class="feature-title">)(.*?)(</h3>\s*<p class="feature-desc">)(.*?)(</p>)',
        re.S,
    )
    replacements = [
        (c["f1t"], c["f1d"]),
        (c["f2t"], c["f2d"]),
        (c["f3t"], c["f3d"]),
    ]
    parts: list[str] = []
    last = 0
    for i, m in enumerate(feature_pattern.finditer(html)):
        if i >= len(replacements):
            break
        title, desc = replacements[i]
        parts.append(html[last : m.start()])
        parts.append(f'{m.group(1)}{title}{m.group(3)}{desc}{m.group(5)}')
        last = m.end()
    if last == 0:
        raise RuntimeError("No feature cards found")
    html = "".join(parts) + html[last:]

    html = replace_once(
        html,
        r'<h2 id="cta-heading" class="cta-title">[^<]*</h2>',
        f'<h2 id="cta-heading" class="cta-title">{c["cta"]}</h2>',
    )
    html = replace_once(
        html,
        r'<p class="cta-desc">[^<]*</p>',
        f'<p class="cta-desc">{c["cta_desc"]}</p>',
    )
    return html


SUPPORT_EN = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0JNXZ901GN"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-0JNXZ901GN');
  </script>
  <meta name="description" content="OneGrab Support — Get help with saves, subscriptions, and more.">
  <title>Support - OneGrab</title>
  <link rel="icon" type="image/svg+xml" href="favicon/favicon.svg">
  <link rel="manifest" href="favicon/site.webmanifest">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/variables.css">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/layout.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/pages.css">
</head>
<body>
  <header class="site-header" role="banner">
    <div class="container header-inner">
      <a href="index.html" class="logo" aria-label="OneGrab home">
        <img src="assets/nameGlow.png" alt="OneGrab" class="logo-img">
      </a>
      <nav class="nav" aria-label="Main">
        <button type="button" class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" hidden>
          <span class="nav-toggle-bar"></span>
          <span class="nav-toggle-bar"></span>
          <span class="nav-toggle-bar"></span>
        </button>
        <ul class="nav-list">
          <li><a href="index.html#features">Features</a></li>
          <li><a href="index.html#download">Get the app</a></li>
          <li><a href="support.html">Support</a></li>
          <li><a href="privacy.html">Privacy</a></li>
          <li><a href="terms.html">Terms</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main id="main" class="main page-main">
    <article class="container page-content">
      <h1 class="page-title">Support</h1>
      <p class="page-meta">We’re here to help.</p>

      <section class="prose">
        <h2>Contact us</h2>
        <p>For questions about OneGrab, saves, subscriptions, or anything else, reach out by email:</p>
        <p>
          <a href="mailto:bonney977@gmail.com">bonney977@gmail.com</a>
        </p>
        <p>We’ll do our best to get back to you within a few business days.</p>

        <h2>Frequently asked questions</h2>

        <h3>How do I save a link?</h3>
        <p>Copy a link from TikTok, Threads, Instagram, or another supported app, open OneGrab, and tap <strong>Save from Clipboard</strong>. Customize your save, then keep it in Photos — or share it right away.</p>

        <h3>Which platforms are supported?</h3>
        <p>OneGrab works with many services, including TikTok, Instagram, YouTube Shorts, X (Twitter), Facebook, Reddit, and more. If a link isn’t supported, the app will let you know.</p>

        <h3>How do I restore my subscription?</h3>
        <p>Open OneGrab, tap the settings (gear) icon, then <strong>Restore purchase</strong>. Your subscription will be restored if it’s still active.</p>

        <h3>Saving isn’t working. What should I try?</h3>
        <p>Make sure you’ve copied a direct link (not a general profile or feed URL). Check your internet connection and try again. If it still fails, email us with the link and we’ll look into it.</p>

        <p><a href="index.html">← Back to OneGrab</a></p>
      </section>
    </article>
  </main>

  <footer class="site-footer" role="contentinfo">
    <div class="container footer-inner">
      <p class="footer-brand">OneGrab</p>
      <p class="footer-legal">
        <a href="support.html">Support</a>
        <span class="footer-sep">·</span>
        <a href="privacy.html">Privacy Policy</a>
        <span class="footer-sep">·</span>
        <a href="terms.html">Terms of Use</a>
      </p>
      <div class="lang-picker-wrap"><div id="lang-picker" class="lang-picker"></div></div>
    </div>
  </footer>
  <script src="js/main.js"></script>
  <script src="js/lang-picker.js"></script>
</body>
</html>
"""


def patch_support_locale(html: str) -> str:
    """Light-touch replacements for localized support pages."""
    replacements = [
        (r"How do I download a video\?", "How do I save a link?"),
        (
            r"Copy the video link from the app \(TikTok, Instagram, YouTube Shorts, etc\.\), open OneGrab, and tap <strong>Download from Clipboard</strong>\. When the download finishes, you can save it to Photos from the Downloads list\.",
            "Copy a link from TikTok, Threads, Instagram, or another supported app, open OneGrab, and tap <strong>Save from Clipboard</strong>. Customize your save, then keep it in Photos — or share it right away.",
        ),
        (r"Downloads aren’t working\. What should I try\?", "Saving isn’t working. What should I try?"),
        (
            r"Make sure you’ve copied a direct link to the video \(not a general profile or feed URL\)\.",
            "Make sure you’ve copied a direct link (not a general profile or feed URL).",
        ),
        (
            r"For questions about OneGrab, downloads, subscriptions, or anything else",
            "For questions about OneGrab, saves, subscriptions, or anything else",
        ),
        (
            r'content="OneGrab Support - Get help with downloads, subscriptions, and more\."',
            'content="OneGrab Support — Get help with saves, subscriptions, and more."',
        ),
    ]
    for pat, repl in replacements:
        html = re.sub(pat, repl, html)
    return html


def main() -> None:
    indexes = sorted(ROOT.rglob("index.html"))
    updated = 0
    for path in indexes:
        key = locale_key(path)
        if key not in COPY:
            print(f"SKIP (no copy): {key}")
            continue
        html = path.read_text(encoding="utf-8")
        new = patch_index(html, COPY[key])
        path.write_text(new, encoding="utf-8")
        updated += 1
        print(f"OK index {key}")

    # Root English support
    (ROOT / "support.html").write_text(SUPPORT_EN, encoding="utf-8")
    print("OK support.html (en)")

    # Localized support: English-ish pages get string replaces; others keep structure
    for path in sorted(ROOT.glob("*/support.html")):
        html = path.read_text(encoding="utf-8")
        new = patch_support_locale(html)
        if new != html:
            path.write_text(new, encoding="utf-8")
            print(f"OK support {path.parent.name}")

    readme = ROOT / "README.md"
    readme.write_text(
        """# OneGrab

Save your favorite TikToks, Threads, and clips for later. Copy a link, open OneGrab, tap Save — then keep it in Photos.

**[Download on the App Store](https://apps.apple.com/app/id6759439265)**

This repo is the source for the [OneGrab website](https://alexryakhin.github.io/OneGrab/) (hosted on GitHub Pages).

**Languages (by folder):** English (root), [ru](https://alexryakhin.github.io/OneGrab/ru/), [de-DE](https://alexryakhin.github.io/OneGrab/de-DE/), [fr-FR](https://alexryakhin.github.io/OneGrab/fr-FR/), [es-ES](https://alexryakhin.github.io/OneGrab/es-ES/), [es-MX](https://alexryakhin.github.io/OneGrab/es-MX/), [it](https://alexryakhin.github.io/OneGrab/it/), [ja](https://alexryakhin.github.io/OneGrab/ja/), [zh-Hans](https://alexryakhin.github.io/OneGrab/zh-Hans/), [zh-Hant](https://alexryakhin.github.io/OneGrab/zh-Hant/), [pt-BR](https://alexryakhin.github.io/OneGrab/pt-BR/), [pt-PT](https://alexryakhin.github.io/OneGrab/pt-PT/), [nl-NL](https://alexryakhin.github.io/OneGrab/nl-NL/), [pl](https://alexryakhin.github.io/OneGrab/pl/), [ko](https://alexryakhin.github.io/OneGrab/ko/), [ar-SA](https://alexryakhin.github.io/OneGrab/ar-SA/), [he](https://alexryakhin.github.io/OneGrab/he/), [th](https://alexryakhin.github.io/OneGrab/th/), [vi](https://alexryakhin.github.io/OneGrab/vi/), [id](https://alexryakhin.github.io/OneGrab/id/), [tr](https://alexryakhin.github.io/OneGrab/tr/), [uk](https://alexryakhin.github.io/OneGrab/uk/), [cs](https://alexryakhin.github.io/OneGrab/cs/), [sk](https://alexryakhin.github.io/OneGrab/sk/), [hu](https://alexryakhin.github.io/OneGrab/hu/), [ro](https://alexryakhin.github.io/OneGrab/ro/), [da](https://alexryakhin.github.io/OneGrab/da/), [no](https://alexryakhin.github.io/OneGrab/no/), [sv](https://alexryakhin.github.io/OneGrab/sv/), [fi](https://alexryakhin.github.io/OneGrab/fi/), [el](https://alexryakhin.github.io/OneGrab/el/), [hr](https://alexryakhin.github.io/OneGrab/hr/), [ca](https://alexryakhin.github.io/OneGrab/ca/), [fr-CA](https://alexryakhin.github.io/OneGrab/fr-CA/), [en-AU](https://alexryakhin.github.io/OneGrab/en-AU/), [en-CA](https://alexryakhin.github.io/OneGrab/en-CA/), [en-GB](https://alexryakhin.github.io/OneGrab/en-GB/), [hi](https://alexryakhin.github.io/OneGrab/hi/), [ms](https://alexryakhin.github.io/OneGrab/ms/).
""",
        encoding="utf-8",
    )
    print("OK README.md")
    print(f"Updated {updated} index pages")


if __name__ == "__main__":
    main()
