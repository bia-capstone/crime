This code takes the original Arrests by District (dist_arrests)
and Crime by District (dist_crime) datasets and adds a county
column to them.

This was done using the 1997-2015 Colorado Crime data, which has
police district and county columns. The police districts in that
data follow very different naming conventions. Some text manipulation
was needed to make them match the districts in the newer district
crime/arrests datasets.