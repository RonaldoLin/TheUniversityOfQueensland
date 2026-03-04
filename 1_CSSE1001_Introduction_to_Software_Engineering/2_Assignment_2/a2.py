"""
CSSE1001 Assignment 2
Semester 2, 2020
"""
from a2_support import *

# Fill these in with your details
__author__ = "{{Xianglong LIN}} ({{45791439}})"
__email__ = "s4579143@uq.edu.au"
__date__ = "24/09/2020"


class Entity:
    '''
    Representation of a entity.
    '''
    def __init__(self):
        '''
        Construct a generic entity within the game.
        Parameters:
            collidable (bool): If the entity can be interacted with.
        '''
        self.id = 'Entity'
        self.collidable = True
    
    def get_id(self):
        '''(str): Returns the id of the entity.'''
        return self.id
    
    def set_collide(self, collidable):
        '''
        Sets rather or not the entity can be interacted with.
        Parameters:
            collidable (bool): True if the entity can be interacted with, False otherwise.
        '''
        self.collidable = collidable
    
    def can_collide(self):
        '''(bool): Returns whether or not the entity can be interacted with.'''
        return self.collidable
    
    def __str__(self):
        return "{}('{}')".format(self.__class__.__name__, self.id)
    
    def __repr__(self):
        return str(self)


class GameLogic:
    '''
    Representation of gamelogic.
    '''
    def __init__(self, dungeon_name="game1.txt"):
        """Constructor of the GameLogic class.

        Parameters:
            dungeon_name (str): The name of the level.
        """
        self._dungeon = load_game(dungeon_name)
        self._dungeon_size = len(self._dungeon)

        self._player = Player(GAME_LEVELS[dungeon_name])
        
        self._game_information = self.init_game_information()

        self._win = False

    def get_positions(self, entity):
        """ Returns a list of tuples containing all positions of a given Entity type.

        Parameters:
            entity (str): The id of an entity.

        Returns:
            )list<tuple<int, int>>): Returns a list of tuples representing the 
            positions of a given entity id.
        """
        positions = []
        for row, line in enumerate(self._dungeon):
            for col, char in enumerate(line):
                if char == entity:
                    positions.append((row,col))

        return positions

    def get_dungeon_size(self):
        '''(int): Returns the width of the dungeon as an integer.'''
        return self._dungeon_size
    
    def init_game_information(self):
        '''Find the position of all entities within the current dungeon.'''
        dungeon = {}
        
        for i in range(self._dungeon_size):
            for j in range(self._dungeon_size):
                if self._dungeon[i][j] == PLAYER:
                    self._player.set_position((i, j))
                elif self._dungeon[i][j] == WALL:
                    dungeon[(i, j)] = Wall()
                elif self._dungeon[i][j] == DOOR:
                    dungeon[(i, j)] = Door()
                elif self._dungeon[i][j] == KEY:
                    dungeon[(i, j)] = Key()
                elif self._dungeon[i][j] == MOVE_INCREASE:
                    dungeon[(i, j)] = MoveIncrease()
                    
        return dungeon
    
    def get_game_information(self):
        '''Returns a dictionary containing the position and the corresponding Entity, as the keys and values, for the current dungeon.'''
        return self._game_information
    
    def get_player(self):
        '''Returns the Player object within the game.'''
        return self._player
    
    def get_entity(self, position):
        '''Returns an Entity at a given position in the dungeon.'''
        if position not in self._game_information:
            return None
        return self._game_information[position]
    
    def get_entity_in_direction(self, direction):
        '''Returns an Entity in the given direction of the Player's position.'''
        player_pos = self._player.get_position()
        entity_pos = (player_pos[0] + DIRECTIONS[direction][0], player_pos[1] + DIRECTIONS[direction][1])
        
        # If there is no Entity in the given direction
        if entity_pos[0] > self._dungeon_size or entity_pos[1] > self._dungeon_size:
            return None

        # If the direction is off map
        if entity_pos not in self._game_information.keys():
            return None
        
        return self._game_information[entity_pos]
    
    def collision_check(self, direction):
        '''Returns ​False​ if a player can travel in the given direction, they won't collide. ​True, they will collide, otherwise.'''
        player_pos = self._player.get_position()
        entity_pos = (player_pos[0] + DIRECTIONS[direction][0], player_pos[1] + DIRECTIONS[direction][1])
        
        # If a player can travel in the given direction, they won't collide
        if entity_pos in self._game_information and self._game_information[entity_pos].can_collide() == False:
            return True
        elif entity_pos[0] < 0 or entity_pos[1] < 0:
            return False
        elif entity_pos[0] > self._dungeon_size or entity_pos[1] > self._dungeon_size:
            return False
        else:
            return False
    
    def new_position(self, direction):
        '''Returns a tuple of integers that represents the new position given the direction.'''
        player_pos = self._player.get_position()
        
        return (player_pos[0] + DIRECTIONS[direction][0], player_pos[1] + DIRECTIONS[direction][1])
    
    def move_player(self, direction):
        '''Update the Player's position to place them one position in the given direction.'''
        self._player.set_position(self.new_position(direction))
    
    def check_game_over(self):
        '''Returns True if the game has been ​lost and False otherwise.'''
        return self._player.moves_remaining() <= 0 or self.won()
    
    def set_win(self, win):
        '''Set the game's win state to be True or False.'''
        self._win = win
        
    def won(self):
        '''Return game's win state.'''
        return self._win


class Wall(Entity):
    '''
    Representation of a wall.
    '''
    def __init__(self):
        '''
        Construct a wall.
        '''
        super().__init__()
        self.id = WALL
        self.collidable = False


class Item(Entity):
    '''
    Representation of a item.
    '''
    def __init__(self):
        '''
        Construct an item.
        '''
        super().__init__()
    
    def on_hit(self, game):
        '''
        This function should raise the NotImplementedError.
        Parameters:
            game (GameLogic): The game created by GameLogic().
        '''
        raise NotImplementedError


class Key(Item):
    '''
    Representation of a key.
    '''
    def __init__(self):
        '''
        Construct a key.
        '''
        super().__init__()
        self.id = KEY
    
    def on_hit(self, game):
        '''
        When the player gets the key.
        Parameters:
            game (GameLogic): The game created by GameLogic().
        '''
        # The Key should be added to the Player's inventory
        player = game.get_player()
        player.add_item(self)
        
        # The Key should then be removed from the dungeon once it's in the Player's inventory
        game_info = game.get_game_information() 
        for k in game.get_positions(KEY):
            game_info.pop(k)


class MoveIncrease(Item):
    '''
    Representation of an item.
    '''
    def __init__(self, moves=5):
        '''
        Construct a MoveIncrease item with a given moves.
        Parameters:
            moves (int): moves of the player.
        '''
        super().__init__()
        self.id = MOVE_INCREASE
        self.moves = moves
    
    def on_hit(self, game):
        '''
        When the player hits the MoveIncrease (M) item.
        Parameters:
            game (GameLogic): The game created by GameLogic().
        '''
        # The number of moves for the player increases
        player = game.get_player()
        player.change_move_count(self.moves)
        
        # The M item is removed from the game
        game_info = game.get_game_information() 
        for m in game.get_positions(MOVE_INCREASE):            
            game_info.pop(m)

            
class Door(Entity):
    '''
    Representation of a door.
    '''
    def __init__(self):
        '''
        Construct a door.
        '''
        super().__init__()
        self.id = DOOR
    
    def on_hit(self, game):
        '''
        If the Player's inventory contains a Key Entity then this method should set the 'game over' state to be True.
        Parameters:
            game (GameLogic): The game created by GameLogic().
        '''
        player = game.get_player()
        for i in player.get_inventory():
            if str(i) == str(Key()):
                return game.set_win(True)
        print("You don't have the key!")

        
class Player(Entity):
    '''
    Representation of a player.
    '''
    def __init__(self, move_count):
        '''
        Construct a door.
        Parameters:
            move_count (int): How many moves a Player can have for the given dungeon they are in.
        '''
        super().__init__()
        self.id = PLAYER
        self.inventory = []
        self.position = None
        self.move_count = move_count

    def set_position(self, position):
        '''Sets the position of the Player.'''
        self.position = position
    
    def get_position(self):
        '''Returns a tuple of ints representing the position of the Player.'''
        return self.position
    
    def change_move_count(self, number):
        '''Number to be added to the Player's move count.'''
        self.move_count += number
    
    def moves_remaining(self):
        '''Returns an int representing how many moves the Player has left before they reach the maximum move count.'''
        return self.move_count
    
    def add_item(self, item):
        '''Adds the item to the Player's Inventory.'''
        self.inventory.append(item)        
    
    def get_inventory(self):
        '''Returns a list that represents the Player's inventory.'''
        return self.inventory


class GameApp:
    '''
    Representation of game app.
    '''
    def __init__(self): 
        '''
        Construct a game app.
        '''
        self.game = GameLogic()
        self.game_info = self.game.get_game_information()
        self.player = self.game.get_player()
        
    def play(self):
        '''Handles the player interaction.'''
        # Loop function for this game
        while not self.game.check_game_over():
            self.draw()
            is_quit = False
            action = input('Please input an action: ').strip()
            if action in VALID_ACTIONS:
                if action == INVESTIGATE: # I
                    continue
                elif action == QUIT: # Q
                    next_action = input('Are you sure you want to quit? (y/n): ').strip()
                    if next_action == 'y':
                        is_quit = True
                        break
                elif action == HELP: # H
                    print(HELP_MESSAGE)
                else: # W/S/D/A
                    # Move once
                    self.player.change_move_count(-1)
                    # If a collision occurs in the next step, invalid
                    if self.game.collision_check(action):
                        print(INVALID)
                    else:
                        # If entity exists, on hit
                        next_pos = self.game.new_position(action)
                        entity = self.game.get_entity(next_pos)
                        if entity:
                            entity.on_hit(self.game) 
                        
                        # Move player to next position
                        self.game.move_player(action)
            # More than 1 input
            elif len(action.split(' ')) >= 2: # I W
                investigate, new_action = [x for x in action.split(' ') if x][:2]
                if investigate == INVESTIGATE:                    
                    if new_action in VALID_ACTIONS:
                        self.player.change_move_count(-1)
                        player_pos = self.player.get_position()
                        next_pos = (player_pos[0] + DIRECTIONS[new_action][0], player_pos[1] + DIRECTIONS[new_action][1])
                        next_entity = self.game.get_entity(next_pos)
                        print('{} is on the {} side.'.format(next_entity, new_action))  
                    else:
                        print(INVALID)
            else:
                print(INVALID)

        # Quit
        if is_quit:
            return
      
        # Win or lose
        if self.game.won():
            print(WIN_TEXT)
        else:
            print(LOSE_TEST)

    def draw(self):
        '''Displays the dungeon with all Entities in their positions.'''
        # Gets the player's attributes
        player_pos = self.player.get_position()
        player_moves = self.player.moves_remaining()
        
        # Draw the map
        display = Display(self.game_info, self.game._dungeon_size)
        display.display_game(player_pos)
        display.display_moves(player_moves)

def main():
    GameApp().play()

if __name__ == "__main__":
    main()
