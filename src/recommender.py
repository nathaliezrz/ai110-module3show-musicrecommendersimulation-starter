from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

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
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read a CSV file of songs and return a list of dicts with typed values."""
    import csv

    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    float(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a (score, reasons) tuple measuring how well a song matches user preferences."""
    score = 0.0
    reasons = []

    # Categorical features
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Numeric features — raw closeness, each contributes 0.0 to 1.0
    energy_score = 1 - abs(song["energy"] - user_prefs["target_energy"])
    score += energy_score
    reasons.append(f"energy closeness (+{energy_score:.2f})")

    valence_score = 1 - abs(song["valence"] - user_prefs["target_valence"])
    score += valence_score
    reasons.append(f"valence closeness (+{valence_score:.2f})")

    danceability_score = 1 - abs(song["danceability"] - user_prefs["target_danceability"])
    score += danceability_score
    reasons.append(f"danceability closeness (+{danceability_score:.2f})")

    acousticness_score = 1 - abs(song["acousticness"] - user_prefs["target_acousticness"])
    score += acousticness_score
    reasons.append(f"acousticness closeness (+{acousticness_score:.2f})")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, List[str]]]:
    """Score all songs against user preferences and return the top k ranked highest first."""
    scored = [(song, *score_song(user_prefs, song)) for song in songs]
    ranked = sorted(scored, key=lambda x: x[1], reverse=True)
    return ranked[:k]
