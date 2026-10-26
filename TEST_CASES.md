# Test Cases

| ID | Scenario | Input | Expected |
|---|---|---|---|
| TC-01 | No push | torque = 0 | Motor output 0 |
| TC-02 | Normal assist | torque = 4, ratio 0.5 | Assist = 2 |
| TC-03 | Speed limit | speed >= 6.0 km/h | Assist = 0 |
| TC-04 | Low battery | battery < 20% | Assist fades out |
| TC-05 | Over-current | current > 15 A | Fault, motors off |
| TC-06 | Sensor loss | no torque data 100 ms | Fault, assist disabled |
| TC-07 | E-stop | e-stop pressed | Motors off < 100 ms |
| TC-08 | Mode switch | assist -> manual | Assist 0, no jerk |
