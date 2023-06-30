# Chemical Checker signaturizer

A set of 25 Chemical Checker bioactivity signatures (including 2D & 3D fingerprints, scaffold, binding, crystals, side effects, cell bioassays, etc) to capture properties of compounds beyond their structures. Each signature has a length of 128 dimensions. In total, there are 3200 dimensions. The signaturizer is periodically updated. We use the 2020-02 version of the signaturizer.

## Identifiers

* EOS model ID: `eos4u6p`
* Slug: `cc-signaturizer`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: 2D projection of bioactivity signatures

## References

* [Publication](https://www.nature.com/articles/s41467-021-24150-4)
* [Source Code](http://gitlabsbnb.irbbarcelona.org/packages/signaturizer)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos4u6p)

## Citation

If you use this model, please cite the [original authors](https://www.nature.com/articles/s41467-021-24150-4) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!