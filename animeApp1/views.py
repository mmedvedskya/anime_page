from django.shortcuts import render, redirect
from django.http import HttpResponse


def pages(request):
    url_elements = request.path.split("/")
    if url_elements[-2] == "welcome":
        return render(request, "index.html")
    elif url_elements[-2] == "directors":
        return render(request, "lists.html")
    elif url_elements[-2] == "top5":
        return render(request, "characters.html", {"characters": get_chars()})
    elif url_elements[-2] == "store":
        return render(request, "pick_me.html", {"products": get_products()})
    elif url_elements[-2] == "studio":
        return redirect("https://ru.wikipedia.org/wiki/Studio_Ghibli")
    elif url_elements[-2] == "education":
        context = get_edu()
        return render(request, "my_edu.html",  context)
    else:
        return redirect("animeApp1:Welcome")

# query - with no arguments here, in url and navigation (inside %)
def task_11_01(request):
    food = request.GET.get('food', '').strip()
    cals = request.GET.get('cals', '').strip()
    error_message = None
    result = ''
    if not food:
        error_message = 'Введите названия продуктов'
    elif not cals:
        error_message = 'Введите калорийность продуктов'
    else: 
        list_food = food.split()
        list_cals = cals.split()
        
        if len(list_food) != len(list_cals):
            error_message = 'Неполноценная информация о продуктах'
        elif len(set(list_food)) != len(list_food):
            error_message = 'Продукты не должны повторяться'
        else:
            calories = {}
            try:
                for i in range(len(list_food)):
                    a, b, c = map(float, list_cals[i].split('-'))
                    count = 0.4*a + 0.3*b + 0.3*c
                    calories[count] = list_food[i]
                result = calories[min(calories)]
            except ValueError:
                error_message = 'Некорректный формат калорийности'
    return render(request, "alg.html", {'result': result, 'food': food,'cals': cals, 'error_message': error_message})

# path
def task_11_02(request, food, cals=None):
    error_message = None
    result = ''
    if not food:
        error_message = 'Введите названия продуктов'
    elif not cals:
        error_message = 'Введите калорийность продуктов'
    else: 
        list_food = food.split()
        list_cals = cals.split()
        
        if len(list_food) != len(list_cals):
            error_message = 'Неполноценная информация о продуктах'
        elif len(set(list_food)) != len(list_food):
            error_message = 'Продукты не должны повторяться'
        else:
            calories = {}
            try:
                for i in range(len(list_food)):
                    a, b, c = map(float, list_cals[i].split('-'))
                    count = 0.4*a + 0.3*b + 0.3*c
                    calories[count] = list_food[i]
                result = calories[min(calories)]
            except ValueError:
                error_message = 'Некорректный формат калорийности'
    return render(request, "alg.html", {'result': result, 'food': food,'cals': cals, 'error_message': error_message})

def get_chars():
    return [
        {
            "name": "Хаул",
            "image": "pictures/char1.jpg",
            "description": "Могущественный волшебник, известный своим эксцентричным поведением и тщеславием, живет в волшебном ходячем замке. Развитие персонажа, от эгоцентричного волшебника до самоотверженного героя, занимает центральное место в повествовании фильма «Ходячий замок».",
            "link": "https://shikimori.one/characters/507-howl",
        },
        {
            "name": "Тоторо",
            "image": "pictures/char2.jpg",
            "description": "Тоторо из фильма «Мой сосед Тоторо» — большой дружелюбный лесной дух, который подружился с двумя девочками, когда они справляются с проблемами, связанными с болезнью их матери и переездом в новый дом. С его пушистым внешним видом, Тоторо воплощает в себе волшебство и невинность детства.",
            "link": "https://shikimori.one/characters/269-totoro",
        },
        {
            "name": "Тихиро Огино",
            "image": "pictures/char3.jpg",
            "description": "Главная героиня «Унесенных призраками» — десятилетняя девочка, которая случайно попадает в мир духов и божеств. Первоначально напуганная и беспомощная, Тихиро постепенно набирается смелости, показывая истинную силу духа.",
            "link": "https://shikimori.one/characters/384-chihiro-ogino",
        },
        {
            "name": "Каонаси",
            "image": "pictures/char4.jpg",
            "description": "Божество, не имеющее своего лица и бродящее в поисках нового. Безликий обладает способностью поглощать черты и эмоции других.",
            "link": "https://shikimori.one/characters/8298-kaonashi",
        },
        {
            "name": "Сан",
            "image": "https://m.media-amazon.com/images/M/MV5BMjIzNjEyNTAzOF5BMl5BanBnXkFtZTgwNDI1MDMzNTE@._V1_.jpg",
            "description": "Воспитанная богиней-волчицей, она борется за защиту леса и его обитателей от посягательств человека. Сан воплощает центральные темы фильма «Принцесса Мононоке» — защиту окружающей среды и тонкий баланс между природой и цивилизацией.",
            "link": "https://shikimori.one/characters/2727-san",
        },
    ]
    
def get_products():
    prod = [
        {"id": 1, "title": "Копилка", "vendor_code": "111", "description": "Двигающаяся копилка в форме Безликого (Каонаси) из фильма «Унесенные призраками»", "price": 200, "img": "https://blog.fromjapan.co.jp/en/wp-content/uploads/2020/03/StudioGhibli_Kaonashi.png"},
        {"id": 2, "title": "Фигурка", "vendor_code": "222", "description": "Полноценная фигурка Навсикая и планер из фильма «Навсикая из Долины Ветров»", "price": 250, "img": "https://blog.fromjapan.co.jp/en/wp-content/uploads/2020/03/Ghibli_Nausicaa.png"},
        {"id": 3, "title": "Кухонные принадлежности", "vendor_code": "333", "description": "Сковорода и лопатка с Кальцифером из фильма «Ходячий замок»", "price": 450, "img": "https://blog.fromjapan.co.jp/en/wp-content/uploads/2020/03/Ghibli_FryingPanSpatula.png"},
        {"id": 4, "title": "Плюшевая игрушка", "vendor_code": "444e", "description": "Кот ведьмы Кики - кот Джи-джи плюшевый 10-15см", "price": 300, "img": "https://enez76gwp29.exactdn.com/wp-content/uploads/2020/04/productimage303754925_2nd.jpg?strip=all&lossy=1&ssl=1"},
        {"id": 5, "title": "Носки", "vendor_code": "4445e", "description": "Комплект носков Studio Ghibli 4 пары", "price": 400, "img": "https://enez76gwp29.exactdn.com/wp-content/uploads/2020/04/PEONFLYNewStripedcartoonfairytaleAnimationTotorosoxAutumnSummerSouthKoreanwomensFashion_2nd.jpg?strip=all&lossy=1&ssl=1"},
        {"id": 6, "title": "Повязка", "vendor_code": "4446e", "description": "Махровая повязка на голову из фильма «Ведьмина служба доставки»", "price": 200, "img": "https://blog.fromjapan.co.jp/en/wp-content/uploads/2020/03/Ghibli_HairBand.png"},
        {"id": 7, "title": "Толстовка", "vendor_code": "4447e", "description": "Толстовка унисекс с подборкой персонажей Studio Ghibli", "price": 700, "img": "https://enez76gwp29.exactdn.com/wp-content/uploads/2020/11/redirect11272020131124-1.jpg?strip=all&lossy=1&ssl=1"},
        {"id": 8, "title": "Декор для сада", "vendor_code": "4448e", "description": "Статуэтки для сада с главной героиней фильма «Рыбка Поньо на утесе»", "price": 400, "img": "https://enez76gwp29.exactdn.com/wp-content/uploads/2019/09/HTB1TVhCSpXXXXc2aFXXq6xXFXXXP-removebg-preview.png?strip=all&lossy=1&ssl=1"},
        {"id": 9, "title": "Брелок", "vendor_code": "4449e", "description": "Брелок духов дерева из фильма «Принцесса Мононоке»", "price": 165, "img": "https://enez76gwp29.exactdn.com/wp-content/uploads/2017/05/HTB11KrJOhjaK1RjSZFAq6zdLFXaF.png?strip=all&lossy=1&ssl=1"},
        {"id": 10, "title": "Фигурка", "vendor_code": "44410e", "description": "Фигурка духов дерева из фильма «Принцесса Мононоке»", "price": 235, "img": "https://enez76gwp29.exactdn.com/wp-content/uploads/2020/11/HTB1u6ZocQGj11JjSZFMq6xnRVXaK.jpg?strip=all&lossy=1&ssl=1"},
        {"id": 11, "title": "Сумка", "vendor_code": "44411e", "description": "Миниатюрная сумка через плечо с Безликим из фильма «Унесенные призраками»", "price": 300, "img": "https://enez76gwp29.exactdn.com/wp-content/uploads/2020/05/H77049cf4c568481a8149a07b858568d2W-removebg-preview.png?strip=all&lossy=1&ssl=1"},
        {"id": 12, "title": "Солонка", "vendor_code": "44412e", "description": "Солонка с перцем «Мой сосед Тоторо»", "price": 300, "img": "https://blog.fromjapan.co.jp/en/wp-content/uploads/2020/03/StudioGhibli_Totoro.png"},
    ]
    return prod
    
def get_edu():
    # Личная информация
    my_info = {
        "full_name": "Медведская Мария Олеговна",
        "image": "pictures/my_photo.jpg",
        "email": "momedvedskaya@edu.hse.ru",
        "phone": "+7 996 64 4220"
    }

    # Информация о программе
    program_info = {
        "name": "Маркетинг и рыночная аналитика",
        "description": "Особое место в программе занимает формирование у студентов навыков практической аналитической работы в области разработки и принятия маркетинговых решений. Практическая ориентация программы достигается за счет:",
        "list": ["участия в реализации программы представителей компаний-лидеров сектора маркетинговых исследований;",
                 "привлечения маркетологов-практиков из ведущих компаний для чтения лекций;",
                 "применения кейс-метода с разбором конкретных ситуаций из опыта фирм;",
                 "подготовки студентами курсовых работ в форме маркетингового исследования."],
        "supervisor": {
            "full_name": "Горчаков Климент Александрович",
            "image": "https://www.hse.ru/pubs/share/thumb/867206034:c2310x2310+0+217:r380x380!.jpg",
            "email": "kagorchakov@hse.ru"
        },
        "manager": {
            "full_name": "Коваленко Анастасия Владимировна",
            "image": "https://www.hse.ru/pubs/share/thumb/894140700:c720x720+0+0:r380x380!",
            "email": "a.kovalenko@hse.ru"
        }
    }

    # Сокурсники
    classmates = [
        {"full_name": "Иванов Иван Иванович", 
        "image": "https://m.media-amazon.com/images/M/MV5BMTk4MzMwNjA5Ml5BMl5BanBnXkFtZTgwNTgyNTEzMzE@._V1_.jpg", 
        "email": "ivan@mail.ru", 
        "phone": "+7 012 345 6789"},
        {"full_name": "Александрова Александра Александровна", 
        "image": "https://m.media-amazon.com/images/M/MV5BMTQzNTE4MzA5NF5BMl5BanBnXkFtZTgwMzU5NDYyMzE@._V1_QL75_UY281_CR11,0,500,281_.jpg", 
        "email": "alex@mail.ru", 
        "phone": "+7 987 654 3210"}
    ]

    edu = {
        "my_info": my_info,
        "program_info": program_info,
        "classmates": classmates,
    }
    return edu

