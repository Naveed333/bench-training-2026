# Day 4 – GitHub Fetcher + Weather CLI

## Scripts

- `github_profile.py` : Fetches a GitHub user's profile and top repos using the GitHub public API
- `weather.py` : Fetches current weather for any city using the Open-Meteo API (no key needed)

---

## Example Output

### github_profile.py
```
$ python github_profile.py Naveed


=============================================
  GitHub Profile: Naveed333
=============================================
  Bio       : Backend || @nodejs developer
  Repos     : 26
  Followers : 4
  Following : 6

  Top 5 Repos by Stars:
  Repo                                 Stars  Language
  -------------------------------------------------------
  ai601-data-engineering                   0  Jupyter Notebook
  batch_analytics_pipeline                 0  Shell
  bench-training-2026                      0  Python
  coins_poc                                0  Vue
  crypto_data_pipeline                     0  Jupyter Notebook
```

### weather.py
```
$ python weather.py Lahore


========================================
  Weather for Lahore, Pakistan
========================================
  Description : Mainly clear
  Temperature : 26.9°C  /  80.4°F
  Wind Speed  : 5.2 km/h
```

---

## What was the hardest part of reading the API response?

For the **GitHub API**, the tricky part was that repos come back as a flat list with no sorting, you get all repos mixed together and have to sort by `stargazers_count` yourself.

For the **Open-Meteo API**, the hardest part was realizing it needs coordinates, not a city name, so you have to chain two API calls. The weather data lives inside `data["current"]` and the weather condition is just a numeric `weather_code`, not a human-readable string.
