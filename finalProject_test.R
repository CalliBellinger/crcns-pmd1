library(ggplot2)
library(tidyverse)
library(dplyr)
library(knitr)

#reading in data and removing unnecessary column
compneuro_df <- read.csv("compneuro_final.csv", header=TRUE, stringsAsFactors = FALSE)
compneuro_df <- compneuro_df[,-1]

###
#uses Tidyverse to spread CellID into long format
compneuro.wide <- spread(compneuro_df, key= cell_id, value = pre_movement_rate)
compneuro.wide <- compneuro.wide[,-57]
#creates dataframes that contain the response variable as well as the neuronal firing rates accross trials
compneuro_speed <-compneuro.wide[,c(1,7:99)]
compneuro_theta <- compneuro.wide[,c(2,7:99)]
compneuro_len_x <- compneuro.wide[,c(4,7:99)]
compneuro_len_y <- compneuro.wide[,c(5,7:99)]
compneuro_reach_len <- compneuro.wide[,c(6:99)]

#creates linear models using the 94 predictor variables for certain response variables to test the R squared
lm_speed <- lm(reach_speed ~ ., data = compneuro_speed)
lm_len_x <- lm(Reach_x ~ ., data = compneuro_len_x)
lm_len_y <- lm(Reach_y ~ ., data = compneuro_len_y)
lm_reach_len <- lm(reach_len ~ ., data = compneuro_reach_len)

#summary statistics for the models
summary(lm_len_y) #R^2: .76
summary(lm_len_x)#R^2: .82
summary(lm_speed)#R^2: .40
summary(lm_reach_len)#R^2: .47
##################
#gets coefficient data from Linear models
Summary_lm_x <- summary(lm_len_x)$coef[,c(1,4)]
Summary_lm_y <- summary(lm_len_y)$coef[,c(1,4)]

####### plotting
#####Cell 74 #####
#creates DF for just cell 74 X Reach
cell74_reach_x <-compneuro.wide[,c(4,79)]
#Plots Regression
ggplot(cell74_reach_x, aes(x=Reach_x, y=`74`)) + geom_point() +
  geom_smooth(method='auto', se=FALSE, colour="red") + ylab('Firing Rate (SpikesPer Second)') +
  xlab('X Component of Reach Movement (cm)') +ggtitle('X Component of Reach Movement and Firing Rate in Cell 74') +theme(plot.title = element_text(hjust = 0.5)) + 
   coord_fixed()

#creates DF for just cell 74 Y Reach
cell74_reach_y <-compneuro.wide[,c(5,79)]
#Plots Regression
ggplot(cell74_reach_y, aes(x=Reach_y, y=`74`)) + geom_point() +
  geom_smooth(method='auto', se=FALSE, colour="red") + ylab('Firing Rate (Spikes Per Second)') +
  xlab('Y Component of Reach Movement (cm)') +ggtitle('Y Component of Reach Movement and Firing Rate in Cell 74') +theme(plot.title = element_text(hjust = 0.5)) + 
  coord_fixed()

##### Cell 29 #######
#creates DF for just cell 21
cell29_reach_y <-compneuro.wide[,c(5,35)]
#Plots Regression
ggplot(cell29_reach_y, aes(x=Reach_y, y=`29`)) + geom_point() +
  geom_smooth(method='auto', se=FALSE, colour="red") + ylab('Firing Rate (Spikes Per Second)') +
  xlab('Y Component of Reach Movement (cm)') +ggtitle('Y Component of Reach Movement and Firing Rate in Cell 29') +theme(plot.title = element_text(hjust = 0.5)) + 
  coord_fixed() + xlim(-5,12)
##### Cell 42 #######
cell42_reach_y <-compneuro.wide[,c(5,48)]
#Plots Regression
ggplot(cell42_reach_y, aes(x=Reach_y, y=`42`)) + geom_point() +
  geom_smooth(method='auto', se=FALSE, colour="red") + ylab('Firing Rate (Spikes Per Second)') +
  xlab('Y Component of Reach Movement (cm)') +ggtitle('Y Component of Reach Movement and Firing Rate in Cell 42') +theme(plot.title = element_text(hjust = 0.5)) + 
  coord_fixed() 

cell42_reach_x <-compneuro.wide[,c(4,48)]
#Plots Regression
ggplot(cell42_reach_x, aes(x=Reach_x, y=`42`)) + geom_point() +
  geom_smooth(method='auto', se=FALSE, colour="red") + ylab('Firing Rate (Spikes Per Second)') +
  xlab('X Component of Reach Movement (cm)') +ggtitle('X Component of Reach Movement and Firing Rate in Cell 42') +theme(plot.title = element_text(hjust = 0.5)) + 
  coord_fixed() 
########