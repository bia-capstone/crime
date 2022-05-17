This code further processes the Arrests by District (dist_arrests)
and Crime by District (dist_crime) datasets, from 2001-2016.
It STARTS with a version of those datasets that has a county
column added, then does the following:

- The original datasets had a 'type' column for crime type.
  So, each police department & year combo would get duplicated
  nearly 30 times, one row for each crime type. I've pivoted The
  dataframes so that there is now a separate column for each
  crime type.

- Arrest data has been separated into juvenile, adult, and totals

- Crime data doesn't have adult/juvenile columns, only totals