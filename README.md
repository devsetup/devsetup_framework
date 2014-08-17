# Devsetup Framework

Devsetup is _system setup automation for developers_.

This is the __devsetup framework__ - a collection of modules that you can quickly and easily reuse in your own `devsetup.py` scripts straight away!

## Using The Devsetup Framework

1. Copy `devsetup-stub.py` to `your-project/devsetup.py`
1. In `your-project/devsetup.py`, add your automation steps to the 'install' function
1. Test, test, test :)
1. Update your README.md to tell your users to run 'python ./devsetup.py install'

That's it :)

## Contributing to Devsetup Framework

We use the [Hubflow](http://datasift.github.io/gitflow) workflow:

* Our __master__ branch contains released code only
* Our __develop__ branch contains all the code accepted for the next release

To submit a feature:

1. Fork the [devsetup/devsetup_framework](https://github.com/devsetup/devsetup_framework) repo on GitHub.
1. Clone your fork to your dev machine
1. Use `git hf feature start <your-feature>` to create a new feature branch
1. Create and test your feature
1. Push your feature back to your clone
1. Using GitHub, send us a Pull Request. Make sure it targets our __develop__ branch.

## License

Devsetup is released under the 3-clause BSD license. See [LICENSE.txt](LICENSE.txt) for details.

Devsetup Framework includes the following third-party open-source code:

* [terminal.py](https://raw.githubusercontent.com/jnu/ncaa/master/ncaalib/aux/terminal.py) - [Joseph Nudell](https://github.com/jnu) / MIT license.
