#
# DBus interface for the Blivet partitioning module.
#
# Copyright (C) 2019 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#

from dasbus.server.interface import dbus_interface
from dasbus.typing import *  # pylint: disable=wildcard-import
from pyanaconda.modules.common.constants.objects import BLIVET_PARTITIONING
from pyanaconda.modules.storage.partitioning.base_interface import PartitioningInterface


@dbus_interface(BLIVET_PARTITIONING.interface_name)
class BlivetPartitioningInterface(PartitioningInterface):
    """DBus interface for the Blivet partitioning module."""

    def SendRequest(self, data: List[Byte]) -> List[Byte]:
        """Send a request to the storage handler.

        :param data: a request data in bytes
        :return: a reply data in bytes
        """
        return self._implementation.send_request(bytes(data))
