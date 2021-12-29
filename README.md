# Sleep Analysis
Are you getting adequate sleep?

### Images
[Sleep Analysis Dashboard](https://public.tableau.com/app/profile/misty.tomison/viz/SleepAnalysis_16403125127800/SleepAnalysis?publish=yes)

Weeks 1 and 2

Square: Misty, Danny
Circle: Megan, Misty
Triangle: Laura, Laura
X: Jordan, Megan
Float: Danny, Jordan



# Sleep_Analysis

How well rested will I be?

## Overview
This project analyzes sleep data collected from Sleep Cycle iOS App in order to determine what contributes to good sleep. Factors examined are caffeine consumption, physical activity, heart rate, and length of time sleeping. We will use machine learning models to predictt if a person will have good or poor sleep based on these factors.

## Content

- Selected topic

  Sleep Study
  
- Reason why they selected their topic
  
  The information is truly valuable with a broad scope of application
  
- Description of their source of data
  
  Sleep Cycle iOS App 
  metrics of caffeine consumption, physical activity, heart rate, and length of time sleeping
  
- Questions they hope to answer with the data

  Which behaviors contribute to quality sleep?
  
  How does one quantify "good sleep"?
  
## Description of the communication protocols:
All communications are done via Slack, Github branch push/pull/merges for each project team member, and during live class times.

## Provisional machine learning mode:
Preliminary data preprocessing originally limited our usable data to only 162 rows. We have decided to make our target the Sleep Quality feature as it is more outcomes to predict. This change in plan required more preprocessing. A df_tranformed.csv has been generated where all features are in the form of a 1 or 0, allowing for model functionality and keeping 887 complete rows of data.  

Before deciding to switch our target we were planning to predict an emoji symbol that represents the mood one should wake up in based upon other features.
This limited our data-frame to only 162 rows, and only one of two outcomes. After some deliberation it made more sense to drop that column and try to predict Sleep Quality on a scale of 1-100. Models have been started.

## Main Branch / Slides / Charts

Main branch currently has folders and files that access Google Slides presentation draft. Theme, images graphs and charts have been loaded onto Tableau Dashboard.
Some models have been created, more are needed. An index.html file has been created for the end user. It is not yet functional. A presentation outline has been created.
