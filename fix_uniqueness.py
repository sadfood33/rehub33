#!/usr/bin/env python3
import os
import re

mo_city_data = {
    'aleksandrov': {'name': 'Александров', 'pop': '55 тыс. человек', 'dist': '110 км от МКАД', 'feature': 'старинный город с богатой историей'},
    'balashiha': {'name': 'Балашиха', 'pop': '250 тыс. человек', 'dist': '15 км от МКАД', 'feature': 'крупнейший городской округ Подмосковья'},
    'chekhov': {'name': 'Чехов', 'pop': '75 тыс. человек', 'dist': '60 км от МКАД', 'feature': 'город назван в честь А.П. Чехова'},
    'dmitrov': {'name': 'Дмитров', 'pop': '65 тыс. человек', 'dist': '65 км от МКАД', 'feature': 'древний город с кремлём'},
    'dolgoprudnyy': {'name': 'Долгопрудный', 'pop': '120 тыс. человек', 'dist': '18 км от МКАД', 'feature': 'город науки и образования'},
    'domodedovo': {'name': 'Домодедово', 'pop': '140 тыс. человек', 'dist': '45 км от МКАД', 'feature': 'город с международным аэропортом'},
    'dubna': {'name': 'Дубна', 'pop': '75 тыс. человек', 'dist': '120 км от МКАД', 'feature': 'наукоград на Волге'},
    'egorevsk': {'name': 'Егорьевск', 'pop': '65 тыс. человек', 'dist': '95 км от МКАД', 'feature': 'купеческий город с музеями'},
    'elektrostal': {'name': 'Электросталь', 'pop': '155 тыс. человек', 'dist': '50 км от МКАД', 'feature': 'промышленный центр Подмосковья'},
    'elektrougli': {'name': 'Электроугли', 'pop': '22 тыс. человек', 'dist': '45 км от МКАД', 'feature': 'город энергетиков'},
    'fryazino': {'name': 'Фрязино', 'pop': '60 тыс. человек', 'dist': '25 км от МКАД', 'feature': 'наукоград с НИИ'},
    'istra': {'name': 'Истра', 'pop': '35 тыс. человек', 'dist': '55 км от МКАД', 'feature': 'город с Новоиерусалимским монастырём'},
    'ivanteevka': {'name': 'Ивантеевка', 'pop': '65 тыс. человек', 'dist': '35 км от МКАД', 'feature': 'город на реке Уча'},
    'kashira': {'name': 'Кашира', 'pop': '40 тыс. человек', 'dist': '110 км от МКАД', 'feature': 'город с ГРЭС'},
    'khimki': {'name': 'Химки', 'pop': '260 тыс. человек', 'dist': '5 км от МКАД', 'feature': 'спутник Москвы у Шереметьево'},
    'klin': {'name': 'Клин', 'pop': '75 тыс. человек', 'dist': '85 км от МКАД', 'feature': 'город ёлочных игрушек'},
    'kolomna': {'name': 'Коломна', 'pop': '140 тыс. человек', 'dist': '115 км от МКАД', 'feature': 'древний город с кремлём'},
    'korolev': {'name': 'Королёв', 'pop': '225 тыс. человек', 'dist': '25 км от МКАД', 'feature': 'наукоград, центр космонавтики'},
    'krasnogorsk': {'name': 'Красногорск', 'pop': '180 тыс. человек', 'dist': '10 км от МКАД', 'feature': 'город с экспоцентром'},
    'lobnya': {'name': 'Лобня', 'pop': '85 тыс. человек', 'dist': '25 км от МКАД', 'feature': 'город у канала им. Москвы'},
    'lukhovitsy': {'name': 'Луховицы', 'pop': '35 тыс. человек', 'dist': '130 км от МКАД', 'feature': 'город огурцов'},
    'lytkarino': {'name': 'Лыткарино', 'pop': '55 тыс. человек', 'dist': '30 км от МКАД', 'feature': 'город на холмах'},
    'lyubertsy': {'name': 'Люберцы', 'pop': '210 тыс. человек', 'dist': '12 км от МКАД', 'feature': 'крупный промышленный центр'},
    'mozhaysk': {'name': 'Можайск', 'pop': '30 тыс. человек', 'dist': '110 км от МКАД', 'feature': 'город воинской славы'},
    'mytishchi': {'name': 'Мытищи', 'pop': '230 тыс. человек', 'dist': '18 км от МКАД', 'feature': 'город с аквапарком'},
    'noginsk': {'name': 'Ногинск', 'pop': '100 тыс. человек', 'dist': '50 км от МКАД', 'feature': 'старинный Богородск'},
    'odintsovo': {'name': 'Одинцово', 'pop': '140 тыс. человек', 'dist': '20 км от МКАД', 'feature': 'престижный район Подмосковья'},
    'orekhovo-zuyevo': {'name': 'Орехово-Зуево', 'pop': '115 тыс. человек', 'dist': '90 км от МКАД', 'feature': 'родина футбола в России'},
    'ozery': {'name': 'Озёры', 'pop': '25 тыс. человек', 'dist': '140 км от МКАД', 'feature': 'город на Оке'},
    'pavlovskiy-posad': {'name': 'Павловский Посад', 'pop': '25 тыс. человек', 'dist': '70 км от МКАД', 'feature': 'родина платков'},
    'podolsk': {'name': 'Подольск', 'pop': '330 тыс. человек', 'dist': '40 км от МКАД', 'feature': 'крупнейший город Подмосковья'},
    'pushkino': {'name': 'Пушкино', 'pop': '110 тыс. человек', 'dist': '30 км от МКАД', 'feature': 'город дачников'},
    'ramenskoe': {'name': 'Раменское', 'pop': '120 тыс. человек', 'dist': '45 км от МКАД', 'feature': 'город с красивыми озёрами'},
    'reutov': {'name': 'Реутов', 'pop': '110 тыс. человек', 'dist': '12 км от МКАД', 'feature': 'наукоград у МКАД'},
    'sergiev-posad': {'name': 'Сергиев Посад', 'pop': '100 тыс. человек', 'dist': '70 км от МКАД', 'feature': 'духовная столица России'},
    'serpukhov': {'name': 'Серпухов', 'pop': '125 тыс. человек', 'dist': '100 км от МКАД', 'feature': 'город с древним кремлём'},
    'shchelkovo': {'name': 'Щёлково', 'pop': '130 тыс. человек', 'dist': '25 км от МКАД', 'feature': 'город на Клязьме'},
    'stupino': {'name': 'Ступино', 'pop': '65 тыс. человек', 'dist': '100 км от МКАД', 'feature': 'промышленный город'},
    'troitsk': {'name': 'Троицк', 'pop': '65 тыс. человек', 'dist': '35 км от МКАД', 'feature': 'наукоград в Новой Москве'},
    'vidnoe': {'name': 'Видное', 'pop': '60 тыс. человек', 'dist': '20 км от МКАД', 'feature': 'город садов'},
    'voskresensk': {'name': 'Воскресенск', 'pop': '85 тыс. человек', 'dist': '90 км от МКАД', 'feature': 'город химиков'},
    'zhukovskiy': {'name': 'Жуковский', 'pop': '110 тыс. человек', 'dist': '40 км от МКАД', 'feature': 'город авиации'},
    'zvenigorod': {'name': 'Звенигород', 'pop': '20 тыс. человек', 'dist': '60 км от МКАД', 'feature': 'город Саввино-Сторожевского монастыря'},
}

def get_city_slug(path):
    parts = path.split('/')
    for part in parts:
        if part.endswith('.html'):
            return part.replace('.html', '')
    return ''

def process_file(filepath, city_data):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    name = city_data['name']
    pop = city_data['pop']
    dist = city_data['dist']
    feature = city_data['feature']
    
    intro = f"Наркологическая клиника «ТыСпас» работает в городе {name} ({pop}), расположенном {dist}. Это {feature}, где наши специалисты оказывают профессиональную помощь людям с алкогольной и наркотической зависимостью."
    
    services_variants = [
        f"<h3>Наши услуги в {name}</h3><p>В клинике «ТыСпас» в {name} предлагаем: вывод из запоя, кодирование, реабилитацию, консультации нарколога.</p>",
        f"<h3>Помощь в {name}</h3><p>Наши врачи в {name} готовы помочь: экстренный вывод из запоя, все виды кодирования, лечение наркомании.</p>",
        f"<h3>Лечение в {name}</h3><p>Клиника в {name} обеспечивает: анонимное лечение, индивидуальный подбор методов, круглосуточный стационар.</p>",
    ]
    services = services_variants[hash(name) % len(services_variants)]
    
    pattern = r'(<h1>Лечение алкоголизма в [^<]+</h1>\s*<p class="subtitle">[^<]+</p>\s*</div>\s*</div>\s*</section>\s*<section class="content-section">\s*<div class="container">\s*<div class="text-content">)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        insert_pos = match.end()
        unique_block = f'<div class="city-intro" style="background:#e3f2fd;padding:20px;border-radius:8px;margin:20px 0;border-left:4px solid var(--primary);">{intro} {services}</div>'
        content = content[:insert_pos] + unique_block + content[insert_pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

print("Обработка городов МО...")
count = 0
for root, dirs, files in os.walk('goroda/moskva'):
    for f in files:
        if f.endswith('.html') and f != 'index.html':
            fp = os.path.join(root, f)
            slug = get_city_slug(fp)
            if slug in mo_city_data:
                if process_file(fp, mo_city_data[slug]):
                    count += 1
print(f"Обработано: {count}")
