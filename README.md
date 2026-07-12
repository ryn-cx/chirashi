# Chirashi

[Crunchyroll](https://www.crunchyroll.com) API wrapper built using [Good Ass
Pydantic Integrator](https://github.com/ryn-cx/good-ass-pydantic-integrator) and
[Get Around](https://github.com/ryn-cx/get-around).

## Installation

```bash
uv add git+https://github.com/ryn-cx/chirashi
```

## Usage

Every endpoint has `get()` (parsed, typed model) and `download()` (raw JSON).

```python
from chirashi import Chirashi

client = Chirashi()

series = client.series.get(series_id)
seasons = client.seasons.get(series_id)
episodes = client.season_episodes.get(season_id)
browse = client.browse_series.get()
search = client.search.get(query)
```
