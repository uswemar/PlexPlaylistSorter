# Changelog
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]
- Add the option to output the results as a .csv
- Add argparse to be able to use the script both via CLI and interactively


## [1.1.0] - 2019-05-30
### Added
- Option to use a config.ini instead of adding auth values to main .py script

### Fixed 
- Spelling, README, and row references

### Changed
- PlexServer auth variables from function to global
- Playlist selection from hard-coded to a user input solution using the PlexAPI utils.choose() function
- Removed the version from the filename and renamed the script to PlexPlaylistSorter.py


## [1.0.0] - 2019-05-29
### Added
- First version, 1.0.0, uploaded
