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
    sum_rating  = sum(m['rating'] for m in movies)
    rating = sum_rating / len(movies)
    return round(rating, 1)

# print(average_rating(movies))

def catalog_age_stats(movies, current_year = 2026):
  age_list = []
  for movie in movies:
    age = current_year - movie['year']
    age_list.append(age)
  mean_age = sum(age_list) / len(age_list)
  return min(age_list), math.ceil(mean_age), max(age_list)

# print(catalog_age_stats(movies))

def duration_in_hours(minutes):
   hours = minutes // 60
   minute = minutes % 60
   return f'{hours}ч {minute}м'

# for m in movies:
#    print(duration_in_hours(m['duration_min']))

# приступаем ко второму этапу

def rating_tier(rating):
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
    match year:
        case y if y > 2020:
          return 'новые'
        case y if y >= 2015 and y <= 2020:
          return 'недавние'
        case _:
          return 'старые'

#for m in movies:
#   print(decade_label(m['year']))