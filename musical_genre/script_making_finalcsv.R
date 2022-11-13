library(tidyverse)
library(stringr)
path <- './Documents/SI5/Cours/DataVisualisation/'
artists <- read.csv(paste(path, 'wasabi_artists.csv', sep=''))
artists <- artists %>% select(X_id, name, locationInfo) %>% filter(locationInfo != "[]")
artists[c('Country', 'Region', 'City')] <- str_split_fixed(artists$locationInfo, ',', 3)
artists$Country <- gsub("\\[", "", artists$Country)
artists$Country <- gsub("\\\"", "", artists$Country)
artists$Country <- gsub("\\]", "", artists$Country)
artists$Region <- gsub("\\\"", "", artists$Region)
artists$Region <- gsub("\\]", "", artists$Region)
artists$City <- gsub("\\\"", "", artists$City)
artists$City <- gsub("\\]", "", artists$City)
artists <- artists %>% mutate_all(na_if, "") 
artists <- artists %>% select(X_id, name, Country, Region, City)
colnames(artists)[1] <- "id_artist"
colnames(artists)[2] <- "name_artist"
colnames(artists)[3] <- "country_artist"
colnames(artists)[4] <- "region_artist"
colnames(artists)[5] <- "city_artist"

albums <- read_csv(paste(path, 'wasabi_albums.csv', sep=''))
albums <- albums %>% filter( explicitLyrics == TRUE & !is.na(genre)) %>% select("_id", "id_artist", "genre")
colnames(albums)[1] <- "id_album"
colnames(albums)[2] <- "id_artist"
colnames(albums)[3] <- "genre_album"

merged = merge(x = artists, y = albums, by = "id_artist")

songs <- read.csv(paste(path, 'wasabi_songs.csv', sep=''), header = TRUE, sep = "\t")
songs <- songs %>% select("X_id","id_album")
colnames(songs)[1] <- "id_song"
colnames(songs)[2] <- "id_album"

final <- merge(x = merged, y = songs, by = "id_album")
write.csv(final, paste(path, 'final.csv', sep=''), row.names = TRUE)
