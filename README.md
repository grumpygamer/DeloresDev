This is the source code to **Delores: A Thimbleweed Park mini-adventure**. Read [Grumpy Gamer](http://grumpygamer.com/delores_dev) for more background.

## License
The source code for Delores is made available under a custom license. See [LICENSE.md](LICENSE.md) for more details.

This repository does not include the source code for the engine, it is just the source for the game Delores. To run the Delores source code, you will need to download a development version of the engine [here](https://thimbleweedpark.com/deloresdev). If you wish to share your changes or modifications, direct people to the preceding page to download the development engine as the [LICENSE.md](LICENSE.md) does not permit redistribution of the engine.

The Delores source is intended solely for personal use to learn and explore. Please respect our choice to release the source by using it as intended.

## Directions
Clone the repository to your local machine. It is assumed that these files are placed in a `DeloresDev` directory.

Download and extract the DeloresDev engine executable from [here](https://thimbleweedpark.com/deloresdev). The engine executable can go anywhere.

Run it once. You will get an error, but that's expected.

Find the `Prefs.json` file that was created.

On Windows:
```
%AppData%\Terrible Toybox\DeloresDev\Prefs.json
```
On Mac:
```
~/Library/Application Support/Terrible Toybox/DeloresDev/Prefs.json
```
On Linux:
```
~/.local/share/Terrible\ Toybox/Delores/Prefs.json
```
Add the following line to the `Prefs.json` file:
```
devPath: "/Path/To/DeloresDev"
```
If you're on Windows, use `/` as a path separator and not `\`

Run the executable again and the game should start.

## Support
If you're looking for help or to help others, please visit [the Thimbleweed Park Forums](https://forums.thimbleweedpark.com/c/delores-engine/18).  

## Debug Console
The debug console can be closed by clicking on the `X` in the upper right. To make it reappear, press `control-TAB`.

If you right-click on the console title bar, more debug options can be found in the drop-down menu.

Add the following to `Prefs.json` to extend the screen to allow more room for the debug console.
```
debugExtraScreenWidth: 550
```
The debug console and debug windows use the amazing [ImGui](https://github.com/ocornut/imgui)

## Sound
All sound is done via **FMOD** and **FMOD** `.bank` files must be created or downloaded before audio can be enabled.

If you want to hear audio and aren't interested in creating new audio, the Delores **FMOD** `.bank` files can be downloaded from [here](https://thimbleweedpark.com/deloresdev). Extract and place both `.bank` files in `DeloresDev/Sounds/`

The **FMOD Studio Tool** can be downloaded [here](https://fmod.com/download). Build and place the `.bank` files in `DeloresDev/Sounds/MasterBank.bank` and `DeloresDev/Sounds/MasterBank.strings.bank`

Describing how to use **FMOD** is beyond the scope of this README.

## Dinky
Delores is coded in a custom language called **Dinky** that is based on and inspired by [Squirrel](https://github.com/albertodemichelis/squirrel).

If you point a browser to `DeloresDev/HelpDocsHtml/home.html` you will find the help files for the **Dinky** language. It is far from complete, hastily written, and probably riddled with spealling mistakes. You've been warned.

## Here be dragons
If this is your first time installing, I suggest you stop here and ensure everything works before proceeding.
If all you're interested in is code, you can also stop here.

## Art
The full art pipeline involves a slew of Python scripts that proved to be an installation nightmare so they are not included.

If you want to add art, place a `.png` for the element in the `Delores/Dev/Images/RoomName` and then run `Bin/munge_images.py` and the sprite sheets will be created.

To do this, you need to have [TexturePacker](https://www.codeandweb.com/texturepacker) installed and working and define an enviornment variable `DELORES_GAMEROOT` that points to your `DeloresDev` directory.

## Animation
Animation control files can be found in `DeloresDev/Animation` and are `.json` files. The tool that created these for Thimbleweed Park is long gone.

## Translations
The version of Delores avaliable in online stores does not include any translation.  This repo version has all the text stripped and wrapped and placed into `DeloresDev/Data/Translations_en.tsv`.  See the help doc on Translations or look at `DeloresDev/Scripts/Helpers/TranslationHelpers.dinky` for more information.

If you're working on a translation you'd like released with the next update of Delores, visit the [Thimbleweed Park Forums
](https://forums.thimbleweedpark.com/c/delores-engine) for more information and to connect with others doing translations.

## Wimpy
The tool to add and position objects is called **Wimpy** and it can be download [here](https://thimbleweedpark.com/deloresdev)

When you first start **Wimpy**, you will see a blank window. To load a `.wimpy` file, drag it into the window. The `.wimpy` file must come from the `DeloresDev/Wimpy` folder and the project directory structure must remain as it is in the repo.

## Known Issues
- Dinky language documentation is sparse.
- There is a bug in the garbage collection for Dinky, so I turned it off. You will notice memory usage climbing, but it's not likely to be an issue unless you're playing for hours and hours.
- Translation system is only half-done, see `TranslationHelper.dinky` for more information.

## Credits
- Delores Programming by Ron Gilbert and David Fox.
- Thimbleweed Park Art by Mark Ferrari, Octavi Navarro, and Gary Winnick.
- Thimbleweed Park Music by Steve Kirk.
