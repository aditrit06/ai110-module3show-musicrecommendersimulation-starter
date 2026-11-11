# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

My music recommender uses content-based filtering to compare each song's genre, mood, energy, and valence with the user's preferences. In my first scoring setup, genre was worth 4 points, mood 3, energy up to 2, and valence up to 1. In this experiment, I reduced genre to 2 points and increased energy to up to 4 points; mood stayed at 3 and valence at 1. The maximum remains 10 points. This change gives energy similarity more influence and exact genre matches less influence.

For my High-Energy Pop profile, the original top three were Sunrise City (9.93), Gym Hero (6.76), and Rooftop Lights (5.78). With the revised weights, they are Sunrise City (9.87), Rooftop Lights (7.60), and Gym Hero (6.60). Rooftop Lights moves above Gym Hero because it matches the preferred happy mood and is close in energy, while Gym Hero's genre-match advantage is smaller under the new weights. This demonstrates that changing weights changes rankings, but does not by itself prove the recommendations are more accurate; that would require checking them against listener judgments or other evaluation examples. The recommender uses a simple, editable formula rather than learning from listening history or other users. The starter project also includes an acoustic preference, but the current scoring formula does not use it.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

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

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
