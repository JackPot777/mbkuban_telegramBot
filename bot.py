# -*- coding: utf-8 -*-
import telebot
import constants, os
import botan
from telebot import types

bot = telebot.TeleBot(constants.token)

class BotMenu:
    def main_menu(self, bot, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("📦Пакеты услуг")
        user_markup.row("💳Финансы", "✴Услуги")
        user_markup.row("🎓Обучение", "🏢Коворкинг")
        user_markup.row("📅События", "☎Контакты")
        bot.send_message(message.from_user.id, "Выберите интересующий Вас пункт", reply_markup=user_markup)

    def cont_menu(self, bot, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("🔙 Вернуться в Меню")
        user_markup.row("🚀Центр поддержки предпринимательства")
        user_markup.row("🚩Иные организации развития бизнеса")
        user_markup.row("✒Жалобы и предложения")
        bot.send_message(message.from_user.id, "Полезные контакты", reply_markup=user_markup)

    def finance_menu(self, bot, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("🔙 Вернуться в Меню")
        user_markup.row("Субсидии")
        user_markup.row("Микрозаймы и кредитование")
        user_markup.row("Поручительства")
        bot.send_message(message.from_user.id, "Финансовая поддержка бизнеса", reply_markup=user_markup)

    def subsid_menu(self, bot, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("🔙 Вернуться в 💳Финансы")
        user_markup.row("Промышленность")
        user_markup.row("Сельское хозяйство")
        user_markup.row("Инновации")
        user_markup.row("Служба занятости")
        bot.send_message(message.from_user.id, "Субсидии для бизнеса", reply_markup=user_markup)

    def mfo_menu(self, bot, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("🔙 Вернуться в 💳Финансы")
        user_markup.row("Старт", "Фермер")
        user_markup.row("Бизнес-оборот", "Ремесленник")
        user_markup.row("Бизнес-инвест", "Новотех")
        user_markup.row("Развитие и инновации")
        bot.send_message(message.from_user.id, "Пакеты микрозаймов и кредитования", reply_markup=user_markup)

    def uslugi_menu(self, bot, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("🔙 Вернуться в Меню")
        user_markup.row("Разработка бизнес-планов")
        user_markup.row("Разработка веб-сайтов")
        user_markup.row("Создание фирменного стиля")
        user_markup.row("Маркетинговые исследования")
        user_markup.row("Консультации")
        user_markup.row("Иные услуги")
        bot.send_message(message.from_user.id, "Бесплатные услуги и консультации центра поддержки предпринимательства", reply_markup=user_markup)

    def grad_menu(self, bot, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("🔙 Вернуться в Меню")
        user_markup.row("Семинары центра поддержки")
        user_markup.row("Школа молодого предпринимателя")
        user_markup.row("«Бизнес класс»")
        bot.send_message(message.from_user.id, "Узнайте о действующих и предстоящих образовательных мероприятиях",
                         reply_markup=user_markup)

    def paketi_menu(self, bot, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True)
        user_markup.row("🔙 Вернуться в Меню")
        user_markup.row("🚀Открывай", "📊Развивай")
        user_markup.row("✅Производи", "🚚Экспортируй")
        user_markup.row("📝Консультация On-Line")
        bot.send_message(message.from_user.id, "Выберите подходящий для Вас пакет услуг",
                         reply_markup=user_markup)

bm = BotMenu()

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == "invest":
        bot.send_message(c.message.chat.id, """\r
<b>Департамент инвестиций и развития малого и среднего предпринимательства Краснодарского края</b>\n
<i>Адрес: 350014, г, Краснодар, ул. Красная, 35
investkuban@krasnodar.ru</i>\n
<a href="https://goo.gl/maps/ARh9L6EuPR52" title="Показать на карте">Показать на карте</a>""", parse_mode="HTML")
        bot.send_message(c.message.chat.id, "+78612517310")
    if c.data == "micro":
        bot.send_message(c.message.chat.id, """\r
<b>Фонд микрофинансирования субъектов малого и среднего предпринимательства Краснодарского края</b>\n
<i>Адрес: г. Краснодар, ул. Трамвайная, 2/6\n 
Представительство: г. Армавир, ул. Ефремова, д. 270, 3 этаж, офис 5
info@fmkk.ru</i>\n
<a href="https://goo.gl/maps/qaatsxURJxn" title="Показать на карте">Показать на карте</a>""", parse_mode="HTML")
        bot.send_message(c.message.chat.id, "+78612980808")
    if c.data == "garant":
        bot.send_message(c.message.chat.id, """\r
<b>Гарантийный фонд Краснодарского края</b>\n
<i>Адрес: г. Краснодар, ул. Трамвайная, 2/6, 5 этаж, офис 505
info@gfkuban.ru</i>\n
<a href="https://goo.gl/maps/qaatsxURJxn" title="Показать на карте">Показать на карте</a>""", parse_mode="HTML")
        bot.send_message(c.message.chat.id, "+78619920365")
    if c.data == "prom":
        bot.send_message(c.message.chat.id, """\r
<b>Департамент промышленной политики Краснодарского края</b>\n
<i>Адрес: 350000, г. Краснодар, ул. Красная, д. 176
dpp@krasnodar.ru</i>\n
<a href="https://goo.gl/maps/UQfxqZeVVXt" title="Показать на карте">Показать на карте</a>""", parse_mode="HTML")
        bot.send_message(c.message.chat.id, "+78612517310")
    if c.data == "sh":
        bot.send_message(c.message.chat.id, """\r
<b>Министерство сельского хозяйства и перерабатывающей промышленности Краснодарского края</b>\n
<i>Адрес: г. Краснодар, ул. Рашпилевская, д. 365
msh@krasnodar.ru</i>\n
<a href="https://goo.gl/maps/ttKL9Hf6fpC2" title="Показать на карте">Показать на карте</a>""", parse_mode="HTML")
        bot.send_message(c.message.chat.id, "+78612142556")
    if c.data == "trud":
        bot.send_message(c.message.chat.id, """\r
<b>Служба труда и занятости населения министерства труда и социального развития Краснодарского края</b>\n
<i>Адрес: 350000, г. Краснодар, ул. Зиповская, д. 5
kancel@dgsz.krasnodar.ru</i>\n
<a href="https://goo.gl/maps/bbee3vzzoRF2" title="Показать на карте">Показать на карте</a>""", parse_mode="HTML")
        bot.send_message(c.message.chat.id, "+78612571370")
    if c.data == "sobit5":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(
            text="19.05. В Москве пройдет Всемирный Саммит по Криптовалюте и Блокчейну",
            callback_data="sob1")
        but_2 = types.InlineKeyboardButton(
            text="06.06. «Неделя Российского Ритейла 2018» пройдет в Москве",
            callback_data="sob2")
        but_3 = types.InlineKeyboardButton(text="12.04. Конференция «Народные художественные промыслы России» пройдет в Москве",
                                           callback_data="sob3")
        but_4 = types.InlineKeyboardButton(
            text="18.04. В Москве состоится совещание по вопросам сохранения и развития ремесленной отрасли",
            callback_data="sob4")
        but_5 = types.InlineKeyboardButton(
            text="24.04. Краснодар включен в график проведения Open Innovations Startup Tour Фонда «Сколково»",
            callback_data="sob5")
        key.add(but_3, but_4, but_5, but_1, but_2)
        bot.send_message(c.message.chat.id, "Ближайшие 5 событий в бизнесе Кубани", reply_markup=key)
    if c.data == "sob1":
        bot.send_message(c.message.chat.id, """\r
        <b>19.05. В Москве пройдет Всемирный Саммит по Криптовалюте и Блокчейну</b>\n
        <a href="http://www.mbkuban.ru/cpp/events/v-moskve-proydet-vsemirnyy-sammit-po-kriptovalyute-i-blokcheynu/" title="Перейти к событию">Перейти к событию</a>""", parse_mode="HTML")
    if c.data == "sob2":
        bot.send_message(c.message.chat.id, """\r
        <b>06.06. «Неделя Российского Ритейла 2018» пройдет в Москве</b>\n
        <a href="http://www.mbkuban.ru/cpp/events/nedelya-rossiyskogo-riteyla-2018-proydet-v-moskve/" title="Перейти к событию">Перейти к событию</a>""", parse_mode="HTML")
    if c.data == "sob3":
        bot.send_message(c.message.chat.id, """\r
        <b>12.04. Конференция «Народные художественные промыслы России» пройдет в Москве</b>\n
        <a href="http://www.mbkuban.ru/cpp/events/konferentsiya-narodnye-khudozhestvennye-promysly-rossii-proydet-v-moskve/" title="Перейти к событию">Перейти к событию</a>""", parse_mode="HTML")
    if c.data == "sob4":
        bot.send_message(c.message.chat.id, """\r
        <b>18.04. В Москве состоится совещание по вопросам сохранения и развития ремесленной отрасли</b>\n
        <a href="http://www.mbkuban.ru/cpp/events/v-moskve-sostoitsya-soveshchanie-po-voprosam-sokhraneniya-i-razvitiya-remeslennoy-otrasli/" title="Перейти к событию">Перейти к событию</a>""", parse_mode="HTML")
    if c.data == "sob5":
        bot.send_message(c.message.chat.id, """\r
        <b>24.04. Краснодар включен в график проведения Open Innovations Startup Tour Фонда «Сколково»</b>\n
        <a href="http://www.mbkuban.ru/cpp/events/krasnodar-vklyuchen-v-grafik-provedeniya-open-innovations-startup-tour-fonda-skolkovo/" title="Перейти к событию">Перейти к событию</a>""", parse_mode="HTML")
    if c.data == "sub1":
        bot.send_message(c.message.chat.id, """\r
<b>Субсидии субъектам деятельности в сфере промышленности при организации трудовой занятости осужденных</b>\n
<i>Cумма субсидии - до 500 000 руб. Возмещается 60% от фактически произведенных затрат. Получатель – субъект деятельности в сфере промышленности.</i>\n
<a href="https://goo.gl/9SNiSg" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
    if c.data == "sub2":
        bot.send_message(c.message.chat.id, """\r
<b>Субсидии субъектам деятельности в сфере промышленности на технологическое присоединение</b>\n
<i>Сумма субсидии - до 1 800 000 руб. Возмещается 30% от затрат на технологическое присоединение. Получатель – субъект деятельности в сфере промышленности.</i>\n
<a href="https://goo.gl/7f5NKN" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
    if c.data == "sub3":
        bot.send_message(c.message.chat.id, """\r
<b>Субсидии на уплату % по кредитам полученным для пополнения оборотных</b>\n
<i>Сумма субсидии - до 5 000 000 руб. Компенсируются проценты в размере не более 3/4 ключевой ставки Банка России, но не более 70 % от фактически уплаченных процентов. Получатель - субъект деятельности в сфере промышленности.</i>\n
<a href="https://goo.gl/iL94ZJ" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
    if c.data == "sub4":
        bot.send_message(c.message.chat.id, """\r
<b>Субсидии на уплату % по кредитам и на уплату дохода лизинговых компаний, полученных на создание новых производств, модернизацию и приобретение оборудования</b>\n
<i>Сумма субсидии - до 10 000 000 руб. По кредитам компенсируются проценты в размере не более 3/4 ключевой ставки Банка России,  но не более 70 % от фактически уплаченных процентов. По лизингу компенсируются часть дохода лизинговых компаний, являющихся частью лизинговых платежей, но не более 50% от фактически уплаченных платежей. Получатель-субъект деятельности в сфере промышленности.</i>\n
<a href="https://goo.gl/VQsM79" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
    if c.data == "sub5":
        bot.send_message(c.message.chat.id, """\r
<b>Субсидии на возмещение затрат, связанных с осуществлением образовательной деятельности</b>\n
<i>Сумма субсидии - до 1 000 000 руб. Возмещается 70 % от фактически произведенных и документально подтвержденных затрат. Получатель - субъект деятельности в сфере промышленности.</i>\n
<a href="https://goo.gl/VZddXH" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
    if c.data == "sub5":
        bot.send_message(c.message.chat.id, """\r
<b>Субсидии на возмещение части затрат на реализацию инвестиционных проектов</b>\n
<i>Сумма субсидии - до 10 000 000 руб. Компенсируются 10 % от фактически произведенных и документально подтвержденных затрат. Получатель - субъект деятельности в сфере промышленности.</i>\n
<a href="https://goo.gl/HLTWDW" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
    if c.data == "sh1":
        bot.send_message(c.message.chat.id, """\r
<b>Сельхозстрахование</b>\n
<i>Возмещается 50% от затрат.</i>\n
<a href="https://goo.gl/rW8NDn" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
    if c.data == "sh2":
        bot.send_message(c.message.chat.id, """\r
<b>Приобретение элитных семян</b>\n
<i>Сумма субсидии рассчитывается согласно установленной форме.</i>\n
<a href="https://goo.gl/M1UKvd" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
    if c.data == "sh3":
        bot.send_message(c.message.chat.id, """\r
<b>Поддержка племенного крупного рогатого скота мясного направления</b>\n
<i>Сумма субсидии рассчитывается согласно установленной форме.</i>\n
<a href="https://goo.gl/EN14mA" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
    if c.data == "sh4":
        bot.send_message(c.message.chat.id, """\r
<b>Субсидии на развитие садоводства и чаеводства</b>\n
<i>Сумма субсидии рассчитывается согласно установленной форме.</i>\n
<a href="https://goo.gl/M4nwTe" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
    if c.data == "sh5":
        bot.send_message(c.message.chat.id, """\r
<b>Другие субсидии министерства сельского хозяйства и перерабатывающей промышленности Краснодарского края</b>\n
<a href="http://www.mbkuban.ru/financial-support/subsidies/" title="Ознакомиться">Ознакомиться</a>""", parse_mode="HTML")
    if c.data == "trud1":
        bot.send_message(c.message.chat.id, """\r
<b>Возмещение затрат на подготовку документов, представляемых при государственной регистрации</b>\n
<i>Сумма по факту понесенных затрат, получатель – граждане, признанные в установленном порядке безработными и граждане, признанные в установленном порядке безработными и прошедшие профессиональное обучение или получившие дополнительное профессиональное образование по направлению органов службы занятости.</i>\n
<a href="https://goo.gl/UTjpE3" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
    if c.data == "trud2":
        bot.send_message(c.message.chat.id, """\r
<b>Возмещение части затрат на дополнительное рабочее место для трудоустройства безработных граждан</b>\n
<i>Сумма возмещения – 58 800 рублей, получатель – граждане, признанные в установленном порядке безработными и граждане.</i>\n
<a href="https://goo.gl/qWzbdi" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
    if c.data == "trud3":
        bot.send_message(c.message.chat.id, """\r
<b>Единовременная финансовая помощь на открытие индивидуального предпринимателя или юридического лица</b>\n
<i>Сумма возмещения – 117 600 рублей (зависит от максимального размера пособия по безработице, Постановление от 19.06.2012 года № 710), получатель – граждане, признанные в установленном порядке безработными и граждане, признанные в установленном порядке безработными и прошедшие профессиональное обучение или получившие дополнительное профессиональное образование по направлению органов службы занятости.</i>\n
<a href="https://goo.gl/9VkG7a" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_photo(message.from_user.id, photo="https://cdn1.savepice.ru/uploads/2018/3/22/2720d857ad2cb63b2995216c4573e92e-full.png")
    bot.send_message(message.from_user.id, "www.mbkuban.ru - официальный портал малого бизнеса Кубани")
    bm.main_menu(bot, message)
    botan.track(constants.botan_key, message.chat.id, message, "start")


@bot.message_handler(content_types=["text"])
def handle_start(message):
    if message.text == "☎Контакты":
        bm.cont_menu(bot, message)
        botan.track(constants.botan_key, message.chat.id, message, "Контакты")
    if message.text == "🚀Центр поддержки предпринимательства":
        bot.send_message(message.from_user.id, """\r
<b>Центр поддержки предпринимательства Краснодарского края</b>\n
<i>Адрес: 350911, г. Краснодар, ул. Трамвайная, 2/6, 1 этаж</i>\n
<a href="https://goo.gl/maps/qaatsxURJxn" title="Показать на карте">Показать на карте</a>""", parse_mode="HTML")
        bot.send_message(message.from_user.id, "+78007070711")
        bot.send_message(message.chat.id, "Для консультации on-line пишите @CPP_Makeeva")
        botan.track(constants.botan_key, message.chat.id, message, "ЦПП_тел")
    if message.text == "🚩Иные организации развития бизнеса":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Департамент инвестиций и развития малого и среднего предпринимательства Краснодарского края", callback_data="invest")
        but_2 = types.InlineKeyboardButton(text="Фонд микрофинансирования Краснодарского края", callback_data="micro")
        but_3 = types.InlineKeyboardButton(text="Гарантийный фонд Краснодарского края", callback_data="garant")
        but_4 = types.InlineKeyboardButton(text="Департамент промышленной политики Краснодарского края", callback_data="prom")
        but_5 = types.InlineKeyboardButton(text="Министерство сельского хозяйства и перерабатывающей промышленности Краснодарского края", callback_data="sh")
        but_6 = types.InlineKeyboardButton(text="Служба труда и занятости населения министерства труда и социального развития Краснодарского края", callback_data="trud")
        key.add(but_1, but_2, but_3, but_4, but_5, but_6)
        bot.send_message(message.chat.id, "Полезные контакты организаций и органов развития бизнеса", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Иныеорг_тел")
    if message.text == "🔙 Вернуться в Меню":
        bm.main_menu(bot, message)
    if message.text == "💳Финансы":
        bm.finance_menu(bot, message)
        botan.track(constants.botan_key, message.chat.id, message, "Финансы")
    if message.text == "🔙 Вернуться в 💳Финансы":
        bm.finance_menu(bot, message)
    if message.text == "Субсидии":
        bm.subsid_menu(bot, message)
        botan.track(constants.botan_key, message.chat.id, message, "Субсидии")
    if message.text == "Инновации":
        bot.send_message(message.chat.id, """\r
<b>Предоставление субсидии в целях финансового обеспечения (возмещения) части затрат, связанных с созданием и (или) обеспечением деятельности центров молодежного инновационного творчества</b>\n
<i>Сумма субсидии - до 3 600 000 руб.
Получатель – субъекты малого и среднего предпринимательства Краснодарского края</i>\n
<a href="https://goo.gl/GmEop5" title="Условия поддержки">Условия поддержки</a>""", parse_mode="HTML")
        bot.send_message(message.chat.id, "+78612517599")
        botan.track(constants.botan_key, message.chat.id, message, "Инновации")
    if message.text == "Микрозаймы и кредитование":
        bm.mfo_menu(bot, message)
        botan.track(constants.botan_key, message.chat.id, message, "Микрозаймы и кредиты")
    if message.text == "Старт":
        bot.send_photo(message.from_user.id, photo="https://photos.app.goo.gl/SWWuLwYzRwDXejBE2")
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Узнать подробнее", url="http://fmkk.ru/types/start/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Микрозайм для начинающих субъектов малого и среднего предпринимательства", reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для консультации on-line напишите @RAGoncharov")
        botan.track(constants.botan_key, message.chat.id, message, "Старт")
    if message.text == "Фермер":
        bot.send_photo(message.from_user.id, photo="https://photos.app.goo.gl/U2wgWWIPjeTjwdxb2")
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Узнать подробнее", url="http://fmkk.ru/types/fermer/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Микрозайм для действующих субъектов малого и среднего предпринимательства, организаций инфраструктуры поддержки малого и среднего предпринимательства", reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для консультации on-line напишите @RAGoncharov")
        botan.track(constants.botan_key, message.chat.id, message, "Фермер")
    if message.text == "Бизнес-оборот":
        bot.send_photo(message.from_user.id, photo="https://photos.app.goo.gl/cIoyHDGBVY914YRE2")
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Узнать подробнее", url="http://fmkk.ru/types/biznes_oborot/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Микрозайм для действующих субъектов малого и среднего предпринимательства, организаций инфраструктуры поддержки малого и среднего предпринимательства на пополнение оборотных средств", reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для консультации on-line напишите @RAGoncharov")
        botan.track(constants.botan_key, message.chat.id, message, "Биз-оборот")
    if message.text == "Ремесленник":
        bot.send_photo(message.from_user.id, photo="https://photos.app.goo.gl/kRFKZ6RRyw3VYjVC2")
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Узнать подробнее", url="http://fmkk.ru/types/remeslennik/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Микрозайм для действующих субъектов малого и среднего предпринимательства, организаций инфраструктуры поддержки малого и среднего предпринимательства", reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для консультации on-line напишите @RAGoncharov")
        botan.track(constants.botan_key, message.chat.id, message, "Ремесленник")
    if message.text == "Бизнес-инвест":
        bot.send_photo(message.from_user.id, photo="https://photos.app.goo.gl/3WL9HJn3HcbW8Fjr2")
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Узнать подробнее", url="http://fmkk.ru/types/biznes_invest/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Микрозайм для действующих субъектов малого и среднего предпринимательства, организаций инфраструктуры поддержки малого и среднего предпринимательства на инвестиционные цели", reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для консультации on-line напишите @RAGoncharov")
        botan.track(constants.botan_key, message.chat.id, message, "Биз-инвест")
    if message.text == "Новотех":
        bot.send_photo(message.from_user.id, photo="https://photos.app.goo.gl/sUY6BDdTPG7l4wPI3")
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Узнать подробнее", url="http://fmkk.ru/types/novotekh/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Микрозайм для действующих субъектов малого и среднего предпринимательства, организаций инфраструктуры поддержки малого и среднего предпринимательства на цели приобретения новых основных средств под их залог", reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для консультации on-line напишите @RAGoncharov")
        botan.track(constants.botan_key, message.chat.id, message, "Новотех")
    if message.text == "Развитие и инновации":
        bot.send_photo(message.from_user.id, photo="https://photos.app.goo.gl/0rjdE8954a00gfgq2")
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Узнать подробнее", url="http://fmkk.ru/types/razvitie_i_innovatsii/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Микрозайм для действующих субъектов малого и среднего предпринимательства, организаций инфраструктуры поддержки малого и среднего предпринимательства", reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для консультации on-line напишите @RAGoncharov")
        botan.track(constants.botan_key, message.chat.id, message, "разв и инновации")
    if message.text == "Поручительства":
        bot.send_photo(message.from_user.id, photo="https://photos.app.goo.gl/l5zfkQ1FILKQoTCA2")
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url_button1 = types.InlineKeyboardButton(text="Узнать подробнее", url="http://www.mbkuban.ru/financial-support/surety/")
        url_button2 = types.InlineKeyboardButton(text="Условия (101.33кБ)",
                                                 url="http://www.mbkuban.ru/upload/iblock/a16/a161d37b98b02959bbb405d4e7cffeff.docx")
        keyboard.add(url_button1, url_button2)
        bot.send_message(message.chat.id, "Привлечение поручительства в случае нехватки залоговой базы. Максимальная сумма поручительства 25 млн. рублей (не > 70% от суммы займа или банковской гарантии)", reply_markup=keyboard)
        botan.track(constants.botan_key, message.chat.id, message, "Поручительства")
    if message.text == "✴Услуги":
        bm.uslugi_menu(bot, message)
        botan.track(constants.botan_key, message.chat.id, message, "Услуги")
    if message.text == "Разработка бизнес-планов":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url_button1 = types.InlineKeyboardButton(text="Узнать подробнее",
                                                 url="http://mbkuban.ru/cpp/services/")
        keyboard.add(url_button1)
        bot.send_message(message.chat.id,
                         "Бизнес план – это документ, дающий развернутое обоснование проекта и возможность всесторонне оценить эффективность принятых решений, планируемых мероприятий, ответить на вопрос, стоит ли вкладывать деньги в данный проект.",
                         reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для записи on-line напишите @CPP_Makeeva")
        botan.track(constants.botan_key, message.chat.id, message, "Разраб.биз.планов")
    if message.text == "Разработка веб-сайтов":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url_button1 = types.InlineKeyboardButton(text="Узнать подробнее",
                                                 url="http://mbkuban.ru/cpp/services/")
        keyboard.add(url_button1)
        bot.send_message(message.chat.id,
                         "Разработка сайтов – важный элемент современного бизнеса. Сайт – это отличная возможность увеличения продаж и клиентской базы. Современный рынок диктует свои правила и сейчас для любой организации, которая хочет добиться успеха в своей нише, очень важно иметь собственный веб-ресурс.",
                         reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для записи on-line напишите @CPP_Makeeva")
        botan.track(constants.botan_key, message.chat.id, message, "Разр.биз.планов")
    if message.text == "Создание фирменного стиля":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url_button1 = types.InlineKeyboardButton(text="Узнать подробнее",
                                                 url="http://mbkuban.ru/cpp/services/")
        keyboard.add(url_button1)
        bot.send_message(message.chat.id,
                         "Фирменный стиль – фирменный стиль помогает потребителю быстрее и проще распознавать и запоминать бренд в условиях высокой конкуренции.",
                         reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для записи on-line напишите @CPP_Makeeva")
        botan.track(constants.botan_key, message.chat.id, message, "Фир.стиль")
    if message.text == "Маркетинговые исследования":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url_button1 = types.InlineKeyboardButton(text="Узнать подробнее",
                                                 url="http://mbkuban.ru/cpp/services/")
        keyboard.add(url_button1)
        bot.send_message(message.chat.id,
                         "Маркетинговые исследования – это систематический сбор, документирование и анализ данных по разным аспектам маркетинговой деятельности. Цель маркетингового исследования — создать информационно-аналитическую базу для принятия управленческих решений.",
                         reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для записи on-line напишите @CPP_Makeeva")
        botan.track(constants.botan_key, message.chat.id, message, "Маркет.исследование")
    if message.text == "Консультации":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url_button1 = types.InlineKeyboardButton(text="Узнать подробнее",
                                                 url="http://www.mbkuban.ru/cpp/consultations/")
        keyboard.add(url_button1)
        bot.send_message(message.chat.id,
                         "Консультационные услуги по различным вопросам",
                         reply_markup=keyboard)
        bot.send_message(message.chat.id, "Для записи on-line напишите @CPP_Makeeva")
        botan.track(constants.botan_key, message.chat.id, message, "Консультации")
    if message.text == "Иные услуги":
        bot.send_message(message.chat.id, "Если у Вас есть вопросы, то напишите нам @CPP_Makeeva")
        botan.track(constants.botan_key, message.chat.id, message, "Иные услуги")
    if message.text == "🎓Обучение":
        bm.grad_menu(bot, message)
        botan.track(constants.botan_key, message.chat.id, message, "Обучение")
    if message.text == "Семинары центра поддержки":
        bot.send_photo(message.from_user.id, photo="http://kuban24.tv/media/cache/item/res/images/07122017/282696.jpg")
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Узнать подробнее", url="http://mbkuban.ru/cpp/events/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id,
                         "В 2017 году ЦПП провело более 180 семинаров, тренингов, мастер-классов и иных бесплатных образовательных мероприятий.",
                         reply_markup=keyboard)
        botan.track(constants.botan_key, message.chat.id, message, "Семинары ЦПП")
    if message.text == "Школа молодого предпринимателя":
        bot.send_photo(message.from_user.id, photo="https://photos.app.goo.gl/fJLaG8rpCpW2Yuhj2")
        bot.send_message(message.chat.id,
                         "В Краснодаре на постоянной основе проходит Школа молодого предпринимателя.  Образовательная программа сочетает в себе основы теории и практики ведения бизнеса.")
        bot.send_message(message.chat.id, "Написать куратору проекта @Silchenko_Kris")
        botan.track(constants.botan_key, message.chat.id, message, "ШМП")
    if message.text == "«Бизнес класс»":
        bot.send_photo(message.from_user.id, photo="https://photos.app.goo.gl/geJf0pZCe2Hp8GVb2")
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url_button1 = types.InlineKeyboardButton(text="Регистрация в проекте",
                                                 url="https://www.business-class.pro/")
        keyboard.add(url_button1)
        bot.send_message(message.chat.id,
                         "Один из самых успешных проектов по повышению предпринимательских навыков – «Бизнес класс», реализуемый ПАО «Сбербанк» и Google",
                         reply_markup=keyboard)
        botan.track(constants.botan_key, message.chat.id, message, "Биз.класс")
    if message.text == "🏢Коворкинг":
        bot.send_photo(message.from_user.id, photo="https://photos.app.goo.gl/4rz7GGEDOtpqFAgV2")
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="Больше фото",
                                                 url="https://drive.google.com/open?id=1mKRj6L16YcGlesnr7deHNOJBRy4kq0U8")
        url_button2 = types.InlineKeyboardButton(text="Больше информация на www.mbkuban.ru",
                                                 url="www.mbkuban.ru/cowork")
        url_button3 = types.InlineKeyboardButton(text="Наш аккаунт Instagram",
                                                 url="www.instagram.com/mdcoworking")
        url_button4 = types.InlineKeyboardButton(text="Наш аккаунт ВКонтакте",
                                                 url="www.vk.com/mdcoworking")
        url_button5 = types.InlineKeyboardButton(text="Наш аккаунт Facebook",
                                                 url="www.facebook.com/mdcoworking")
        keyboard.add(url_button1, url_button2, url_button3, url_button4, url_button5)
        bot.send_message(message.chat.id,
                         "Государственный коворкинг для предпринимателей «Место действия». Пространство для развития вашего стартапа. Консультации специалистов по вашему бизнесу, бухгалтерское и юридическое сопровождение и мудрые наставники!",
                         reply_markup=keyboard)
        bot.send_message(message.chat.id, "Написать администратору @Burakov_Sergey")
        botan.track(constants.botan_key, message.chat.id, message, "Коворкинг")
    if message.text == "📅События":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but_2 = types.InlineKeyboardButton(text="Ближайшие 5 событий", callback_data="sobit5")
        keyboard.add(but_2)
        bot.send_message(message.chat.id, "Будьте в курсе основных событий в бизнесе Кубани! Подпишитесь на наш канал и узнайте о ближайщих событиях в крае", reply_markup=keyboard)
        botan.track(constants.botan_key, message.chat.id, message, "События")
    if message.text == "📦Пакеты услуг":
        bm.paketi_menu(bot, message)
        botan.track(constants.botan_key, message.chat.id, message, "Пакеты")
    if message.text == "🚀Открывай":
        bot.send_message(message.chat.id, """\r
<b>ОТКРЫВАЙ</b>
<i>Возможность открыть бизнес легко и без ошибок\n
Консультации: 
по вопросам регистрации в качестве индивидуального предпринимателя
по вопросам выбора формы собственности и системы налогообложения
по постановке управленческого учета и др.
по составлению бухгалтерской и налоговой отчетности
по действующим налоговым льготам
по возможностям портала Бизнес-Навигатор МСП
по действующим программам субсидирования предпринимателей. \n
Услуги: 
по разработке бизнес-планов
по разработке или модернизации веб сайтов
по созданию фирменного стиля\n
Обучение: 
образовательный проект «Школа молодого предпринимателя»
обучающие мероприятия Центра поддержки предпринимательства\n
Финансовая поддержка: 
предоставление микрозаймов до 700 тыс.руб. под 5,75% годовых на срок до 2 лет\n
Имущественная поддержка:
предоставление оборудованных офисных помещений в коворкинг центре «Место действия»
предоставление на льготных условиях помещений бизнес-инкубатора (г. Кропоткин). </i>\n""", parse_mode="HTML")
        bot.send_message(message.chat.id, """\r<a href="http://www.mbkuban.ru/" title="Узнайте подробнее">Узнайте подробнее</a>""", parse_mode="HTML")
        bot.send_message(message.chat.id, "+78007070711")
        botan.track(constants.botan_key, message.chat.id, message, "Открывай")
    if message.text == "📊Развивай":
        bot.send_message(message.chat.id, """\r
<b>РАЗВИВАЙ </b>
<i>Инструментарий развития действующего бизнеса \n
Kонсультации:
по вопросам финансового планирования
по вопросам юридического сопровождения деятельности
направленные на повышение доступности для малых и средних кредитных и иных финансовых ресурсов
по вопросам маркетингового сопровождения деятельности
по патентно-лицензионному сопровождению деятельности
по организации сертификации товаров, работ и услуг
по информационному сопровождению деятельности
по действующим программам субсидирования предпринимателей в сфере сельского хозяйства, промышленности, инноваций, занятости населения\n
Услуги:
по разработке бизнес-планов
по разработке или модернизации веб сайтов
по созданию фирменного стиля
по проведению маркетингового исследованию
по регистрации товарного знака
по анализу потенциала компании\n
Обучение:
образовательный проект «Школа молодого предпринимателя»
семинары, бизнес-тренинги, круглые столы, конференции Центра поддержки предпринимательства
программа Корпорации МСП «Азбука предпринимательства» \n
Финансовая поддержка:
предоставление микрозаймов до 3 млн. руб. под 7,75% годовых на срок до 3 лет
поручительства по кредитам, займам и банковским гарантиям до 70% от суммы кредита, но не более 25 млн. руб.
субсидии\n
Имущественная поддержка:
предоставление оборудованных офисных помещений в коворкинг центре «Место действия»
консультирование по вопросам предоставления муниципального имущества
предоставление на льготных условиях помещений бизнес-инкубатора (г. Кропоткин)</i>\n""", parse_mode="HTML")
        bot.send_message(message.chat.id, """\r<a href="http://www.mbkuban.ru/" title="Узнайте подробнее">Узнайте подробнее</a>""", parse_mode="HTML")
        bot.send_message(message.chat.id, "+78007070711")
        botan.track(constants.botan_key, message.chat.id, message, "Развивай")
    if message.text == "✅Производи":
        bot.send_message(message.chat.id, """\r
<b>ПРОИЗВОДИ </b>
<i>Приоритетная поддержка для производственных компаний \n

Консультации:
по повышению эффективности действующего производства
по действующим программам субсидирования предпринимателей в сфере сельского хозяйства, промышленности, инноваций, занятости населения\n
Услуги:
по разработке бизнес-планов
по разработке или модернизации веб сайтов
по созданию фирменного стиля
по проведению маркетингового исследованию
по регистрации товарного знака
по анализу потенциала компании
по модернизации технического перевооружения производства\n
Обучение:
по программе «Проектный подход к управлению бизнесом»
семинары, бизнес-тренинги, круглые столы, конференции Центра поддержки предпринимательства\n
Финансовая поддержка:
предоставление микрозаймов до 3 млн. руб. под 7,75% годовых на срок до 3 лет
поручительства по кредитам, займам и банковским гарантиям до 70% от суммы кредита, но не более 25 млн. руб.
разработка проектной документации и образцов, модернизация существующего оборудования на условиях софинансирования
предоставление налоговых льгот промышленным инвесторам в рамках специальных инвестиционный контрактов
субсидии\n
Имущественная поддержка:
предоставление оборудованных офисных помещений в коворкинг центре «Место действия»
консультирование по вопросам предоставления муниципального имущества</i>\n""", parse_mode="HTML")
        bot.send_message(message.chat.id, """\r<a href="http://www.mbkuban.ru/" title="Узнайте подробнее">Узнайте подробнее</a>""", parse_mode="HTML")
        bot.send_message(message.chat.id, "+78007070711")
        botan.track(constants.botan_key, message.chat.id, message, "Производи")
    if message.text == "🚚Экспортируй":
        bot.send_message(message.chat.id, """\r
<b>ЭКСПОРТИРУЙ </b>
<i>Поддержка экспортоориентированного бизнеса \n

Kонсультации:
по тематике ведения внешнеэкономической деятельности\n
Обучение:
семинары, бизнес-тренинги, круглые столы, конференции Центра поддержки экспорта;
по образовательной программе РЭЦ «Жизненный цикл экспортных проектов» \n
Экспортная поддержка:
участие в международных бизнес-миссиях;
участие в международных выставках за рубежом и на территории Российской Федерации;
подготовка и перевод на иностранные языки презентационных материалов;
проведение B2B-переговоров с иностранными партнерами;
создание и (или) модернизация сайта, в том числе на иностранном языке</i>\n""", parse_mode="HTML")
        bot.send_message(message.chat.id, """\r<a href="http://www.mbkuban.ru/" title="Узнайте подробнее">Узнайте подробнее</a>""", parse_mode="HTML")
        bot.send_message(message.chat.id, "+78007070711")
        botan.track(constants.botan_key, message.chat.id, message, "Экспортируй")
    if message.text == "Промышленность":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="При организации трудовой занятости осужденных", callback_data="sub1")
        but_2 = types.InlineKeyboardButton(text="На технологическое присоединение ", callback_data="sub2")
        but_3 = types.InlineKeyboardButton(text="На уплату % по кредитам полученным для пополнения оборотных средств", callback_data="sub3")
        but_4 = types.InlineKeyboardButton(text="На уплату % по кредитам и на уплату дохода лизинговых компаний", callback_data="sub4")
        but_5 = types.InlineKeyboardButton(text="На возмещение затрат, связанных с осуществ.образоват.деятельности", callback_data="sub5")
        but_6 = types.InlineKeyboardButton(text="На возмещение части затрат на реализацию инвестиционных проектов", callback_data="sub6")
        but_7 = types.InlineKeyboardButton(text="Контакты", callback_data="prom")
        key.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7)
        bot.send_message(message.chat.id, "Субсидии департамента промышленной политики Краснодарского края", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Суб.деп.промышл.")
    if message.text == "Сельское хозяйство":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Сельхозстрахование", callback_data="sh1")
        but_2 = types.InlineKeyboardButton(text="Приобретение элитных семян", callback_data="sh2")
        but_3 = types.InlineKeyboardButton(text="Поддержка племенного крупного рогатого скота мясного направления", callback_data="sh3")
        but_4 = types.InlineKeyboardButton(text="Субсидии на развитие садоводства и чаеводства", callback_data="sh4")
        but_5 = types.InlineKeyboardButton(text="Ознакомиться с другими субсидиями", callback_data="sh5")
        but_6 = types.InlineKeyboardButton(text="Контакты", callback_data="sh")
        key.add(but_1, but_2, but_3, but_4, but_5, but_6)
        bot.send_message(message.chat.id, "Субсидии министерства сельского хозяйства и перерабатывающей промышленности Краснодарского края", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Суб.деп.промышл.")
    if message.text == "Служба занятости":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Возмещение затрат на подготовку документов, представляемых при государственной регистрации", callback_data="trud1")
        but_2 = types.InlineKeyboardButton(text="Возмещение части затрат на дополнительное рабочее место для трудоустройства безработных граждан", callback_data="trud2")
        but_3 = types.InlineKeyboardButton(text="Единовременная финансовая помощь на открытие индивидуального предпринимателя или юридического лица", callback_data="trud3")
        but_6 = types.InlineKeyboardButton(text="Контакты", callback_data="trud")
        key.add(but_1, but_2, but_3, but_6)
        bot.send_message(message.chat.id, "Субсидии службы труда и занятости населения министерства труда и социального развития Краснодарского края", reply_markup=key)
        botan.track(constants.botan_key, message.chat.id, message, "Служба занятости")
    if message.text == "✒Жалобы и предложения":
        bot.send_message(message.chat.id, "Если у Вас есть вопросы, то напишите нам @VSVoronov @avdeev_v")
        botan.track(constants.botan_key, message.chat.id, message, "Жалобы и предложения")
    if message.text == "📝Консультация On-Line":
        bot.send_message(message.chat.id, "Для консультации on-line пишите @CPP_Makeeva")
        botan.track(constants.botan_key, message.chat.id, message, "Консультация On-Line")

while True:
    try:

        bot.polling(none_stop=True)

    except Exception as err:

        logging.error(err)

        time.sleep(5)

        print
        "Internet error!"