
import json
from spacex_mission import SpaceXMission

# JSON object
spacex_mission_json = '{"mission_name": "Crew-3", "mission_id": "2"}'
spacex_mission_dict = json.loads(spacex_mission_json)
spacex_mission = SpaceXMission(**spacex_mission_dict)
print(spacex_mission.mission_name)

# JSON array
spacex_missions_json = '[{"mission_name": "Crew-3", "mission_id": "2"}, {"mission_name": "Inspiration-4", "mission_id": "1"}]'
spacex_missions_array = json.loads(spacex_missions_json)
spacex_missions = [SpaceXMission(**mission) for mission in spacex_missions_array]
for mission in spacex_missions:
    print(mission.mission_name)
