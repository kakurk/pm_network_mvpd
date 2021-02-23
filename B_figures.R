# Analyze the homogeneity of our ROIs

library(tidyverse)
library(magrittr)

# load
df <- read_csv(file = 'roi_homogeneity.csv', col_types = cols())

# tidy
df %<>% 
  pivot_longer(cols = var_expl_pc1:var_expl_pc23, 
               names_to = 'PC', 
               values_to = 'var_expl', 
               names_prefix = 'var_expl_')
  
# figure
ggplot(data = df, mapping = aes(x = roi, y = var_expl, group = subject)) +
  stat_summary(geom = 'point', fun.data = 'mean_se', alpha = .4) +
  stat_summary(geom = 'line', fun.data = 'mean_se', alpha = .2) +
  stat_summary(aes(group = NULL), geom = 'crossbar', fun.data = mean_se, width = .2, fill = 'gray') +
  facet_grid(.~PC) +
  labs(x = 'ROI', y = 'Proportion Variance Explained') -> p

print(p)
