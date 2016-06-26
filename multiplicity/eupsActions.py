"""
"""
import os
import glob
__all__ = ['eupsPkgName']


def eupsPkgName(repo):
    """
    """
    installFile = os.path.join(repo, 'Sconstruct')
    lines = None
    if not os.path.exists(installFile):
        return None
    with open(installFile, 'r') as fp:
        counts = 0
        lines= fp.readlines()
    if lines is None:
        raise ValueError('Nothing read in')
    for line in lines:
        if 'SConstruct' in line:
            vals = line.split('"')
            
    fname = vals[-2]
    return fname



