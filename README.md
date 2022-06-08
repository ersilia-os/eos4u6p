# Chemical Checker signaturizer

Chemical Checker 25 bioactivity signatures

| Description | Input  | Output  | Training Data | Experimental Validation |
| ------- | --- | --- | --- | --- |
| A set of 25 chemical and bioactivity signatures based on the Chemical Checker | SMILES | CC bioactivity signatures | ~800,000 molecules | Yes |

## Source code
This model has been published by Martino Bertoni, Miquel Duran-Frigola, Pau Badia-i-Mompel, Eduardo Pauls, Modesto Orozco-Ruiz, Oriol Guitart-Pla, Víctor Alcalde, Víctor M. Diaz, Antoni Berenguer-Llergo, Isabelle Brun-Heath, Núria Villegas, Antonio García de Herreros & Patrick Aloy, Nature Communications volume 12, Article number: 3932 (2021) Bioactivity descriptors for uncharacterized chemical compounds

Code: http://gitlabsbnb.irbbarcelona.org/packages/signaturizer

## Extended description
Chemical descriptors encode the physicochemical and structural properties of small molecules. This model is a collection of deep neural networks able to infer bioactivity signatures for any compound of interest. Our signaturizers relate to bioactivities of 25 different types and can be used as drop-in replacements for chemical descriptors in day-to-day chemoinformatics tasks. We illustrate how inferred bioactivity signatures are useful to navigate the chemical space in a biologically relevant manner, unveiling higher-order organization in natural product collections, and to enrich mostly uncharacterized chemical libraries for activity against the drug-orphan target Snail1. 

### Summary
* 25 bioactivity signatures from the [Chemical Checker](https://bioactivitysignatures.org).
* Each bioactivity signature is a numerical vector of 128 dimensions.
* Signatures are organised in 5 levels of increasing complexity, namely Chemistry (A), Targets (B), Networks (C), Cells (D) and Clinics (E)
* Chemical Checker publication: [Duran-Frigola et al. 2020](https://www.nature.com/articles/s41587-020-0502-7).
* Chemical Checker web: https://chemicalchecker.com

### Specifications
* Input: SMILES string

## History
* We [downloaded](https://bioactivitysignatures.org/) the signaturizer on May 3, 2021.
* Model was incorporated to Ersilia on September 13, 2021.
