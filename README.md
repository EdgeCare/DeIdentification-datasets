# De-Identification Dataset

## Overview

This repository contains a de-identification dataset designed for anonymizing personal information in medical text. The dataset consists of structured data where sensitive information is labeled and categorized for easy identification and removal.

## Data Structure

The dataset is stored in `all_data.json` and follows the structure below:

```json
{
    "sentence": "James Turner, 54, was admitted to Bright Horizons Medical on 06/13/2027 for treatment.",
    "meta": {
        "note_id": "2002",
    },
    "spans": [
        {
            "id": "0",
            "start": 0,
            "end": 12,
            "label": "PATIENT"
        },
        {
            "id": "1",
            "start": 14,
            "end": 16,
            "label": "AGE"
        },
        {
            "id": "2",
            "start": 35,
            "end": 56,
            "label": "HOSP"
        },
        {
            "id": "3",
            "start": 60,
            "end": 70,
            "label": "DATE"
        }
    ]
}
```

### Fields:
- **sentence**: The original text containing sensitive medical information.
- **meta**: Metadata related to the text sample.
  - **note_id**: Unique identifier for the note.
- **spans**: A list of entities detected in the sentence.
  - **id**: Unique identifier for the entity.
  - **start**: Start index of the entity in the sentence.
  - **end**: End index of the entity in the sentence.
  - **label**: Type of sensitive information.

## Labels

The dataset includes the following entity labels:

| ID  | Label      | Description                                     |
|-----|-----------|-------------------------------------------------|
| 0   | O         | Non-entity tokens                               |
| 1   | PATIENT   | Patient's name                                  |
| 2   | STAFF     | Medical staff name                              |
| 3   | AGE       | Patient's age                                   |
| 4   | BIRTHDATE | Patient's birthdate                             |
| 5   | DATE      | Any date (admission, discharge, etc.)           |
| 6   | PHONE     | Phone number                                    |
| 7   | ID        | Identifiers (e.g. patient ID)             |
| 8   | EMAIL     | Email addresses                                 |
| 9   | LOC       | Location (city, state, address, etc.)           |
| 10  | HOSP      | Hospital or medical institution                 |
| 11  | ORG       | Organizations or institutions                   |


## Applications

This dataset can be used for:
- **De-identification tasks**: Removing personal identifiers from medical text.
- **Named Entity Recognition (NER) models**: Training machine learning models to detect sensitive information.
- **Privacy-preserving data processing**: Ensuring compliance with HIPAA and other privacy regulations.

## Contributing

If you would like to contribute to this dataset, feel free to:
- Open an issue for any errors or improvements.
- Submit a pull request with additional data or enhancements.
