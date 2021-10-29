from flask import Flask
from flask_restful import Api

from Player import Players, PlayerId, PlayerInfo, AllTimeStats, SeasonStats
from GameLog import PlayerGameLogAllTime, PlayerGameLogSeason


app = Flask(__name__)
api = Api(app)

api.add_resource(Players, '/players')
api.add_resource(PlayerId, '/players/<string:name>')
api.add_resource(PlayerInfo, '/players/<int:_id>')
api.add_resource(AllTimeStats, '/players/<int:_id>/stats')
api.add_resource(SeasonStats, '/players/<int:_id>/stats/<int:season>')
api.add_resource(PlayerGameLogAllTime, '/gamelog/<int:_id>')
api.add_resource(PlayerGameLogSeason, '/gamelog/<int:_id>/<int:season>')

if __name__ == "__main__":
    app.run(debug=True)
