import os
import json
import io

class PersistentEmulate():
    savemoment = {}
    character_mention = {}

persistent = PersistentEmulate()

persistent.savemoment = {"chapter": 1, "scene": "1", "dialogue": ["dialogue", "1"]}

def CheckJSON(filename):
    with io.open(f"game/{filename}", "r", encoding='utf-8') as f:
        try :d = json.loads(f.read())
        except: return False
        test1 = ["characters", "scenes"]
        test2 = ["music", "background", "events"]
        test3 = ["type", "sound", "characters"]
        test4 = ["text", "text_author_name", "next_event", "next_scene"]
        test5 = ["option_text", "next_event", "next_scene"]
        
        for key in test1:
            if key not in d.keys():
                return False
        
        scenes = d["scenes"]
        if not isinstance(scenes, dict):
            return False
        for scene in scenes.keys():
            if not isinstance(scene, str) or not scene.isdigit():
                return False
            
            attributes = scenes[scene]
            if not isinstance(attributes, dict):
                return False
            
            for key in test2:
                if key not in attributes.keys():
                    return False
                
            events = attributes["events"]
            if not isinstance(events, dict):
                return False
            
            for event in events.keys():
                if not isinstance(event, str) or not event.isdigit():
                    return False
                event_attributes = events[event]

                for key in test3:
                    if key not in event_attributes.keys():
                        return False
                    
                if event_attributes["type"] == "dialogue":
                    for key in test4:
                        if key not in event_attributes.keys():
                            return False
                    next_event = event_attributes["next_event"]
                    next_scene = event_attributes["next_scene"]
                    if next_scene is None:
                        if next_event is None:
                            return False
                        if next_event not in events.keys():
                            return False
                    elif next_event is None:
                        if next_scene != "0" and next_scene not in scenes.keys():
                            return False
                    else:
                        return False
                        
                elif event_attributes["type"] == "choice":
                    if "menu" not in event_attributes.keys():
                        return False
                    menu = event_attributes["menu"]
                    if not isinstance(menu, dict):
                        return False
                    
                    for choices in menu.keys():
                        if isinstance(choices, str) and choices.isdigit():
                            choice = menu[choices]
                            for key in test5:
                                if key not in choice.keys():
                                    return False
                            next_event = choice["next_event"]
                            next_scene = choice["next_scene"]
                            if next_scene is None:
                                if next_event is None:
                                    return False
                                if next_event not in events.keys():
                                    return False
                            elif next_event is None:
                                if next_scene != "0" and next_scene not in scenes.keys():
                                    return False
                            else:
                                return False
                else:
                    return False
        return True


 
#print(CheckJSON("1.json"))
#print(GetNotInDirectoryFilenames())
               

"""renpy
init -988 python:
"""
import json
import glob
import os



def GetNotInDirectoryFilenames():
    directory = os.path.dirname(os.path.abspath(__file__))
    filenames_list = []
    for (dirpath, dirnames, filenames) in os.walk(f"{directory}/chapters"):
        filenames_list.append(filenames)
    return filenames_list[0]


def EditSavesJson(slot):
        with renpy.open_file("saves.json") as j:
            name = j.name
            name = name.replace("\\","/")
            if len(j.read()) == 0:
                saves = dict()
            else:
                j.seek(0)
                saves = json.loads(j.read())
        save_string = {"chapter": str(persistent.savemoment["chapter"]), "scene": persistent.savemoment["scene"], "dialogue": persistent.savemoment["dialogue"][1]}
        saves[str(slot)] = save_string
        with open(name, "w") as j:
            json.dump(saves,j)
        return

"""renpy
init -100 python:
"""
#persistent.savemoment = {"chapter": 1, "scene": "1", "dialogue": ["dialogue", "1"]}

jsonFile = None

chapter = persistent.savemoment["chapter"]
scene = persistent.savemoment["scene"]
dialogue = persistent.savemoment["dialogue"]

def get_number(array):
    return array.get('number')
       

def GetFilenames():
    filenames = GetNotInDirectoryFilenames()
    newFilenames = []
    for filename in filenames:
        if os.path.basename(filename).split('.')[0].isdigit() and os.path.basename(filename).split('.')[1] == 'json':
            newFilenames.append(filename)
    newArray = []
    for ar in newFilenames:
        number = int(ar.split('\\')[-1].split('.')[0])
        newArray.append({'path': ar, 'number': number})
    newArray.sort(key = get_number)
    result = []
    for ar in newArray:
        result.append(ar['path'])
    return result

