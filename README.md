# Web demo of M3

This is the code of a simple Python Flask app that provides a demo of the [m3inference Python library](http://www.github.com/euagendas/m3inference).

You probably are not interested in this repository, but instead should go to [m3inference](http://www.github.com/euagendas/m3inference) or read the WebConf (WWW) 2019 paper [Demographic Inference and Representative Population Estimates from Multilingual Social Media Data](https://doi.org/10.1145/3308558.3313684) that created m3.

## Try the demo

Please visit a live copy of the web demo at http://www.euagendas.org/m3demo/

## Running the demo locally

Clone this repository and then run 

```
pip install -r requirements.txt
FLASK_APP=application.py python -m flask run
```

This demo requires Python>=3.6 

## Citation
Please cite our WWW 2019 paper if you use this package in your project.

```
@inproceedings{wang2019demographic,
  title={Demographic Inference and Representative Population Estimates from Multilingual Social Media Data},
  author={Wang, Zijian and Hale, Scott A. and Adelani, David and Grabowicz, Przemyslaw A. and Hartmann, Timo and Fl{\"o"}ck, Fabian and Jurgens, David},
  booktitle={Proceedings of the 2019 World Wide Web Conference},
  year={2019},
  organization={ACM}
}
```

## More Questions

We use issues on this GitHub for all questions or suggestions.  For specific inqueries, please contact us as `hello@euagendas.org`.  Please note that we are unable to release or provide training data for this model due to existing terms of service.

## License

This source code is licensed under the GNU Affero General Public License, which allows for non-commercial re-use of this software.  For commercial inquiries, please contact us directly. Please see the LICENSE file in the root directory of this source tree for details.

This source code includes a copy of [jQuery-Autocomplete](https://github.com/devbridge/jQuery-Autocomplete). See the file or linked repository for further details about its licensing.

We also use [Vizsla](https://github.com/gjmcn/vizsla), a simple JavaScript API for Vega-Lite.

## Acknowledgements
This web demo was created by [Scott A. Hale](https://www.oii.ox.ac.uk/people/hale/) and [Graham McNeill](https://www.oii.ox.ac.uk/people/graham-mcneill/). The research leading to M3 was carried out by [Zijian Wang](https://twitter.com/zijianwang30), [Scott A. Hale](https://www.oii.ox.ac.uk/people/hale/), [David Adelani](https://www.lsv.uni-saarland.de/?id=231),
[Przemyslaw A. Grabowicz](https://www.cics.umass.edu/people/grabowicz-przemyslaw), [Timo Hartmann](https://www.researchgate.net/profile/Timo_Hartmann), 
[Fabian Fl&ouml;ck](https://www.gesis.org/person/fabian.floeck), and [David Jurgens](http://jurgens.people.si.umich.edu/). We thank the Volkswagen Foundation and the EPSRC for supporting the research.

