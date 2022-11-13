import pandas as pd

"""
Reprise de la hiérarchie établie dans le fichier "script_genre_python.py"
Fusion de la table contenant GENRE_ALBUM ; TOTAL_COUNT et de la hiérarchie pour générer un fichier json qui est affiché dans la sortie standard du terminal
"""

unknown = {'other_style':['acoustic', 'chanson', 'medieval', 'freestyle', 'mixed', 'dark cabaret', 'cabaret&#x200e;', 'avant-garde', 'classical', 'contemporary christian', 'indie', 'industrial', 'merengue', 'native american', 'bolero', 'neue deutsche h&#xe4;rte', 'neue deutsche welle', 'norte&#xf1;o', 'soundtrack', 'crossover', 'crossover thrash', 'world music', 'schlager', 'christmas', 'singer-songwriter', 'comedy', 'parody', 'musical'],
            'voice_style':['vocal', 'spoken word', 'beatbox']}
electronic = {'industrial_style':['aggrotech', 'ebm', 'edm', 'electronica', 'chiptune', 'techno', 'indietronica', 'experimental', 'drum and bass'],
            'house_style':['electro house', 'hip house', 'house', 'progressive house'],
            'ambient_style':['ambient', 'glitch', 'downtempo'],
            'disco_style':['disco', 'italo disco', 'eurodance', 'europop', 'alternative dance', 'dance', 'idm'],
            'breakbeat_style':['breakbeat', 'big beat', 'dubstep', 'rave', 'new rave', 'trance'],
            'electro_style':{'dark electro', 'electro', 'electroclash', 'electronic', 'electronicore'}}
rock = {'heavy_metal_style':['deathcore', 'goregrind', 'grindcore', 'black metal', 'death &apos;n&apos; roll', 'alternative metal', 'thrash metal', 'brutal death metal', 'nu metal', 'death metal', 'deathrock', 'progressive death metal', 'melodic death metal', 'technical death metal', 'avant-garde metal', 'christian metal', 'doom metal', 'dark metal', 'extreme metal', 'gothic metal', 'groove metal', 'industrial metal', 'melodic metalcore', 'heavy metal', 'metalcore', 'power metal', 'rap metal', 'rap  metal', 'symphonic metal', 'speed metal', 'sludge metal', 'progressive metal', 'pirate metal', 'glam metal', 'viking metal', 'symphonic black metal', 'mathcore', 'happy hardcore', 'digital hardcore', 'melodic hardcore', 'post-hardcore'],
        'rock_style':['lo-fi', 'shoegazing', 'rio', 'jovem guarda', 'grunge', 'canterbury', 'post-grunge', 'britpop', 'alternative rock', 'art rock', 'soft rock', 'celtic rock', 'blues rock', 'country rock', 'comedy rock', 'electronic rock', 'experimental rock', 'folk rock', 'garage rock', 'glam rock', 'hard rock', 'krautrock', 'industrial rock', 'gothic rock', 'indie rock', 'noise rock', 'post-rock', 'j-rock', 'pop rock', 'math rock', 'instrumental rock', 'rap rock', 'psychedelic rock', 'latin rock', 'rock', 'rock &apos;n&apos; roll', 'southern rock', 'stoner rock', 'progressive rock'],
        'funk_style':['g-funk', 'funk', 'funk metal', 'funk rock'],
        'punk_style':['emo', 'screamo', 'gothic', 'powerviolence', 'riot grrrl', 'dark wave', 'new wave', 'queercore', 'anarcho-punk', 'crust punk', 'folk punk', 'deutschpunk', 'electropunk', 'garage punk', 'hardcore punk', 'garage punk', 'horror punk', 'gypsy punk', 'oi-punk', 'pop punk', 'post-punk', 'post-punk&#x200e;', 'punk cabaret', 'punk rock', 'ska punk', 'skate punk', 'steampunk', 'street punk', 'punk blues', 'dance punk', 'psychobilly']}
hiphop = {'crunk_style':['crunk', 'crunkcore', 'trap'],
        'hip_hop_style':['alternative hip hop', 'french hip hop' ,'australian hip hop', 'horrorcore', 'trip hop', 'christian hip hop', 'experimental hip hop', 'east coast hip hop', 'west coast hip hop', 'hip hop', 'hardcore hip hop', 'political hip hop', 'nerdcore hip hop', 'southern hip hop', 'underground hip hop']}
jazz = {'jazz_style':['jazz', 'jazz fusion', 'vocal jazz', 'afrobeat', 'swing'],
        'blues_style':['blues', 'country blues', 'doo-wop']}
country = {'country_style':['country', 'sertanejo', 'americana', 'alternative country', 'bakersfield sound', 'bluegrass']}
folk = {'folk_style':['filk', 'anti-folk', 'contemporary folk', 'folk', 'folk metal', 'irish folk', 'indie folk', 'neofolk', 'psych folk']}
reggae = {'reggae_style':['reggae', 'reggae fusion', 'reggaeton', 'ska', 'dancehall']}
samba = {'samba_style':['samba', 'bossa nova', 'mpb']}
rnbsoul = {'r&b_soul_style':['blue-eyed soul', 'neo soul&#x200e;', 'neo soul', 'soul', 'r&amp;b', 'gospel', 'worship']}
pop = {'pop_style':['baroque pop', 'classic pop', 'electropop', 'grime', 'dream pop', 'french pop', 'indie pop', 'adult contemporary', 'noise pop', 'power pop', 'pop', 'pop rock&#x200e;', 'j-pop', 'dance-pop', 'teen pop', 'psychedelic pop', 'latin pop', 'k-pop', 'synthpop', 'futurepop']}
rap = {'rap_style':['gangsta rap', 'j-rap', 'midwest rap', 'rapcore']}

tree = {'unknown':unknown, 'electronic':electronic, 'rock':rock, 'hiphop':hiphop, 
'jazz':jazz, 'country':country, 'folk':folk, 'reggae':reggae, 'samba':samba, 'rnbsoul':rnbsoul, 'pop':pop, 'rap':rap}

data = pd.read_csv('genre_counted.csv')
sorted = {}
for index, row in data.iterrows():
    sorted[row['genre_album'].lower()] = row['total_count']

json = '{"name": "all_genre", "children": ['
for genre_index, genre_name_dic in enumerate(tree.items()):
    json += '{"name": "' + genre_name_dic[0] + '", "children": ['
    for style_index, style_name_list in enumerate(genre_name_dic[1].items()):
        json += '{"name": "' + style_name_list[0] + '", "children": ['
        for i, style in enumerate(style_name_list[1]): 
            json += '{"name": "' + style + '", "value":' + str(sorted[style]) + '}'
            if i != len(style_name_list[1]) - 1:
                json += ','
        json += ']}'
        if style_index != len(genre_name_dic[1]) - 1:
            json += ','
    json += ']}'
    if genre_index != len(tree) - 1:
        json += ','
json += ']}'
print(json)