from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from hello.models import Account, Status, Profile, month, subscribersbot, typing, storage, security, changing



welcome = 'добро пожаловать!\nВы можете видеть свои отчеты\nЧерез меню настроек вы можете изменить свой пароль и логин'
start_text = 'Вы можете видеть свои отчеты\nЧерез меню настроек вы можете изменить свой пароль и логин'
TOKEN = '1328029303:AAFqLZ_GIcf_K6iw_TCnBFGNhvQZeIb4Rx4'
def start(update, context):
    if subscribersbot.objects.filter(user_id=update.message.chat.id):
        if subscribersbot.objects.get(user_id = update.message.chat.id).parol:
            i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
            i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
            mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
            update.message.reply_text(start_text, reply_markup = mrk)
            
        else:
            update.message.reply_text('Повторно введите пароль')
            istyping = typing.objects.get(user_id=update.message.chat.id)
            istyping.parol = True
            istyping.save()
    else:
        update.message.reply_text('введите логин')
        try:
            t = typing.objects.get(user_id=update.message.chat.id)
        except:
            t = typing.objects.get_or_create(user_id=update.message.chat.id, login=True, parol=False)
        
        ch = changing.objects.get_or_create(user_id=update.message.chat.id, login=False, parol=False)
        t.save()
        ch.save()


    bot = context.bot
    login = subscribersbot.objects.get(user_id = update.message.chat.id).login
    
    pseudonym = Profile.objects.get(login=login).pseudonym
    year = update.message.text[9:13]
    month = update.message.text[14:]
    
    obj = Account.objects.get(pseudonym=pseudonym, year=int(year), month=int(month)).document
    bot.send_document(update.message.chat.id, obj)
    i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
    i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
    mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
    update.message.reply_text('Welcome', reply_markup = mrk)
def callback_query(update, context):
    bot = context.bot
    c = update.callback_query
    
    if c.data == 'home':
        i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
        i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
        mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
        c.edit_message_text(start_text, reply_markup = mrk)
    if c.data == 'accounts':
        s = subscribersbot.objects.get(user_id = c.message.chat.id)
        obj = Profile.objects.get(login=s.login)
        all_accounts = Account.objects.filter(pseudonym=obj.pseudonym)
        
        if all_accounts:
            available = []
            items = []
            for i in all_accounts:
                if i.year in available:
                    pass
                else:
                    available.append(i.year)
                    items.append(InlineKeyboardButton(text=i.year, callback_data='year'+str(i.year)))
            i_back = InlineKeyboardButton(text = 'Назад', callback_data='home')
            items.append(i_back)
            mrk = InlineKeyboardMarkup([items])
            
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Выберите год', reply_markup=mrk)
        else:
            i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
            i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
            mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
            c.edit_message_text('Отчёты пока нет\n'+start_text, reply_markup = mrk)
            
    
    if c.data[:4] == 'year':
        
        obj = storage.objects.get_or_create(user_id=c.message.chat.id)
        y = obj[0]
        
        y.year = int(c.data[4:])
        y.save()
        login = subscribersbot.objects.get(user_id = c.message.chat.id).login
        obj = Profile.objects.get(login=login)
        all_accounts = Account.objects.filter(pseudonym=obj.pseudonym, year = int(c.data[4:]))
        
        available = []
        items = []
        for i in all_accounts:
            if i.month in available:
                pass
            else:
                available.append(i.month)
                items.append(InlineKeyboardButton(text=i.month.month, callback_data='month'+str(i.month.month)))
        year = c.data[4:]
        buttons = []
        massiv = []
        for i in items:
            massiv.append(i)
            if len(massiv) == 3:
                buttons.append(massiv)
                massiv = []


        if massiv:
            buttons.append(massiv)
        i_back = InlineKeyboardButton(text = 'Назад', callback_data='accounts')
        buttons.append([i_back])
        
        markup = InlineKeyboardMarkup(buttons)
        
        c.edit_message_text('Год: '+year+'\nвыберите месяц', reply_markup=markup)
    
    if c.data[:5] == 'month':
        months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        login = subscribersbot.objects.get(user_id = c.message.chat.id).login
        obj = Profile.objects.get(login=login)
        year = storage.objects.get(user_id=c.message.chat.id).year
        all_accounts = Account.objects.get(pseudonym = obj.pseudonym, year = year, month = months.index(c.data[5:]) + 1)
        i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
        i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')

        mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
        period = 'Период: '+ all_accounts.month.month + ' ' + str(all_accounts.year)
        if obj.card_number:
            card = '\n' + str(obj.card_number)
        else:
            card = ''
        try:
            status = all_accounts.status.s
        except:
            status = "Не оплачен"
        
        if all_accounts.summa:
            summa = '\nСумма: ' + all_accounts.summa
        else:
            summa = ''


        text = period + summa + '\nСтатус: ' + status + card
        c.edit_message_text(text)
        
        bot.send_document(c.message.chat.id, all_accounts.document)
        c.message.reply_text(start_text, reply_markup = mrk)
    
    if c.data == 'setting':
        i_da = InlineKeyboardButton(text = 'Да', callback_data='change_login')
        mrk = InlineKeyboardMarkup([[i_da]])
        c.edit_message_text('Хотите обновить логин и пароль?', reply_markup=mrk)
    
    if c.data == 'change_login':
        c.edit_message_text('пожалуйста, введите новый логин:')
        ch = changing.objects.get(user_id=c.message.chat.id)
        ch.login = True
        ch.save()
      
    
    if c.data == 'start':
        obj = subscribersbot.objects.get(user_id=c.message.chat.id)
        obj.delete()

        bot.send_message(c.message.chat.id, 'Введите логин')
        try:
            t = typing.objects.get(user_id=c.message.chat.id)
            t.login = True
            t.parol = False
        except:
            t = typing.objects.get_or_create(user_id=c.message.chat.id, login=True, parol=False)
        
        ch = changing.objects.get_or_create(user_id=c.message.chat.id, login=False, parol=False)
        t.save()
        ch.save()

    if c.data == 'deleteuser':
        
        i_back = InlineKeyboardButton(text='Назад', callback_data='start')
        mrk = InlineKeyboardMarkup([[i_back]])
        bot.send_message(c.message.chat.id, 'Введите пароль', reply_markup=mrk)
        t = typing.objects.get(user_id=c.message.chat.id)
        t.parol = True
        t.save()
            
def text(update, context):
    bot = context.bot
    try:
        ischanging = changing.objects.get(user_id = update.message.chat.id)
        istyping = typing.objects.get(user_id=update.message.chat.id)
    except:
        dwedewdw = 0

    if istyping.login:
        if subscribersbot.objects.filter(login=update.message.text):
            i_back = InlineKeyboardButton(text='Назад', callback_data='start')
            i_yes = InlineKeyboardButton(text='Да', callback_data='deleteuser')
            mrk = InlineKeyboardMarkup([[i_back, i_yes]])
            update.message.reply_text('К этому профилю уже подключен другой пользователь.\тХотите авторизоваться и удалить другого пользователя?', reply_markup=mrk)
            subscribersbot.objects.create(user_id=update.message.chat.id, login=update.message.text, parol = 'r/e/q')
            istyping.login = False
            istyping.save()
        elif Profile.objects.filter(login=update.message.text):
            subscribersbot.objects.create(user_id=update.message.chat.id, login=update.message.text)
            istyping.login = False
            istyping.parol = True
            istyping.save()
            update.message.reply_text('Хорошо, введите пароль')
        else:
            update.message.reply_text('Неправильно, повторно введите логин')
    elif istyping.parol:
        current_login = subscribersbot.objects.get(user_id=update.message.chat.id)
        if current_login.parol == 'r/e/q':
            prof_obj = Profile.objects.get(login=current_login.login)
            if prof_obj.parol == update.message.text:
                del_obj = subscribersbot.objects.get(login = prof_obj.login, parol = prof_obj.parol)
                bot.send_message(del_obj.user_id, 'К Вашему профилю только что подключился другой пользователь. Если это были не вы то немедленно обратитесь Вашему менеджеру по работе с партнерами или по почты: support@nevo.uz')
                typing.objects.get(user_id = del_obj.user_id).delete()
                changing.objects.get(user_id = del_obj.user_id).delete()
                del_obj.delete()

                obj = subscribersbot.objects.get(user_id=update.message.chat.id)
                obj.parol = update.message.text
                obj.save()
                istyping.parol = False
                
                istyping.save()
                i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
                i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
                mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
                update.message.reply_text(welcome, reply_markup = mrk)



        elif Profile.objects.get(login=current_login.login).parol == update.message.text:
            obj = subscribersbot.objects.get(user_id=update.message.chat.id)
            obj.parol = update.message.text
            obj.save()
            istyping.parol = False
            istyping.save()
            i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
            i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
            mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
            update.message.reply_text(welcome, reply_markup = mrk)
        else:
            update.message.reply_text('неверно, пожалуйста, введите пароль еще раз')
    elif ischanging.login:
        subs = subscribersbot.objects.get(user_id = update.message.chat.id)
        prof = Profile.objects.get(login = subs.login)
        try:
            Profile.objects.get(login=update.message.text)
            update.message.reply_text('Этот логин доступен, пожалуйста, введите другой логин')
        except:
            subs.login = update.message.text
            prof.login = update.message.text
            subs.save()
            prof.save()
            ischanging.login = False
            ischanging.parol = True
            ischanging.save()
            update.message.reply_text('логин, успешно изменен\n введите новый пароль:')
    elif ischanging.parol:
        subs = subscribersbot.objects.get(user_id = update.message.chat.id)
        prof = Profile.objects.get(login = subs.login)
        subs.parol = update.message.text
        prof.parol = update.message.text
        subs.save()
        prof.save()
        update.message.reply_text('пароль успешно изменен')
        i_accounts = InlineKeyboardButton(text='Отчеты', callback_data='accounts')
        i_setting = InlineKeyboardButton(text='Настройки', callback_data='setting')
        mrk = InlineKeyboardMarkup([[i_accounts, i_setting]])
        update.message.reply_text(start_text, reply_markup = mrk)
        ischanging.parol = False
        ischanging.save()
def error(update, context):
    
    print(logger.warning('Update "%s" caused error "%s"', update, context.error))
# update bot
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, text))
dp.add_handler(CallbackQueryHandler(callback_query))
dp.add_error_handler(error)
updater.start_polling()










class Command(BaseCommand):
    help="BOT"
    def handle(self, *args, **options):
        pass