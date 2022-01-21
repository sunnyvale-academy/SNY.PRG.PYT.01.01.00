import json
from json import JSONEncoder
from spacex_mission import SpaceXMission

class MissionEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
    
# Single object
spacex_mission = SpaceXMission(mission_name='Inspiration 4')
print(json.dumps(spacex_mission, cls=MissionEncoder))

# Object array
spacex_missions = [SpaceXMission(mission_name='Crew-3'), SpaceXMission(mission_name='Inspiration-4')]
print(json.dumps(spacex_missions, cls=MissionEncoder))
