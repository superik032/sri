phone = '+79026381976'  # Номер киви
qiwi_token = '5f02ec7ca92bead9b8019c58cf94a03f'  # https://qiwi.com/api
telegram_token = '1968531829:AAENYJbCbUgRR5bGY1jGxWKf4jAQlli1FHI'  # Бота создавать через @Botfather
easyliker_token = 'NcsY3a3meGUSRjBqG6mN9db9e9WPy1KD'  # Токен получать тут https://easyliker.ru/profile/api

admins = [803029497]  # список адинов через запятую
send_notify = 1  # Отправлять уведомления при покупке? 1 - Да 0 - Нет
min_balance = 10  # Отправка уведомления если баланс после покупки составляет меньше x рублей
min_refill = 50  # Минимальная сумма пополнения
extra_charge = 200  # Наценка в процентах

supports = 'TG: https://t.me/orkhangusejnov'  # контакты тех.поддержки


"""
Резервные слова:
first_name - Имя
last_name - Фамилия 
id - Ид юзера
username - Ник юзера

"""

start_msg = f'Привет,<b>first_name</b>👋. Это бот для раскрутки своих соц. сетей. У нас самые дешевые цены и самый большой выбор.\nИспользуй кнопки ниже, что бы купить накрутку.'  # Первый запуску
help_msg = f'Что-то сломалось или появились вопросы?\nТы всегда можешь обратиться к нам по контактам: {supports}'


msg_menu = '<b>first_name</b>, Я вывел тебе кнопки, что бы мог пользоваться ботом.'  # Главное меню

msg_support = f'Наши контакты для связи {supports}'  # Тех. поддержка

other_type = 'Ничего не понял🧐, но на всякий случай переведу Вас в меню'  # Если человек отравил не текст

balance_msg = f'Ваш ID: <b>id</b>\nТекущий баланс: BALANCE₽\nВсего заказов: COUNT_ORDERS'  # BALANCE - баланс  COUNT_ORDERS - кол-во заказов

choice_website = 'Выберите социальную сеть, которую хотите раскрутить.'  # Выбор соц сети

choice_type = 'Выберите тип предоставляемой услуги в социальной сети <b>WEBSITE</b>.'  # WEBSITE - соц сеть

choice_quality = 'Выберите качество накрутки <b>TYPE</b> в социальной сети <b>WEBSITE</b>.'  # TYPE меняется на тип накрутки в Р.п

input_link_ = 'Введите ссылку.\n<code>Не забудьте открыть профиль</code>'  # Ввод ссылки

success_purchase = f'Спасибо за покупку! Ваш заказ выполняется.\nСтатус заказа можно отслеживать, нажав кнопку <b>мои заказы</b>'  # Успешная покупка

input_count = f"Введите количество.\n<code>Минимальное кол-во для заказа - MIN</code>"  # MIN - минимальное кол-во для заказа. У каждого свое значение

if_min_refill = f'Минимальная сумма пополнения составляет {min_refill}₽'  # Если меньше минимального пополнения

input_refill = f'Введите сумму пополнения.\n<code>Минимальная сумма пополнения - {min_refill}₽</code>'

bill = f'Счет для оплаты:\nНомер для оплаты: {phone}\nСумма к оплате: SUM\nКомментарий к переводу: COMMENT'  # Счет для оплаты

no_orders = 'У вас пока нету заказов'  # Если у человека нету заказов



"""текст кнопки при выборе типа накрутки"""
dict_types = {'comments': 'Комментарии💬',
              'likes': 'Лайки❤️',
              'clip_views': 'Просмотры клипов',
              'reply_comments': 'Ответы на комментарии',
              'comment_likes': 'Лайки комментариев',
              'poll_votes': 'Опросы',
              'chat_participants': 'Участники беседы',
              'subs': 'Подписчики👥',
              'views_history': 'Просмотры истории👀',
              'video_views': 'Просмотры видео👀',
              'views': 'Просмотры👀',
              'friends': 'Друзья👥',
              'group_subs': 'Подписчики в группу👥',
              'reposts': 'Репорты📢 ',
              'reports': 'Жалобы',
              'post_views': 'Глазики👁',
              'channel_subs': 'Подписчики на канал👥',
              ' ': ' '}

"типы накрутки в Р.п для choice_quality """
genitive_dict = {'comms': 'комментариев',
                 'likes': 'лайков',
                 'subs': 'подписчиков',
                 'views_history': 'просмотров истории',
                 'video_views': 'просмотров видео',
                 'views': 'просмотров',
                 'friends': 'друзей',
                 'group_subs': 'подписчиков в группу',
                 'interviews': '123',
                 'reposts': 'репортов',
                 'post_views': 'глазиков на пост',
                 'channel_subs': 'подписчиков на канал'}