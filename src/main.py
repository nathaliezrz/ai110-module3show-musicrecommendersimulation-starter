"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "Indie Pop Fan": {
            "favorite_genre":      "indie pop",
            "favorite_mood":       "happy",
            "target_energy":       0.75,
            "target_valence":      0.80,
            "target_danceability": 0.78,
            "target_acousticness": 0.30
        },
        "High-Energy Pop": {
            "favorite_genre":      "pop",
            "favorite_mood":       "happy",
            "target_energy":       0.90,
            "target_valence":      0.85,
            "target_danceability": 0.88,
            "target_acousticness": 0.05
        },
        "Chill Lofi": {
            "favorite_genre":      "lofi",
            "favorite_mood":       "chill",
            "target_energy":       0.38,
            "target_valence":      0.58,
            "target_danceability": 0.60,
            "target_acousticness": 0.78
        },
        "Deep Intense Rock": {
            "favorite_genre":      "rock",
            "favorite_mood":       "intense",
            "target_energy":       0.92,
            "target_valence":      0.45,
            "target_danceability": 0.65,
            "target_acousticness": 0.08
        },
        # --- Adversarial profiles ---
        "The Contradiction": {
            "favorite_genre":      "rock",
            "favorite_mood":       "chill",   # no rock song is chill
            "target_energy":       0.91,
            "target_valence":      0.48,
            "target_danceability": 0.66,
            "target_acousticness": 0.10
        },
        "The Perfect Numeric Trap": {
            "favorite_genre":      "classical",
            "favorite_mood":       "peaceful",
            "target_energy":       0.91,       # exactly matches Storm Runner (rock/intense)
            "target_valence":      0.48,
            "target_danceability": 0.66,
            "target_acousticness": 0.10
        },
        "The Unicorn": {
            "favorite_genre":      "synthwave", # only Night Drive Loop matches
            "favorite_mood":       "moody",
            "target_energy":       0.20,        # opposite of Night Drive Loop's actual values
            "target_valence":      0.20,
            "target_danceability": 0.20,
            "target_acousticness": 0.90
        },
    }

    for name, user_prefs in profiles.items():
        print(f"\n{'='*40}")
        print(f" Profile: {name}")
        print(f"{'='*40}\n")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {', '.join(explanation)}")
            print()


if __name__ == "__main__":
    main()
