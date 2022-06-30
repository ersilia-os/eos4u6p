# Chemical Checker signaturizer

## Model Identifiers
- Slug: cc-signaturizer
- Ersilia ID: eos4u6p
- Tags: fingerprint, ML, bioactivity

## Model Description 
A set of 25 Chemical checker bioactivity signatures (including 2D & 3D fingerprints, scaffold, binding, crystals, side effects, cell bioassays, etc) to capture properties of compounds beyond their structures 
- Input: SMILES 
- Output: Vectors 
- Model type: Regression
- Training ddata: ~800,000 molecules (https://gitlabsbnb.irbbarcelona.org/packages/chemical_checker/-/tree/master/package/chemicalchecker/database)
- Experimentally validated: Yes 

## Source code
This model has been published by Bertoni, M., Duran-Frigola, M., Badia-i-Mompel, P. et al. Bioactivity descriptors for uncharacterized chemical compounds. Nat Commun 12, 3932 (2021). https://doi.org/10.1038/s41467-021-24150-4

- Code: http://gitlabsbnb.irbbarcelona.org/packages/signaturizer

## License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "signaturizer", located at `/model` and licensed under a MIT License

## History
* We downloaded  the signaturizer on May 3, 2021.
* Model was incorporated to Ersilia on September 13, 2021.
