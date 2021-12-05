import pygal
worldmap = pygal.maps.world.SupranationalWorld()
worldmap.title = 'Continents'
worldmap.add('Africa', [('africa')])
worldmap.add('North america', [('north_america')])
worldmap.add('Oceania', [('oceania')])
worldmap.add('Sount america', [('south_america')])
worldmap.add('Asia', [('asia')])
worldmap.add('Europe', [('europe')])
worldmap.add('Antartica', [('antartica')])
worldmap.render_to_file('abc.svg')