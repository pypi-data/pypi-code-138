# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dvbctrl']

package_data = \
{'': ['*']}

install_requires = \
['psutil>=5.9.1,<6.0.0']

setup_kwargs = {
    'name': 'dvbctrl',
    'version': '0.3.2',
    'description': 'Controls a local dvbstreamer',
    'long_description': '# dvbctrl\n\n## starting\n\n```python\nfrom dvbctrl.dvbstreamer import DVBStreamer\n\nadapter = 0\ndvbs = DVBStreamer(adapter)\nrunning = dvbs.start()\nif not running:\n    raise Exception(f"Failed to start dvbstreamer on adapter {adapter}")\n```\n\n## stopping\n\n```python\nfrom dvbctrl.dvbstreamer import DVBStreamer\n\nadapter = 0\ndvbs = DVBStreamer(adapter)\n\n...\n\nif dvbs.isRunning():\n    dvbs.stop()\n```\n\n## commands\n\n```python\nfrom dvbctrl.commands import DVBCommand\n\nkwargs = {\n    "adapter": 0,\n    "host": "127.0.0.1"\n    "pass": "dvbctrl"\n    "user": "dvbctrl"\n}\ndvbc = DVBCommand(**kwargs)\n\n# services (channels)\nchans = dvbc.lsservices()\n```\n\n## dvbctrl commands\n\n1.       select - Select a new service to stream.\n1.       setmrl - Set the MRL of the primary service filter.\n1.       getmrl - Get the primary service filter MRL.\n1.        addsf - Add a service filter.\n1.         rmsf - Remove a service filter.\n1.        lssfs - List all service filters.\n1.        setsf - Set the service to be filtered by a service filter.\n1.        getsf - Get the service to stream to a secondary service output.\n1.     setsfmrl - Set the service filter\'s MRL.\n1.     getsfmrl - Get the service filter\'s MRL.\n1. setsfavsonly - Enable/disable streaming of Audio/Video/Subtitles only.\n1. getsfavsonly - Get whether Audio/Video/Subtitles only streaming is enabled.\n1.   lsservices - List all services or for a specific multiplex.\n1.      lsmuxes - List multiplexes.\n1.       lspids - List the PIDs for a specified service.\n1.  serviceinfo - Display information about a service.\n1.      muxinfo - Display information about a mux.\n1.        stats - Display the stats for the PAT,PMT and service PID filters.\n1.     festatus - Displays the status of the tuner.\n1.         scan - Scan the specified multiplex(es) for services.\n1.   cancelscan - Cancel the any scan that is in progress.\n1.        lslcn - List the logical channel numbers to services.\n1.      findlcn - Find the service for a logical channel number.\n1.    selectlcn - Select the service from a logical channel number.\n1.      current - Print out the service currently being streamed. (NOT IMPLEMENTED)\n1.     feparams - Get current frontend parameters. (NOT IMPLEMENTED)\n1.      lsprops - List available properties. (NOT IMPLEMENTED)\n1.      getprop - Get the value of a property. (NOT IMPLEMENTED)\n1.      setprop - Set the value of a property. (NOT IMPLEMENTED)\n1.     propinfo - Display information about a property. (NOT IMPLEMENTED)\n1.      dumptsr - Dump information from the TSReader (NOT IMPLEMENTED)\n1.       lslnbs - List known LNBs (NOT IMPLEMENTED)\n1.      epgdata - Register to receive EPG data in XML format. (NOT IMPLEMENTED)\n1.         date - Display the last date/time received. (NOT IMPLEMENTED)\n1.  enabledsmcc - Enable DSM-CC data download for the specified service filter. (NOT IMPLEMENTED)\n1. disabledsmcc - Disable DSM-CC data download for the specified service filter. (NOT IMPLEMENTED)\n1.    dsmccinfo - Display DSM-CC info for the specified service filter. (NOT IMPLEMENTED)\n1. epgcaprestart - Starts or restarts the capturing of EPG content. (NOT IMPLEMENTED)\n1.  epgcapstart - Starts the capturing of EPG content. (NOT IMPLEMENTED)\n1.   epgcapstop - Stops the capturing of EPG content. (NOT IMPLEMENTED)\n1.          now - Display the current program on the specified service. (NOT IMPLEMENTED)\n1.         next - Display the next program on the specified service. (NOT IMPLEMENTED)\n1.  addlistener - Add a destination to send event notification to. (NOT IMPLEMENTED)\n1.   rmlistener - Remove a destination to send event notification to. (NOT IMPLEMENTED)\n1.  lslisteners - List all registered event listener (NOT IMPLEMENTED)\n1. addlistenevent - Add an internal event to monitor. (NOT IMPLEMENTED)\n1. rmlistenevent - Remove an internal event to monitor (NOT IMPLEMENTED)\n1. lslistenevents - List all registered event listener (NOT IMPLEMENTED)\n1.        addmf - Add a new destination for manually filtered PIDs. (NOT IMPLEMENTED)\n1.         rmmf - Remove a destination for manually filtered PIDs. (NOT IMPLEMENTED)\n1.        lsmfs - List current filters.\n1.     setmfmrl - Set the filter\'s MRL. (NOT IMPLEMENTED)\n1.     addmfpid - Adds a PID to a filter. (NOT IMPLEMENTED)\n1.      rmmfpid - Removes a PID from a filter. (NOT IMPLEMENTED)\n1.     lsmfpids - List PIDs for filter. (NOT IMPLEMENTED)\n1.    addoutput - Add a new output. (NOT IMPLEMENTED)\n1.     rmoutput - Remove an output. (NOT IMPLEMENTED)\n1.  enablesicap - Enable the capture of PSI/SI data. (NOT IMPLEMENTED)\n1. disablesicap - Disable the capture of PSI/SI data. (NOT IMPLEMENTED)\n1.    lsplugins - List loaded plugins. (NOT IMPLEMENTED)\n1.   plugininfo - Display the information about a plugin. (NOT IMPLEMENTED)\n1.          who - Display current control connections. (NOT IMPLEMENTED)\n1.         auth - Login to control dvbstreamer. (NOT IMPLEMENTED)\n1.       logout - Close the current control connection. (NOT IMPLEMENTED)\n1.         quit - Exit the program. (NOT IMPLEMENTED)\n1.         help - Display the list of commands or help on a specific command. (NOT IMPLEMENTED)\n',
    'author': 'ccdale',
    'author_email': 'chris.charles.allison+dvbctrl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
