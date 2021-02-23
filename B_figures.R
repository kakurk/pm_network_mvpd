# Analyze the homogeneity of our ROIs

library(tidyverse)

df <- read_csv(file = 'roi_homogeneity.csv', col_types = cols())

ggplot(data = df, mapping = aes(x = roi, y = var_expl, group = subject)) +
  stat_summary(geom = 'point', fun.data = 'mean_se', alpha = .4) +
  stat_summary(geom = 'line', fun.data = 'mean_se', alpha = .2) +
  stat_summary(aes(group = NULL), geom = 'crossbar', fun.data = mean_se, width = .2, fill = 'gray') +
  labs(x = 'ROI', y = 'Homogeneity',
       caption = 'Homoggeneity = % variance explained by first PC') -> p

print(p)