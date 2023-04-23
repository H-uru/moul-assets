# Contributing
We are glad that you are interested in contributing to moul-assets! We happily accept contributions, including:
- bug reports
- bug fixes
- art assets
- and much more!

Please take a moment to read these guidelines to ensure your contributions are accepted.

## Project Goals
The goal of the moul-assets project is to provide baseline assets for the MMORPG [Myst Online: Uru Live](https://mystonline.com) to be used in the [Plasma Engine](https://github.com/H-uru/Plasma). In the interest of doing so, we have identified these project goals:
- providing a coherent, well-tested content baseline for [Myst Online: Uru Live](https://mystonline.com) shard operators
- conservatively improving the base game Ages as created by Cyan Worlds, Inc. with objective bug fixes and enhancements
- improving the player experience
- integrating new content/Ages that serve a clear purpose in enhancing Myst Online: Uru Live as a video game
- avoiding nontrivial breaks in compatibility with the official **Myst Online: Uru Live (again)** game run by Cyan Worlds, Inc.

Further, we have identified these non-goals:
- accepting all fan created content
- accepting fan created content published on any particular shard, including the official **Myst Online: Uru Live (again)** game run by Cyan Worlds, Inc.
- accepting fan content geared toward role-playing done on any particular shard, including the official **Myst Online: Uru Live (again)** game run by Cyan Worlds, Inc.
- supporting exploit-based gameplay

These are tasks that run contrary to the project's priorities stated above, and as such are not likely to be accepted if submitted for inclusion. Any changes implementing these are best maintained on an independent fork.

## Getting Involved
Real-time discussion with team members and other contributors is an excellent way to begin contributing. We welcome feedback and discussion of proposed changes. Active maintainers can be found on the Guild of Writers IRC channel:
- Server: irc.guildofwriters.org:6667
- Channel: #writers

We also use the [Guild of Writers' forum](https://forum.guildofwriters.org/viewforum.php?f=3) for more permanent discussions. Further, many team members can also be found on the [OpenUru discord](https://discord.com/invite/tVknpHQ).

## Reporting Bugs and Requesting Features
We use GitHub's [issue tracker](https://github.com/H-uru/moul-assets/issues) to list bugs and feature requests. Good bug reports tend to have:
- a summary or background
- steps to reproduce the bug, the more specific, the better!
- what you expect to happen
- what actually happens
- any other pertinent notes, such as why you think the issue is happening and any mitigation you attempted

## Submitting Changes
Changes to moul-assets generall fall under two categories: objective and subjective. Before submitting any changes to the repository, you will need to [request access](https://guildofwriters.org/assets_repo) to the LFS store.

### Submitting Objective Changes
Objective changes tend to be limited in scope and are generally minor adjustments or fixes to content already accepted to the repository. These changes should require limited discussion and should demonstrate a clear and apparent improvement to the game. These changes may be developed and submitted using [GitHub Flow](https://guides.github.com/introduction/flow/index.html). To propose changes to the repository:
- fork the repository and make your changes as described by GitHub flow
- open a pull request and ensure that all test coverage and continuous integration passes
- document in the pull request body what you have changed and why

### Submitting Subjective Changes
Subjective changes tend to be larger in scope, such as a new Age or expansion of a previously existing Age, and generally require discussions around myriad aspects of their development. This can be a lengthy process involving many revisions to your contribution. For this reason, we do not accept pull requests for subjective changes until the changes have gone through an external content review process. There is currently no accepted content review process; we leave it up to the contributor to revise their content with discerning member(s) of the Age creation and development community. For a subjective change to be considered, an endorsement from at least *one* (1) discerning member of the Age creation and development community must be provided. If you need assistance with identifying a process or a discerning member, contact a [maintainer](https://github.com/H-uru/moul-assets/people).

Subjective changes to the game are, by their very nature, subjective, hence our relucance to impose and document a specific review process. However, all subjective submissions should:
- be relatively bug-free
- be tested against the Myst Online: Uru Live version of the [Plasma Engine](https://github.com/H-uru/Plasma) by the creator (at minimum)
- match the art style of the currently accepted content both visually and audibly
- not look like a "video game"
- have largely correct lighting

Ensuring contributions meet these criteria should be done as part of the preliminary review process done outside of this repository.
