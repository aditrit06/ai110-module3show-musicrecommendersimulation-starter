# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---


## How The System Works

My music recommendation system uses content-based filtering to suggest songs based on a user's music preferences. Real platforms like Spotify and YouTube use information such as listening history, likes, skips, and song characteristics to recommend content. My version is simpler and focuses on matching songs to a user's preferred genre, mood, energy, and valence.

### Song Features

Each Song object contains an ID, title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. I started with 10 songs and added 8 more from different genres and moods to make the dataset more diverse.

### User Profile

For my example user, I chose these preferences:

- Favorite genre: lofi
- Favorite mood: chill
- Target energy: 0.40
- Target valence: 0.60

I chose these preferences because I wanted the recommender to recognize the difference between relaxing music and more intense songs. Using both categorical and numerical features should help make the recommendations more specific.

### Algorithm Recipe

My system will compare each song with the user's preferences and give it a score out of 10 points.

- **Genre match:** 4 points if the genre matches the user's favorite genre.
- **Mood match:** 3 points if the mood matches the user's preferred mood.
- **Energy similarity:** Up to 2 points depending on how close the song's energy is to the user's target.
- **Valence similarity:** Up to 1 point depending on how close the song's valence is to the user's target.

For energy, the formula is `2 * (1 - abs(song_energy - target_energy))`.

For valence, the formula is `1 - abs(song_valence - target_valence)`.

I decided to give genre and mood the highest weights because I think they have a bigger impact on the type of music someone wants to hear. Energy and valence help make the results more accurate by considering how a song feels.

### Recommendation Process

The system will first read the user's preferences and load all the songs from the CSV file. It will then go through each song, compare its features with the user's preferences, and calculate a total score.

After every song has been scored, the system will sort the songs from highest to lowest and return the top three recommendations. Each recommendation will also include an explanation of why it matches the user's taste.

**Input → Compare Features → Calculate Scores → Rank Songs → Top 3 Recommendations**

### Potential Biases and Limitations

One possible issue with my system is that it gives more importance to genre, which means it might overlook songs from other genres that still match the user's preferred mood and energy. For example, someone who likes chill lofi music might also enjoy relaxing jazz, but the system could rank jazz lower just because the genre is different.

Another limitation is that my dataset only contains 18 songs, so the recommendations will be limited. The system also doesn't consider lyrics, listening history, or how a person's music taste might change over time. I think adding more songs and considering user feedback would make the recommender better in the future.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



