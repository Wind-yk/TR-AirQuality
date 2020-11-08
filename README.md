# TR - Qualitat de l'aire

 Code used to extract data graphics and tables by using data collected by `Smart Citizen Kit` (data not incuded in this repository), installed in a high school in Barcelona.
 
## Files

 * **`Analisi de dades.ipynb`**: notebook with code to obtain the stadistics and plots.
 * **`utils.py`**: defined methods to facilitate the extraction and classification of data.

## Background

  There are two `.csv` files (not in this repository), containing outdoor and indoor air quality data for 4 weeks, respectively.
  
  The aim is twofold:
  * to generate comparison plots for indoor and outdoor data for each defined parameter by weeks, such as `PM10` or `eCO2` concentracions.
  * to generate concentration tables defined by the schedule of high school; i.e. for each lesson, the respective concentration.
     
  These plots and tables are generated for further analysis.
     
## Comment

   The code is written without further purposes, so it is of low quality by means of its maintainability; even though, I tried to make it comprehensive and usable for different inputs.
