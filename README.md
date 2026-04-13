# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Real-world recommenders like Spotify combine user behavior patterns with song attributes. My version focuses purely on content-based filtering. Each song will be scored against a user profile using weighted features like genre, mood, and energy, then ranking all songs by that score to gather the best matches.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

Each song gets a single number between 0 and 1 that represents how well it matches the user's taste profile. That number is built from six features, each contributing to a weighted total.

Genre and mood are checked as simple matches if the song's genre matches the user's favorite genre, it earns full points for that feature. If not, it earns zero, and the same can be said about mood.

Energy, valence, danceability, and acousticness are scored by closeness.

Input          →        Process          →       Output
User Profile        Score every song            Sort + slice
(6 features)        (weighted formula)          (top K songs)
                    repeated 18 times

Potential Flaws: The algorithm may over prioritize mood when genre doesn't match.

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

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

- Raising genre weight to +2.0 made it dominate ranking. The correct song still won in The Contradiction even with a conflicting mood.
- Adding valence improved separation between songs that share a genre but feel emotionally different.
- High-Energy Pop and Chill Lofi produced the most intuitive results. The Unicorn exposed that a single catalog match always wins regardless of numeric fit.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

- Only 18 songs. most genres have one entry, so niche users have no real choice.
- Does not understand lyrics, context, or listening history.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

Recommenders reduce taste to numbers, and every design choice about what to measure and how to weight it quietly shapes who the system works for. Building this made it clear how bias enters through small decisions, like treating all numeric features equally even when users don't care about all of them.

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

VibeMatcher 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

VibeMatch 1.0 suggests up to 5 songs from an 18-song catalog based on a user's preferred genre.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

Each song is scored by awarding points for a genre match (+2.0) and mood match (+1.0), then adding closeness scores for energy, valence, danceability, and acousticness (each 0–1), and ranking all songs from highest total to lowest.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

The catalog contains 18 songs across 15 genres and 14 moods. Most genres appear only once and the dataset reflects predominantly popular music.

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

The system produces accurate, explainable results for users whose preferred genre and mood are well-represented in the catalog, and every recommendation comes with a point-by-point breakdown of why it ranked where it did.

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

I would add partial credit for related genres and moods and allow users to weight which features matter most to them.

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

I learned that recommender systems are genuinely difficult to build, as it is hard to accurately capture what a user likes or cares about most without detailed information about their preferences. In the past, I have definitely felt that recommendation systems are not always great, and now I can see why that is sometimes the case.