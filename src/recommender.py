import csv
from typing import List, Dict, Tuple
from dataclasses import asdict, dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Save the song catalog for this recommender."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs ranked by the shared scoring function."""
        preferences = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }
        song_by_id = {song.id: song for song in self.songs}
        ranked_results = recommend_songs(
            preferences,
            [asdict(song) for song in self.songs],
            k=k,
        )
        return [song_by_id[result["id"]] for result, _, _ in ranked_results]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain a song using the shared score and its component reasons."""
        preferences = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }
        _, reasons = score_song(preferences, asdict(song))
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs from a CSV file and convert their numeric fields."""
    songs = []
    with open(csv_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against the user's preferences and list the reasons."""
    score = 0.0
    reasons = []

    if song["genre"].lower() == user_prefs["genre"].lower():
        score += 4.0
        reasons.append("genre match (+4.00)")
    else:
        reasons.append("genre does not match (+0.00)")

    if song["mood"].lower() == user_prefs["mood"].lower():
        score += 3
        reasons.append("mood match (+3.00)")
    else:
        reasons.append("mood does not match (+0.00)")

    # These features are on a 0-to-1 scale, so closeness gives more points.
    energy_similarity = max(0.0, 1.0 - abs(song["energy"] - user_prefs["energy"]))
    energy_points = 2.0 * energy_similarity
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    preferred_valence = user_prefs.get("valence", 0.6)
    valence_similarity = max(0.0, 1.0 - abs(song["valence"] - preferred_valence))
    valence_points = valence_similarity
    score += valence_points
    reasons.append(f"valence similarity (+{valence_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return up to k songs with explanations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    # sorted() creates a new list, leaving the original songs list unchanged.
    ranked_songs = sorted(scored_songs, key=lambda result: result[1], reverse=True)
    return ranked_songs[:max(0, k)]
