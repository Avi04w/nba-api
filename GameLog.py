from flask_restful import Resource
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll


class PlayerGameLogAllTime(Resource):
    def get(self, _id):
        game_log = playergamelog.PlayerGameLog(player_id=_id, season=SeasonAll.all).get_dict()
        game_list = {}
        for i in range(len(game_log['resultSets'][0]['rowSet'])):
            x = {}
            for j in range(len(game_log['resultSets'][0]['headers'])):
                x[game_log['resultSets'][0]['headers'][j]] = game_log['resultSets'][0]['rowSet'][i][j]
            game_list["game"+str(len(game_log['resultSets'][0]['rowSet']) - i)] = x
        return game_list


class PlayerGameLogSeason(Resource):
    def get(self, _id, season):
        game_log = playergamelog.PlayerGameLog(player_id=_id, season=season).get_dict()
        game_list = {}
        for i in range(len(game_log['resultSets'][0]['rowSet'])):
            x = {}
            for j in range(len(game_log['resultSets'][0]['headers'])):
                x[game_log['resultSets'][0]['headers'][j]] = game_log['resultSets'][0]['rowSet'][i][j]
            game_list["game" + str(len(game_log['resultSets'][0]['rowSet']) - i)] = x
        return game_list

