# Chemical Checker signaturizer

A set of 25 Chemical Checker bioactivity signatures (including 2D & 3D fingerprints, scaffold, binding, crystals, side effects, cell bioassays, etc) to capture properties of compounds beyond their structures. Each signature has a length of 128 dimensions. In total, there are 3200 dimensions. The signaturizer is periodically updated. We use the 2020-02 version of the signaturizer.

This model was incorporated on 2021-05-03.Last packaged on 2025-08-29.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4u6p`
- **Slug:** `cc-signaturizer`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Descriptor`, `Bioactivity profile`, `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `3200`
- **Output Consistency:** `Fixed`
- **Interpretation:** Vector representation of a molecule

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| a1_000 | float |  | Dimension 0 for Chemical Checker dataset chemistry (A) 2D chemistry (A1) |
| a1_001 | float |  | Dimension 1 for Chemical Checker dataset chemistry (A) 2D chemistry (A1) |
| a1_002 | float |  | Dimension 2 for Chemical Checker dataset chemistry (A) 2D chemistry (A1) |
| a1_003 | float |  | Dimension 3 for Chemical Checker dataset chemistry (A) 2D chemistry (A1) |
| a1_004 | float |  | Dimension 4 for Chemical Checker dataset chemistry (A) 2D chemistry (A1) |
| a1_005 | float |  | Dimension 5 for Chemical Checker dataset chemistry (A) 2D chemistry (A1) |
| a1_006 | float |  | Dimension 6 for Chemical Checker dataset chemistry (A) 2D chemistry (A1) |
| a1_007 | float |  | Dimension 7 for Chemical Checker dataset chemistry (A) 2D chemistry (A1) |
| a1_008 | float |  | Dimension 8 for Chemical Checker dataset chemistry (A) 2D chemistry (A1) |
| a1_009 | float |  | Dimension 9 for Chemical Checker dataset chemistry (A) 2D chemistry (A1) |

_10 of 3200 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4u6p](https://hub.docker.com/r/ersiliaos/eos4u6p)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4u6p.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4u6p.zip)

### Resource Consumption
- **Model Size (Mb):** `538`
- **Environment Size (Mb):** `1973`
- **Image Size (Mb):** `2572.08`

**Computational Performance (seconds):**
- 10 inputs: `50.93`
- 100 inputs: `47.3`
- 10000 inputs: `1600.05`

### References
- **Source Code**: [http://gitlabsbnb.irbbarcelona.org/packages/signaturizer](http://gitlabsbnb.irbbarcelona.org/packages/signaturizer)
- **Publication**: [https://www.nature.com/articles/s41587-020-0502-7](https://www.nature.com/articles/s41587-020-0502-7)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4u6p
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4u6p
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
