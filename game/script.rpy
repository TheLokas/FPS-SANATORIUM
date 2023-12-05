init:
    $ e = Character(u'Калыван', color="#c8ffc8")
    python:
        import json
        import glob
        import os
        config.has_autosave = False
        config.has_quicksave = False
        config.hard_rollback_limit = 0

        jsonFile = None
        #renpy.image("kalivan", Image("kalivan nice.png", xalign=0.5, yalign=0, oversample=2))
        def get_number(array):
            return array.get('number')

        def Test():
            #renpy.scene("bg strashno")
            renpy.show("bg strashno")
            renpy.show("kalivan", tag="k", at_list=[Position(xalign=0.5, yalign=0.5)])
            #renpy.show("kalivan", tag="k")
            #Character(kind=k)("ТЕстовый диалог")
            renpy.say("Калыван", "ТЕстовый диалог")

        def GetFilenames():
            filenames = renpy.list_files()
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


        #Добавить аргументы в старт, начинающие игру с определённого файла, сцены, диалога
        # StartGame(chapter, scene, dialogue)
        def StartGame():
            filenames = GetFilenames()
            # i = 0
            for filename in filenames:
                # i += 1
                # if i < chapther:
                #     continue
                with renpy.open_file(filename) as j:
                    scenario = json.load(j)
                    scenes = scenario["scenes"]
                    
                    #next = scene
                    next = "1"

                    while next is not "0":
                        # next = ShowScene(scenes[next], dialogue)
                        next = ShowScene(scenes[next])
                        # dialogue = ["dialogue", "1"]
                        
            #for filename in filenames:
                
                # scenario = json.load(j)
                # scenes = scenario["scenes"]
                # next = "1"
                # while next is not "0":
                #     next = ShowScene(scenes[next])
            return



        # ShowScene(scene, dialogue)
        def ShowScene(scene):
            renpy.scene()
            renpy.show(scene["background"])
            events = scene["events"]
            if scene["music"] is not None:
                renpy.play(scene["music"], channel='music')

            next = ["dialogue", "1"]
            #next = dialogue

            while next[1] is not "0":
                next = ShowDialogue(events[next[1]])
                if next[0]=="scene":
                    return next[1] 
            return 0
            

        def ShowDialogue(event):
            eventType = event["type"]
            if event["sound"] is not None:
                renpy.play(event["sound"], channel='sound')
            if eventType == "dialogue":
                characters = event["characters"]
                if characters is not None:
                    for character in characters:
                        renpy.show(character["name"], at_list=[Position(xalign = character["xalign"], yalign = character["yalign"])])
                renpy.say(event["text_author_name"], event["text"])
                nextEvent = event["next_event"]
                nextScene = event["next_scene"]
                if nextEvent is not None:
                    return ["event", nextEvent]
                elif nextScene is not None:
                    return ["scene", nextScene]

            elif eventType =="choice":
                characters = event["characters"]
                menu = event["menu"]
                if characters is not None:
                    for character in characters:
                        renpy.show(character["name"], at_list=[Position(xalign = character["xalign"], yalign = character["yalign"])])
                renpy.say(menu["text_author_name"], menu["choice_text"])

                lenght = len(menu.keys())
                choices = list()
                for i in range(1, lenght - 1):
                    ch = str(i)
                    choices.append((menu[ch]["option_text"], ch))
                #archoices = choices.array()

                result = renpy.display_menu(choices)


                nextEvent = menu[result]["next_event"]
                nextScene = menu[result]["next_scene"]
                if nextEvent is not None:
                    return ["event", nextEvent]
                elif nextScene is not None:
                    return ["scene", nextScene]

             


        def JsonTest(n):
            with renpy.open_file('scenario.json') as j:
                scenario = json.load(j)
                scenes = scenario["scenes"]
                ShowScene(scenes[n])
                return
            
        filenames = GetFilenames()
        for filename in filenames:
            with renpy.open_file(filename) as j:
                scenario = json.load(j)
                characters = scenario["characters"]
                #jsonFile.append(j)
                    #scenes = scenario["scenes"]
                for character in characters:
                    renpy.image(character["code_name"], Image(character["image"],oversample = character["oversample"]))
                    

                    
            # next = 1
            # while next != 0:
            #     next = ShowScene(scenes[next])


label start:
    #$ Test()
    #$ JsonTest("1")
    #$ JsonTest("2")
    #$ StartGame(jsonFile)
    $ StartGame()
    return
