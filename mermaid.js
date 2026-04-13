flowchart TD
    A[User Profile\ngenre · mood · energy · valence · danceability · acousticness] --> B[Load Song Library\nsongs.csv]
    B --> C[For Each Song]

    C --> D{Genre match?}
    D -- yes --> D1[+0.30]
    D -- no --> D2[+0.00]

    C --> E{Mood match?}
    E -- yes --> E1[+0.25]
    E -- no --> E2[+0.00]

    C --> F[Energy closeness\n1 - gap × 0.20]
    C --> G[Valence closeness\n1 - gap × 0.15]
    C --> H[Danceability closeness\n1 - gap × 0.05]
    C --> I[Acousticness closeness\n1 - gap × 0.05]

    D1 & D2 & E1 & E2 & F & G & H & I --> J[Sum All Weighted Scores\ntotal score 0.0 – 1.0]

    J --> K[Repeat for every song]
    K --> C

    K --> L[Sort All Songs by Score\nhighest first]
    L --> M[Return Top K Results]
