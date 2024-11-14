# MOUL Assets
This repository is used to host assets used in Cyan World's Myst Online: Uru Live game in both their source and compiled form. The purpose of this repository is to track fan contributions to the game content and be used as a source to build a functioning asset distribution server for the Myst Online: Uru Live game.

## Related Projects
* [Plasma](https://github.com/H-uru/Plasma) - CyanWorlds.com Plasma Engine used by Myst Online: Uru Live.
* [moul-scripts](https://github.com/H-uru/moul-scripts) - Myst Online: Uru Live game scripts.
* [dirtsand](https://github.com/H-uru/dirtsand) - An open-source Plasma-compatible server project.
* [korman](https://github.com/H-uru/korman) - Blender plugin for creating ages for Cyan Worlds' Plasma engine.

## Browsing MOUL Assets
You may notice while browsing this repository online or after cloning on your own machine that most files seem to be small text files containing some kind of hash reference. This is because the MOUL assets repository is too large for (free) GitHub. We therefore use an external Git Large File Storage server. The easiest way to download the entire repository is to use `git lfs clone`. Do keep in mind that the repository is very large (over 20GB), so make sure to run this command in a location with sufficient space. You may also choose to enable Git LFS by default. You can find some basic information on the [Git LFS website](https://git-lfs.com/) or refer to the [Git LFS wiki page on pulling and cloning](https://github.com/git-lfs/git-lfs/wiki/Tutorial#pulling-and-cloning).

## Contributing
This repository is intended to track large binary files where diffs are impractical. All binary objects are stored on the Guild of Writers server to avoid incurring additional fees from GitHub. To prevent abuse/spam, the ability to push binary objects is restricted to approved users, even in your own fork. If you would like to contribute to this repository, you can request access [here](https://guildofwriters.org/assets_repo).

## Source Assets
Source assets in this repository must be complete and in a format that is trivial to export or compile for the Myst Online version of the Plasma engine. Therefore, the sources must be one of the following:
* A Korman/Blender `.blend` file
* A 3ds Max 7 `.max` file

Ancillary files such as audio and textures are permissible, however, code should be tracked in the appropriate repository. Absolutely no Blender 2.49/PyPRP `.blend` files will be accepted due to their inherent incompatibility with Myst Online.

## Compiled Assets
Compiled assets are the binary assets used directly by the game engine. Code files should be tracked in the appropriate repository.

## Help! I ran `git push` and only see a blinking caret!
As stated above, push access is restricted to approved users. You can request access [here](https://guildofwriters.org/assets_repo). If you have already been approved, then this is likely the result of a permissions error. Gitea, the solution we use for hosting the binary objects, disallows password authentication if you have enabled Two-Factor Authentication (2FA). You will need to create an API token on the [Guild of Writers Gitea](https://git.guildofwriters.org) and use that as your password when prompted for a password for https://git.guildofwriters.org.
