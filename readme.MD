# cli_worms

*A command line interface implementation of Worms - or something.*

## Implemented so far!

### 1. Set team + worm names

![Setting team / worm names](images/set_team_names.gif)

### 2. ... or randomly generate team / worm names

![Randomly generating team / worm names](images/random_names.gif)

### 3. Worms fall into the sea / game ends once a team has no worms left!

![End game condition](images/end_game_condition.gif)

### 4. `left` and `right` commands control movement

![left and right commands in action](images/left_right_command.gif)

### 5. `ljump` and `rjump` to jump

![jjump and rjump commands in action](images/ljump_rjump_commands.gif)

### 6. `shoot` to fire an arrow in a given direction

![shoot command in action](images/shoot_command.gif)

### 7. `mine` to lay a landmine for a given number of frames

![mine command in action](images/mine_command.gif)

## #TODO

### 8. More intelligent frame refresh

Unfortuantely the really doesn't work very well on computers slower than my new build (AMD Ryzen 3600) - need to consider a way to only update certain parts of the frame, e.g. considering which worm is currently under control and which grid coords can be possibly be affected, ignoring those that cannot and just printing them directly (as string rather than chars) from some sort of buffer.

### 9. Damage

At the moment arrows don't do anything - perhaps they should push back enemy worms so you can use this to make them fall into the gaps? Mines also cause no damage - gravity does not seem to be working correctly once the platform underneath a worm disappears.

### 10. A bigger arsenal?

The game is pretty limited using one unicode character per grid pixel so I might choose to keep it simple. Not sure if these constraints will allow for any sort of reasonable implementation of banana bomb, sheep bomb, ninja rope etc.! :D

![Fully fledged arsenal in the original game](https://66.media.tumblr.com/41116d6c3facaa57976f9c3d0dcbb508/tumblr_nuwadjHK3z1skasmxo1_500.gif)