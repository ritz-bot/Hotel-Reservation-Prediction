# -*- coding: utf-8 -*- #
# Copyright 2014 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Commands for reading machine types."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


@base.UniverseCompatible
@base.ReleaseTracks(
    base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA, base.ReleaseTrack.GA)
class MachineTypes(base.Group):
  """Read Compute Engine virtual machine types."""


MachineTypes.category = base.INFO_CATEGORY

MachineTypes.detailed_help = {
    'DESCRIPTION': """
        Read Compute Engine virtual machine types.

        For more information about machine types, see the
        [machine types documentation](https://cloud.google.com/compute/docs/machine-types).

        See also: [Machine types API](https://cloud.google.com/compute/docs/reference/rest/v1/machineTypes).
    """,
}
