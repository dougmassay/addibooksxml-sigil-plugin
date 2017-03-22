AddiBooksXML (A Sigil Plugin)
============

Add proprietary iBooks' xml files to an epub in Sigil.

**NOTE: this plugin periodically checks for updated versions by connecting to this Github repository**

Links
=====

* Sigil website is at <http://sigil-ebook.com>
* Sigil support forums are at <http://www.mobileread.com/forums/forumdisplay.php?f=203>
* AddiBooksXML plugin MobileRead support thread: <http://www.mobileread.com/forums/showthread.php?t=272241>

Building
========

First, clone the repo and cd into it:

    $ git clone https://github.com/dougmassay/addibooksxml-sigil-plugin.git
    $ cd addibooksxml-sigil-plugin
    
To create the plugin zip file, run the buildplugin.py script (root of the repository tree) with Python (2 or 3)

    $ python buildplugin.py
    
This will create the AddiBooksXML_vX.X.X.zip file that can then be installed into Sigil's plugin manager.

Using AddiBooksXML
=================
If you're using Sigil v0.9.0 or later on OSX or Windows, all dependencies should already be met so long as you're using the bundled Python interpreter (default).

Linux users will have to make sure that the Tk graphical python module is present if it's not already.  On Debian-based flavors this can be done with "sudo apt-get install python-tk" for python 2.7 or "sudo apt-get install python3-tk" for Python 3.4.

* **Note:** Do not rename any Sigil plugin zip files before attempting to install them

This plugin will work with either Python 3.4+ or Python 2.7+ (defaults to 3.x if both are present).
The absolute minimum version of Sigil required is v0.8.3 (Python must be installed separately prior to v0.9.0)


Configurable preferences (available after first run in the plugin's corresponding json prefs file) are:

* **check_for_updates** : a boolean value (defaults to true) that controls whether the plugin checks for updates. Change to false if you don't wish to be notified when a new version of this plugin is available.


Get more help at the AddiBooksXML plugin [MobileRead support thread:](<http://www.mobileread.com/forums/showthread.php?t=272241>)

    
Contributing / Modifying
============
From here on out, a proficiency with developing / creating Sigil plugins is assumed.
If you need a crash-course, an introduction to creating Sigil plugins is available at
http://www.mobileread.com/forums/showthread.php?t=251452.


The core plugin files (this is where most contributors will spend their time) are:

    > plugin.py
    > plugin.xml
    > updatecheck.py
    > utilities.py

    
Files used for building/maintaining the plugin:

    > buildplugin.py  -- this is used to build the plugin.
    > setup.cfg -- used for flake8 style checking. Use it to see if your code complies.
    > checkversion.xml -- used by automatic update checking.

Feel free to fork the repository and submit pull requests (or just use it privately to experiment).


License Information
=======

### AddiBooksXML

    Licensed under the GPLv3.
