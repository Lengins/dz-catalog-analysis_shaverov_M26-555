import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]}, # noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# выполняем первый этап

def average_rating(movies):
    '''функция для подсчёта средней
    пользовательской оценки фильмов'''
    sum_rating  = sum(m['rating'] for m in movies)
    rating = sum_rating / len(movies)
    return round(rating, 1)

# print(average_rating(movies))

def catalog_age_stats(movies, current_year = 2026):
  '''функция, возвращающая кортеж
  из 3 значений - минимальный, средний 
  и максимальный возраст фильма'''
  age_list = []
  for movie in movies:
    age = current_year - movie['year']
    age_list.append(age)
  mean_age = sum(age_list) / len(age_list)
  return min(age_list), math.ceil(mean_age), max(age_list)

# print(catalog_age_stats(movies))

def duration_in_hours(minutes):
   '''функция перевода длительности фильма
   из минут в формат "1ч 20м"   '''
   hours = minutes // 60
   minute = minutes % 60
   return f'{hours}ч {minute}м'

# for m in movies:
#    print(duration_in_hours(m['duration_min']))

# приступаем ко второму этапу

def rating_tier(rating):
    '''категоризируем фильмы по 
        пользовательской оценке'''
    if rating >= 9:
        return 'шедевр' if rating <= 10 else 'некорректный рейтинг'
    elif rating >= 7 and rating <= 8.9:
        return 'хорошо'
    elif rating >= 5 and rating <= 6.9:
       return 'средне'
    else:
       return 'слабо'

# for m in movies:
#   print(rating_tier(m['rating']))

def decade_label(year):
    '''категоризируем фильмы по 
    году выпуска'''
    match year:
        case y if y > 2020:
          return 'новые'
        case y if y >= 2015 and y <= 2020:
          return 'недавние'
        case _:
          return 'старые'

#for m in movies:
#   print(decade_label(m['year']))

# приступаем к третьему этапу

for movie in movies:
    '''выводим все названия фильмов
    не комедий'''
    if 'comedy' in movie['genres']:
       continue
    print(f'Not a comedy movie: {movie['title']}')

i = 0
while i < len(movies):
    '''функция выводит название первого
    фильма с рейтингом больше 9'''
    if movies[i]['rating'] > 9:
        print(f'Первый шедевр: {movies[i]['title']}')
        break
    i += 1
else:
    print('Шедевров не найдено')

def count_long_movies(movies, threshold=120):
    '''считаем и выводим количество 
    длительных фильмов, длительные = дольше 
    порога (threshold)'''
    i = 0
    for movie in movies:
        if movie['duration_min'] > 120:
            i += 1
    return f'Длинных фильмов: {i}'

#print(count_long_movies(movies))

# приступаем к 4 этапу

def normalize_title(title):
    """функция, делающая первую букву
    каждого слова в названии фильма
    заглавной"""
    words = title.split()
    return " ".join(word[0].upper() + word[1:] for word in words)

#for m in movies:
#   print(normalize_title(m['title']))
       
def make_slug(title):
   """заменяем пробелы дефисами
   приводим к нижнему индексу"""
   return title.lower().replace(" ", "-")

#for m in movies:
#   print(make_slug(m['title']))

def format_report_line(movie):
   """функция формирует отчёт о каждом фильме
   в определённом формате"""
   genre = ", ".join(sorted(movie['genres']))
   return (
    f'"{normalize_title(movie['title'])}" ({movie['year']})'
    f' - {movie['rating']}/10, {duration_in_hours(movie['duration_min'])},'
    f' жанры: {genre}' # разбили по строкам для проверки ruff, обошлись без E501
)
# "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi (ТЗ)
# "The Quiet Algorithm" (2024) - 9.2/10, 1ч 58м, жанры: drama, sci-fi (Вывод функции)

#for m in movies:
#   print(format_report_line(m))

# приступаем к 5 этапу работы

def titles_sorted_by_rating(movies):
   """функция возвращает список названий
   фильмов, отсортированных по
   убыванию рейтинга"""
   sorted_movies = sorted(movies, key = lambda m: m['rating'], reverse=True)
   return [m['title'] for m in sorted_movies]

#print(titles_sorted_by_rating(movies))

def top_n_by_rating(movies, n=3):
    '''функция формирует топ 3 фильма 
    по рейтингу и выводит название с рейтингом
    для каждого фильма'''
    top_n = sorted(movies, key = lambda m: m['rating'], reverse=True)[:n]
    return [(m['title'] , m['rating']) for m in top_n]

print(top_n_by_rating(movies))

# этап 6 - пишем функции со словарями

def count_by_genre(movies):
    '''функция считает количество фильмов
    для кажджого жанра'''
    result = {}
    for movie in movies:
        for genre in movie['genres']:
            result[genre] = result.get(genre, 0) + 1
    return result

#print(count_by_genre(movies))

def actor_filmography(movies):
    '''возвращает словарь актёров и
    списков фильмов с их участием'''
    result = {}
    for movie in movies:
        for actor in movie['actors']:
            if actor not in result:
                result[actor] = []
            result[actor].append(movie['title'])
    return result

#print(actor_filmography(movies))

top_movies = {m['title']: m['rating']
              for m in movies
              if m['rating'] > average_rating(movies)}

#print(top_movies)

# приступаем к 7 этапу - множествам

def all_genres(movies):
    '''функция, возвращающая
    все уникальные жанры фильмов'''
    result = set()
    for movie in movies:
        result.update(movie['genres'])
    return result

# print(all_genres(movies))

def common_actors(movie1, movie2):
    '''функция принимает два
    фильма и возвращает актёров
    игравших в обоих фильмах'''
    return set(movie1['actors']) & set(movie2['actors'])

def genres_only_in_one(movies_a, movies_b):
    '''функция принимает два
        фильма и возвращает жанры
        которые есть в первом фильме
        и отсутствуют во втором'''
    genres_a = {g for m in movies_a for g in m['genres']}
    genres_b = {g for m in movies_b for g in m['genres']}
    return genres_a - genres_b

def iter_high_rated(movies, min_rating=8.0):
    '''функция выводит фильмы с рейтингом
    выше минимального заданного'''
    for movie in movies:
        if movie['rating'] >= min_rating:
            yield movie

for movie in iter_high_rated(movies):
    print(format_report_line(movie))
# "The Dune Chronicles" (2021) — 8.6/10, 2ч 35м, жанры: drama, sci-fi
# "Midnight In Oslo" (2020) — 8.9/10, 2ч 4м, жанры: mystery, thriller
# "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi

total_minutes = sum(m["duration_min"] for m in movies if m["rating"] > 7)
print(f'суммарная длительность фильмов с рейтингом выше 7: {total_minutes}')