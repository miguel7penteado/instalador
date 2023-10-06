Release notes
=============

This document describes major installer-related changes in Fedora releases.

Fedora 38
#########

Changes in the graphical interface
----------------------------------

Modernized welcome screen on Live CD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The welcome screen on Live CD has been changed to follow the current design patterns,
as well as fit better into the surrounding GTK4-based interface.
See the pull request `#4616 <https://github.com/rhinstaller/anaconda/pull/4616>`__ for more information.

Improved configuration of additional repositories in GUI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuration of additional repositories in the graphical user interface has been improved.
The protocol selection is now replaced with a drop-down menu of source actions.
The screen also shows only configuration options relevant to the selected source action.
See the pull request `#4498 <https://github.com/rhinstaller/anaconda/pull/4498>`__ for more details.

Installation source errors are visible again
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Previously, errors related to contents of the Installation Source screen did not cause the
error message bar to appear at the bottom of the screen. As a consequence, users could not review
the error messages and immediately correct the errors on the screen. The error message bar now
appears correctly when errors occur. As a result, users can immediately notice errors in the
Installation Source screen and correct them.
See the pull request `#4501 <https://github.com/rhinstaller/anaconda/pull/4501>`__.

Japanese translation fits the whole screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Previously, using Anaconda in Japanese caused the main screen elements to use larger font than in
other languages. As a consequence, the user settings were hidden outside the visible screen area
and required scrolling. The sizing has been corrected, and Japanese users can now see the user
settings icon and description even on the smallest supported screen sizes again.
See the pull request `#4325 <https://github.com/rhinstaller/anaconda/pull/4325>`__.

Architecture and hardware support changes
-----------------------------------------

Do not pass the `rd.znet` boot argument on to the installed system unconditionally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With this change, the `rd.znet` boot argument is no longer passed on to the installed
system unconditionally on IBM Z systems and the network device is configured and
activated after switchroot by udev/NetworkManager. When networking is needed early in
initramfs (like in a case of the root file system on iSCSI), `rd.znet` is automatically
added to the kernel command line of the installed via a different mechanism.
See the pull request `#4303 <https://github.com/rhinstaller/anaconda/pull/4303>`__.

The dmraid and nodmraid boot options are removed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``inst.dmraid`` and ``inst.nodmraid`` boot options have been removed. These options no longer
controlled any functionality, after Anaconda started using ``mdadm`` instead of ``dmraid``.
See the pull request `#4517 <https://github.com/rhinstaller/anaconda/pull/4517>`__ and the related
`Fedora Change <https://fedoraproject.org/wiki/Changes/UseMdadmForBIOSRAIDInAnaconda>`__.

Biosboot partition verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The biosboot partition is now verified on all installation target disks.
This improves support for booting from an array.
See the pull request `#4277 <https://github.com/rhinstaller/anaconda/pull/4277>`__.

Multiple bootloader devices on the Manual Partitioning screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With this change, the graphical interface displays correctly all bootloader devices on the
Manual Partitioning screen.
See the pull request `#4271 <https://github.com/rhinstaller/anaconda/pull/4271>`__.

Payload changes
-----------------

Add support for OSTree native containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fedora is adding a new enhanced container support for the (rpm-)ostree stack to
natively support OCI/Docker containers as a transport and delivery mechanism
for operating system content. Anaconda now supports these containers by
a new kickstart command `ostreecontainer`.
See the pull request `#4617 <https://github.com/rhinstaller/anaconda/pull/4617>`__,
`Fedora Change <https://fedoraproject.org/wiki/Changes/OstreeNativeContainerStable>`__
and `Pykickstart <https://pykickstart.readthedocs.io/en/latest/kickstart-docs.html#ostreecontainer>`__.

rpm-ostree now validates checksums for local repositories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Previously, rpm-ostree installations verified checksums only for installations from a remote
repository, while installations from local repositories did not verify the checksums.
As a consequence, rpm-ostree installations from local repositories could install corrupted data
without any indication. This behavior is now unified, and Anaconda verifies checksums for all
rpm-ostree repositories. As a result, all rpm-ostree installations are now protected against
installing corrupted data.
See the pull request `#4357 <https://github.com/rhinstaller/anaconda/pull/4357>`__ for more information.

Kickstart support
-----------------

Creating hibernation swap from kickstart
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The new ``autopart (...) --hibernation`` kickstart option creates a swap partition with an
automatically determined size that is big enough for hibernation.
See the pull request `#4275 <https://github.com/rhinstaller/anaconda/pull/4275>`__.

General changes
---------------

Faster core dumps
^^^^^^^^^^^^^^^^^

Previously, Anaconda used a custom setup for handling tracebacks and saving core dumps. This is
now realized by using the ``faulthandler`` Python module and the ``systemd-coredump`` service.
As a result, the same debugging data is still available, while the installation environment
becomes responsive significantly sooner after tracebacks. As a side effect, the logs from Anaconda
and the installation environment now contain different error messages.
See the pull request `#4350 <https://github.com/rhinstaller/anaconda/pull/4350>`__ for more information.

The Web UI of Anaconda is now packaged in Fedora
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Anaconda team is working for some time on the new Web UI frontend for the installer and to make
this in development Web UI more accessible to people we decided to add this as a new package to
Fedora repositories. To be able to consume this Web UI, you need to build ISO with the Web UI
package and add kernel boot arguments `inst.webui`. This package is not included in the existing
Fedora images by default.
See the pull request `#4269 <https://github.com/rhinstaller/anaconda/pull/4269>`__.

Fedora 37
#########

General changes
---------------

GPT is the default disk label type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fedora Linux systems installed on legacy x86 BIOS systems will get GPT partitioning by default
instead of legacy MBR partitioning. This should be a new default for all products. See the
`Fedora Change <https://fedoraproject.org/wiki/Changes/GPTforBIOSbyDefault>`__ for more info.

Read-only /sysroot on RPM OSTree systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The RPM OSTree installations set the ``/sysroot`` mount point as read-only instead of read-write
to make the newly installed systems more robust. Users and administrators are not expected to
directly interact with the content available there and should use the available interfaces to
manage their system. See the `pull request <https://github.com/rhinstaller/anaconda/pull/4240>`__
and the `Fedora Change <https://fedoraproject.org/wiki/Changes/Silverblue_Kinoite_readonly_sysroot>`__.

Anaconda doesn't copy /etc/resolv.conf to systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Anaconda does not copy the ``/etc/resolv.conf`` file from the installation environment to
the installed system anymore. Creating the file is a business of ``systemd-resolved`` or
the Network Manager. Anaconda is not going to interfere into this process anymore.
Currently the file is created by ``systemd-resolved`` package during the installation.
See the pull requests `#3814 <https://github.com/rhinstaller/anaconda/pull/3814>`__ and
`#3818 <https://github.com/rhinstaller/anaconda/pull/3818>`__.

Correct SELinux contexts on existing home directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Previously, the installer set incorrect SELinux contexts on home directory contents when
reusing home directory from previous installation. The contexts are now set correctly.
See the `pull request <https://github.com/rhinstaller/anaconda/pull/3993>`__.

Enabled hibernation on arm64 with swap
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Previously, the installer enabled resume from hibernation by adding kernel command line option
``resume=swap_device`` only on the x86 architecture family. With this change, the same is done
also for the arm64 architecture. As a result, devices of the arm64 architecture are now able to
correctly resume from hibernation.
See the `pull request <https://github.com/rhinstaller/anaconda/pull/4221>`__.

Changed default swap size for large-memory systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The default swap size on systems with 64 GiB or more RAM is 32 GiB now. Previously, it was 4 GiB.
See the `pull request <https://github.com/rhinstaller/anaconda/pull/4049>`__.

Removed some scripts provided by Anaconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following undocumented installed scripts were removed from `anaconda` packages:

- ``/usr/bin/analog``
- ``/usr/bin/restart-anaconda``

The following unused development scripts were removed from the Anaconda repository:

- ``run_boss_locally.py``
- ``anaconda-read-journal``
- ``list-screens``
- ``make-sphinx-docs``

See the pull requests `#3839 <https://github.com/rhinstaller/anaconda/pull/3839>`__ and
`#3838 <https://github.com/rhinstaller/anaconda/pull/3838>`__.

Changes in the graphical interface
----------------------------------

The media verification dialog is improved
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Previously, the media verification dialog indicated a good or bad media check result using the
same sentence, differing only in presence of a single "not". Additionally, the dialog did not
visually change much upon completion of the check. Consequently, it was not easy to interpret
the result of the media check, or even see if it was finished.

The dialog now uses a large icon to signal whether the media is good or not, and while the
check is running, this icon is absent. As a result, it is now possible to easily tell the state
of the media check. See the `pull request <https://github.com/rhinstaller/anaconda/pull/4230>`__
and the `screenshot <https://user-images.githubusercontent.com/15903878/176200267-789a86fe-e874-4b14-aa20-878e63381dca.png>`__.

Improved calculation of the space estimation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During automatic partitioning the disk spoke estimates the space required for the installation
and if there isn't enough free space it display a warning dialog suggesting more space should
be reclaimed. This estimate included the recommended swap size even when swap wasn't configured
to be created. See the bug `2068290 <https://bugzilla.redhat.com/show_bug.cgi?id=2068290>`__.

The zFCP dialog supports NPIV-enabled devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The "Add zFCP" dialog supports NPIV-enabled zFCP devices. NPIV-enabled devices are activated just
by using the device ID. The kernel module will detect the WWPNs and LUNs and bring all the devices
up automatically. This means the user doesn't have to provide the WWPN and LUN IDs.
See the `pull request <https://github.com/rhinstaller/anaconda/pull/4188>`__.

The timezone map doesn't show borders
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Anaconda is not showing timezone borders in the Time & Date spoke. The map is white now.
See the bug `2103657 <https://bugzilla.redhat.com/show_bug.cgi?id=2103657>`__

Changes in the kickstart support
--------------------------------

Prompt for a missing passphrase in GUI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the kickstart file defines a partitioning that requires a passphrase, the graphical user
interface shows a dialog that allows users to provide the missing passphrase. The installation
automatically continues after the passphrase is provided. It works the same way in the text user
interface. See the `pull request <https://github.com/rhinstaller/anaconda/pull/4164>`__.

``rootpw --allow-ssh`` is supported
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the ``--allow-ssh`` option of ``rootpw`` kickstart command to allow remote logins of the
root user via SSH using only the password. This is disabled by default for the security reasons,
so be aware of risks. See the `pull request <https://github.com/rhinstaller/anaconda/pull/4154>`__
and the `Fedora Change <https://fedoraproject.org/wiki/Changes/DisableRootPasswordLoginInSshd>`__
for the default behaviour.

``zfcp --devnum=`` is supported
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``zfcp`` kickstart command supports NPIV-enabled zFCP devices. NPIV-enabled devices are
activated just by using the device ID. The kernel module will detect the WWPNs and LUNs and
bring all the devices up automatically. This means the user doesn't have to provide the WWPN
and LUN IDs::

    zfcp --devnum=<device_number>

See the `pull request <https://github.com/pykickstart/pykickstart/pull/410>`__ for more info.

Changes in Anaconda options
---------------------------

``inst.gpt`` is deprecated
^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the ``inst.disklabel`` boot option to specify a preferred disk label type. Specify ``gpt``
to prefer creation of GPT disk labels. Specify ``mbr`` to prefer creation of MBR disk labels if
supported. The ``inst.gpt`` boot option is deprecated and will be removed in future releases.
See the `pull request <https://github.com/rhinstaller/anaconda/pull/4232>`__.

Changes in Anaconda configuration files
---------------------------------------

The ``gpt`` option is replaced
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The default value of the preferred disk label type is specified by the ``disk_label_type``
option in the Anaconda configuration files. The ``gpt`` configuration option is no longer
supported. See the `pull request <https://github.com/rhinstaller/anaconda/pull/4232>`__.

The ``decorated_window`` option is removed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``decorated_windows`` option is removed from Anaconda's configuration files.
It was never requested and we have no evidence that it was used.
See the `pull request <https://github.com/rhinstaller/anaconda/pull/3933>`__.

The ``enable_ignore_broken_packages`` option is removed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``enable_ignore_broken_packages`` option in Anaconda's configuration files is removed.
The pykickstart decides whether the ``%packages --ignorebroken`` feature is supported or not.
See the `pull request <https://github.com/rhinstaller/anaconda/pull/3897>`__.

The ``blivet_gui_supported`` option is removed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The support for Blivet-GUI will be disabled automatically if it is not installed.
Use the ``hidden_spokes`` option of the ``User Interface`` section to disable it explicitly.
See the `pull request <https://github.com/rhinstaller/anaconda/pull/3925>`__.

The ``can_detect_unsupported_hardware`` and ``can_detect_support_removed`` options were removed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The support for detection of unsupported hardware is no longer available.
See the `pull request <https://github.com/rhinstaller/anaconda/pull/3842>`__ for more info.

Fedora 36
#########

General changes
---------------

The help support is unified
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The help support on RHEL and Fedora uses new mapping files with a unified format.
The mappings files are located in the root of the help directory.
For example for RHEL, they are expected to be at::

    /usr/share/anaconda/help/rhel/anaconda-gui.json
    /usr/share/anaconda/help/rhel/anaconda-tui.json

The mapping files contain data about the available help content.
The UI screens are identified by a unique screen id returned by
the ``get_screen_id`` method, for example ``installation-summary``.
The help content is defined by a relative path to a help file and
(optionally) a name of an anchor in the help file.

For example::

    {
      "_comment_": [
        "This is a comment",
        "with multiple lines."
      ],
      "_default_": {
        "file": "default-help.xml",
        "anchor": "",
      },
      "installation-summary": {
        "file": "anaconda-help.xml",
        "anchor": "",
      },
      "user-configuration": {
        "file": "anaconda-help.xml",
        "anchor": "creating-a-user-account"
      }
    }

The ``default_help_pages`` configuration option is removed. The ``helpFile`` attribute is removed
from the UI classes. See the `pull request`_ for more info.

.. _pull request:
  https://github.com/rhinstaller/anaconda/pull/3575

Changes in the graphical interface
----------------------------------

Users are administrators by default
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the User spoke, the "Make this user administrator" checkbox is now checked by default. This
improves installation experience for users who do not know and need to rely on the default values
to guide them. See the `Users are admins by default`_ change.

.. _Users are admins by default:
   https://fedoraproject.org/wiki/Changes/Users_are_admins_by_default_in_Anaconda

Keyboard configuration is disabled on Live media with Wayland
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The keyboard switching in the Anaconda installer on the Live media did not behave as expected
on Wayland based environments (`#2016613`_). When users changed the keyboard layout configuration
that configuration was reflected in the Live environment. However, if users pressed modifier keys
(CTRL or SHIFT) the keyboard specified by the Anaconda installer was changed back for the Live
environment. That is the result of how the Wayland protocol handles keyboard layout.

To avoid this unexpected behavior Anaconda will no longer control keyboard layout configuration
of the Live systems on Wayland Live environment. The keyboard configuration set by Anaconda on
the Live environment will be reflected only to the installed system. This means that users have
to pay attention that their passwords are written by the correct layout in the installer running
inside the Live environment to be able to use the password in the system after installation.

.. _#2016613:
  https://bugzilla.redhat.com/show_bug.cgi?id=2016613

Changes in the kickstart support
--------------------------------

The `%anaconda` section is removed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The support for the deprecated `%anaconda` section is removed.
Use `Anaconda configuration files`_ instead.

.. _Anaconda configuration files:
  https://anaconda-installer.readthedocs.io/en/latest/configuration-files.html

`ANA_INSTALL_PATH` is deprecated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `ANA_INSTALL_PATH` environment variable is deprecated. The support for this variable will be
removed in future releases. Use the `/mnt/sysroot` path in your kickstart scripts instead.
See the `Installation mount points`_ documentation.

.. _Installation mount points:
  https://anaconda-installer.readthedocs.io/en/latest/mount-points.html


Changes in Anaconda options
---------------------------

`inst.nompath` is deprecated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `inst.nompath` boot option is deprecated. It has not been doing anything useful for some
time already.


Changes in Anaconda configuration files
---------------------------------------

Saving Anaconda's data to target system
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Anaconda configuration file format now includes additional options to control
what is saved to the target system.

The options are::

    # Should we copy input kickstart to target system?
    can_copy_input_kickstart = True

    # Should we save kickstart equivalent to installation settings to the new system?
    can_save_output_kickstart = True

    # Should we save logs from the installation to the new system?
    can_save_installation_logs = True

The default values above cause no change in behavior, the new options are
only another way to configure the behavior.

Fedora 35
#########

General changes
---------------

Limited support for braille devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Server image (boot.iso) now contains the `brltty` accessibility software.
This means that some braille output devices can be automatically detected and used.
This feature works only in text mode, started with the `inst.text` boot option.
See `the bug <https://bugzilla.redhat.com/show_bug.cgi?id=1584679>`_.

Visible warnings in initrd
^^^^^^^^^^^^^^^^^^^^^^^^^^

Installation shows critical warnings raised in Dracut/initrd again when Anaconda is
starting or when Dracut starts to timeout. This should help users to resolve installation
issues by avoiding that the important message was scrolled out too fast.
See `the bug <https://bugzilla.redhat.com/show_bug.cgi?id=1983098>`_.

Changes in the graphical interface
----------------------------------

New look of the NTP server dialog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The NTP server dialog has been redesigned. The new look uses more traditional approach to
management of lists (such as in `hexchat`). See `the pull request <https://github.com/rhinstaller/anaconda/pull/3538>`_.

- The set of controls to add a new server is no longer present. Instead, a "blank" new server
  is added by clicking an "add" button. The details can be filled in by editing the server
  in the list, as was already possible.
- The method to remove a server is now more intuitive. Users can simply click the "remove"
  button and the server is instantly removed from the list. Previously, users had to uncheck
  the "Use" checkbox for the server in the list and confirm the dialog.

New look of the root configuration screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The root configuration screen has been redesigned and is no longer ambiguous. All root account
options are visible only if root account is enabled. The new layout also contains text to let
users understand their choices. See `the pull request <https://github.com/rhinstaller/anaconda/pull/3511>`_.

Changes in the text interface
-----------------------------

The packaging log in ``tmux`` tabs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add a new tab to the ``tmux`` session starting the Anaconda installer. This new tab will follows
the ``/tmp/packaging.log`` log file. This change should make it easier for users to spot software
installation errors. See `the pull request <https://github.com/rhinstaller/anaconda/pull/3472>`_.

Changes in Anaconda configuration files
---------------------------------------

Replacement of product configuration files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The support for the product configuration files was removed and replaced with profiles.
See `the Fedora change <https://fedoraproject.org/wiki/Changes/Replace_Anaconda_product_configuration_files_with_profiles>`_
and `the documentation <https://anaconda-installer.readthedocs.io/en/latest/configuration-files.html#profile-configuration-files>`_.

Each profile can be identified by a unique id and it can define additional options for
the automated profile detection. The profile will be chosen based on the ``inst.profile``
boot option, or based on the ``ID`` and ``VARIANT_ID`` options of the os-release files.
The profile configuration files are located in the ``/etc/anaconda/profile.d/`` directory.

The ``inst.product`` and ``inst.variant`` boot options are deprecated.

Options for Anaconda DBus module activation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have introduced new configuration options that affect the detection and activation of
the Anaconda DBus modules. Use the ``activatable_modules`` option to specify Anaconda DBus
modules that can be activated. Use the ``forbidden_modules`` option to specify modules that
are not allowed to run. Use the ``optional_modules`` to specify modules that can fail to run
without aborting the installation.

The DBus modules can be specified by a DBus name or by a prefix of the name that ends with
an asterisk. For example::

    org.fedoraproject.Anaconda.Modules.Timezone
    org.fedoraproject.Anaconda.Addons.*

The ``addons_enabled`` and ``kickstart_modules`` options are deprecated and will be removed
in the future.

See `the pull request <https://github.com/rhinstaller/anaconda/pull/3464>`_.
