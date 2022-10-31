#!/usr/bin/python
import subprocess
import sys
import os
import tempfile
if sys.version[0] == '3':
    import urllib.request as url
    from shlex import quote
else:
    import urllib as url
    from pipes import quote
    if pip_options:
        if isinstance(pip_options, list):
            options = [quote(option) for option in pip_options]
            cmd.extend(options)
        else:
            raise TypeError('pip_options passed to install must be a list')

    cmd.append('install')SELECT DISTINCT neighborhood 
FROM nomnom;
SELECT DISTINCT cuisine 
FROM nomnom;
SELECT * 
FROM nomnom
WHERE review >= 4;
SELECT * 
FROM nomnom 
WHERE cuisine = ' Italian '
   AND price = '900$';



    if install_options:
        if isinstance(install_options, list):
            options = [quote(option) for option in install_options]
            cmd.extend(options)
        else:
            raise TypeError('install_options passed to install must be a list') 

    if use_pep517 is True:
        cmd.append('--use-pep517')
    elif use_pep517 is False:
        cmd.append('--no-use-pep517')

    if requirements:
        cmd.append('-r')
    
    pkg = quote(pkg)
    cmd.append(pkg)

    subprocess.check_call(cmd)

