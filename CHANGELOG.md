# Changelog
<!-- ### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security -->

All notable changes to this project will be documented in this file. This project adheres to [Semantic Versioning](http://semver.org/).

## [1.5.2] - 2025-03-13

### Fixed

- Fixed invalid syntax during v2 and v7

## [1.5.1] - 2025-03-10

### Fixed

- Fixed missing `KingsData` causing crash

## [1.5.0] - 2024-11-20

### Added

- Added in-game walkthrough

### Fixed

- Fix "NotImplementedError" in the phone and other NPC interactions

## [1.4.18] - 2024-06-23

### Fixed

- Various bug fixes to the phone and characters

## [1.4.17] - 2024-06-05

### Fixed

- Fixed missing `points` (on save) causing crash
- Fixed missing `mood` (on save) causing crash
- Fixed instances where `kiwii` was crashing due to old data

## [1.4.15] - 2024-06-04

### Fixed

- Fixed missing `points` attribute causing crash
- Fixed missing `mood` attribute causing crash
- Handle instances where `relationship` is not the expected data type

## [1.4.14] - 2024-06-02

### Added

- Added clear persistent data button to settings

### Changed

- Updated uuid format to comply with latest server updates
- Various optimisations to the phone
- Various optimisations to the Character classes

### Fixed

- Fixed phone missing applications
- Fixed messenger missing contacts
- Fixed NPCs missing text messages
- Fixed relationship app showing Friend for all girls
- Fixed missing kiwii.posts causing game crash on saves
- Fixed missing "mood" property on characters causing crash
- Fixed npc relationships being the wrong data type
- Fixed server infinitely retrying connection causing lag during H-scenes
- Various save compat fixes

## [1.4.13] - 2024-05-06

### Fixed

- Fixed relationship app not showing the correct relationship status

## [1.4.12] - 2024-04-25

### Added

- Added Lovense integration

### Fixed

- Fixed crash during phone_setup

## [1.4.11] - 2024-04-18

### Fixed

- Fixed bold text in alert popup being unreadable
- Fixed server url causing lovense crash
- Fixed simplr missing from phone

## [1.4.10] - 2024-04-15

### Fixed

- Fixed old kiwii image missing from image remap
- Fixed applications missing app icon image
- Fixed CharacterService.get_user_by_str not returning a user
- Fixed notification error in Messenger

## [1.4.9] - 2024-04-09

### Added

- Added choice guide to V1

### Removed

- Removed Calendar and Tracker from the phone

### Fixed

- Fixed various minor issues

## [1.4.8] - 2024-03-17

### Changed

- Changed how the phone handles notifications to reduce lag and improve user experience

### Fixed

- Fixed character object inheritance causing weird save issues

## [1.4.7] - 2024-03-01

### Fixed

- Fixed lag due to phone screen prediction. We have had to remove the notification system for now. We will work on fixing the lag and re-adding the notification system in a future update.

## [1.4.6] - 2024-02-28

### Fixed

- Fixed relationships showing as Friend in the phone app
- Fixed Car Ambience bleed in v11 scene 34

## [1.4.5] - 2024-02-28

### Fixed

- Fixed path builder starting location grid
- Attempted fix for UI lag

## [1.4.4] - 2024-02-01

### Fixed

- Fixed Charli's name typo causing game crash during murder mystery

## [1.3.22] - 2024-01-28

### Added

- Added gallery unlock button to steam edition

### Changed

- Updated dependencies and submodules

## [1.3.21] - 2023-11-16

### Fixed

- Fixed various typos (Thanks to @MenehuneP99green)

## [1.3.20] - 2023-11-04

### Fixed

- Fixed blank achievements page ([#433](https://github.com/College-Kings/College-Kings/issues/433))
- Fixed incorrect achievement ATL name causing crash ([#435](https://github.com/College-Kings/College-Kings/issues/435))

## [1.3.19] - 2023-10-14

### Fixed

- Fixed not being able to delete username in kiwii ([#430](https://github.com/College-Kings/College-Kings/issues/430))
- Fixed MC's profile picture being reset to default ([#431](https://github.com/College-Kings/College-Kings/issues/431))
- Fixed achievements causing game crash ([#432](https://github.com/College-Kings/College-Kings/issues/432))

## [1.3.18] - 2023-10-11

### Added

- Added ck2 episode 2 banner

### Fixed

- Fixed missing timer_bar screen ([#427](https://github.com/College-Kings/College-Kings/issues/427))
- Fixed missing recap jump

### Changed

- Updated what's new news post

- Updated characters module
- Updated phone module
- Updated reputation module
- Updated screens module
- Updated tl module
For more information on module updates see College Kings 2 changelog
