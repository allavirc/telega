import random
import time
import config
import telebot
from telebot import types


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_welcome = types.KeyboardButton('Привет! Давай)')

    markup.add(button_welcome)

    bot.send_message(message.chat.id, "Привет, <b>{0.first_name}!</b>\nЕсли ты обратилась ко мне значит тебя что-то беспокоит.\n"
                                      "Давай выясним насколько это серьезно".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('да, здорово 😊')

    markup.add(button)

    if message.chat.type == 'private':
        if message.text == 'Привет! Давай)':

            bot.send_message(message.chat.id, 'Выбери какая помощь тебе необходима:\n\n'
                                              '1) Тебе сложно эмоционально, страшно/ случаются панические'
                                              'атаки тогда отправь мне цифру <b>1</b>\n\n'
                                              '2) Тебя беспокоит твое физическое состояние?\n'
                                              'Что-то болит и ты чувствуешь что что-то не так?\n'
                                              'Жми цифру <b>2</b>'.format(message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)


        if message.text == '1':

            bot.send_message(message.chat.id, 'Постарайся максимально расслабиться и я задам тебе несколько легких вопросов'.format(message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)

            time.sleep(3)

            markup2 = types.InlineKeyboardMarkup(row_width=2)
            button_yes = types.InlineKeyboardButton("Да", callback_data='yes')
            button_no = types.InlineKeyboardButton("Нет", callback_data='no')

            markup2.add(button_yes, button_no)

            bot.send_message(message.chat.id, 'С тех пор, как я узнала, что беременна, я нахожусь в нервном напряжении',reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'Я стараюсь вообще не думать ни о беременности, ни о предстоящих родах',reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'Я не задумываюсь о предстоящем материнстве',reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'Я плохо сплю ночью, часто снятся кошмары', reply_markup=markup2)
            time.sleep(5)
            bot.send_message(message.chat.id, 'Меня мало интересует  отношение  к  моей  беременности  даже близких мне людей', reply_markup=markup2)
            time.sleep(5)

            markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = types.KeyboardButton('Узнать результаты теста!')

            markup5.add(button)

            bot.send_message(message.chat.id, 'Нажми на кнопку, чтобы узнать результаты'.format(
                message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup5)


        if message.text == '2':

            markup3 = types.InlineKeyboardMarkup(row_width=2)
            button_yes = types.InlineKeyboardButton("Головная боль", callback_data='head')
            button_no = types.InlineKeyboardButton("Токсикоз", callback_data='tox')

            markup3.add(button_yes, button_no)

            bot.send_message(message.chat.id, 'Что тебя беспокоит?',
                             reply_markup=markup3)
            time.sleep(5)

            # if message.callback_data == 'head':
            #     ...

    if message.text == 'да, здорово 😊':

        ans_good = []
        bad_list = []
        warning = []

        bot.send_message(message.chat.id, 'Напишите как часто происходит рвота за день?'.format(
            message.from_user, bot.get_me()), parse_mode='html')

        if int(message.text) <= int('5'):
            ans_good.append('*')

        if int(message.text) > int('5') and message.text <= int('10'):
            bad_list.append('*')

        if int(message.text) > int('10'):
            warning.append('*')

        if message.text == '3' or '5' or '12':

            bot.send_message(message.chat.id, 'Напишите сколько килограмм вы потеряли за неделю?'.format(
                message.from_user, bot.get_me()), parse_mode='html')

            if int(message.text) <= int('2'):
                ans_good.append('*')

            if int(message.text) > int('2') and int(message.text) <= int('4'):
                bad_list.append('*')

            if int(message.text) > int('4'):
                warning.append('*')

        if message.text == '1' or '3' or '12':

            bot.send_message(message.chat.id, 'Напишите сколько часов в сутки вы спите?'.format(
                message.from_user, bot.get_me()), parse_mode='html')

            if int(message.text) >= int('7'):
                ans_good.append('*')

            if int(message.text) < int('7'):
                bad_list.append('*')

            if int(message.text) < int('5'):
                warning.append('*')

        markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton('Узнать результаты диагностики')

        markup6.add(button)

        bot.send_message(message.chat.id, 'Нажми на кнопку, чтобы узнать результаты'.format(
            message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup6)


        if message.text == 'Узнать результаты диагностики':

            if len(ans_good) > len(bad_list) or len(ans_good) > len(warning):

                        bot.send_message(message.chat.id,
                                     f'Вам и вашему малышу не гразит никакой опасности.\n\n'
                                     f'Ранний токсикоз с вашими показателями это нормальное '
                                     f'состояние для беременной девушки\n\n'
                                     f'Но все же, если вы чувствуете, что что-то не так,'
                                     f'или я что-то упустил - обязательно обратитесь к врачу')

            if len(bad_list) > len(ans_good) or len(bad_list) > len(warning):

                        bot.send_message(message.chat.id,
                                     f'У вас обнаружен токсикоз средней тяжести.\n\n'
                                     f'При таких показателях легко может развиться '
                                     f'обезвоживание отрганизма - это опасно как для вас, '
                                     f'так и для вашего малыша\n\n'
                                     f'Вызовите скорую\n\n'
                                     f'Что говорить- Меня зовут ... Мой адрес ...'
                                     f'Срок беременности ...'
                                     f'У меня токсикоз средней тяжести, 2 категория')

            if len(warning) > len(ans_good) or len(warning) > len(bad_list):

                        bot.send_message(message.chat.id,
                                     f'У вас обнаружен опасный для жизни токсикоз\n\n'
                                     f'Показатели указывают на обезвоживание'
                                     f'организма - это опасно\n\n'
                                     f'Срочно!'
                                     f'Вызовите скорую\n\n'
                                     f'Что говорить- Меня зовут ... Мой адрес ... '
                                     f'Срок беременности ...'
                                     f'У меня обезвоживание организма, 1 категория\n\n'
                                     f'Если вы не в силах этого сделать или долго не можете'
                                     f'дозвониться до скорой, немедленно сообщите об этом близким')


        if message.text == 'Узнать результаты теста!':

            bad_answer_list = [
                'Твой организм проделывает колосальную работу поэтому это может\n'
                'негативно сказываться на твоем эмоциональном и психическом состоянии.\n\n'
                'Позволь дать пару советов, которые смогут тебе помочь'
            ]

            if len(yes_list) >= len(no_list):
                markup_lets = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button_welcome = types.KeyboardButton('Узнать советы)')

                markup_lets.add(button_welcome)

                bot.send_message(message.chat.id, f'{random.choice(bad_answer_list)}\n\n'
                                                  f'Если же отрицательные эмоции никак не проходят, '
                                                  f'постоянно наблюдается плохое настроение, сопровождающееся '
                                                  f'снижением или потерей аппетита, бессонницей, физической слабостью, '
                                                  f'апатией, тоской, чувством безысходности, то в такой ситуации без '
                                                  f'помощи врача не обойтись.\n\n'
                                                  f'Все вышеперечисленное – это признаки депрессии, '
                                                  f'которая не является безобидным состоянием, '
                                                  f'а представляет собой серьезную болезнь.\n\n'
                                                  f'Длительная депрессия обязательно нуждается в лечении.', reply_markup=markup_lets)

            good_anwer_list = [
                'не забывай о том, что психологические изменения в организме беременной женщины временны. '
                'После родов они уже не будут беспокоить, так как появится на свет маленькое чудо, '
                'которое будет приносить счастье и радость',

                'старайся не загонять все свои обиды и мрачные мысли в глубину души '
                '(беременным женщинам издавна советовали делиться своими размышлениями '
                'с близкими людьми, рассказывать о своих проблемах',

                'начать подготовку вещей для малыша или хотя бы составить список всего необходимого, '
                'присмотреть определенные товары.'
                'Нужно не забывать, что беременность является периодом перемен. '
                'Противоречивые чувства всё равно могут посещать женщину в положении. '
                'Задача состоит в том, чтобы значительно уменьшить отрицательные эмоции и увеличить положительные',

                'Не стоит переживать из-за внешних изменений (например, из-за лишних килограмм, плохого состояния волос '
                'или кожи). Все эти явления временны. Когда женщина примет свое новое состояние по-настоящему, то она станет '
                'очень обаятельной несмотря ни на что.'
            ]

            if len(no_list) >= len(yes_list):
                bot.send_message(message.chat.id,
                                 f'Все отлично!\nУ вас хорошие результаты, но на всякий случай вот тебе совет как избежать эмоционального выгорания:\n\n    '
                                 f'{random.choice(good_anwer_list)}')

            if message.text == 'Узнать советы)':
                bot.send_message(message.chat.id,
                                 f'А вот один из полезных советов для тебя:\n\n'
                                 f'{random.choice(good_anwer_list)}')

yes_list = []
no_list = []
answer = '*'


@bot.callback_query_handler(func=lambda call: True)
def callback_buttons(call):
    try:
        if call.message:
            if call.data == 'yes':
                yes_list.append(answer)

            if call.data == 'no':
                no_list.append(answer)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Ответ принят',
                                  reply_markup=None)

            if call.data == 'tox':

                bot.send_message(call.message.chat.id, f'Сейчас я задам несколько вопросов:')

    except Exception as e:
        print(repr(e))

    return f'{len(yes_list)} --- {no_list}'



bot.polling(none_stop=True)
