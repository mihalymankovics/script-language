# Tachometer Complex Example

[Tachometer](https://en.wikipedia.org/wiki/Tachometer) measures speed of a vehicle (bus, truck, etc.).

## Recquirements

### Minimum Viable Product

- As a driver, I want to record a route with start time and speed measurements so that the route can be queried and analyzed.
- As a driver, I want to query a route by id so that I can check the report of the route.


### Optional

- As a driver, I want to check the speed limit violations in the report.
- As a driver, I want to get statistical report from the route.
- As a driver,  I want to see my speed in a line chart.

#### Note: User Story

As a __role__, I want to __do something__, so that __benefit__.

#### Note: Tachometer Recording

˙˙˙json
{
    "driver": "John Doe"
    "vehicle": "ABC-123"
    "start": "2021-10-15 13:26:32"
    "speed": [0,0,1,3]
}
˙˙˙

The _speed_ contains a measurement for each seconds.
The _start_ is a string in _YYYY-mm-dd HH-MM-SS_ format.