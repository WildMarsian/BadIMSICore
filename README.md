# MIMSI

## BadIMSICore
The whole BadIMSICore developement is made in Python 3.4.

### init_openbts.py
To launch the OpenBTS Command Line Interface, we must be sure that the **sipauthserve** and the **smqueue** modules are installed.
We have defined functions with no parameters and return True or False if the module starts/stops correctly.
```sh
$ init_sipauthserve()
$ stop_sipauthserve()
$ init_smqueue()
$ stop_smqueue()
$ init_transceiver()
$ init_openbts()
```
The main function to launch the OpenBTS module is :
```sh
$ launch_openbts()
```