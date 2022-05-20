# Colorado Crime Analysis
> Analyzing crime data by county for Denver Police, with a focus on education and area demographics

<table>
    <tr>
        <td>Anna Jackson</td>
        <td>Sonia Romero</td>
        <td>Ryan Young</td>
    </tr>
    <tr>
        <td>Connor McWilliams</td>
        <td>Brett Boos</td>
        <td></td>
    </tr>
</table>

<br>

## [<img src="https://github.com/ryayoung/icons/blob/main/svg/stack.overflow.blue.svg" height="25"/> &nbsp; Data Sources &nbsp; <img src="https://github.com/ryayoung/icons/blob/main/svg/chevron.right.blue.svg" height="18"/>](source_data/README.md)
- Retrieved from **Socrata Open Data API** under the `data.colorado.gov` endpoint

## [<img src="https://github.com/ryayoung/icons/blob/main/svg/funnel.blue.svg" height="25"/> &nbsp; Prepared Data &nbsp; <img src="https://github.com/ryayoung/icons/blob/main/svg/chevron.right.blue.svg" height="18"/>](prepared_data)
- Modified/engineered datasets to use in analyses

## [<img src="https://github.com/ryayoung/icons/blob/main/svg/bar.chart.line.blue.svg" height="25"/> &nbsp; Visualization &nbsp; <img src="https://github.com/ryayoung/icons/blob/main/svg/chevron.right.blue.svg" height="18"/>](visualization)
- Initial visualizations to better understand data prior to analysis
- Final visualizations to communicate key findings and model results

## [<img src="https://github.com/ryayoung/icons/blob/main/svg/gear.blue.svg" height="25"/> &nbsp; Models &nbsp; <img src="https://github.com/ryayoung/icons/blob/main/svg/chevron.right.blue.svg" height="18"/>](models)
- Predicting crime rates with **multilinear regression**
- Clustering counties based on a holistic view of crime activity

## [<img src="https://github.com/ryayoung/icons/blob/main/svg/easel.blue.svg" height="25"/> &nbsp; Presentation &nbsp; <img src="https://github.com/ryayoung/icons/blob/main/svg/chevron.right.blue.svg" height="18"/>](presentation)
- Key findings and interpretations
- Presentation slide deck for Denver Police

<br>
<br>



---
# DOCUMENTATION
---

1. [**Research Framing and Understanding**](#part1)
2. [**Data Preparation and Analysis Overview**](#part2)
3. [**Analysis Execution and Result Interpretation**](#part3)

> Slide deck PDF of final presentation can be found in the `/presentation` directory [**here**](presentation).


<br>
<a id='part1'></a>

# _Research Framing and Understanding_
**Focus**
> Using the crime datasets available, we are exploring the age range of K-12 (where age < 19) for insight on what type of crimes this age group commits (offense category name) along with where (county name) and when (incident date, incident hour) these crimes occur. We will then tie in various outside data sources in order to apply intricate reasoning and rationale behind the “why”, “where” and “when” these crimes occur by this age range.  

**Business Purpose**
> The business purpose of our project is to equip the Colorado State Police Department with brand new key information on the “why”, “when” and “where” crimes that are occurring by our defined age range (K-12 students) for them to enact mitigation and prevention strategies in order to preserve the safety of Colorado residents.

<br>

## Research Questions

#### Crime based on demographics
1. Is there a common set of crimes that our defined age range is committing? 
2. Does seasonality play a part in where the crimes are more likely to occur by our defined age range? (e.g., are crimes more likely to occur in the summer months when school is out?) 
3. Which district possesses the highest/lowest crime rates by our defined age range? 

#### Crime based on education statistics
1. Do districts that see a higher/lower mobility rate also see a higher/lower crime rate by our defined age range?  
2. Do districts with a higher/lower gifted and talented student population also see higher/lower crime rates by our defined age range? What about migrant students, disabled students, English learners, homeless students, or economically disadvantaged student populations? 

<br>

## Review of Previous Findings

- [National Profile of US Public High School Crime Patterns](https://www2.ed.gov/offices/OUS/PES/studies-school-violence/school-crime-pattern.pdf)
  - Reveals key patterns in high school crime that we could potentially seek out in our datasets  
- [Colorado School Violence Prevention and Student Disipline Manual](https://www.cde.state.co.us/sites/default/files/documents/fedprograms/dl/ov_tiv_res_coloschviol.pdf)
  - Provides an understanding of what current measures are being taken to prevent and mitigate crime 

<br>

## Data Collection
> Data will be collected from the state of Colorado using Socrata’s API’s data.colorado.gov endpoint.

#### Crimes in Colorado
- At the core of our analysis, we will be using the 2016-2019 crime data that was given to us in our capstone class. Additionally, we will use the 1997-2015 version of that same data to better understand changes and patterns over time.

#### District Student Mobility/Stability Statistics for 2011-2012
- This dataset will be used to answer questions about student homelessness and other student populations (noted below) from the 2011-2012 school year. This 184-row dataset is aggregated by school year and school district and includes rows for state totals. It contains 60 columns, with aggregations on pupil count, stable student count, stability, mobility, instances for mobility, and mobility incidence for the following student populations: students with disabilities, English language learners, economically disadvantaged, migrant students, title 1 students, homeless students, and gifted & talented students. [This online resource](http://www.cde.state.co.us/cdereval/mobility-stabilitycurrent) explains how the rates are calculated.  

<br>
<a id='part2'></a>

#
# _Data Preparation and Analysis Overview_

> Central to our research will be a **linear regression model** that predicts crime rate for an area based on its demographics and school systems. Additionally, we intend to conduct clustering analyses to group counties together based on factors that might necessitate different approaches or strategies of law enforcement, though it’s unclear what those factors will be. 


## Hypotheses
> These hypotheses highlight our predictions on how certain variables will contribute to the success of our model. 

#### Education
- Student **stability rate** will significantly, negatively, predict certain types of crime, such as violence and gang-related activity. 
- The percentage of adults in a county who don’t have a **high school diploma** should significantly predict crime rates. 
- The percentage of **grade-school-enrolled** students who are in **grades 9-12** should significantly predict crime rates; when the number of high-school students falls below the **expected mean** for a county, this indicates a higher rate of students dropping out, which may predict crime. 
- **Mobility/stability rates** of **economically disadvantaged** students might be able to explain cases in which a county has **lower** crime rates than expected/predicted by our models. In poor areas, an unexpectedly high stability rate might indicate that the school system or local government has been effective in giving disadvantaged students the support they need to succeed. It’s possible that mobility/stability rates will be mostly dependent upon **population density** (less mobility in rural areas), so we may need to alter the mobility rates to correct for population density. 

#### Demographics
- The ratio of **number of households** to **total population** in a county will significantly predict crime rates. A lower number of households might indicate higher rates of drug-related crimes and homelessness. 
- The standard deviation of **owner-occupied housing unit** prices may significantly predict crime. If so, this might be due to a variety of reasons, such as police forces favoring higher-income areas within a county and neglecting others. 
- The percentage of **vacant housing units** in a county should significantly predict certain types of crime, such as violence or drug use. 
- The percentage of **U.S. born**, **out-of-state**, residents should negatively predict crime rates in an area, as this is a sign of tourism. 
- The percentage of **owner-occupied housing units** which are valued at less than **$50,000** should predict crime in an area. 
- The percentage of **below-poverty-line residents** who are under the age of **18** may significantly predict certain types of crime, such as violence or gang-related activities. 

<br>

## Variables
> We aim to focus on crime at the **county** level. A county column has been created for all datasets which did not have one (converted police district to county, and school district to county). 

#### Targets
- Predict overall crime rate, given a county 
- Predict crime rate for each category of crime, given a county 
- Predict juvenile crime rate, given a county 
- Datasets: `crime_16_19`, `crime_97_15`, `dist_arrests`

#### Predictors
- County demographics (33 of 157 continuous columns selected) 
- Crime demographics – age, gender, year (from crime datasets above) 
- Education demographics – (enrollment, graduation, mobility, stability) 
- Datasets: `dist_student_mobility`, `dist_grad_rate`, `county_demographics`

<br>

## Data Preparation and Integration
> Standardizing the geographic location granularity across all datasets was the biggest technical challenge in our data preparation. In their raw form, not a single pair of datasets could be merged, nor could comparisons be made across groups. Each dataset was indexed by either county, or a district-related field, but naming conventions for such fields were not standardized. The following steps were taken to ensure that each dataset could be aggregated by county.

#### Standardize and combine crime records across the 97-15 and the 16-19 `Crimes in Colorado` data
- County naming conventions differed across datasets. The old crime data used `primary_county`, whereas the new data included both the primary and secondary county in a single string. These were modified to remove the secondary county. 
- Police department naming conventions differed across datasets. These were standardized. 
- Crime data from State Patrol and Colorado Bureau of Investigation were removed. 
- The 97-15 and 16-19 crime datasets were concatenated into a single table. 

#### Add county to the aggregate crime rate datasets (`Crime Arrests`, `Crime Offenses`)
- Unique police departments and counties were retrieved from crime records from the previous step, to use for string matching. 
- The two aggregated crime datasets have different naming conventions for police department, so they were first modified to use the same names as each other and were further modified to use the same names as the crime records data from the previous step. 
- Finally, the county column was merged in. 


#### Add county to education datasets (`Student Mobility/Stability`, `Graduation Rate`)
- The Student Mobility data does not provide a county column, but the Graduation Rate data does. This column was merged into the Student Mobility data.

#### Pivot and aggregate the `County Population` dataset
- This dataset has nearly 400,000 rows despite being aggregated already. It offers a separate row for each individual age, for each county, for each year. First, the data was aggregated into two age groups (minor, adult).
- Next, the age range column was eliminated, and the data was pivoted to be indexed by county and year to remove redundancy. The new format is better for models and analysis, whereas the unpivoted format is better for creating charts.

<table>
    <tr>
        <td> <img width="200" alt="Screen Shot 2022-05-16 at 4 50 38 PM" src="https://user-images.githubusercontent.com/90723578/168773427-de4c1aa7-bb5e-4ae2-8185-507bf4d52fce.png"> </td>
        <td> <img src="https://github.com/ryayoung/icons/blob/main/svg/arrow.right.svg" height="25"/> </td>
        <td> <img width="300" alt="Screen Shot 2022-05-16 at 4 51 26 PM" src="https://user-images.githubusercontent.com/90723578/168773412-722b5a2f-21fa-4948-b8f3-1ef9d2c3efc0.png"> </td>
    </tr>
</table>


#### Demographic Data (`Census Counties Colorado` for 2012, and 2019): Select variables, group categories together
- The census data contains roughly 150 variables. We selected the 33 variables which seemed most useful. The Census Field Descriptions dataset from Socrata was used to interpret variables. 
- The 8 columns for race were reduced to: [hispanic, white, black, other]. 
- Housing price distributions were described by 11 bins. We reduced these to 6 bins. 



<br>

## Analytic Techniques

#### Descriptive Analysis

- Once the data has been prepared, we will create an initial set of visualizations to better understand the data. This will include correlation matrices, histograms, and time series plots. Additional visualizations will be created once the research is complete, to communicate key findings.

#### Multilinear Regression
- We aim to predict the overall crime rate in an area based on education and census data. In a practical setting, this model is intended to be used when future predictions have been made about general statistics/demographics in an area (i.e. estimated population growth, etc.), and a prediction must be made for how crime rates will respond to such changes.

#### Clustering
- In addition to forecasting and predictions, it’s also desirable to create models that help law enforcers better understand what makes their area/county different. Therefore, we intend to create one or more clustering analyses to place counties into categories that differ in ways that are most meaningful to local police departments. For instance, in each cluster, law enforcement agencies might wish to take different approaches to the following: who to hire, where to direct manpower, how to charge violators in certain situations, how to interpret risk in certain situations, effective scheduling, etc.



<br>
<a id='part3'></a>

#
# _Analysis and Interpretation_
> The models our team intends to use include the analytical techniques mentioned above. We are currently in the process of creating our analytical models. Once completed, we will fill in the missing information for the rest of this section, as well as update our Reproducibility documentation files (PDF and Excel). Below are our plans for the section. 

## Model Design and Execution

#### Model Execution
- The Python file will have the Descriptive Analysis, Multilinear Regression, and Clustering models. With descriptive analysis, we will be able to better understand the data and find patterns that we see significant in predicting and mitigating crime. 
- Model details such as type, variables, predictors, and results will be included here. 

#### Analytical Results
- The results of the model will be analyzed here in terms of observations and statistical significance 
- Analysis of the results in terms of business or focus context will be added here along with any additional details or screenshots.  

#### Visualizations
- All visualizations with detail labeling, description, and analysis will be added here. 
- Visualization may be outputted from sources other than Python, such as Tableau or Power BI, whichever we deem most appropriate to best display our findings. 

<br>

## Results/Findings
> All model findings will be described here. Overall findings about crime for our target age group will be described here.

<br>

## Interpretations and Recommendations
> The interpretations of the model and analysis in terms of our focus, and business recommendations, will be described here. This will be more focused on ‘business’ understanding rather than statistical understanding. 

