# Dataset Schema

## Target Variable

| Column | Type | Description |
|--------|--------|--------|
| disease_risk | integer | 0 = Low Risk, 1 = High Risk |

---

# Features

## Demographics

| Column | Type |
|----------|----------|
| age | integer |
| sex | string |

---

## Lifestyle

| Column | Type |
|----------|----------|
| smoking | string |
| alcohol | string |
| exercise_level | string |
| bmi | float |

---

## Vitals

| Column | Type |
|----------|----------|
| heart_rate | integer |
| systolic_bp | integer |
| diastolic_bp | integer |
| blood_sugar | float |
| cholesterol | float |

---

## Family History

| Column | Type |
|----------|----------|
| family_history | string |

---

## Symptoms

| Column | Type |
|----------|----------|
| fatigue | string |
| fever | string |

---

# Categories

## Sex

- Male
- Female

## Smoking

- Yes
- No

## Alcohol

- Yes
- No

## Exercise

- Low
- Medium
- High

## Family History

- Yes
- No

## Symptoms

- Yes
- No

---

# Example Label

```text
0 = Low risk

1 = High risk
```