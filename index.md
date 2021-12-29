# Sleep Analysis
## Overview
This project analyzes sleep data collected from Sleep Cycle iOS App in order to determine what contributes to good sleep. Factors examined are caffeine consumption, physical activity, heart rate, and length of time sleeping. We will use machine learning models to predictt if a person will have good or poor sleep based on these factors.

### Questions to answer with the data

> Which behaviors contribute to quality sleep?
> How does one quantify "good sleep"?
> What will my sleep quality be?
> How well rested will I be?

## [Presentation](https://github.com/mtomison/Sleep_Analysis/blob/87e52ae2c04c7f6e4d39e198b6799acf30284674/Sleep%20Analysis%20Deliverable%202%20Draft%20v2.pdf)

### Content
- Selected topic

  Sleep Study
  
- Reason for topic selection
  
  The information is truly valuable with a broad scope of application
  
- Description of source data
  
  Sleep Cycle iOS App 
  metrics of caffeine consumption, physical activity, heart rate, and length of time sleeping
  
- Questions to answer with the data

  Which behaviors contribute to quality sleep?
  
  How does one quantify "good sleep"?


## [Machine Learning Model](https://github.com/mtomison/Sleep_Analysis/blob/4d5ef2822083da144fef9e1293622215375d8374/Machine%20Learning.md)
> Initially: RandomForest; RandomForest was not useable because there is not enough data. We ended up with 887 records, so we concluded that the best machine learning model is...

[Preprocessing Jupyter Notebook](sleepDataPreprocessing.ipynb)

## Database
- Description of source data
  
  Sleep Cycle iOS App 
  metrics of caffeine consumption, physical activity, heart rate, and length of time sleeping
  
  [Schema](https://github.com/mtomison/Sleep_Analysis/blob/d4f4f5e70c98f9fe5b5c7734a78d91e9b74008f0/Schema.jpg)

## [Dashboard](https://public.tableau.com/app/profile/misty.tomison/viz/SleepAnalysis_16403125127800/SleepAnalysis?publish=yes)
### Visualizing the Data with Tableau:

1. [Wake Up](https://public.tableau.com/app/profile/megan.speaks/viz/WakeUp/WakeUp)
2. [Sleep Notes](https://public.tableau.com/app/profile/megan.speaks/viz/SleepNotes/SleepNotes)
3. [Activity](https://public.tableau.com/app/profile/megan.speaks/viz/Activity_16405816723450/Activity)
4. [Time in Bed](https://public.tableau.com/app/profile/megan.speaks/viz/TimeinBed/TimeinBed)
5. [Heart Rate](https://public.tableau.com/app/profile/megan.speaks/viz/HeartRate_16405815842860/HeartRate)

## Description of the communication protocols:

