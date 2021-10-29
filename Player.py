from flask_restful import Resource
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats


class Players(Resource):
    def get(self):
        return players.get_players()


class PlayerId(Resource):
    def get(self, name):
        p = [i for i in players.find_players_by_full_name(name)]

        players_id_list = []

        for i in p:
            players_id_list.append({'name': i['full_name'], 'id': i['id']})

        return players_id_list


class PlayerInfo(Resource):
    def get(self, _id):
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=_id).get_dict()

        info = {}

        for i in range(len(player_info['resultSets'][0]['headers'])):
            info[player_info['resultSets'][0]['headers'][i]] = player_info['resultSets'][0]['rowSet'][0][i]

        return info


class AllTimeStats(Resource):
    def get(self, _id):
        player_stats = playercareerstats.PlayerCareerStats(player_id=_id).get_dict()
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=_id).get_dict()

        seasons = len(player_info["resultSets"][0]['rowSet'])
        stats = {}

        for i in range(len(player_stats['resultSets'][0]['headers'])):
            stats[player_stats['resultSets'][0]['headers'][i]] = player_stats['resultSets'][0]['rowSet'][seasons-2][i]

        return stats


class SeasonStats(Resource):
    def get(self, _id, season):
        pass
