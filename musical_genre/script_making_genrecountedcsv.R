# library
library(tidyverse)
library(stringr)

datas <- read.csv('./Documents/SI5/Cours/DataVisualisation/final.csv')

group <- datas %>% group_by(genre_album) %>% summarise(total_count=n(),.groups = 'drop')

write.csv(group, './Documents/SI5/Cours/DataVisualisation/genre_counted.csv', row.names = TRUE)