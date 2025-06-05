from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField()
    description = models.TextField()
    link = models.URLField()
    
    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE) # удалит всё о его фильмах
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    vendor_code = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    img = models.URLField()

    def __str__(self):
        return self.title


class Personal_Info(models.Model):
    name = models.CharField(
        verbose_name="Имя",
        default="Иван",
        max_length=20,
    )
    
    surname = models.CharField(
        verbose_name="Фамилия",
        default="Иванов",
        max_length=20,
    )
    
    phone = models.CharField(
        verbose_name="Номер телефона",
        default="+7 999 999 99 99",
        max_length=20,
    )
    
    email = models.EmailField(
        verbose_name="Адрес эл. почты",
        default="example@gmail.com",
        max_length=20,
        help_text="Обязательно для заполнения"
    )
    
    date = models.DateTimeField(
    verbose_name="Дата отправки данных", 
    auto_now_add=True
    )
    
    contact_choices = (
    ('email', 'Электронная почта'),
    ('phone', 'Телефон'),
    ('messenger', 'Мессенджер'),
    ('socials', 'Социальные сети')
    )
    
    contact = models.CharField(
        verbose_name="Предпочитаемый способ взаимодействия",
        choices=contact_choices,
        default='email',
        max_length=255)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = "Контактные данные"
        verbose_name_plural = "Контактные данные"
        ordering = ("-pk", )
        

class Feedback(models.Model):
    person = models.ForeignKey(
        'Personal_Info',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    
    like_choices = (
    ('yes', 'Да'),
    ('no', 'Нет')
    )
    like = models.CharField(
        verbose_name="Нравятся ли вам фильмы Studio Ghibli?",
        choices=like_choices,
        default='yes',
        max_length=255)
    
    number_of_movies = models.PositiveIntegerField(
        verbose_name="Как много фильмов Studio Ghibli вы смотрели?",
        default='0')
    
    character_choices = (
    ('Totoro', 'Тоторо'),
    ('Chihiro', 'Тихиро Огино'),
    ('NoFace', 'Безликий'),
    ('Princess Mononoke', 'Сан (Принцесса Мононоке)'),
    ('Howl', 'Хаул')
    )
    characters = models.CharField(
        verbose_name="Какие из перечисленных персонажей вам больше всего нравятся?",
        choices=character_choices,
        default='Totoro',
        max_length=255)
    
    producer_choices = (
    ('Хаяо Миядзаки', 'Хаяо Миядзаки'),
    ('Хироюки Морита', 'Хироюки Морита'),
    ('Хиромаса Ёнэбаяси', 'Хиромаса Ёнэбаяси'),
    ('Томоми Мотидзуки', 'Томоми Мотидзуки'),
    ('Михаэль Дюдок де Вит', 'Михаэль Дюдок де Вит'),
    ('Исао Такахата', 'Исао Такахата'),
    ('Ёсифуми Кондо', 'Ёсифуми Кондо'),
    ('Горо Миядзаки', 'Горо Миядзаки'),
    )
    fav_producer = models.CharField(
        verbose_name="Фильмы какого режиссера вы предпочитаете?",
        choices=producer_choices,
        default='Хаяо Миядзаки',
        max_length=255)
    
    film_choices = (
    ('film1', '«Унесенные призраками»'),
    ('film2', '«Мой сосед Тоторо»'),
    ('film3', '«Небесный замок Лапута»'),
    ('film4', '«Ведьмина служба доставки»'),
    ('film5', '«Шепот сердца»'),
    ('film6', '«Принцесса Мононоке»'),
    ('film7', '«Ходячий замок»'),
    ('film8', '«Рыбка Поньо на утесе»'),
    ('film9', '«Со склонов Кокурико»'),
    ('film10', '«Ветер крепчает»'),
    )
    films = models.CharField(
        verbose_name="Какой из представленных фильмов по вашему мнению является лучшим?",
        choices=film_choices,
        default='film1',
        max_length=255)
    
    fav_film = models.TextField(
        verbose_name="Какой ваш любимый фильм студии и почему?",
    )
    
    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опрос"
        ordering = ("-pk", )
        
    def __str__(self):
        return f'{self.person.name} {self.person.surname}'
    