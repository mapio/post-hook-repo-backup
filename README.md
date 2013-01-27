post-hook-repo-backup
=====================

This repository contains two simple WSGI applications that "backup" a remote
repository that has a POST post-receive hook (e.g., GitHub or BitBucket).

To setup the backup, first intsall the suitable application on a public web
server so that you can get a reachable URL to which the repository hosting
service can make a POST.

Then follow the provider specific instructions:

* [GitHub](https://help.github.com/articles/post-receive-hooks),
* [Bitbucket](https://confluence.atlassian.com/display/BITBUCKET/POST+Service+Management).

You can automate the setup of GitHub hooks using [clhub](https://github.com/mapio/clhub).
