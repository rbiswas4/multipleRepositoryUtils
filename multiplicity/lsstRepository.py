from .repoActions import *
from .eupsActions import *
from .repositorylists import *
import eups
import glob

__all__ = ['LocalLSSTRepos']


class LocalLSSTRepos(object):

    def __init__(self, universalDir, forgetRepos=None):

        self.repoList = list(absPathsIn(universalDir))
        if forgetRepos is not None:
            self.repoList = list(repo for repo in self.repoList
                                 if repo not in forgetRepos)

        self.lsstrepos = list(repo for repo in self.repoList
                              if self.islsstRepo(repo))

        self.dirtyRepos = list(listDirtyRepos(self.lsstrepos))
        if len(self.dirtyRepos) > 0:
            raise ValueError('Repos dirty', self.dirtyRepos)  
        

    @staticmethod
    def islsstRepo(repoPath, remoteName='origin'):
        """
        return True if local git repository at repoPath satisfies certain
        conditions deemed necessary for being a lsstRepo. Here the conditions
        are that it should have a remote called origin in the github lsst repos
        'githhub.com/lsst'

        Parameters
        ----------
        repoPath :

        remoteName :

        Returns
        -------
        Bool
        """
        val = False
        repo_url = get_remoteURL(repoPath=repoPath, remoteName=remoteName)
        if repo_url is None:
            return val
        if 'github.com:lsst' in repo_url:
            val = True
        tablefile = glob.glob(repoPath+'/ups/*.table')
        if len(tablefile) == 0:
            val = False
        return val
        
    def declareEupsWithTag(self, versionName, tag):
        """
        """
        for repo in self.lsstrepos:
            packageName = eupsPkgName(repo)
            eups.declare(productName=packageName,
                         versionName=versionName,
                         productDir=repo,
                         eupsPathDir=None,
                         tag=tag)

