.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=========================
sixfeetup.ploptimizations
=========================

This package provides front-end optimizations to Plone.

Features
--------

- Switches to minified version of Products/CMFPlone/static/components/requirejs/require.js
- Minifies config.js by overriding Products/CMFPlone/resources/browser/configjs.py


Installation
------------

Install sixfeetup.ploptimizations by adding it to your buildout::

    [buildout]

    ...

    eggs =
        sixfeetup.ploptimizations


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/sixfeetup.ploptimizations/issues
- Source Code: https://github.com/collective/sixfeetup.ploptimizations
- Documentation: https://github.com/collective/sixfeetup.ploptimizations


License
-------

The project is licensed under the GPLv2.
