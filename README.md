[![Download](https://api.bintray.com/packages/glportal/generic/glportal-editor/images/download.svg) ](https://bintray.com/glportal/generic/glportal-editor/_latestVersion)
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
- [Download latest version](https://bintray.com/glportal/generic/glportal-editor/_latestVersion) of GlPortal editor. *Don’t unzip* !
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
If you want to use the development version of the map editor you can symlink it to your blender plugin directory with the linkExtension script for more information call the linkExtension script with the h option.
