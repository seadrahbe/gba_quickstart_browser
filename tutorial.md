# Getting Started

## Prerequisites

The only things you need for this tutorial are a web browser and a GitHub account. 
Go to [GitHub Signup](https://github.com/signup) to create a new GitHub account if you don't have one already.
After you've logged in to GitHub, you're ready to begin the tutorial.

## Creating the Codespace

A Codespace is a GitHub feature that lets you explore a GitHub repository, create and modify files, and run code from your web browser. 
It's free up to a generous quota of usage and doesn't require any downloads or manual setup.

1. Open https://github.com/alope107/gba-quickstart in a new tab, and keep this tutorial open for reference.
1. On the **gba-quickstart** repository page, click the green "Use this template" button near the upper right of the window.
1. Select "Create a new repository." This creates a copy of the files in a new repository under your own GitHub username.
1. Name the repository what you want to call your game and add an optional description. Leave the other options at their default values.
1. Click "Create repository" and wait a few moments for the repository to be generated. When it's finished, you'll see the same files that were in **gba-quickstart**, now copied to your own repository.
1. Click the green "Code" button at the top right of the file list. In the popup, switch to the "Codespaces" tab and click "Create codespace on main."
1. The Codespace opens and starts to build in a new tab. The first time you do this for a repository it takes about 2-5 minutes. It'll be faster when you re-open the Codespace later. If you're interested, you can click on the blue "Building codespace" link on the bottom right to see the logs as it builds.

Your Codespace is finished building when you see a list of files on the side, a README.md file in the center view, and a terminal at the bottom of the screen.
   
## Compiling the sample game

You'll run commands in the Codespace terminal to compile the game so you can run it. When you create the Codespace, its working directory is `/workspaces/NAME-OF-YOUR-GAME`, also known as the root directory of your repository. You have other directories in your repository, the most important of which is `game/`. 


1. In the left view panel, you can click the arrow next to the `game/` directory to open it and see the files inside.
1. In the terminal at the bottom, type `cd game` and hit Enter to move the working directory to the `game/` directory so you can compile the files there.
1. Type `make` and hit Enter. This compiles the game files into a ROM, taking about a minute for this demo game.

This process takes a minute or so because it's the first time the game has been compiled. 
If you make changes and compile again, it'll be faster because it'll only have to compile what was changed.
When the compile step is finished, you'll see a new file under the `game/` directory called `game.gba`, and also some other files that you can ignore.

## Running the sample game

Now you can run the sample game you compiled. This Codespace includes a GBA Emulator that can play `.gba` ROM files.

1. In the left file picker, click on `tools.md` to open it in the main view window.
1. Click on the "Emulator" link to open the web GBA emulator. It should open in a new tab.
1. You should see your `.gba` ROM file listed. Click it and the emulator should start running the game! Use the arrow keys to move the yellow sprite around.
   
## Making changes to the sample game code

1. Switch back to the Codespace tab.
1. In the left file picker, choose `game/src/Main.cpp` to open it in the main view window. This file holds the game logic.

You'll make two changes: changing the backdrop color and changing the speed at which the sprite moves. 

1. Find the line of code in `Main.cpp` where the backdrop color is set. Instead of `(0, 0, 0)` (black), change it to `(31, 0, 0)` (red).
1. Find the line where the speed is set. Change the speed from `1.5` to `5.5`.

Each time you want to test changes to the code, you need to recompile the ROM. 

1. Check that the terminal is still in the `game` directory (`game` should show up as the end of the path).
1. Type `make` and hit Enter to rebuild the game with your new changes. If it fails, check the error message to see if there were any mistakes in the code you changed, like a missing comma or bracket.
1. Switch back to the emulator tab and **refresh the page**. If you closed the tab, you can always reopen it by opening `tools.md` and clicking the Emulator link again.
1. Select your ROM again.
1. You should see your new backdrop color! Use the arrow keys to see the character zip around at high speed.

Even though you've made changes in your Codespace and compiled the new ROM, everything gets deleted when a Codespace disappears.
Continue the tutorial to save your changes permanently.

## Committing and pushing your changes

You've made some valuable changes and it's important to make sure those changes are saved. 
In GitHub Codespaces, you should always both **commit** and **push** your changes frequently to avoid losing your work. 
If you delete a codespace and it has unpushed changes, they are lost forever!

If you're familiar with git, you can use your normal command-line workflow in the Codespace terminal to add/commit/push your changes as you would in any repository. 
If you're new to git, you can do the same things with the git plugin in Codespaces. 

1. On the left of your editor there should be an icon with a couple of circles, one of them blue with a number in it. If you hover over it, it should say "Source Control." Click that icon.
1. The sidebar will show that `Main.cpp` is changed. Click the plus sign that appears to the right of it so that it moves to the "Staged Changes" sidebar section.
1. Above the Commit button, write a short message describing your changes, like "Changed background to red and increased player speed."
1. Click the Commit button.
1. Click on the new Sync Changes button that shows up. Click OK if there's an additional popup.

Great! You've pushed your changes!
**Make sure to do this each time you make a new update to your game.**
This makes sure you have your changes saved, even if you delete the codespace. 
If you're unhappy with a commit, you can also undo or revert commits to go back to a previous snapshot of your game development. 

## Editing a game sprite

You've already edited the game logic by modifying `Main.cpp`. Now, you'll edit the player sprite. 

1. Click on the icon with the two pieces of paper on the left bar to go back to the file select tab view.
1. Choose `tools.md` again, and this time open the LibreSprite Sprite Editor. This should open LibreSprite in a new window.
1. Click "Open File".
1. Double-click through the folders to get to `NAME-OF-YOUR-GAME > game > graphics > dot.bmp`. This opens the sprite for editing. You may need to zoom in using (Ctrl-+) or (Cmd-+) depending on your operating system.
1. Use the palette on the left to select a color, and use the mouse to draw a smiley face on the circle or make any other changes that strike your fancy.
1. Click `File -> Save` in the menu at the top of the editor to save your edited sprite back to the Codespace.
1. Switch back to the Codespace tab so you can recompile the ROM again. Even a small change to a sprite needs a recompile of the whole ROM! 
1. Make sure the terminal's working directory is the `game/` directory, and run `make`.
1. Switch back to the emulator tab and refresh the page.
1. Select your ROM from the list to reopen it. You should see your new sprite! Play around and enjoy.

Remember, even though your sprite change appears in the Codespace, it hasn't been committed and pushed to the repository yet. 
Go back to the code editor and follow the same steps from the previous section to commit and push the changes to `dot.bmp`.

## Next steps

Congratulations! You are now a Game Boy Advance homebrew developer! 
There is a lot more to learn, but you're well on your way. 
Butano comes preloaded with a number of examples you can find in `third_party/butano/examples`. 
You can compile them one at a time by navigating your terminal to one of those example directories and running `make`. 
Afterward, the ROM should show up in the emulator page and you can test it out.

When you want to return to your codespace later, go back to your repository, click on the green Code button again, select Codespaces. 
You should see your existing Codespace still there for you to pick up where you left off.

## Resources

- [Butano Docs](https://gvaliente.github.io/butano/)
- [GBA Dev Discord](https://discord.gg/ctGSNxRkg2)
- [GBA Dev Site](https://gbadev.net/)

The GBA Dev Discord is an excellent place to get help developing your game. 
If you run into problems with this environment itself, e.g. the emulator or LibreSprite doesn't work, please [open an issue here](https://github.com/alope107/gba-quickstart/issues). 
As a short-term fix, you can try deleting your codespace and restarting it to see if that fixes the issue. 
JUST MAKE SURE YOU'VE COMMITTED AND PUSHED ANY CHANGES YOU WANT TO SAVE!

Have fun! More tutorials may be added later to help you learn more.

## Appendix: Terminal command reference

- `pwd`: **P**rint **W**orking **D**irectory. Run `pwd` to print a line to the terminal showing you the directory your terminal window is running commands in.
- `cd`: **C**hange **D**irectory. Type the directory after `cd` to move your terminal's working directory there.
  - `cd game`: Navigates to the directory `game/` if `game/` is under your working directory, otherwise prints an error because it can't find it.
  - `cd ..`: Navigates to the parent directory, or in other words whatever directory holds your working directory.
- `git add FILE-PATH`: Stages a file to get ready for a commit to git.
  - `git add Main.cpp`: Stages `Main.cpp` if it's under your working directory, otherwise prints an error because it can't find it.
  - `git add .`: Stages every modified file, no matter the location.
- `git commit -m "MESSAGE"`: Commits all the files you've staged, with a message to label the commit.
- `git push`: Pushes your changes to the repository.
