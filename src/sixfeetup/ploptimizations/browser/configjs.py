# -*- coding: utf-8 -*-
from slimit import minify

from Products.CMFPlone.resources.browser.configjs import \
    configjs, \
    _format_shims, \
    RequireJsView

import json


class ConfigJsView(RequireJsView):
    """ config.js for requirejs for script rendering. """

    def __call__(self):
        (paths, shims) = self.get_requirejs_config()
        self.request.response.setHeader(
            'Content-Type',
            'application/javascript'
        )
        file = configjs % (
            json.dumps(paths, indent=4),
            _format_shims(shims)
        )
        return minify(file, mangle=False, mangle_toplevel=False)
