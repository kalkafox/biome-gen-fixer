# biome-gen-fixer

A python 3 utility with the use of @twoolie's [NBT](https://github.com/twoolie/NBT) library to fix dimension generation settings.

This works by accessing a `level.dat` of your choosing (it is recommended to make a backup of your world, but the utility will hold a backup of the file before doing anything with it anyway) and checking the biome source settings for The End and The Nether respectively. Some custom generators (Terraforged in this instance) has a habit of defaulting the biome source generator settings of both of these dimensions to vanilla. What this will cause is biome splattering and mainly lots of conflicting terrain features in both dimensions respectively, causing some structures to not appear.

In general, this issue is not needed if you are using a custom generator that does not set the world settings appropriately, but if you are using biome gen mods like Better End: Forge, Better Nether: Forge, or Biomes You'll Go, the script will ask if you do and set the generator settings according to what is the most compatible.

Further research can conclude on which ones will make a difference for generation, but it is assumed that either of the generator settings will integrate with eachother unless the mod author says otherwise.

