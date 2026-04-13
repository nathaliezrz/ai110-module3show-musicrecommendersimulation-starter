# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

VibeMatcher 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

VibeMatch 1.0 suggests up to 5 songs from an 18-song catalog based on a user's preferred genre.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Each song is scored by awarding points for a genre match (+2.0) and mood match (+1.0), then adding closeness scores for energy, valence, danceability, and acousticness (each 0–1), and ranking all songs from highest total to lowest.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---
The catalog contains 18 songs across 15 genres and 14 moods. Most genres appear only once and the dataset reflects predominantly popular music.

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system produces accurate, explainable results for users whose preferred genre and mood are well-represented in the catalog, and every recommendation comes with a point-by-point breakdown of why it ranked where it did.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The system's genre and mood matching is all-or-nothing. Similar labels like "chill" and "relaxed" are treated as completely unrelated, which means users whose preferred mood or genre is rare in the catalog are  disadvantaged before any numeric scoring begins. The proximity formula also favors moderate preferences: a user targeting energy 0.50 can never score below 0.50 on that feature, while a user with a strong preference like 0.95 faces penalties across most of the catalog.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

I tested seven profiles in total:
- Indie Pop Fan — indie pop / happy / moderate energy
- High-Energy Pop — pop / happy / high energy, low acousticness
- Chill Lofi — lofi / chill / low energy, high acousticness
- Deep Intense Rock — rock / intense / very high energy
- The Contradiction — rock genre + chill mood + high energy target (internally conflicting)
- The Perfect Numeric Trap — classical/peaceful genre+mood with numeric targets that exactly match a rock song
- The Unicorn — synthwave genre with numeric targets that are the opposite of the only synthwave song in the catalog

When running these profiles, I looked for accuracy in the recommendations - meaning that if a profile was created as an "Indie Pop Fan," I expected indie music to be ranked higher. In certain adversarial tests, like "The Contradiction," I was surprised to find the algorithm still worked, as the high weight given to genre allowed the correct choice to be made.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

Add partial credit for related genres and moods and allow users to weight which features matter most to them.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that recommender systems are genuinely difficult to build, as it is hard to accurately capture what a user likes or cares about most without detailed information about their preferences. In the past, I have definitely felt that recommendation systems are not always great, and now I can see why that is sometimes the case.

