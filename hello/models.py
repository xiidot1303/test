from django.db import models

class Account(models.Model):
    pseudonym = models.CharField(null=True, max_length=40, verbose_name="Псевдоним")
    
    month = models.ForeignKey('month', null=True, on_delete=models.PROTECT, verbose_name="Месяц")
    year=models.IntegerField(null=True, verbose_name="Год")
    status = models.ForeignKey('Status', null = True, on_delete=models.PROTECT, verbose_name="Статус", blank=True)
    day_payment = models.CharField(verbose_name="Дата оплата", null=True, max_length=40)
    document = models.FileField(upload_to='%Y/%m/%d/', null=True)
    published = models.DateTimeField(db_index = True, null=True, auto_now_add=True)
    summa = models.CharField(max_length=20, null=True)
    card_number = models.CharField(max_length=50, null=True)
    comment = models.TextField(blank=True, null=True)

    
class Status(models.Model):
    s = models.CharField(max_length=20, db_index=True, null=True)
    def __str__(self):
        return self.s

class Profile(models.Model):
    published = models.DateTimeField(db_index = True, null=True, verbose_name='published date', name='published')
    login = models.CharField(null=True, max_length=50, verbose_name="Логин")
    parol = models.CharField(null=True, max_length=50, verbose_name="Парол")
    pseudonym = models.CharField(null=True, max_length=50, verbose_name="Псевдоним")
    number = models.IntegerField(blank=True, verbose_name="")
    code = models.CharField(max_length=5, blank=True, verbose_name="t", null=True)
    name = models.CharField(max_length=50, blank=True, verbose_name="name")
    prefix = models.CharField(max_length=20, null=True)
    type_payment = models.CharField(max_length=50, null=True)
    valute_card = models.CharField(max_length=10, null=True)
    card_number = models.CharField(max_length=30, null=True)
    date_card = models.CharField(max_length=20, null=True, blank=True)
    owner_card = models.CharField(null=True, max_length=100)
    comment = models.TextField(blank=True, null=True)
class card(models.Model):
    pseudonym = models.CharField(max_length=50, null=True)
    card_number = models.CharField(max_length=50, null=True)
    type_payment = models.CharField(max_length=50, null=True, blank=True)
    valute_card = models.CharField(max_length=10, null=True, blank=True)
    card_number = models.CharField(max_length=30, null=True, blank=True)
    owner_card = models.CharField(null=True, max_length=100, blank=True)
class month(models.Model):
    month = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.month

class sendmessage(models.Model):
    select = models.CharField(max_length=50, null=True)
    message = models.TextField(max_length=500, null=True)

class subscribersbot(models.Model):
    user_id = models.IntegerField(null=True)
    login = models.CharField(null=True, max_length=100)
    parol = models.CharField(null=True, max_length=100, blank=True)
class typing(models.Model):
    user_id = models.IntegerField(null=True)
    login = models.BooleanField(primary_key=False, blank=True)
    parol = models.BooleanField(primary_key=False, blank=True)
class changing(models.Model):
    user_id = models.IntegerField(null=True)
    login = models.BooleanField(primary_key=False, blank=True)
    parol = models.BooleanField(primary_key=False, blank=True)
class storage(models.Model):
    user_id = models.IntegerField(null=True)
    year = models.IntegerField(null=True, blank=True)

class security(models.Model):
    parol = models.CharField(null=True, max_length=100)

class stories(models.Model):   #all stories otchets and profiles, for table
    published = models.DateTimeField(db_index = True, null=True, auto_now_add=True)
    admin = models.CharField(max_length=100, null=True)
    obj = models.CharField(max_length=20, null=True)
    text = models.TextField(null=True)
    obj_id = models.IntegerField(null=True, blank=True)


class action_story(models.Model):   # 4) у каждой действии оставлять подписи админов. +разработать просмотра истории с объектами (с отчетами, с партнерами)
    username = models.CharField(max_length=100, null=True) 
    obj = models.CharField(max_length=20, null=True)
    pseudonym = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=30, null=True)


class acc_pre_value(models.Model):
    pseudonym = models.CharField(null=True, max_length=40, verbose_name="Псевдоним")
    
    month = models.CharField(null=True, max_length=100)
    year=models.IntegerField(null=True, verbose_name="Год")
    status = models.CharField(null=True, max_length=100)
    day_payment = models.CharField(verbose_name="Дата оплата", null=True, max_length=40)
    document = models.FileField(upload_to='%Y/%m/%d/', null=True)
    published = models.DateTimeField(db_index = True, null=True, auto_now_add=True)
    summa = models.CharField(max_length=20, null=True)
    card_number = models.CharField(max_length=50, null=True)

class prof_pre_value(models.Model):
    
    login = models.CharField(null=True, max_length=50, verbose_name="Логин")
    parol = models.CharField(null=True, max_length=50, verbose_name="Парол")
    pseudonym = models.CharField(null=True, max_length=50, verbose_name="Псевдоним")
    number = models.IntegerField(blank=True, verbose_name="")
    code = models.CharField(max_length=5, blank=True, verbose_name="t", null=True)
    name = models.CharField(max_length=50, blank=True, verbose_name="name")
    prefix = models.CharField(max_length=20, null=True)
    type_payment = models.CharField(max_length=50, null=True)
    valute_card = models.CharField(max_length=10, null=True)
    card_number = models.CharField(max_length=30, null=True)
    date_card = models.CharField(max_length=20, null=True, blank=True)
    owner_card = models.CharField(null=True, max_length=100)
    comment = models.TextField(blank=True, null=True)

class contract(models.Model):
    file = models.FileField(upload_to='main/', null=True)




class Audio(models.Model):
    composition = models.CharField(null=True, max_length=200, verbose_name='Произведение')
    artist = models.CharField(null=True, max_length=100, verbose_name='Артист')
    autor_music = models.CharField(null=True, max_length=100, verbose_name='Автор музыки')
    autor_text = models.CharField(null=True, max_length=100, verbose_name='Автор текста')
    album = models.CharField(null=True, max_length=100, verbose_name='Альбом')
    isrc = models.CharField(null=True, max_length=100, verbose_name='ISRC (код)')
    genre = models.CharField(null=True, max_length=50, verbose_name='Жанр')
    copyright = models.CharField(null=True, max_length=100, verbose_name='Авторские права')
    related_rights = models.CharField(null=True, max_length=100, verbose_name='Смежные права')
    upc = models.CharField(null=True, max_length=100, verbose_name='UPC')
    release_date = models.CharField(null=True, max_length=100, verbose_name='Дата релиза')
    territory = models.CharField(null=True, max_length=100, verbose_name='Территория')
    link = models.CharField(null=True, max_length=200, verbose_name='Ссылка на файл')
    pseudonym = models.CharField(null=True, blank=True, max_length=100)
    status = models.CharField(null=True, blank=True, max_length=5)

class Video(models.Model):
    composition = models.CharField(null=True, max_length=200, verbose_name='Произведение')
    type = models.CharField(null=True, max_length=100, verbose_name='Тип')
    artist = models.CharField(null=True, max_length=100, verbose_name='Артист')
    isrc = models.CharField(null=True, max_length=100, verbose_name='ISRC (код)')
    producer = models.CharField(null=True, max_length=100, verbose_name='Режиссер-постановщик')
    operator = models.CharField(null=True, max_length=100, verbose_name='Оператор-постановщик')
    autor_script = models.CharField(null=True, max_length=100, verbose_name='Автор сценария')
    painter = models.CharField(null=True, max_length=100, verbose_name='Художник-постановщик')
    copyright = models.CharField(null=True, max_length=100, verbose_name='Авторские права')        
    release_date = models.CharField(null=True, max_length=100, verbose_name='Дата релиза')
    territory = models.CharField(null=True, max_length=100, verbose_name='Территория')
    link = models.CharField(null=True, max_length=200, verbose_name='Ссылка на файл')
    pseudonym = models.CharField(null=True, blank=True, max_length=100)
    status = models.CharField(null=True, blank=True, max_length=5)
