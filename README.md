# FilmMikirAPI 

This repo is a simple rest-api which is used for scrapping on the [Kincir](https://kincir.com) website using the Python and Flask package

## Endpoint

| Url Usage | Params Type | Endpoint |
| ------------- |:-------------:| :-----:| 
| / | - | Default Endpoint | 
| /news  | - | Get News Article from kincir | 
| /news/`<page>`  | Integer | ^ same but with Pagination | 
| /news/read/`<id>`  | String | Get Article from some news | 
| /review  | - | Get movie reviews from kincir | 
| /review/`<page>`  | Integer | ^ same but with Pagination | 
| /review/read/`<id>`  | String | ^ Get Article from some review | 
| /rating  | - | Get movie ratings from ImDb | 
| /rating/`<page>`  | Integer | ^ same but with Pagination | 
| /search/`<article\|rating>`/`<keyword>`  | String,String | Search Specific Article or Rating | 
| /search/`<article\|rating>`/`<keyword>`/`<page>`| String,String,Number | ^ same but with Pagination | 

#note: The Article `id` contained in the search result can be used for `/review/read/<id>` and `/news/read/<id>` endpoints

## API Usage
**BaseURL:**
```url
https://film-mikir.vercel.app/
```
**Example:**
* https://film-mikir.vercel.app/news/2
* https://film-mikir.vercel.app/news/read/zWQ4BWRgjo0Or
* https://film-mikir.vercel.app/search/article/marvel/2
* https://film-mikir.vercel.app/search/article/monster%20hunter

## Development
* (For Windows) set the flask app
```bash
set FLASK_APP=app.py
```
* Start server with command:
```bash
python -m flask run
```
Then open [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Package Used
This project uses several packages contained in [requirements](requirements.txt), which can be installed using the PIP command:

```bash
python -m pip install -r requirements.txt
```

## License
This API Scrapper is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)
