from anilist_api import search_anime, search_manga, get_user, search_character

anime_results = search_anime("One Piece")
manga_results = search_manga("Berserk")
user_info = get_user("anbuinfosec")
characters = search_character("Naruto")

print(anime_results)
print(manga_results)
print(user_info)
print(characters)