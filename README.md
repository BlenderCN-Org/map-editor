[![Download](https://img.shields.io/badge/download-latest_release-brightgreen.svg)](https://github.com/GlPortal/map-editor/releases/)
[![Build Status](https://travis-ci.org/GlPortal/map-editor.svg?branch=master)](https://travis-ci.org/GlPortal/map-editor)
[![Join the chat at https://gitter.im/GlPortal/glPortal](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/GlPortal/glPortal?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Join Chat](https://img.shields.io/badge/irc-join_chat-brightgreen.svg)](http://webchat.freenode.net/?channels=%23%23glportal&uio=d4)

# Radix Map Editor Blender Extension
The Radix Map Editor Extension allows Blender to import, edit, create and export Radix maps.

## Features
- Easy import and export of Radix maps
- Radix specific tool panels
- Preview with textures

## Installation
- Install [Blender](http://www.blender.org/download/)
- [Download the latest version](https://github.com/GlPortal/map-editor/releases/) of the Radix editor. *Don’t unzip* !
- Run Blender:
  - Select `File > User Preferences...`
  - Move to the Addons tab.
  - Click `Install From File...` in the bottom of the window.
  - Find the downloaded zip file and select it.
  - Find and check the `GlPortal XML Format` box. Wait a moment for activation to complete.
  - Find and click on right Arrow to display details and preferences.
  - Go to `Set up GlPortal data directory` and find GlPortal data directory.
  - Click `Save User Settings` and close the window.
If you are upgrading, you may need to restart Blender.

## Development
-   Install Blender
-   Clone or download this repository
-   Install the plugin
    -   Copy directory `glportal-editor` into Blender configuration folder `/home/user/.config/blender/VERSION/scripts/addons`
    -   use our script `linkExtension` which will create soft link of glportal-editor directory to blender configuration folder
-   Run Blender:
    -   Find and check the `GlPortal XML Format` box. Wait a moment for activation to complete.
    -   Find and click on right arrow to display details and preferences.
    -   Go to `Set up GlPortal data directory` and find GlPortal data directory.
    -   Go to `Set up GlPortal executable` and find GlPortal executable.
    -   Click `Save User Settings` and close the window. If you are upgrading, you may need to restart Blender.


## Usage of linkExtension

Open terminal in the main repository directory and type:

```
./linkExtension -b blender_version
```

Where the `blender_version` is replaced with your installed Blender version.


### Example
```
./linkExtension -b 2.77
```
