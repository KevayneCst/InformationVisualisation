import pandas as pd
"""
J'ai d'abord obtenu l'ensemble des genres des albums. Ensuite à l'aide d'internet, j'ai trié manuellement les 259 genres dans une hiérarchie. A partir de la hiérarchie établie,
j'ai écrit un script qui génère un fichier json en prenant en compte la hiérarchie établie et le group-by count établi sur les genres.
Je fournis le json à d3js qui établie la visualisation sunburst
"""

data = pd.read_csv('genre_counted.csv')
genres  = data['genre_album'].unique()
lvl1 = [genre.lower() for genre in genres]
lvl1 = sorted(lvl1)
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

unknown_list = []
for k,v in unknown.items(): # style, genres
    for val in v:
        unknown_list.append(val)
print("Nb traité unknown:", len(unknown_list))

electronic_list = []
for k,v in electronic.items(): # style, genres
    for val in v:
        electronic_list.append(val)
print("Nb traité elec:", len(electronic_list))

rock_list = []
for k,v in rock.items(): # style, genres
    for val in v:
        rock_list.append(val)
print("Nb traité rock_metal:", len(rock_list))

hiphop_list = []
for k,v in hiphop.items(): # style, genres
    for val in v:
        hiphop_list.append(val)
print("Nb traité hiphop_list:", len(hiphop_list))

jazz_list = []
for k,v in jazz.items(): # style, genres
    for val in v:
        jazz_list.append(val)
print("Nb traité jazz_list:", len(jazz_list))

country_list = []
for k,v in country.items(): # style, genres
    for val in v:
        country_list.append(val)
print("Nb traité country_list:", len(country_list))

folk_list = []
for k,v in folk.items(): # style, genres
    for val in v:
        folk_list.append(val)
print("Nb traité folk_list:", len(folk_list))

reggae_list = []
for k,v in reggae.items(): # style, genres
    for val in v:
        reggae_list.append(val)
print("Nb traité reggae_list:", len(reggae_list))

samba_list = []
for k,v in samba.items(): # style, genres
    for val in v:
        samba_list.append(val)
print("Nb traité samba_list:", len(samba_list))

rnbsoul_list = []
for k,v in rnbsoul.items(): # style, genres
    for val in v:
        rnbsoul_list.append(val)
print("Nb traité rnbsoul_list:", len(rnbsoul_list))

pop_list = []
for k,v in pop.items(): # style, genres
    for val in v:
        pop_list.append(val)
print("Nb traité pop_list:", len(pop_list))

rap_list = []
for k,v in rap.items(): # style, genres
    for val in v:
        rap_list.append(val)
print("Nb traité rap_list:", len(rap_list))

treated = []
for val in unknown_list:
    if val not in treated:
        treated.append(val)
for val in electronic_list:
    if val not in treated:
        treated.append(val)
for val in rock_list:
    if val not in treated:
        treated.append(val)
for val in hiphop_list:
    if val not in treated:
        treated.append(val)
for val in jazz_list:
    if val not in treated:
        treated.append(val)
for val in country_list:
    if val not in treated:
        treated.append(val)
for val in folk_list:
    if val not in treated:
        treated.append(val)
for val in reggae_list:
    if val not in treated:
        treated.append(val)
for val in samba_list:
    if val not in treated:
        treated.append(val)
for val in rnbsoul_list:
    if val not in treated:
        treated.append(val)
for val in pop_list:
    if val not in treated:
        treated.append(val)
for val in rap_list:
    if val not in treated:
        treated.append(val)

rest = []
for genre in lvl1:
    if genre not in treated:
        rest.append(genre)
print("Reste", len(rest), "a traiter")
print("Total restant + traité / Total existant:", len(rest)+len(treated), "/", len(lvl1))
print("Typo sur les genres traités:", list(set(treated) - set(lvl1)))
print("Genres non triés:", rest)
