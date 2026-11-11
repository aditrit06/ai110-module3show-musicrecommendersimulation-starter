# 🎧 Model Card: VibeMatch 1.0

## 1. Model Name
**VibeMatch 1.0 — Music Recommender Simulation**

I chose this name because the goal is to match songs to a person's preferred music vibe.

---

## 2. Intended Use
VibeMatch is a small music recommendation program I made for my AI110 project. It is designed to help someone discover songs in a sample catalog based on their favorite genre, mood, energy level, and valence (how positive a song feels). It assumes a person can describe those preferences and that each song has accurate labels. The program is for learning and experimenting, not for use as a real streaming service. It should not be used to predict someone's entire personality or make important decisions about them.

---

## 3. How the Model Works  

My recommender uses **content-based filtering**. It compares the user's preferences to each song instead of looking at what other listeners enjoy. In the current scoring rule, a matching genre adds 2 points and a matching mood adds 3 points. Energy similarity can add up to 4 points and valence similarity up to 1 point, depending on how close each value is to what the user wants. Each song receives a score out of 10, and the program sorts the songs and shows the top five with reasons for their scores.

This is a rule-based program, not an AI model that learns from training data. I tested a weight change from genre 4, mood 3, energy 2, valence 1 to genre 2, mood 3, energy 4, valence 1. The revised weights are the ones currently active, and the maximum score remains 10. The CSV also has tempo, danceability, and acousticness, but the final scoring rule does not use those features.

---

## 4. Data  

I started with the 10 fictional songs in the provided data/songs.csv file and added 8 more, for **18 songs total**. The catalog includes styles such as pop, lofi, rock, jazz, ambient, synthwave, R&B, hip-hop, folk, classical, EDM, country, Latin, and metal. Every row includes a song title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

The dataset is small, and some genres and moods have only one song. The songs and their labels are examples for this simulation, not a real-world music catalog. The system also does not have listening history, skips, or ratings from actual users.

---

## 5. Strengths  

The recommender is easy to understand because every recommendation has a score and an explanation. It gave results that made sense for my main test profiles: **Sunrise City** for High-Energy Pop, **Midnight Coding** for Chill Lofi, and **Storm Runner** for Deep Intense Rock. I also liked being able to change one weight and immediately see how the rankings responded. It was a simple way to understand how recommendation rules affect what people are shown.

---

## 6. Limitations and Bias 

The catalog is small, with only 18 songs, so a user's requested genre and mood may not be represented. For example, it has no song labeled sad. In the Sad EDM test, Festival Rush ranked first even though its mood is euphoric: it earned points for EDM and its close energy match, while receiving no mood-match points and only 0.18 valence points. This is the closest available result under the formula, not a true sad EDM match.

My original scoring gave genre more points than mood, which could favor a genre match over the requested feeling. In the current experiment, I changed the weights: genre is 2 points, mood is 3, energy similarity is worth up to 4, and valence similarity is worth up to 1. Genre is no longer weighted more than mood, but genre matching is still exact, so related labels such as pop and indie pop do not count as a match. Energy can also outweigh a mood mismatch. These choices can produce recommendations that score well but do not feel right to a listener.

The system only recommends from this fixed catalog and does not learn from listening history, other users, or feedback. It also ignores tempo, danceability, and acousticness even though those features are in the dataset. The small catalog and fixed scoring rule may limit variety; this demo does not learn a user's behavior over time, so that limitation is different from a streaming service's learned filter bubble.

---

## 7. Evaluation  

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and the edge-case Sad EDM. I checked the top five results, scores, and explanations. The results below were run with the current weights: genre 2, mood 3, energy up to 4, and valence up to 1. The maximum possible score remains 10.

### High-Energy Pop

```
PROFILE: High-Energy Pop
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.85, 'valence': 0.85}
1. Sunrise City by Neon Echo - 9.87/10
	Because: genre match (+2.00); mood match (+3.00); energy similarity (+3.88); valence similarity (+0.99)
2. Rooftop Lights by Indigo Parade - 7.60/10
	Because: genre does not match (+0.00); mood match (+3.00); energy similarity (+3.64); valence similarity (+0.96)
3. Gym Hero by Max Pulse - 6.60/10
	Because: genre match (+2.00); mood does not match (+0.00); energy similarity (+3.68); valence similarity (+0.92)
4. Midnight Salsa by Luna Sol - 4.93/10
	Because: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+3.96); valence similarity (+0.97)
5. Concrete Dreams by Metro Verse - 4.61/10
	Because: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+3.76); valence similarity (+0.85)
```

### Chill Lofi

```
PROFILE: Chill Lofi
Preferences: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.4, 'valence': 0.6}
1. Midnight Coding by LoRoom - 9.88/10
	Because: genre match (+2.00); mood match (+3.00); energy similarity (+3.92); valence similarity (+0.96)
2. Library Rain by Paper Lanterns - 9.80/10
	Because: genre match (+2.00); mood match (+3.00); energy similarity (+3.80); valence similarity (+1.00)
3. Spacewalk Thoughts by Orbit Bloom - 7.47/10
	Because: genre does not match (+0.00); mood match (+3.00); energy similarity (+3.52); valence similarity (+0.95)
4. Focus Flow by LoRoom - 6.99/10
	Because: genre match (+2.00); mood does not match (+0.00); energy similarity (+4.00); valence similarity (+0.99)
5. Coffee Shop Stories by Slow Stereo - 4.77/10
	Because: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+3.88); valence similarity (+0.89)
```

### Deep Intense Rock

```
PROFILE: Deep Intense Rock
Preferences: {'genre': 'rock', 'mood': 'intense', 'energy': 0.95, 'valence': 0.4}
1. Storm Runner by Voltline - 9.76/10
	Because: genre match (+2.00); mood match (+3.00); energy similarity (+3.84); valence similarity (+0.92)
2. Gym Hero by Max Pulse - 7.55/10
	Because: genre does not match (+0.00); mood match (+3.00); energy similarity (+3.92); valence similarity (+0.63)
3. Iron Echoes by Ash Engine - 4.79/10
	Because: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+3.88); valence similarity (+0.91)
4. Festival Rush by Electric Tide - 4.44/10
	Because: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+3.96); valence similarity (+0.48)
5. Night Drive Loop by Neon Echo - 4.11/10
	Because: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+3.20); valence similarity (+0.91)
```

### Edge Case: Sad EDM

```
PROFILE: Edge Case: Sad EDM
Preferences: {'genre': 'edm', 'mood': 'sad', 'energy': 0.95, 'valence': 0.1}
1. Festival Rush by Electric Tide - 6.14/10
	Because: genre match (+2.00); mood does not match (+0.00); energy similarity (+3.96); valence similarity (+0.18)
2. Iron Echoes by Ash Engine - 4.67/10
	Because: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+3.88); valence similarity (+0.79)
3. Storm Runner by Voltline - 4.46/10
	Because: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+3.84); valence similarity (+0.62)
4. Gym Hero by Max Pulse - 4.25/10
	Because: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+3.92); valence similarity (+0.33)
5. Night Drive Loop by Neon Echo - 3.81/10
	Because: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+3.20); valence similarity (+0.61)
```

### What surprised me

The weight change moved Rooftop Lights above Gym Hero for High-Energy Pop. Rooftop Lights matches the requested happy mood and has similar energy, while Gym Hero's genre match is worth less under the revised weights. For Chill Lofi, Spacewalk Thoughts moved ahead of Focus Flow because it matches the chill mood and has similar energy, despite not matching the lofi genre. In the Sad EDM case, Festival Rush still ranks first even though it is euphoric rather than sad, because it matches EDM and nearly matches the requested energy.

### Comparing the profiles

- **High-Energy Pop vs. Chill Lofi:** Sunrise City ranks first for High-Energy Pop, while Midnight Coding ranks first for Chill Lofi. Their genres, moods, and energy levels fit the different profiles.
- **High-Energy Pop vs. Deep Intense Rock:** Sunrise City ranks first for pop, while Storm Runner ranks first for rock. Gym Hero appears in both lists because it is energetic; its intense mood also helps it rank second for Deep Intense Rock.
- **High-Energy Pop vs. Sad EDM:** Sunrise City ranks first for the pop profile, while Festival Rush ranks first for Sad EDM. Festival Rush matches EDM and energy but not the requested sad mood.
- **Chill Lofi vs. Deep Intense Rock:** Midnight Coding ranks first for the calm lofi profile, while Storm Runner ranks first for the intense rock profile.
- **Chill Lofi vs. Sad EDM:** The lofi profile has songs matching both genre and mood. The Sad EDM profile has no exact mood match in the catalog, so its top recommendation has a lower score and a conflicting mood.
- **Deep Intense Rock vs. Sad EDM:** Both profiles ask for high energy. Storm Runner also matches rock and intense, while Festival Rush matches EDM but is euphoric rather than sad.

### Weight-shift experiment

I compared my initial weights (genre 4, mood 3, energy up to 2, valence up to 1) with the revised weights used for the results above (genre 2, mood 3, energy up to 4, valence up to 1). Both versions have a maximum score of 10. In the initial High-Energy Pop run, the top three were Sunrise City (9.93), Gym Hero (6.76), and Rooftop Lights (5.78). With the revised weights, they were Sunrise City (9.87), Rooftop Lights (7.60), and Gym Hero (6.60). This shows that the new weights change the ranking and give energy similarity more influence; it does not prove that the recommendations are more accurate. Listener feedback or further evaluation would be needed to judge that. The revised weights are the ones currently active in my code.

---

## 8. Future Work  

If I kept developing VibeMatch, I would:

1. Add more songs, especially moods and genres that are missing or underrepresented.
2. Let users like, skip, or rate songs so the system can adjust to their feedback.
3. Try a more balanced scoring system and use features like acousticness or danceability to find good matches across different genres.

---

## 9. Personal Reflection  

My biggest learning moment was realizing that a recommendation system does not have to be super complicated to give results that feel personal. At first, I thought it would take a lot more AI to recommend music, but even a few scoring rules gave me songs that made sense for different users. I was surprised that **Gym Hero** could rank highly for both happy pop and intense rock, but for different reasons. It showed me that the weights I choose can change what the program thinks is a good match.

Using an AI coding assistant helped me understand the CSV code, work through the scoring logic, and think of unusual test profiles. But I still needed to check the output myself. I even had to fix an import error before the program ran correctly, which reminded me that generated code is not always ready to use right away. The Sad EDM test was another important example: the program chose a song that matched the genre but not the mood. That made me realize that a high score does not always mean a recommendation actually feels right to a person. If I continued this project, I would add more variety and let users give feedback so the recommender could improve over time.
