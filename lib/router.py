import lib.model as model
from lib.static import errorMessage
class Router:
    @staticmethod
    def run(app):
        @app.route('/')
        def root():
            return model.getRootData()
        @app.route('/review/<id>')
        def a(id):
            return model.getReview(id)
        @app.route('/reviews')
        @app.route('/reviews/<page>')
        def b(page=1):
            return model.getReviews(page)
        @app.route('/ratings')
        @app.route('/ratings/<page>')
        def c(page=1):
            return model.getRatings(page)
        @app.route('/search/<a>/<keyword>')
        @app.route('/search/<a>/<keyword>/<page>')
        def d(a,keyword,page=1):
            return model.getSearch(a,keyword,page)
        @app.route('/<path:path>')
        def e(path):
            return errorMessage
            

