from django.shortcuts import render
import sqlite3

#[(actor, movies_with(actor)) for actor in actors_in('A Beautiful Mind (2001)')]

def index(request):
    return render(request, 'first_app/index.html')

# def expanded(dictionary):
#     # new_dictionary = {}
#     # for key in dictionary:
#     #     for actor in dictionary[key]:
#     #         new_dictionary[actor] = movies_with(actor)
#     pass



# def movie_layer_from(actor_list):
#     new_item = {}
#     for actor in actor_list:
#         new_item[actor] = movies_with(actor)
#     return new_item

# def actor_layer_from(movie_list):
#     new_item = {}
#     for movie in movie_list:
#         new_item[movie] = actors_in(movie)
#     return new_item



# def test(request):
#     conn = sqlite3.connect('../../linkme.db')
#     c = conn.cursor()
#     first_actor = request.POST['first_actor']
#     print(first_actor)
#     a = c.execute('SELECT * FROM linkme WHERE ACTOR = ?', (first_actor,))
#     movies = a.fetchall()
#     return render(request, 'first_app/index.html', {'movies': [i[1] for i in movies]})


def movies_with(actor):
    conn = sqlite3.connect('../../linkme.db')
    c = conn.cursor()
    a = c.execute('SELECT * FROM linkme WHERE ACTOR = ?', (actor,))
    movies = a.fetchall()
    return [movie[1] for movie in movies]

def actors_in(movie):
    conn = sqlite3.connect('../../linkme.db')
    c = conn.cursor()
    a = c.execute("SELECT * FROM linkme WHERE MOVIE = ?" , (movie,))
    actors =  a.fetchall()
    return [actor[0] for actor in actors]



# def link(request):
#     (first_link, second_link, third_link, fourth_link, fifth_llnk, sixth_link) = ({}, {}, {}, {}, {}, {})
#     d = {}
#     e = {}
#     i = 6
#     while i > 0:
#
#         print(request)
#         if request.method == 'POST':
#             conn = sqlite3.connect('../../linkme.db')
#             first_actor = request.POST['first_actor']
#             second_actor = request.POST['second_actor']
#             print(first_actor)
#             print(second_actor)
#
#             for movie in movies_with(first_actor):
#                 first_link[movie] = actors_in(movie)
#                 if second_actor in actors_in(movie):
#                     return render(request, 'first_app/index.html', {'success': 'Success! %s and %s were in %s' % (first_actor, second_actor, each_movie), 'first_actor': first_actor, 'second_actor': second_actor, 'item': each_movie})
#             for movie in movies_with(second_actor):
#                 first_link[movie] = actors_in(movie)
#                 if first_actor in first_link[movie]:
#
#                     return render(request, 'first_app/index.html', {'success': 'Success! %s and %s were in %s' % (first_actor, second_actor, each_movie), 'first_actor': first_actor, 'second_actor': second_actor, 'item': each_movie})
#             i -= 1
#             if i == 5:
#                 for key in first_link:
#                     movie_list = first_link[key]
#                     for movie_ in movie_list:
#                         second_link[movie_] = actors_in(movie_)
#                     second_link
#             if i == 4:
#                 for key in second_link:
#                     actor_list = second_link[key]
#                     for actor_ in actor_list:
#                         third_link[actor_] = movies_with(actor_)
#             the_new_list1 = [{movie: actors_in(movie)} for movie in movies_with(actor) for actor in actors_in(movie_b) for movie_b in movies_with(actor_b) for actor_b in actors_in(first_actor)]
#             the_new_list2 = [{actor: movies_with(actor)} for actor in actors_in_(movie) for movie in movies_with(actor_b) for actor_b in actors_in(movie_b) for movie_b in movies_with(second_actor)]
#
#         return render(request, 'first_app/index.html',{'error': 'An error has occurred'})

# def link_beta(request):
#     (first_link, second_link, third_link, fourth_link, fifth_llnk, sixth_link) = ({}, {}, {}, {}, {}, {})
#     if request.POST['isActor']:
#         first_actor = request.POST['first_actor']
#         second_actor = request.POST['second_actor']
#         actors_in_movies_with_first_actor = layer_from(movies_with(first_actor)).values()
#         actors_in_movies_with_second_actor = layer_from(movies_with(second_actor)).values()
#         for actor_list in actors_in_movies_with_first_actor:
#             if second_actor in actor_list:
#                 print('Success')
#         for actor_list in actors_in_movies_with_second_actor:
#             if first_actor in actor_list:
#                 print('Success')

def link_actors(request):
    actor1 = request.POST['actor1']
    actor2 = request.POST['actor2']
    for movie in movies_with(actor1):
       for actor in actors_in(movie):
          if actor == actor2:
             return render(request, 'first_app/index.html', {"context": "%s was in %s with %s" % (actor1, movie, actor2)})

    for movie in movies_with(actor2):
       for actor in actors_in(movie):
          if actor == actor1:
             return render(request, 'first_app/index.html', {"context": "%s was in %s with %s" % (actor1, movie, actor2)})
          for movie_b in movies_with(actor):
             for actor_b in actors_in(movie_b):
                if actor_b == actor1 and actor_b != actor:
                    return render(request, 'first_app/index.html', {"context": "%s was in %s with %s, who was in %s with %s" % (actor1, movie_b, actor, movie, actor2)})
                for movie_c in movies_with(actor_b):
                   for actor_c in actors_in(movie_c):
                      if actor_c == actor1 and actor_c not in [actor_b, actor]:
                          return render(request, 'first_app/index.html', {"context": "%s was in %s with %s, who was in %s with %s, who was in %s with %s" % (actor1, movie_c, actor_b,movie_b, actor, movie, actor2)})
                      for movie_d in movies_with(actor_c):
                         for actor_d in actors_in(movie_d):
                            if actor_d == actor1 and actor_d not in [actor_c, actor_b, actor]:
                                 return render(request, 'first_app/index.html', {"context": "%s was in %s with %s, who was in %s with %s, who was in %s with %s, who was in %s with %s" % (actor1,movie_d, actor_c, movie_c, actor_b,movie_b, actor, movie, actor2)})
                         for movie_e in movies_with(actor_d):
                             for actor_e in actors_in(movie_e):
                                 if actor_e == actor1 and actor_d not in [actor_d, actor_c, actor_b, actor]:
                                      return render(request, 'first_app/index.html', {"context": "%s was in %s with %s, who was in %s with %s, who was in %s with %s, who was in %s with %s, who was in %s with %s" % (actor1,movie_e, actor_d, movie_d, actor_c, movie_c, actor_b,movie_b, actor, movie, actor2)})
                                 for movie_f in movies_with(actor_e):
                                     for actor_f in actors_in(movie_f):
                                         if actor_f == actor1 and actor_f not in [actor_e, actor_d, actor_c, actor_b, actor]:
                                              return render(request, 'first_app/index.html', {"context": "%s was in %s with %s, who was in %s with %s, who was in %s with %s, who was in %s with %s, who was in %s with %s, who was in %s with %s" % (actor1, movie_f, actor_e, movie_e, actor_d, movie_d, actor_c, movie_c, actor_b,movie_b, actor, movie, actor2)})

    return "No match found"

# def link_movies(movie1, movie2):
#
#      for actor in actors_in(movie2):
#         for movie in movies_with(actor):
#           if movie == movie1:
#             return "%s featured %s, who was in %s" % (movie1, actor, movie2)
#      for actor in actors_in(movie1):
#         for movie in movies_with(actor):
#           if movie == movie2:
#             return "%s featured %s, who was in %s" % (movie2, actor, movie1)
#      for actor in actors_in(movie2):
#         for movie in movies_with(actor):
#             for actor_b in actors_in(movie):
#                 for movie_b in movies_with(actor_b):
#                     if movie_b == movie1:
#                         return "%s featured %s, who was in %s, which featured %s, who was in %s" % (movie1, actor_b, movie_b, actor, movie2)
#      for actor in actors_in(movie1):
#         for movie in movies_with(actor):
#             for actor_b in actors_in(movie):
#                 for movie_b in movies_with(actor_b):
#                     if movie_b == movie2:
#                         return "%s featured %s, who was in %s, which featured %s, who was in %s" % (movie2, actor_b, movie_b, actor, movie1)
