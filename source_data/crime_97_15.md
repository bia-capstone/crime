[<img src="https://github.com/ryayoung/icons/blob/main/svg/arrow.left.blue.svg" height="30"/>](https://github.com/bia-capstone/crime/tree/main/source_data)

|  |  |  |  |
| - | - | - | - |
| [crime_16_19](crime_16_19.md) | [_**crime_97_15**_](crime_97_15.md) | [dist_arrests](dist_arrests.md) | [dist_student_mobility](dist_student_mobility.md) |
| [dist_grad_rate](dist_grad_rate.md) | [county_demographics](county_demographics.md) | [census_field_desc](census_field_desc.md) | [county_population](county_population.md) |

```text
Crimes in Colorado 1997 to 2015
https://dev.socrata.com/foundry/data.colorado.gov/6vnq-az4b 

Crime stats for the State of Colorado from 1997 to 2015. Data provided
by the CDPS and the FBI's Crime Data Explorer (CDE).

Rows:    4952282
Cols:    10
Period:  1997 to 2015

COLUMNS:
-------
Agency Name
  Field:  agency_name
  Type:   text
  Null:   380
  Count:  4,951,902
  ITEMS:
     Colorado Springs Police Department  (768,694)
     Aurora Police Department  (587,700)
     Denver Police Department  (521,028)
     Lakewood Police Department  (320,384)
     Adams County Sheriff's Office  (161,497)
     Jefferson County Sheriff's Office  (145,019)
     Westminster Police Department  (122,324)
     Grand Junction Police Department  (120,420)
     Fort Collins Police Department  (105,624)
     Greeley Police Department  (102,768)
     Arapahoe County Sheriff's Office  (97,761)
     Pueblo Police Department  (87,106)
     Commerce City Police Department  (83,376)
     Longmont Police Department  (81,454)
     El Paso County Sheriff's Office  (78,617)
     Northglenn Police Department  (69,986)
     Arvada Police Department  (66,881)
     Larimer County Sheriff's Office  (66,564)
     Mesa County Sheriff's Office  (64,631)
     Centennial Police Department  (59,761)

Agency Type Name
  Field:  agency_type_name
  Type:   text
  Null:   380
  Count:  4,951,902
  ITEMS:
     City  (4,012,471)
     County  (850,360)
     University or College  (60,693)
     State Police  (24,480)
     Other State Agency  (3,325)
     Other  (557)
     Tribal  (16)

City Name
  Field:  city_name
  Type:   text
  Null:   939,702
  Count:  4,012,580
  ITEMS:
     Colorado Springs  (768,694)
     Aurora  (587,700)
     Denver  (541,421)
     Lakewood  (320,384)
     Westminster  (122,324)
     Grand Junction  (120,420)
     Fort Collins  (105,624)
     Greeley  (102,768)
     Englewood  (97,958)
     Pueblo  (87,106)
     Commerce City  (83,376)
     Longmont  (81,454)
     Northglenn  (69,986)
     Arvada  (66,881)
     Broomfield  (56,900)
     Wheat Ridge  (56,554)
     Brighton  (37,813)
     Boulder  (36,768)
     Montrose  (33,409)
     Parker  (31,949)

Primary County
  Field:  primary_county
  Type:   text
  Null:   24,938
  Count:  4,927,344
  ITEMS:
     El Paso  (881,966)
     Arapahoe  (846,285)
     Jefferson  (620,866)
     Adams  (535,522)
     Denver  (530,939)
     Larimer  (212,468)
     Mesa  (189,866)
     Weld  (169,254)
     Boulder  (155,403)
     Pueblo  (99,231)
     Douglas  (87,111)
     Eagle  (56,952)
     Broomfield  (46,913)
     Garfield  (45,575)
     Montrose  (42,692)
     Fremont  (31,983)
     Summit  (31,567)
     Logan  (25,578)
     Routt  (23,988)
     Montezuma  (23,656)

Incident Hour
  Field:  incident_hour
  Type:   number
  Null:   139,976
  Count:  4,812,306
  Min:    -
  Max:    23.0
  Avg:    -
  Sum:    -

Offense Name
  Field:  offense_name
  Type:   text
  Null:   2,376
  Count:  4,949,906
  ITEMS:
     Destruction/Damage/Vandalism of Property  (856,498)
     All Other Larceny  (490,294)
     Burglary/Breaking & Entering  (417,155)
     Theft From Motor Vehicle  (409,580)
     Simple Assault  (384,606)
     Drug/Narcotic Violations  (336,799)
     Shoplifting  (333,980)
     Motor Vehicle Theft  (236,154)
     Theft From Building  (227,305)
     Drug Equipment Violations  (215,826)
     Aggravated Assault  (149,720)
     Theft of Motor Vehicle Parts or Accessories  (149,304)
     Counterfeiting/Forgery  (101,317)
     Impersonation  (93,960)
     False Pretenses/Swindle/Confidence Game  (91,190)
     Robbery  (78,457)
     Weapon Law Violations  (69,222)
     Credit Card/Automated Teller Machine Fraud  (59,983)
     Intimidation  (40,110)
     Stolen Property Offenses  (33,671)

Crime Against
  Field:  crime_against
  Type:   text
  Null:   2,376
  Count:  4,949,906
  ITEMS:
     Property  (3,635,797)
     Person  (677,735)
     Society  (636,117)
     Not a Crime  (257)

Offense Category Name
  Field:  offense_category_name
  Type:   text
  Null:   2,585
  Count:  4,949,697
  ITEMS:
     Larceny/Theft Offenses  (1,629,963)
     Destruction/Damage/Vandalism of Property  (856,498)
     Assault Offenses  (574,436)
     Drug/Narcotic Offenses  (552,625)
     Burglary/Breaking & Entering  (417,155)
     Fraud Offenses  (250,330)
     Motor Vehicle Theft  (236,154)
     Counterfeiting/Forgery  (101,317)
     Robbery  (78,457)
     Sex Offenses  (75,765)
     Weapon Law Violations  (69,222)
     Stolen Property Offenses  (33,671)
     Kidnapping/Abduction  (24,622)
     Arson  (19,202)
     Prostitution Offenses  (10,778)
     Embezzlement  (10,102)
     Pornography/Obscene Material  (3,068)
     Homicide Offenses  (3,047)
     Extortion/Blackmail  (1,850)
     Bribery  (1,079)

Age Num
  Field:  age_num
  Type:   number
  Null:   2,337,245
  Count:  2,615,037
  Min:    1.0
  Max:    98.0
  Avg:    -
  Sum:    -

Incident Date
  Field:  incident_date
  Type:   calendar_date
  Null:   2,756
  Count:  4,949,526


```
