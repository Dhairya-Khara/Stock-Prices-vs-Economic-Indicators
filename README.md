# Stock-Prices-vs-Economic-Indicators
This project analyzies the Impact of COVID-19 on the Correlation Between Classic Economic Indicators and Monthly Median Stock prices.

## Introduction
The COVID-19 pandemic has impacted the lives of people across the world.
Industries from energy to healthcare have undergone drastic changes because of the pandemic. The New York Stock
Exchange (NYSE) has experienced unparalleled growth during the pandemic, despite many industries being negatively impacted by the pandemic, 
American federal debt being higher than ever, and there being abnormally high
uncertainty about everything (Bloomberg).

The US experienced grave unemployment during the first couple months of the pandemic, yet many speculate
that the outflow of stimulus checks, the less busy schedules of individuals, and the ease with which one can access
the stock exchange through apps like Robinhood has led to this unexpected growth. Investors have put more money
into stocks in the last 5 months than in the previous 12 years combined (CNBC). The average consumer spending
patterns have grown to include investments in the stock market. The S&P 500 gained more than 16 percent in 2020,
a very strong return during a year of nationwide lock downs and steep job losses in the United States (Washington
Post).

Altogether, so far, the stock market during the pandemic can be summarised in one word: unexpected. Classic
economic indicators such as unemployment rate and number of unemployed persons per job opening have been used
as predicting factors for the stock exchange throughout history (Allen). However, during the pandemic, each indicator
experienced extreme swings unlike anything in recent history. This led us to question the difference in the correlation
between median monthly stock prices and classic economic indicators between August 2018 to December 2019 (a
period of seventeen months before COVID-19 began) versus the seventeen months during the peak of COVID, from
April 2020 to August 2021.

Since the pandemic could not have been predicted, we want to know whether the median monthly NYSE price
action’s correlation to unemployment rates and unemployed per job opening statistics was impacted by COVID-19.
This project will attempt to answer the research question: **How has the COVID-19 pandemic impacted the
correlation between median monthly stock prices and the classic economic indicators of Unemployment Rates and Number of Unemployed Persons per Job Opening?**

## Dataset Description

**Historical Stock Data** <br />
Historical stock data will be collected from Yahoo Finance using their public API. This API returns a csv file
upon request. The csv file that we receive contains the ”Opening”, ”High”, ”Low”, ”Closing, Adj.”, ”Close” and
”Volume” of that stock for each date in the specified time period. Data will be collected from August 2018 to
December 2019 for the analysis of the correlation before COVID-19 began and data will be collected from April 2020 to August 2021 for the analysis of the correlation during COVID-19.

**Monthly Unemployment Statistics of the US** <br />
The monthly unemployment statistics of the US was found from the [US Bureau of Labor Statistics (“Civilian
unemployment rate”)](https://www.bls.gov/charts/employment-situation/civilian-unemployment-rate.htm). This data is used to create a custom .xlsx file and stored in the local directory of the program.
This file will have two sheets, with the first sheet (named “Before”) representing the data before COVID-19 began
(August 2018 to December 2019), and the second sheet (named “COVID”) representing the data during COVID-19
(April 2020 to August 2021).

**Number of Unemployed Persons per Job Opening by Month in the US** <br />
The monthly number of unemployed persons per job opening in the US was found from the [US Bureau of Labor
Statistics (“Number of unemployed persons...”)](https://www.bls.gov/charts/job-openings-and-labor-turnover/unemp-per-job-opening.htm). This data is used to create a custom .xlsx file and is stored in the
local directory of the program. This file will also have two sheets, with the first sheet (named “Before”) representing
the data before COVID (August 2018 to December 2019), and the second sheet (named “COVID”) representing the
data during COVID (April 2020 to August 2021).

## Getting Started
After cloning the repository, install all the required dependencies using pip.
```bash
pip install -r requirements.txt
```
Run the main.py file. Make sure to ’Run’ the file and not ’Run file in Python Console’.

Recommended calls to type into the interactive search bar are TSLA, AMZN, VGT, NFLX, VHT, and
VDE or any other stock ticker of your choice.

## Results and Analysis
**How has the COVID-19 pandemic impacted the correlation between median monthly stock prices
and the classic economic indicators of Unemployment Rates and Number of Unemployed Persons per
Job Opening?**

To answer this research question we will investigate three stock indexes. These indexes are the Vangaurd Information Technology Index Fund ETF (VGT), Vangaurd Healthcare Index Fund ETF (VHT), and Vangaurd Energy
Index Fund ETF (VDE).

<!-- ![VGT Index](https://i.ibb.co/Z6QzHzr/VGT.png) -->
<p align="center">
  <img 
    src="https://i.ibb.co/Z6QzHzr/VGT.png"
  >
</p>
<h5 align="center"> Figure 1: VGT Index </h5> 
From the graphs above we can see that the unemployment rate vs the median monthly stock price before COVID19 has a correlation coefficient of 0.77 which indicates a moderately strong positive correlation compared to 0.85
for the R<sup>2</sup> value of the unemployment rate during COVID-19 vs the median monthly stock price before COVID-19. This means COVID-19 did not have a particularly meaningful impact on the strength of the correlation between
technology stocks and unemployment rates. As for the correlation between unemployed per job opening vs median
monthly stock prices, before COVID-19 there was a 0.02 R<sup>2</sup>
correlation and during COVID-19 there was an R<sup>2</sup> value
of 0.85. This means COVID-19 heavily impacted the correlation between unemployed per job opening and median
monthly stock prices for technology stocks. <br /> <br />


<p align="center">
  <img 
    src="https://i.ibb.co/w7RJZmW/VHT.png"
  >
</p>
<h5 align="center"> Figure 2: VHT Index </h5> 
From the graphs above we can see that the unemployment rate vs the median monthly stock price before COVID19 has a correlation coefficient of 0.25 which indicates a weak positive correlation compared to 0.74 for the R<sup>2</sup> value
of the unemployment rate during COVID-19 vs the median monthly stock price before COVID-19. That means
COVID-19 had an impact on the strength of the correlation between healthcare stocks and unemployment rates. As
for the correlation between unemployed per job opening vs median monthly stock prices, before COVID-19 there
was a 0.04 R<sup>2</sup>
correlation and during COVID-19 there was 0.75 R<sup>2</sup> value. This means COVID-19 heavily impacted
the correlation between unemployed per job opening and median monthly stock prices for healthcare stocks. <br/> <br />


<p align="center">
  <img 
    src="https://i.ibb.co/kJ4w6hH/VDE.png"
  >
</p>
<h5 align="center"> Figure 3: VDE Index </h5> 
From the graphs above we can see that the unemployment rate vs the median monthly stock price before COVID-19 has a correlation coefficient of 0.13 which indicates a weak positive correlation compared to 0.35 for the R<sup>2</sup> value
of the unemployment rate during COVID-19 vs the median monthly stock price before COVID-19. That means
COVID-19 did have an impact on the strength of the correlation between energy stocks and unemployment rates.
However, both of these correlations are weak and hence we can deduce from the data that in general unemployment
rates does not impact energy stocks in the same way it impacts technology and healthcare stocks. As for the correlation between unemployed per job opening vs median monthly stock prices, before COVID-19 there was a 0.01
R<sup>2</sup>
correlation and during COVID-19 there was 0.4 R<sup>2</sup> value. Once again, this means COVID-19 had an impact on
the correlation between median monthly energy stock prices and unemployed per job openings, but the correlation
is still not statistically significant.

## Limitations
The primary limitation that we encountered with the data set, was that data for all of our independent variables
was only available based on months, while the data with regards to the stock price is only available on a daily basis.
Thus in order to solve this problem, we converted the daily stock data into monthly stock data by taking the median
stock price of each month. The primary limitation with this is that the median stock price cannot accurately consider all the fluctuations that occur during a month, and cannot represent the month as a whole on an accurate basis.

## Conclusions
Altogether, COVID-19 most greatly impacted the correlation between unemployed per job opening statistics and
the median monthly stock price for all three indices of stocks: technology, healthcare and energy. The index which
showed the least impact by COVID-19 was the VDE energy index. This might be because energy companies’ stocks
are more impacted by factors such as government policies and price elasticity of demand. Ultimately, there is a clear
impact of COVID-19 on the correlation between unemployment rates and median monthly stock prices, as well as,
unemployed per job opening and median monthly stock prices.

## Further Investigation
In regards to further exploration, we could identify more classic economic indicators and not only compare the
correlation between before and during COVID, but we could also compare the classic economic indicators against each
other to identify which indicator correlates the best with the different categories of stocks (technology, healthcare,
education etc.) before and during COVID. Furthermore, our investigation focused on the United States, using stocks
only listed on the NASDAQ, therefore we could further our investigation by getting stock information from other
stock exchanges to include statistics from other countries. Then we could analyse the correlation by country as well
to possibly uncover other trends in the impact of COVID-19 on the correlations between stock price predictors and
stock prices.















