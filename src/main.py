"""Evaluate the recommender with different user profiles."""

from .recommender import load_songs, recommend_songs

PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.85,
        "valence": 0.85
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.40,
        "valence": 0.60
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.95,
        "valence": 0.40
    },
    "Edge Case: Sad EDM": {
        "genre": "edm",
        "mood": "sad",
        "energy": 0.95,
        "valence": 0.10
    }
}


def main():
    """Print the top five songs for each test profile."""
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for name, user_prefs in PROFILES.items():
        print("\n" + "=" * 55)
        print(f"PROFILE: {name}")
        print(f"Preferences: {user_prefs}")
        print("=" * 55)

        recommendations = recommend_songs(
            user_prefs, songs, k=5
        )

        for rank, (song, score, explanation) in enumerate(
            recommendations, 1
        ):
            print(
                f"{rank}. {song['title']} by "
                f"{song['artist']} - {score:.2f}/10"
            )
            print(f"   Because: {explanation}")


if __name__ == "__main__":
    main()
