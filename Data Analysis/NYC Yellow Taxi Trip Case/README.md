# Dashboard for NYC Yellow Taxi Trip Case Analysis

## Description

This dashboard is designed to provide insight into **NYC yellow taxi trip cases** based on data sourced from a CSV file. The presented analysis and visualization aim to help understand the performance of NYC Yellow Taxis, starting from the orders and then breaking it down by payment type, vendor, and distance. An analysis is also provided based on the activity locations of NYC Yellow Taxis, using pickup and drop-off points.

## Data Source

- CSV file used: `yellow_tripdata_2016-01.csv`.
- This CSV file consists of several columns, including:
  - `VendorID`: TPEP provider ID.
  - `tpep_pickup_datetime`: The date and time when the meter was engaged.
  - `tpep_dropoff_datetime`: The date and time when the meter was disengaged.
  - `Passenger_count`: The number of passengers in the vehicle.
  - `Trip_distance`: The elapsed trip distance in miles reported by the taximeter.
  - `Pickup_longitude`: Longitude where the meter was engaged.
  - `Pickup_latitude`: Latitude where the meter was engaged.
  - `RateCodeID`: The final rate code in effect at the end of the trip.
  - `Store_and_fwd_flag`: This flag indicates whether the trip record was held in vehicle memory.
  - `Dropoff_longitude`: Longitude where the meter was disengaged.
  - `Dropoff_latitude`: Latitude where the meter was disengaged.
  - `Payment_type`: A numeric code signifying how the passenger paid for the trip.
  - `Fare_amount`: The time-and-distance fare calculated by the meter.
  - `Extra`: Miscellaneous extras and surcharges.
  - `MTA_tax`: 0.50 MTA tax that is automatically triggered based on the metered rate in use.
  - `Improvement_surcharge`: 0.30 improvement surcharge assessed trips at the flag drop.
  - `Tip_amount`: Tip amount – This field is automatically populated for credit card tips.
  - `Tolls_amount`: Total amount of all tolls paid in trip.
  - `Total_amount`: The total amount charged to passengers. Does not include cash tips.

## Dashboard Content

The dashboard can be accessed at [NYC Yellow Taxi Trip Case Dashboard](https://lookerstudio.google.com/reporting/cb59c434-958d-4613-a67c-b0b1cd75a798/page/p_sc7yv35otd)

### Summary

The **Summary** section provides a general overview of the available data, including:

- **Total order and revenue of NYC Yellow Taxi**.
- **Breakdown per Vendor**.
- **Breakdown per Payment Type**.
- **Breakdown per Distance Group**.
- **Total Order based on Geographical View**.

### Visualizations

- **Pie Chart**: Distribution of revenue by vendor.
- **Bar Chart**: Distribution of order by payment type.
- **Geographical Chart**: Distribution of order per city.

### Pivot Table

A **pivot table** is available for more granular analysis:

- Groups patients by **distance group** to get average of order, revenue, and total passenger.

This is helpful for identifying patterns or trends, for instance:

- Which distance that user mainly take?
