[<img src="https://github.com/ryayoung/ryayoung/blob/main/Buttons/symbol/arrow.left.blue.svg" height="30"/>](https://github.com/bia-capstone/crime)



# <img src="https://github.com/ryayoung/ryayoung/blob/main/Buttons/symbol/stack.overflow.svg" height="32"/> &nbsp; Data Sources
> All data was retrieved from the [Socrata Open Data API](https://dev.socrata.com/)'s `data.colorado.gov` endpoint. We used the [crime](https://pypi.org/project/crime/) package to explore, load, describe, and generate documentation for all datasets.


<table>
  <thead>
    <tr>
       <th>Name</th> <th>Full Name</th> <th>Columns</th> <th>Rows</th> <th>From</th> <th>To</th> <th>Indexed By</th> <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>crime_16_19</td>
      <td><a href="https://github.com/bia-capstone/crime/tree/main/source_data/crime_16_19.md">Crimes in Colorado</a></td>
      <td>9</td> <td>1851996</td> <td>2016</td> <td>2019</td> <td>Police Dept + County</td>
      <td><a href="https://dev.socrata.com/foundry/data.colorado.gov/j6g4-gayk"><img src="https://github.com/ryayoung/ryayoung/blob/main/Buttons/symbol/link.45deg.blue.svg" height="22"/></a></td>
    </tr>
    <tr>
      <td>crime_97_15</td>
      <td><a href="https://github.com/bia-capstone/crime/tree/main/source_data/crime_97_15.md">Crimes in Colorado 1997 to 2015</a></td>
      <td>10</td> <td>4952282</td> <td>1997</td> <td>2015</td> <td>Police Dept + County</td>
      <td><a href="https://dev.socrata.com/foundry/data.colorado.gov/6vnq-az4b"><img src="https://github.com/ryayoung/ryayoung/blob/main/Buttons/symbol/link.45deg.blue.svg" height="22"/></a></td>
    </tr>
    <tr>
      <td>dist_arrests</td>
      <td><a href="https://github.com/bia-capstone/crime/tree/main/source_data/dist_arrests.md">Crime Arrests by Police District 2001-2016 in Colorado</a></td>
      <td>5</td> <td>93114</td> <td>2001</td> <td>2016</td> <td>Year -&gt; Police Dept -&gt; Crime Type</td>
      <td><a href="https://dev.socrata.com/foundry/data.colorado.gov/2e5i-5hfy"><img src="https://github.com/ryayoung/ryayoung/blob/main/Buttons/symbol/link.45deg.blue.svg" height="22"/></a></td>
    </tr>
    <tr>
      <td>dist_student_mobility</td>
      <td><a href="https://github.com/bia-capstone/crime/tree/main/source_data/dist_student_mobility.md">District Student Mobility/Stability Statistics for 2011-2012 by Instructional Program/Service Type</a></td>
      <td>60</td> <td>184</td> <td>2011</td> <td>2012</td> <td>School District</td>
      <td><a href="https://dev.socrata.com/foundry/data.colorado.gov/6wcd-ysh5"><img src="https://github.com/ryayoung/ryayoung/blob/main/Buttons/symbol/link.45deg.blue.svg" height="22"/></a></td>
    </tr>
    <tr>
      <td>dist_grad_rate</td>
      <td><a href="https://github.com/bia-capstone/crime/tree/main/source_data/dist_grad_rate.md">District Graduation Data by Instructional Program Service type for class of 2011-12</td>
      <td>38</td> <td>185</td> <td>2011</td> <td>2012</td> <td>School District</td>
      <td><a href="https://dev.socrata.com/foundry/data.colorado.gov/cfyh-6xxg"><img src="https://github.com/ryayoung/ryayoung/blob/main/Buttons/symbol/link.45deg.blue.svg" height="22"/></a></td>
    </tr>
    <tr>
      <td>county_demographics</td>
      <td><a href="https://github.com/bia-capstone/crime/tree/main/source_data/county_demographics.md">Census Counties in Colorado 2019</a></td>
      <td>157</td> <td>64</td> <td>2019</td> <td>2019</td> <td>County</td>
      <td><a href="https://dev.socrata.com/foundry/data.colorado.gov/8j3i-rjn4"><img src="https://github.com/ryayoung/ryayoung/blob/main/Buttons/symbol/link.45deg.blue.svg" height="22"/></a></td>
    </tr>
    <tr>
      <td>census_field_desc</td>
      <td><a href="https://github.com/bia-capstone/crime/tree/main/source_data/census_field_desc.md">Census Field Descriptions</a></td>
      <td>7</td> <td>753</td> <td>2019</td> <td>2019</td> <td>County -&gt; Year -&gt; Age</td>
      <td><a href="https://dev.socrata.com/foundry/data.colorado.gov/qten-sdpn"><img src="https://github.com/ryayoung/ryayoung/blob/main/Buttons/symbol/link.45deg.blue.svg" height="22"/></a></td>
    </tr>
    <tr>
      <td>county_population</td>
      <td><a href="https://github.com/bia-capstone/crime/tree/main/source_data/county_population.md">Population Colorado</a></td>
      <td>4</td> <td>381504</td> <td>1990</td> <td>2040</td> <td>Field Name</td>
      <td><a href="https://dev.socrata.com/foundry/data.colorado.gov/eeah-cmy8"><img src="https://github.com/ryayoung/ryayoung/blob/main/Buttons/symbol/link.45deg.blue.svg" height="22"/></a></td>
    </tr>
  </tbody>
</table>
