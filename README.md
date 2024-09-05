# World Covid News
A web application that displays a world map and the latest covid news of the country clicked on.

![](static/web%20app%20screenshot.PNG)
<br>

**Here are the technologies I used:**
- Python
- Flask
- PostgreSQL
- [NewsCatcher API](https://rapidapi.com/newscatcher-api-newscatcher-api-default/api/covid-19-news)
- [amCharts](https://www.amcharts.com/)

## Installation
### 1. Prerequisites
Python 3.10+, Git

### 2. Clone Project
Open a terminal and run the following commands:
```bash
git clone https://github.com/emmaduru/world-covid-news.git
cd world-covid-news
```

### 3. Create virtual environment and install dependencies from pyproject.toml
```bash
poetry install
```


### 4. Running the web application
Rename the .env.example file to .env and enter your personal information.
Then seed the database:

```bash
python seed_db.py
```

Then launch the development server:

```bash
python app.py
```

Go to http://127.0.0.1:5000 in a web browser
