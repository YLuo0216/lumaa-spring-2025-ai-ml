# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

**Setup**
   - I am using Python 3.12.9, though it should work with other versions as well.
   - run these commands to setup (install dependencies and spaCy model):
   ```sh
   chmod +x setup.sh
   ./setup.sh
   ```

**Running**
   - To get recommendations, run
   ```sh
   python recommendation.py
   ```
   You will be prompted for user preferences.
   - If running preprocessing.py, download the data first and place in the same directory.

**Dataset**
   - Kaggle dataset: [Wikipedia Movie Plots](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots?resource=download)
   - I chose to use the title, genre, and plot columns for my approach.
   - Instances without genres were filtered out, and 500 instances were kept with a random seed.

**Modules**
   - preprocessing.py
      - Filters the dataset, tokenize and lemmatize movie description for recommendation.
      - This script outputs the file preprocessed_500.csv, with 500 movie titles, genres, plots, and tokenized and lemmatized keywords.
      - There is no need to rerun this file for generating recommendations.
   - recommendation.py
      - Takes user query and makes recommendations.
      - This script uses the processed data csv, uses tfidf and cosine similarity to find the matching movies.
      - The user query undergoes the same preprocessing to match best with the movie keywords.

**Example Output**
```What are your preferences? I love thrilling action movies set in space, with a comedic twist.
Here are your top movie recommendations:

Title: Henry Aldrich Gets Glamour
Genre: comedy
Plot: Henry Aldrich becomes the most sought after guy in town when he wins a date with a movie star.
Similarity Score: 0.086

Title: Tiger
Genre: thriller drama
Plot: The movie Tiger is a Kannada action packed thriller film led by the young star Pradeep (protagonist) who dreams to become a police officer which is against the wish of his father played by the well known actor and also a very famous Ex IAS officer K Shivram. Why is the father against the wish and the dream of his son is the crux of the story.
Similarity Score: 0.071

Title: Listen... Amaya
Genre: drama
Plot: The film is set in Delhi, where a widowed mother, Leela, runs library cafe " Book a Coffee." Here she makes a new friend, a widowed photographer, Jayant 'Jazz', and soon finds their friendship growing. However, Leela's daughter Amaya, a budding writer, feels insecure about the relationship when she finds out about it. While she collaborates with Jazz on producing a coffee table book about the bazaars of Old Delhi, when her mother takes her relationship with Jazz further, she is unable to accept it. The journeys of all the principal characters and a subtle twist at the end make up the narrative of the film. ..
Similarity Score: 0.063

Title: Violent Cop
Genre: action
Plot: A cop teams up with a pimp to catch a killer who castrates his male victims.
Similarity Score: 0.057

Title: Thikka
Genre: action comedy
Plot: The film is a confusion kidnap drama; Aditya (Sai Dharam Tej) is a booze-happy youngster who enjoys his day to day life until he meets a beautiful girl Anjali in an accident. He falls in love with her at first sight itself and also makes her fall in love with him too. After she entered to his life his entire lifestyle changes he leaves one by one all his bad habits, acquires a job in a corporate company and she also separates Aditya from his father Manohar (Rajendra Prasad) who is a big womanizer and drunker than him and also joins Manohar in a rehabilitation center.
The twist in the story arises when complications erupt between the couple and they break up with each other for a small quarrel. Anjali is a daughter of a multimillionaire Madan Mohan (Anand) who fixes her marriage with another rich man’s son Jayanth (Vennela Kishore). Simultaneously in the office, Aditya conned by Kapoor (Ali) who wants to give promotion to his girlfriend Kavitha (Mumaith Khan), so he traps Aditya makes him cheat his childhood friend Stephen (Sathya) which makes the conflict between them.
The frustrated Aditya call for a break up party along with his friends where so many characters enter into his life, Starting from his father Manohar escaping from rehabilitation center along with a girl Kamala (VJ Bani) his lover, who is a daughter of a late mafia don Devraj (Jakki), then a prostitute Padma come into the picture, suddenly two gangs of Sadhu Bhai (Ajay) and Narasimha (Raghu Babu) are after Aditya. A series of mad events follow - they fight with some guys, destroy a restaurant, a petrol bunk is burnt, etc. More on that Anjali elopes from marriage for Aditya and her father Madan Mohan’s men are also behind him and another beautiful girl Virisha (Mannara Chopra) tries to kill Aditya saying herself as his ex-lover. Rest of the story how Aditya comes out from this crazy situation.
Similarity Score: 0.040
```

**Video Demo**
[demo video](demo.mov)

**Salary Expectation**
I am looking for compensation around $25 per hour, which equates to around $2000 per month working 20 hours each week. Although, I value the experience and learning more than the compensation. I would love to know about the projects being worked on at Lumaa.
