# ---------------------------------------------------------------------#
# Warlight AI Challenge - Attack Bot                                   #
# ============                                                         #
#                                                                      #
# Last update: 20 Mar, 2014                                            #
#                                                                      #
# @author Jackie <jackie@starapple.nl>                                 #
# @version 1.0                                                         #
# @license MIT License (http://opensource.org/licenses/MIT)            #
# ---------------------------------------------------------------------#

# Modified by Joe Coleman
#
# Original code has been modified for our CS 541 project to
# work with our modified map and split from the bot class to
# provide a convenient way for us to create new AIs

from bot import Bot, PlaceArmyBuilder, AttackTransferBuilder
from const import PLACE_ARMIES, ATTACK_TRANSFER, NO_MOVES
from math import fmod, pi
from time import clock

# AttacBot decides to attack enemy positions over spreading army out to neutral
# territory 
class AttacBot(Bot):
    def __init__(self, map_weights, heuristic):
        super(AttacBot, self).__init__(map_weights, heuristic)

     
    # Choose a random 6 regions from the ones supplied
    # options[0] is time limit
    ''' THIS SHOULD BE MODIFIED TO PICK OUT OF THE BOTTLE NECKED REGIONS 
        WE WILL USE options PROVIDED BY SERVER AND EVALUATE WHICH 
        LOCATION FOR PLACING TROOPS '''
    def pick_starting_regions(self, options):
        options = options[1:]
        priority = options.split()
        ordered_regions = sorting(priority)
#        shuffled_regions = MyRandom.shuffle(options)
        return ' '.join(ordered_regions[:6])

    # Places up to 2 armies on random regions
    ''' REPLACE SHUFFLED_REGIONS WITH TUPLE FOR split_last_update WHICH SPLITS 
        THE LIST OF REGIONS INTO player_owned , neighbors , outliers ''' 
    def place_armies(self, time_limit):
        placements = PlaceArmyBuilder(self.name)
        region_index = 0
        troops_remaining = self.available_armies
        owned_regions = self.map.get_owned_regions(self.name)  # returns a copy of references to owned regions
        shuffled_regions = MyRandom.shuffle(owned_regions)
        while troops_remaining:
            region = shuffled_regions[region_index]
            if troops_remaining > 1:
                placements.add(region.id, 2)
                region.troop_count += 2
                troops_remaining -= 2
            else:
                placements.add(region.id, 1)
                region.troop_count += 1
                troops_remaining -= 1
            region_index += 1
        return placements.to_string()

    # Currently checks whether a region has more than six troops placed to attack,
    # or transfers if more than 1 unit is available.
    def attack_transfer(self, time_limit):
        attack_transfers = AttackTransferBuilder(self.name)
        owned_regions = self.map.get_owned_regions(self.name)
        for region in owned_regions:
            neighbors = [region for region in region.neighbors]   # make a copy of references to neighbor regions
            while len(neighbors) > 1:
                target_region = neighbors[MyRandom.randrange(0, len(neighbors))]
                if region.owner != target_region.owner and region.troop_count > 6:
                    attack_transfers.add(region.id, target_region.id, 5)
                    region.troop_count -= 5
                elif region.owner == target_region.owner and region.troop_count > 1:
                    attack_transfers.add(region.id, target_region.id, region.troop_count - 1)
                    region.troop_count = 1
        else:
                    neighbors.remove(target_region)
        return attack_transfers.to_string()

    def sorting(items):
        #set up array for weight values
        int weights[len(items)]
        #get weight values for regions
        int x = 0 
        for i in items:
            weights[x] = self.region_weight[i]
            x = x+1

        sorted(weights, reverse=True)
        ordered_regions = items
        
        for x in range(0,len(items)):
            for i in items:
                if(i!= -1)
                {
                    if( weights[x] == self.region_weight[i])
                    {
                            ordered_regions[x] = i
                            i = -1
                    }
                }
        return ordered_regions
        


                

class MyRandom(object):
    @staticmethod
    def randrange(r_min, r_max):
        # A pseudo random number generator to replace random.randrange
        #
        # Works with an inclusive left bound and exclusive right bound.
        # E.g. Random.randrange(0, 5) in [0, 1, 2, 3, 4] is always true
        return r_min + int(fmod(pow(clock() + pi, 2), 1.0) * (r_max - r_min))

    @staticmethod
    def shuffle(items):
        # Method to shuffle a list of items
        i = len(items)
        while i > 1:
            i -= 1
            j = MyRandom.randrange(0, i)
            items[j], items[i] = items[i], items[j]
        return items
    @staticmethod
    def selectionSort(items):
        #sort by greatest weight value
