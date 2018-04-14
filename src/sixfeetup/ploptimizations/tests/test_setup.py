# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from sixfeetup.ploptimizations.testing import SIXFEETUP_PLOPTIMIZATIONS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that sixfeetup.ploptimizations is properly installed."""

    layer = SIXFEETUP_PLOPTIMIZATIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sixfeetup.ploptimizations is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'sixfeetup.ploptimizations'))

    def test_browserlayer(self):
        """Test that ISixfeetupPloptimizationsLayer is registered."""
        from sixfeetup.ploptimizations.interfaces import (
            ISixfeetupPloptimizationsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ISixfeetupPloptimizationsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SIXFEETUP_PLOPTIMIZATIONS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['sixfeetup.ploptimizations'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if sixfeetup.ploptimizations is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'sixfeetup.ploptimizations'))

    def test_browserlayer_removed(self):
        """Test that ISixfeetupPloptimizationsLayer is removed."""
        from sixfeetup.ploptimizations.interfaces import \
            ISixfeetupPloptimizationsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ISixfeetupPloptimizationsLayer,
            utils.registered_layers())
