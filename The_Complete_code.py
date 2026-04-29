"""
Movie Recommendation System 
Algorithms and Data Structures -- Final Project
Authors : Mahmudul Hasan Niloy
        Myeirim Khairat
        Sayed Rahmat
Implements: Hash Tables, FIFO Queue, Graph + BFS
"""
 
from collections import deque
 
 
# ============================================================
# DATASET -- Hash Table 1: Movie Registry
# ============================================================
 
movie_registry = {
    1:  {"id": 1,  "title": "The Matrix",
         "genres": ["Sci-Fi", "Action"],
         "sum_rating": 480, "count": 100},
    2:  {"id": 2,  "title": "Inception",
         "genres": ["Sci-Fi", "Action", "Thriller"],
         "sum_rating": 450, "count": 95},
    3:  {"id": 3,  "title": "Interstellar",
         "genres": ["Sci-Fi", "Drama"],
         "sum_rating": 470, "count": 100},
    4:  {"id": 4,  "title": "The Godfather",
         "genres": ["Crime", "Drama"],
         "sum_rating": 490, "count": 100},
    5:  {"id": 5,  "title": "Pulp Fiction",
         "genres": ["Crime", "Thriller"],
         "sum_rating": 430, "count": 90},
    6:  {"id": 6,  "title": "The Dark Knight",
         "genres": ["Action", "Crime", "Drama"],
         "sum_rating": 485, "count": 100},
    7:  {"id": 7,  "title": "Schindler's List",
         "genres": ["Drama", "History"],
         "sum_rating": 460, "count": 95},
    8:  {"id": 8,  "title": "Forrest Gump",
         "genres": ["Drama", "Romance"],
         "sum_rating": 440, "count": 100},
    9:  {"id": 9,  "title": "The Shawshank Redemption",
         "genres": ["Drama"],
         "sum_rating": 495, "count": 100},
    10: {"id": 10, "title": "Gladiator",
         "genres": ["Action", "Adventure", "Drama"],
         "sum_rating": 420, "count": 90},
    11: {"id": 11, "title": "Alien",
         "genres": ["Sci-Fi", "Horror"],
         "sum_rating": 380, "count": 85},
    12: {"id": 12, "title": "The Silence of the Lambs",
         "genres": ["Crime", "Horror", "Thriller"],
         "sum_rating": 410, "count": 90},
    13: {"id": 13, "title": "Seven",
         "genres": ["Crime", "Mystery", "Thriller"],
         "sum_rating": 390, "count": 85},
    14: {"id": 14, "title": "The Prestige",
         "genres": ["Drama", "Mystery", "Sci-Fi"],
         "sum_rating": 445, "count": 95},
    15: {"id": 15, "title": "Memento",
         "genres": ["Mystery", "Thriller"],
         "sum_rating": 405, "count": 90},
    16: {"id": 16, "title": "The Lion King",
         "genres": ["Animation", "Adventure", "Drama"],
         "sum_rating": 475, "count": 100},
    17: {"id": 17, "title": "Spirited Away",
         "genres": ["Animation", "Adventure", "Fantasy"],
         "sum_rating": 480, "count": 100},
    18: {"id": 18, "title": "Back to the Future",
         "genres": ["Sci-Fi", "Adventure", "Comedy"],
         "sum_rating": 455, "count": 100},
    19: {"id": 19, "title": "Blade Runner 2049",
         "genres": ["Sci-Fi", "Drama"],
         "sum_rating": 340, "count": 80},
    20: {"id": 20, "title": "Parasite",
         "genres": ["Drama", "Thriller", "Comedy"],
         "sum_rating": 465, "count": 100},
}
 
 
# ============================================================
# Hash Table 2: User Ratings
# ============================================================
 
user_ratings = {}
 
 
# ============================================================
# Queue: Viewing History (FIFO, max capacity = 5)
# ============================================================
 
viewing_history = deque(maxlen=5)
 
 
# ============================================================
# GRAPH: Building Adjacency List from shared genres -- O(n^2)
# ============================================================
 
def build_graph(registry):
    
    graph = {movie_id: [] for movie_id in registry}
    ids = list(registry.keys())
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            id1, id2 = ids[i], ids[j]
            shared = set(registry[id1]["genres"]) & set(registry[id2]["genres"])
            if shared:
                graph[id1].append(id2)
                graph[id2].append(id1)
    return graph
 
 
graph = build_graph(movie_registry)
 
 
# ============================================================
# FEATURE 1 -- Listing All Movies -- O(n)
# ============================================================
 
def list_all_movies(registry):
    
    print("\n" + "=" * 65)
    print(f"  {'ALL MOVIES':^61}")
    print("=" * 65)
    print(f"  {'ID':<5} {'Title':<35} {'Avg Rating':<10} {'Genres'}")
    print("-" * 65)
    for movie_id, movie in registry.items():
        avg = movie["sum_rating"] / movie["count"]
        genres = ", ".join(movie["genres"])
        print(f"  {movie_id:<5} {movie['title']:<35} {avg:<10.2f} {genres}")
    print("=" * 65)
 
 
# ============================================================
# FEATURE 2 -- Top 5 Movies by Rating -- O(n log n)
# ============================================================
 
def get_top_movies(registry, n=5):
    
    sorted_movies = sorted(
        registry.values(),
        key=lambda m: m["sum_rating"] / m["count"],
        reverse=True
    )[:n]
    print("\n" + "=" * 55)
    print(f"  {'TOP ' + str(n) + ' MOVIES BY RATING':^51}")
    print("=" * 55)
    print(f"  {'Rank':<6} {'Title':<35} {'Avg Rating'}")
    print("-" * 55)
    for rank, movie in enumerate(sorted_movies, 1):
        avg = movie["sum_rating"] / movie["count"]
        print(f"  #{rank:<5} {movie['title']:<35} {avg:.2f} / 5.00")
    print("=" * 55)
    return sorted_movies
 
 
# ============================================================
# FEATURE 3 -- Watching a Movie (adding to Queue) -- O(1)
# ============================================================
 
def watch_movie(movie_id, registry, history):
 
    if movie_id not in registry:
        print(f"  [ERROR] Movie ID {movie_id} not found.")
        return
    title = registry[movie_id]["title"]
    if len(history) == history.maxlen:
        evicted_id = history[0]
        evicted_title = registry[evicted_id]["title"]
        history.append(movie_id)
        print(f"\n  [WATCHED]  '{title}'")
        print(f"  [REMOVED]  '{evicted_title}' removed (queue full)")
    else:
        history.append(movie_id)
        print(f"\n  [WATCHED]  '{title}' added to viewing history")
 
 
# ============================================================
# FEATURE 4 -- Rating a Movie -- O(1)
# ============================================================
 
def rate_movie(movie_id, score, registry, user_ratings_table):
    
    if movie_id not in registry:
        print(f"  [ERROR] Movie ID {movie_id} not found.")
        return
    movie = registry[movie_id]
    if movie_id in user_ratings_table:
        old_score = user_ratings_table[movie_id]
        movie["sum_rating"] = movie["sum_rating"] - old_score + score
        user_ratings_table[movie_id] = score
        print(f"\n  [UPDATED]  '{movie['title']}' rating: {old_score} -> {score}")
        print(f"  [CALC]     New average: {movie['sum_rating'] / movie['count']:.2f}")
    else:
        movie["sum_rating"] += score
        movie["count"] += 1
        user_ratings_table[movie_id] = score
        print(f"\n  [RATED]    '{movie['title']}' rated: {score}")
        print(f"  [CALC]     New average: {movie['sum_rating'] / movie['count']:.2f}")
 
 
# ============================================================
# FEATURE 5 -- Viewing History -- O(1)
# ============================================================
 
def view_history(history, registry):
    
    print("\n" + "=" * 55)
    print(f"  {'VIEWING HISTORY (Last 5)':^51}")
    print("=" * 55)
    if not history:
        print("  No movies watched yet.")
    else:
        for i, movie_id in enumerate(reversed(history), 1):
            title = registry[movie_id]["title"]
            print(f"  {i}. {title}")
    print(f"\n  Queue size: {len(history)} / {history.maxlen}")
    print("=" * 55)
 
 
# ============================================================
# FEATURE 6 -- Recommendations via BFS -- O(V + E)
# ============================================================
 
def get_recommendations(history, graph, registry, user_rt):
    
    if not history:
        print("  [INFO] Watch some movies first!")
        return []
    visited = set(history)
    queue   = deque(history)
    recs    = []
    while queue:
        current = queue.popleft()
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                recs.append(neighbor)
    recs_sorted = sorted(
        recs,
        key=lambda x: registry[x]["sum_rating"] / registry[x]["count"],
        reverse=True
    )
    print("\n" + "=" * 65)
    print(f"  {'PERSONALIZED RECOMMENDATIONS (BFS)':^61}")
    print("=" * 65)
    print(f"  Based on your watch history:")
    for movie_id in history:
        print(f"    -> {registry[movie_id]['title']}")
    print()
    print(f"  {'Rank':<6} {'Title':<35} {'Avg Rating':<12} {'Genres'}")
    print("-" * 65)
    for rank, movie_id in enumerate(recs_sorted[:8], 1):
        movie = registry[movie_id]
        avg   = movie["sum_rating"] / movie["count"]
        genres = ", ".join(movie["genres"])
        print(f"  #{rank:<5} {movie['title']:<35} {avg:<12.2f} {genres}")
    print("=" * 65)
    return recs_sorted
 
 
# ============================================================
# BONUS -- Printing Graph Connections
# ============================================================
 
def print_graph_sample(graph, registry, sample_ids):
    
    print("\n" + "=" * 65)
    print(f"  {'GRAPH CONNECTIONS (Sample)':^61}")
    print("=" * 65)
    for movie_id in sample_ids:
        title = registry[movie_id]["title"]
        neighbors = graph[movie_id]
        print(f"\n  [{title}]")
        for n in neighbors:
            print(f"    +-- {registry[n]['title']}")
    print("=" * 65)
 
 
# ============================================================
# RUNNING ALL FEATURES
# ============================================================
 
print("\n>>> FEATURE 1: LIST ALL MOVIES")
list_all_movies(movie_registry)
 
print("\n>>> FEATURE 2: TOP 5 MOVIES")
get_top_movies(movie_registry, n=5)
 
print("\n>>> FEATURE 3: SIMULATE WATCHING MOVIES")
watch_movie(1,  movie_registry, viewing_history)
watch_movie(6,  movie_registry, viewing_history)
watch_movie(3,  movie_registry, viewing_history)
watch_movie(4,  movie_registry, viewing_history)
watch_movie(17, movie_registry, viewing_history)
watch_movie(9,  movie_registry, viewing_history)
 
print("\n>>> FEATURE 4: RATE MOVIES")
rate_movie(1,  9,  movie_registry, user_ratings)
rate_movie(6,  10, movie_registry, user_ratings)
rate_movie(17, 8,  movie_registry, user_ratings)
rate_movie(1,  10, movie_registry, user_ratings)
 
print("\n>>> FEATURE 5: VIEW HISTORY")
view_history(viewing_history, movie_registry)
 
print("\n>>> FEATURE 6: RECOMMENDATIONS (BFS)")
get_recommendations(viewing_history, graph, movie_registry, user_ratings)
 
print("\n>>> BONUS: GRAPH CONNECTIONS")
print_graph_sample(graph, movie_registry,[1, 4, 17])
