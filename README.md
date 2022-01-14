# FilmMikirAPI 

This repo is a rest-api which is scraping to the [Kincir](https://kincir.com) website and made up using Flask.


## Endpoint

| Url Usage | Params Type | Endpoint |
| ------------- |:-------------:| :-----:| 
| / | - | Default Endpoint | 
| /reviews  | - | Get movie reviews from kincir | 
| /reviews/`<page>`  | Integer | ^ same but with Pagination | 
| /ratings  | - | Get movie ratings from ImDb | 
| /ratings/`<page>`  | Integer | ^ same but with Pagination | 
| /search/`<review\|rating>`/`<keyword>`  | String,String | Search Specific Review or Rating | 
|  /search/`<review\|rating>`/`<keyword>`/`<page>`| String,String,Number | ^ same but with Pagination | 

## Usage

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
This Project use some packages witch 
This project uses several packages contained in [requirements](requirements.txt), which can be installed using the PIP command:

```bash
python -m pip install -r requirements.txt
```

## License
This API Scrapper is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)
