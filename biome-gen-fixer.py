from argparse import ArgumentParser
from gzip import BadGzipFile
from os import getcwd
from os.path import exists
import sys
from time import time
from nbt import nbt

class BiomeGenFixer():
    end_choices = [
        'betterendforge:betterend_biome_provider',
        'byg:bygend'
    ]

    nether_choices = [
        'byg:bygnether'
    ]

    def __init__(self):
        self.parser = ArgumentParser(
            description='biome-gen-fixer.py'
        )
        self.parser.add_argument('-l', '--level', help=f'level.dat directory. Defaults to {getcwd()}', default=getcwd())
        self.args = self.parser.parse_args()
    
    def get_level_file(self):
        level_dir = f'{self.args.level}/level.dat'
        if exists(level_dir):
            print("Parsing level.dat...")
            try:
                self.nbt_file = nbt.NBTFile(level_dir)
            except BadGzipFile as e:
                print(f"I'm sorry, but the NBT file you entered was not valid. Make sure you entered the right one and that it is valid. ({e})")
                sys.exit()
            t = time()
            print("Making a backup...")
            with open(level_dir, 'rb') as f:
                with open(f'{self.args.level}/level_backup_{int(t)}.dat', 'wb') as b:
                    b.write(f.read())
        else:
            print(f"level.dat not found. Looking in directory {self.args.level}. Are you sure you placed it correctly?")
        return self.nbt_file
        
        

if __name__ == "__main__":
    bgf = BiomeGenFixer()
    from rich import inspect
    f = bgf.get_level_file()
    dimensions = ["minecraft:the_end", "minecraft:the_nether"]
    end_value = f["Data"]["WorldGenSettings"]["dimensions"][dimensions[0]]["generator"]["biome_source"]["type"]
    nether_value = f["Data"]["WorldGenSettings"]["dimensions"][dimensions[1]]["generator"]["biome_source"]["type"]
    print(f"Changing value type of biome source in dimension {dimensions[0]} from {end_value} to {bgf.end_choices[0]}")
    end_value = bgf.end_choices[0]
    print(f"Changing value type of biome source in dimension {dimensions[1]} from {nether_value} to {bgf.nether_choices[0]}")
    nether_value = bgf.nether_choices[0]
    bgf.nbt_file.write_file()
