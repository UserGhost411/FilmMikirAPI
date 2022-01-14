import lib.model as model
from lib.static import errorMessage
class Router:
    @staticmethod
    def run(app):
        @app.route('/')
        def root():
            return model.getRootData()
        @app.route('/news/')
        @app.route('/news/<page>')
        def a(page=1):
            return model.getNews(page)
        @app.route('/review/read/<id>/')
        @app.route('/news/read/<id>/')
        def b(id):
            return model.getReview(id)
        @app.route('/review/')
        @app.route('/review/<page>/')
        def c(page=1):
            return model.getReviews(page)
        @app.route('/rating/')
        @app.route('/rating/<page>/')
        def d(page=1):
            return model.getRatings(page)
        @app.route('/search/<a>/<keyword>/')
        @app.route('/search/<a>/<keyword>/<page>/')
        def e(a,keyword,page=1):
            return model.getSearch(a,keyword,page)
        @app.route('/<path:path>')
        def f(path):
            return errorMessage
        @app.after_request
        def z(response):
            response.headers["server"] = "UserGhost.my.id"
            response.headers["Access-Control-Allow-Origin"]="*"
            return response

