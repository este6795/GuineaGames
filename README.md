# Guinea Games! 
Empty Right Now!....
Buuuuuuut....
Mini-game logic is in place!

## Minigame Documentation
Before running any of the files in minigame please do the following: 
- Ensure that Python 3.10.x - 3.12.x is installed as pygame only functions on older versions of Python
- Next in the terminal please run `pip install pygame` if you are asked to upgrade pip/new version please do so
- After installing pygame please run all files in the following order:
   - setting.py
   - asset_loader.py (work in progess)
   - maze_generator.py
   - maze.py
   - hud.py (work in progress)
   - enemy.py
   - fruits.py
   - player.py
   - game.py
   - main.py
- Finally enjoy!

## The Maze
🐹 Guinea Pig vs. Fruit-Hoarding Dragon! 🐉
You’re a brave little guinea pig with a big appetite and an even bigger problem: you’ve been plopped into a fruit-filled maze… guarded by a hungry dragon who thinks guinea pig is the tastiest snack of all! 🍓🔥
Your mission? Snatch every last fruit before the dragon snatches you.
Use WASD or ↑↓←→ to scurry, squeak, and sprint your way through twisty tunnels.
If the dragon catches you—crunch! Game over.
But if you collect all the fruit first? Victory is yours! 🎉
Just don’t get too comfy… this maze has a funny way of calling you back for seconds. 🍒👀


## Updates: 
- 10/31/25 Repo initialized with basic maze logic
- 11/4/25 New version released with emphasis on OOP concepts
- 11/5/25 Player logic, enemy spawn logic, maze generation logic, and other various features added
- 11/6/25 Fruit logic added, along with win/lose conditions, and logic for looping in maze
- 11/11/25 Basic speed logic added, still a work in progress
- 11/14/25 Speed logic implemented in levels of 1-10, attempting to fix asset loading logic

## Future Implementations/Fixes
1. As of now only "background" audio is loaded, interestingly enough pygame does not like using relative pathing, and therefore assets need to be stored in the same file directory
2. "Random" maze generation is not implemented correct, thus only one map is being loaded at the moment
3. "Random" spawns of fruits, enemies, and players are being handled by a set seed for debugging purposes, in the future it will be truly random (set seed will be removed)
4. asset_loader.py is not functioning properly due to pygame not loading relative pathing properly and needs to be fixed
5. hud.py is incomplete and at the moment it only has score logic
6. Sprites of fruits, the enemy, the player, as well as the maze itself are not loaded, and instead are being represented by tile colors.
7. Enemy movement logic at the moment causes the enemy to be stuck in the center unless the player is in the direct path to the opening
8. Moreover, enemy movement logic forces the enemy to try to move directly to the player, this should instead have an element of randomness


## Misc
If any bugs happen please report them on the discord, and I will take a look at them.
Otherwise have a great time with this little mini-game.
