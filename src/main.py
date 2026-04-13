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

    user_prefs = {
        "favorite_genre":      "indie pop",
        "favorite_mood":       "happy",
        "target_energy":       0.75,
        "target_valence":      0.80,
        "target_danceability": 0.78,
        "target_acousticness": 0.30
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {', '.join(explanation)}")
        print()


if __name__ == "__main__":
    main()
