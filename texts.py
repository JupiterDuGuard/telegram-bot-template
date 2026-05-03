"""
Тексты бота на разных языках.
Чтобы добавить новый язык — добавь новый ключ в словарь TEXTS.
Чтобы изменить текст — отредактируй нужную строку.
"""

# Список доступных языков с эмодзи-флагами для отображения в кнопках
LANGUAGES = {
    "ru": "🇷🇺 Русский",
    "en": "🇬🇧 English",
    "pl": "🇵🇱 Polski",
    "de": "🇩🇪 Deutsch",
}

# Все тексты бота. Структура: TEXTS[язык][ключ] = "перевод"
TEXTS = {
    # === Русский ===
    "ru": {
        "choose_language": "Выберите язык / Choose language / Wybierz język / Sprache wählen:",
        "language_set": "✅ Язык установлен: Русский",
        "welcome": (
            "👋 Добро пожаловать в питомник саженцев голубики!\n\n"
            "🌱 Мы выращиваем качественные саженцы голубики высокорослой "
            "и поставляем их в Беларусь, Польшу, Германию и страны Прибалтики.\n\n"
            "Чем могу помочь?"
        ),
        "btn_catalog": "🌿 Каталог сортов",
        "btn_about": "ℹ️ О питомнике",
        "btn_contact": "📞 Связаться",
        "btn_change_lang": "🌐 Сменить язык",
        "menu_catalog": "🌿 Меню",
        "menu_help": "❓ Помощь",
        "menu_contact": "📞 Контакты",
        "catalog_text": (
            "🌿 <b>Наши сорта голубики</b>\n\n"
            "• <b>Bluecrop</b> — классический урожайный сорт\n"
            "• <b>Duke</b> — раннеспелый, очень морозостойкий\n"
            "• <b>Patriot</b> — крупная ягода, неприхотливый\n"
            "• <b>Elliott</b> — позднеспелый, длительное плодоношение\n"
            "• <b>Chandler</b> — рекордный размер ягод\n\n"
            "Для подробной консультации — нажмите «Связаться»."
        ),
        "about_text": (
            "ℹ️ <b>О питомнике</b>\n\n"
            "Мы — питомник саженцев голубики с многолетним опытом.\n"
            "Экспортируем продукцию в страны ЕС.\n\n"
            "Качество саженцев подтверждено сертификатами."
        ),
        "contact_text": (
            "📞 <b>Контакты</b>\n\n"
            "Для оптовых заказов и консультаций:\n"
            "Telegram: @JupiterDuGuard\n"
            "Email: example@example.com"
        ),
        "help_text": (
            "❓ <b>Помощь</b>\n\n"
            "Команды бота:\n"
            "/start — главное меню\n"
            "/lang — сменить язык\n"
            "/help — эта справка\n\n"
            "Также можно использовать кнопки внизу экрана."
        ),
        "echo": "Я получил ваше сообщение: {text}\n\nВоспользуйтесь меню для навигации.",
    },

    # === English ===
    "en": {
        "choose_language": "Выберите язык / Choose language / Wybierz język / Sprache wählen:",
        "language_set": "✅ Language set: English",
        "welcome": (
            "👋 Welcome to our blueberry seedling nursery!\n\n"
            "🌱 We grow high-quality highbush blueberry seedlings "
            "and supply them to Belarus, Poland, Germany, and the Baltic countries.\n\n"
            "How can I help you?"
        ),
        "btn_catalog": "🌿 Variety catalog",
        "btn_about": "ℹ️ About us",
        "btn_contact": "📞 Contact",
        "btn_change_lang": "🌐 Change language",
        "menu_catalog": "🌿 Menu",
        "menu_help": "❓ Help",
        "menu_contact": "📞 Contact",
        "catalog_text": (
            "🌿 <b>Our blueberry varieties</b>\n\n"
            "• <b>Bluecrop</b> — classic high-yield variety\n"
            "• <b>Duke</b> — early ripening, very frost-resistant\n"
            "• <b>Patriot</b> — large berries, hardy\n"
            "• <b>Elliott</b> — late ripening, extended fruiting\n"
            "• <b>Chandler</b> — record-large berries\n\n"
            "For detailed consultation — press «Contact»."
        ),
        "about_text": (
            "ℹ️ <b>About the nursery</b>\n\n"
            "We are a blueberry seedling nursery with many years of experience.\n"
            "We export to EU countries.\n\n"
            "Seedling quality confirmed by certificates."
        ),
        "contact_text": (
            "📞 <b>Contact</b>\n\n"
            "For wholesale orders and consultations:\n"
            "Telegram: @JupiterDuGuard\n"
            "Email: example@example.com"
        ),
        "help_text": (
            "❓ <b>Help</b>\n\n"
            "Bot commands:\n"
            "/start — main menu\n"
            "/lang — change language\n"
            "/help — this help\n\n"
            "You can also use the buttons at the bottom of the screen."
        ),
        "echo": "I received your message: {text}\n\nUse the menu to navigate.",
    },

    # === Polski ===
    "pl": {
        "choose_language": "Выберите язык / Choose language / Wybierz język / Sprache wählen:",
        "language_set": "✅ Język ustawiony: Polski",
        "welcome": (
            "👋 Witamy w naszej szkółce sadzonek borówki!\n\n"
            "🌱 Uprawiamy wysokiej jakości sadzonki borówki wysokiej "
            "i dostarczamy je do Białorusi, Polski, Niemiec oraz krajów bałtyckich.\n\n"
            "W czym mogę pomóc?"
        ),
        "btn_catalog": "🌿 Katalog odmian",
        "btn_about": "ℹ️ O nas",
        "btn_contact": "📞 Kontakt",
        "btn_change_lang": "🌐 Zmień język",
        "menu_catalog": "🌿 Menu",
        "menu_help": "❓ Pomoc",
        "menu_contact": "📞 Kontakt",
        "catalog_text": (
            "🌿 <b>Nasze odmiany borówki</b>\n\n"
            "• <b>Bluecrop</b> — klasyczna, wysokoplenna odmiana\n"
            "• <b>Duke</b> — wczesna, bardzo mrozoodporna\n"
            "• <b>Patriot</b> — duże owoce, odporna\n"
            "• <b>Elliott</b> — późna, przedłużone owocowanie\n"
            "• <b>Chandler</b> — rekordowo duże owoce\n\n"
            "Aby uzyskać szczegółową konsultację — naciśnij «Kontakt»."
        ),
        "about_text": (
            "ℹ️ <b>O szkółce</b>\n\n"
            "Jesteśmy szkółką sadzonek borówki z wieloletnim doświadczeniem.\n"
            "Eksportujemy do krajów UE.\n\n"
            "Jakość sadzonek potwierdzona certyfikatami."
        ),
        "contact_text": (
            "📞 <b>Kontakt</b>\n\n"
            "Zamówienia hurtowe i konsultacje:\n"
            "Telegram: @JupiterDuGuard\n"
            "Email: example@example.com"
        ),
        "help_text": (
            "❓ <b>Pomoc</b>\n\n"
            "Komendy bota:\n"
            "/start — menu główne\n"
            "/lang — zmień język\n"
            "/help — ta pomoc\n\n"
            "Możesz też używać przycisków na dole ekranu."
        ),
        "echo": "Otrzymałem Twoją wiadomość: {text}\n\nUżyj menu do nawigacji.",
    },

    # === Deutsch ===
    "de": {
        "choose_language": "Выберите язык / Choose language / Wybierz język / Sprache wählen:",
        "language_set": "✅ Sprache eingestellt: Deutsch",
        "welcome": (
            "👋 Willkommen in unserer Heidelbeer-Baumschule!\n\n"
            "🌱 Wir züchten hochwertige Heidelbeer-Setzlinge "
            "und liefern sie nach Belarus, Polen, Deutschland und in die baltischen Länder.\n\n"
            "Wie kann ich Ihnen helfen?"
        ),
        "btn_catalog": "🌿 Sortenkatalog",
        "btn_about": "ℹ️ Über uns",
        "btn_contact": "📞 Kontakt",
        "btn_change_lang": "🌐 Sprache ändern",
        "menu_catalog": "🌿 Menü",
        "menu_help": "❓ Hilfe",
        "menu_contact": "📞 Kontakt",
        "catalog_text": (
            "🌿 <b>Unsere Heidelbeersorten</b>\n\n"
            "• <b>Bluecrop</b> — klassische ertragreiche Sorte\n"
            "• <b>Duke</b> — frühreifend, sehr frostbeständig\n"
            "• <b>Patriot</b> — große Beeren, robust\n"
            "• <b>Elliott</b> — spätreifend, lange Fruchtperiode\n"
            "• <b>Chandler</b> — rekordgroße Beeren\n\n"
            "Für detaillierte Beratung — drücken Sie «Kontakt»."
        ),
        "about_text": (
            "ℹ️ <b>Über die Baumschule</b>\n\n"
            "Wir sind eine Heidelbeer-Baumschule mit langjähriger Erfahrung.\n"
            "Wir exportieren in EU-Länder.\n\n"
            "Qualität der Setzlinge durch Zertifikate bestätigt."
        ),
        "contact_text": (
            "📞 <b>Kontakt</b>\n\n"
            "Großhandelsbestellungen und Beratungen:\n"
            "Telegram: @JupiterDuGuard\n"
            "Email: example@example.com"
        ),
        "help_text": (
            "❓ <b>Hilfe</b>\n\n"
            "Bot-Befehle:\n"
            "/start — Hauptmenü\n"
            "/lang — Sprache ändern\n"
            "/help — diese Hilfe\n\n"
            "Sie können auch die Tasten unten auf dem Bildschirm verwenden."
        ),
        "echo": "Ich habe Ihre Nachricht erhalten: {text}\n\nNutzen Sie das Menü zur Navigation.",
    },
}


def get_text(lang: str, key: str) -> str:
    """
    Достаёт перевод по языку и ключу.
    Если язык не найден — fallback на английский.
    Если ключ не найден — возвращает сам ключ (для отладки).
    """
    if lang not in TEXTS:
        lang = "en"
    return TEXTS[lang].get(key, f"[MISSING: {key}]")