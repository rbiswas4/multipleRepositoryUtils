"""
module for tools to obtain sequences of directoris that may house repositories
of interest
"""

import os
import git

__all__ = ['absPathsIn', 'remoteChar']
def absPathsIn(dirname):
    """
    return an iterator to a sequence of absolute paths to directories that
    are located.
    
    Parameters
    ----------
    dirname : directory directly under which the repositories live
    
    Returns
    -------
    generator of absolute paths to the directories

    Examples
    --------
    >>> dirs = multiplicity.absPathsIn('/Users/rbiswas/src/LSST/')
    >>> for dirname in dirs:
    >>>     print(dirname)
    """
    res = os.walk(dirname, topdown=True)
    topdir, dirList, filenames = res.next()
    return (os.path.join(topdir, dirname) for dirname in dirList)

def remoteChar(gen, likeDesired):
    """
    generating function to filter git remotes using a function likeDesired

    Parameters
    ----------
    gen : generator to a sequence of strings
        the strings are absolute paths of repositories that will be checked
        to be of the class desired
    likeDesired : callable, returning a boolean
        user defined callable function which takes in an absolute path as a
        parameter and returns True if the repository satisfies certain
        characteristics and False otherwise

    Examples
    -------
    """
    for repo in gen:
        g = git.cmd.Git(repo)
        remoteString = g.remote(verbose=True)
        if likeDesired(remoteString):
            yield repo

