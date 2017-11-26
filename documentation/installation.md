# Installation

## Stable version
See README.md in main directory.


## Development version

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
