# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import sixfeetup.ploptimizations


class SixfeetupPloptimizationsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=sixfeetup.ploptimizations)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sixfeetup.ploptimizations:default')


SIXFEETUP_PLOPTIMIZATIONS_FIXTURE = SixfeetupPloptimizationsLayer()


SIXFEETUP_PLOPTIMIZATIONS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SIXFEETUP_PLOPTIMIZATIONS_FIXTURE,),
    name='SixfeetupPloptimizationsLayer:IntegrationTesting',
)


SIXFEETUP_PLOPTIMIZATIONS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SIXFEETUP_PLOPTIMIZATIONS_FIXTURE,),
    name='SixfeetupPloptimizationsLayer:FunctionalTesting',
)


SIXFEETUP_PLOPTIMIZATIONS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SIXFEETUP_PLOPTIMIZATIONS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SixfeetupPloptimizationsLayer:AcceptanceTesting',
)
