"""
This is a module which uses absolute paths to local git repositories to
return information about them, or to do git operations on the repositories.
"""
import git

__all__ = ['listDirtyRepos', 'get_remoteURL', 'switchBranchToMaster']
def listDirtyRepos(repoPaths):
    """
    return a sequence of dirty repositorieso

    Parameters
    ----------
    repoPaths : sequence of abs path to repos 

    Returns
    -------
    A generator to the sequence of absolute paths to repositories in repoPaths
    that are dirty
    """
    for repo in repoPaths:
        gitRepo = git.Repo(repo)
        if gitRepo.is_dirty():
            yield repo

def get_remoteURL(repoPath, remoteName='origin'):
    """
    return the url to the remote repository of a local git repository

    Parameters
    ----------
    repoPath : string, mandatory
        absolute path to a local git repository
    remoteName : string, optional, defaults to 'origin'
        name of the remote repository

    Returns
    -------
    string containing the url of the remote repository.

    Examples
    --------
    >>> remoteURL = get_remoteURL('/Users/rbiswas/src/LSST/sims_catUtils')
    """
    try:
        repo = git.Repo(repoPath)
    except:
        return None
    url = repo.remotes[remoteName].url
    return url

def switchBranchToMaster(repoPath):
    try:
        repo = git.Repo(repoPath)
    except:
        print('Not a valid git repository')
        return None
    


