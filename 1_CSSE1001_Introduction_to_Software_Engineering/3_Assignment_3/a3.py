import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import time

__author__ = "{{Xianglong LIN}} ({{45791439}})"
__email__ = "s4579143@uq.edu.au"
__date__ = "24/09/2020"

GAME_LEVELS = {
    # dungeon layout: max moves allowed
    "game1.txt": 7,
    "game2.txt": 12,
    "game3.txt": 19,
}

PLAYER = "O"
KEY = "K"
DOOR = "D"
WALL = "#"
MOVE_INCREASE = "M"
SPACE = " "
NORTH = "N"
WEST = "W"
EAST = "E"
SOUTH = "S"

TASK_ONE = 1
TASK_TWO = 2

TASK_ONE_HEIGHT = 36
TASK_TWO_HEIGHT = 100

# DIRECTIONS = {
#     "N": (-1, 0),
#     "S": (1, 0),
#     "E": (0, 1),
#     "W": (0, -1)
# }

DIRECTIONS = {
    "W": (-1, 0),
    "S": (1, 0),
    "D": (0, 1),
    "A": (0, -1)
}

INVESTIGATE = "I"
QUIT = "Q"
HELP = "H"

VALID_ACTIONS = [INVESTIGATE, QUIT, HELP, *DIRECTIONS.keys()]

HELP_MESSAGE = f"Here is a list of valid actions: {VALID_ACTIONS}"

INVALID = "That's invalid."

WIN_TEXT = "You have won the game with your strength and honour!"

LOSE_TEST = "You have lost all your strength and honour."
LOSE_TEXT = "You have lost all your strength and honour."


class Entity:
    """ """

    _id = "Entity"

    def __init__(self):
        """
        Something the player can interact with
        """
        self._collidable = True

    def get_id(self):
        """ """
        return self._id

    def set_collide(self, collidable):
        """ """
        self._collidable = collidable

    def can_collide(self):
        """ """
        return self._collidable

    def __str__(self):
        return f"{self.__class__.__name__}({self._id!r})"

    def __repr__(self):
        return str(self)


class Wall(Entity):
    """ """

    _id = WALL

    def __init__(self):
        """ """
        super().__init__()
        self.set_collide(False)


class Item(Entity):
    """ """

    def on_hit(self, game):
        """ """
        raise NotImplementedError


class Key(Item):
    """ """

    _id = KEY

    def on_hit(self, game):
        """ """
        player = game.get_player()
        player.add_item(self)
        game.get_game_information().pop(player.get_position())


class MoveIncrease(Item):
    """ """

    _id = MOVE_INCREASE

    def __init__(self, moves=5):
        """ """
        super().__init__()
        self._moves = moves

    def on_hit(self, game):
        """ """
        player = game.get_player()
        player.change_move_count(self._moves)
        game.get_game_information().pop(player.get_position())


class Door(Entity):
    """ """
    _id = DOOR

    def on_hit(self, game):
        """ """
        player = game.get_player()
        for item in player.get_inventory():
            if item.get_id() == KEY:
                game.set_win(True)
                return
        messagebox.showinfo("", "You don't have the key!")
        # print("You don't have the key!")


class Player(Entity):
    """ """

    _id = PLAYER

    def __init__(self, move_count):
        """ """
        super().__init__()
        self._move_count = move_count
        self._inventory = []
        self._position = None

    def set_position(self, position):
        """ """
        self._position = position

    def get_position(self):
        """ """
        return self._position

    def change_move_count(self, number):
        """
        Parameters:
            number (int): number to be added to move count
        """
        self._move_count += int(number)

    def moves_remaining(self):
        """ """
        return self._move_count

    def add_item(self, item):
        """Adds item (Item) to inventory
        """
        self._inventory.append(item)

    def get_inventory(self):
        """ """
        return self._inventory

    def set_moves_remaining(self, moves_remaining):
        self._move_count = int(moves_remaining)


class GameLogic:
    """ """

    def __init__(self, dungeon_name="game1.txt"):
        """ """
        self._dungeon = load_game(dungeon_name)
        self._dungeon_size = len(self._dungeon)
        self._player = Player(GAME_LEVELS[dungeon_name])
        self._game_information = self.init_game_information()
        self._win = False

    def get_positions(self, entity):
        """ """
        positions = []
        for row, line in enumerate(self._dungeon):
            for col, char in enumerate(line):
                if char == entity:
                    positions.append((row, col))

        return positions

    def init_game_information(self):
        """ """
        player_pos = self.get_positions(PLAYER)[0]
        key_position = self.get_positions(KEY)[0]
        door_position = self.get_positions(DOOR)[0]
        wall_positions = self.get_positions(WALL)
        move_increase_positions = self.get_positions(MOVE_INCREASE)

        self._player.set_position(player_pos)

        information = {
            key_position: Key(),
            door_position: Door(),
        }

        for wall in wall_positions:
            information[wall] = Wall()

        for move_increase in move_increase_positions:
            information[move_increase] = MoveIncrease()

        return information

    def get_player(self):
        """ """
        return self._player

    def get_entity(self, position):
        """ """
        return self._game_information.get(position)

    def get_entity_in_direction(self, direction):
        """ """
        new_position = self.new_position(direction)
        return self.get_entity(new_position)

    def get_game_information(self):
        """ """
        return self._game_information

    def set_game_information(self, game_information):
        """ """
        self._game_information = game_information

    def get_dungeon_size(self):
        """ """
        return self._dungeon_size

    def move_player(self, direction):
        """ """
        new_pos = self.new_position(direction)
        self.get_player().set_position(new_pos)

    def collision_check(self, direction):
        """
        Check to see if a player can travel in a given direction
        Parameters:
            direction (str): a direction for the player to travel in.

        Returns:
            (bool): False if the player can travel in that direction without colliding otherwise True.
        """
        new_pos = self.new_position(direction)
        entity = self.get_entity(new_pos)
        if entity is not None and not entity.can_collide():
            return True

        return not (0 <= new_pos[0] < self._dungeon_size and 0 <= new_pos[1] < self._dungeon_size)

    def new_position(self, direction):
        """ """
        x, y = self.get_player().get_position()
        dx, dy = DIRECTIONS[direction]
        return x + dx, y + dy

    def check_game_over(self):
        """ """
        return self.get_player().moves_remaining() <= 0

    def set_win(self, win):
        """ """
        self._win = win

    def won(self):
        """ """
        return self._win


class AbstractGrid(tk.Canvas):
    """BoardView Class handles the gui interactions between user and data.
    Attributes:
        **kwargs
        master (root widget): parent widget
        rows (int): the number of rows  to be shown
        cols (int): the number of columns  to be shown
        width, height(int): height and width of the game board in pixels
        Keyword Arguement:
        contoller: reference to controller class
    """

    def __init__(self, master, rows, cols, width, height, **kwargs):
        
        
        super(AbstractGrid, self).__init__(master)
        self._master = master
        self._controller = kwargs["controller"]

        self._rows = rows
        self._cols = cols
        self._board_width = width
        self._board_height = height
        self._grid_width = int(width / cols)
        self._grid_height = int(height / rows)

    def draw_grid(self, game_information):
        '''Draws the grid from characters in the board string (NO PNGs).
        '''
        self._game_information = game_information
        game_canvas = tk.Canvas(self._frame_game)
        game_canvas.config(width=self._board_width, height=self._board_height)

        game_canvas.pack()

    def bind_key_board(self, game_canvas):
        game_canvas.bind(sequence="<Key>", func=self._callback)

    def _callback(self, event):
        pressed_key = event.char.upper()
        self._controller.processKeyboardEvent(pressed_key)

    def update_status(self, elapsed_time):
        if self._controller.get_task_mode() == TASK_TWO:
            self._status_bar.update_status_bar(elapsed_time)

    def update_moves_remaining(self, moves_remaining):
        if self._controller.get_task_mode() == TASK_TWO:
            self._status_bar.updade_moves_remaining(moves_remaining)

    def bind_mouse_buttuons(self, keypad_canvas):
        """Binds the mouse click to the game board and handles call backs.
        Parameters:
            keypad_canvas: The tkinter canvas for just the grid area
        """
        keypad_canvas.bind("<Button-1>", self._callback_mouse)
        keypad_canvas.bind("<Button-2>", self._callback_mouse)
        keypad_canvas.bind("<Button-3>", self._callback_mouse)

    def _callback_mouse(self, event):
        """Handles the type of click and the index of where was clicked.
        Parameters:
            event (object): object describing the event, mouse coordinates and button clicked
        """
        # work out from coordinates what game cell they clicked
        keypad_grid_width = self._keypad.get_keypad_width() // 3
        keypad_grid_height = self._keypad.get_keypad_height() // 2
        col = event.x // keypad_grid_width
        row = event.y // keypad_grid_height
        key_info = {(0, 1): 'W', (1, 0): 'A', (1, 1): 'S', (1, 2): 'D'}
        if (row, col) in key_info:
            pressed_key = key_info[(row, col)]
            self._controller.processKeyboardEvent(pressed_key)

    # Returns the bounding box for the (row, col) position.
    def get_bbox(self, position):
        pass

    # Converts the x, y pixel position (in graphics units) to a (row, col) position.
    def pixel_to_position(self, pixel):
        pass

    # Gets the graphics coordinates for the center of the cell at the given (row, col) position.
    def get_position_center(self, position):
        pass

    # Annotates the cell at the given (row, col) position with the provided text.
    def annotate_position(self, position, text):
        pass


class DungeonMap(AbstractGrid):
    def __init__(self, master, size, width=600, **kwargs):
        super().__init__(master, size, size, width, width, controller=kwargs["controller"])
        self._frame_header = tk.Frame(self._master, bg="white")
        self._frame_header.pack(side=tk.TOP, fill=tk.X)
        self._keypad = self._controller.get_keypad_info()
        self._frame_game = tk.Frame(self._master, bg="white", width=width, height=width)
        self._frame_game.pack(side=tk.TOP, anchor=tk.NW)
        # self._master.geometry(str(int(self._board_width) + 400) + "x" + str(int(self._board_height) + 200))
        self._controller = kwargs["controller"]
        if self._controller.get_task_mode() == TASK_ONE:
            status_bar_heights = TASK_ONE_HEIGHT
        else:
            status_bar_heights = TASK_TWO_HEIGHT
        self._master.geometry(
            str(self._board_width + self._keypad.get_keypad_width()) + "x" + str(
                self._board_width + status_bar_heights))

        label = tk.Label(self._frame_header, text="Key Cave Adventure Game", bg="#d36d69", fg="white",
                         font=("Courier New", 18, "bold"), width=self._board_width)
        label.pack(side=tk.TOP, fill=tk.X)

    # Draws the dungeon on the DungeonMap based on dungeon,and draws the player at the specified (row, col) position.
    def draw_grid(self, dungeon, player_position):
        for widget in self._frame_game.winfo_children():
            widget.destroy()
        game_canvas = tk.Canvas(self._frame_game)
        game_canvas.config(width=self._board_width, height=self._board_height)
        rect_size = self._board_width / self._cols

        for row in range(self._rows):
            for col in range(self._cols):
                position = (row, col)
                entity = dungeon.get(position)
                square_colour = ""
                text = ""
                if entity is not None:
                    char = entity.get_id()
                    if char == WALL:
                        square_colour = "darkgrey"

                    elif char == MOVE_INCREASE:
                        square_colour = "orange"
                        text = "Bananna"
                    elif char == KEY:
                        square_colour = "yellow"
                        text = "Trash"
                    elif char == DOOR:
                        square_colour = "red"
                        text = "Nest"
                elif position == player_position:
                    square_colour = "mediumspringgreen"
                    text = "Ibis"
                else:
                    square_colour = 'white'
                game_canvas.create_rectangle(col * rect_size, row * rect_size, (col * rect_size) + rect_size,
                                             (row * rect_size) + rect_size, fill=square_colour, outline='white')
                game_canvas.create_text((col * rect_size) + rect_size / 2,
                                        (row * rect_size) + rect_size / 2, text=text)
        game_canvas.pack(side='left')

        self._key_info = {(0, 1): 'W', (1, 0): 'A', (1, 1): 'S', (1, 2): 'D'}
        key_canvas = tk.Canvas(self._frame_game)
        key_canvas.config(width=self._keypad.get_keypad_width(), height=self._keypad.get_keypad_height())
        rect_width = self._keypad.get_keypad_width() / 3
        rect_height = self._keypad.get_keypad_height() / 2
        for row in range(2):
            for col in range(3):
                position = (row, col)
                key_name = self._key_info.get(position)
                text = ''
                if key_name is not None:
                    square_colour = "gray"
                    if key_name == 'W':
                        text = 'N'
                    if key_name == "D":
                        text = 'E'
                    if key_name == "A":
                        text = 'W'
                    if key_name == "S":
                        text = 'S'
                else:
                    square_colour = "white"
                key_canvas.create_rectangle(col * rect_width, row * rect_height, (col * rect_width) + rect_width,
                                            (row * rect_height) + rect_height, fill=square_colour)
                key_canvas.create_text((col * rect_width) + rect_width / 2,
                                       (row * rect_height) + rect_height / 2, text=text)
        # key_canvas.place(relx=2, rely=0)
        # key_canvas.grid(column=1, row=0, sticky=tk.S)
        key_canvas.pack(side='right')

        game_canvas.focus_set()

        # rebind keyboard as the widget destroy seems to clear them
        self.bind_key_board(game_canvas)
        # rebind mouse buttons as the widget destroy seems to clear them
        self.bind_mouse_buttuons(key_canvas)


class AdvancedDungeonMap(DungeonMap):
    def __init__(self, master, size, width=600, **kwargs):
        """ImageBoardView initializer method
              sets member variables as described in class description.
          Parameters:
              master: parent widget
              size (int): The number of grids (rows or columns)
              width (int): The height/ width in pixels of the windows
              Keyword Argument:
              args and kwargs: reference to controller class
          """
        super().__init__(master, size, width, controller=kwargs["controller"])
        if self._controller.get_task_mode() == TASK_TWO:
            self._status_bar = StatusBar(master, controller=self._controller, bg="white")
            self._status_bar.pack(side=tk.BOTTOM, anchor=tk.SW, expand=True, fill=tk.X, pady=5)
        self._entity = {
            "clock": self.load_image("images\\clock.png", self._grid_width),
            "door": self.load_image("images\\door.png", self._grid_width),
            "empty": self.load_image("images\\empty.png", self._grid_width),
            "key": self.load_image("images\\key.png", self._grid_width),
            "lightning": self.load_image("images\\lightning.png", self._grid_width),
            "lives": self.load_image("images\\lives.png", self._grid_width),
            "moveIncrease": self.load_image("images\\moveIncrease.png", self._grid_width),
            "player": self.load_image("images\\player.png", self._grid_width),
            "wall": self.load_image("images\\wall.png", self._grid_width),
        }

    def load_image(self, filename, size):
        """Loads the image to the Tkinter/ PILL format for showing images.
        Parameters:
            filename (str): the filename for the image
            size (int): the size to resize the pngs to (px width and height)
        """
        img = Image.open(filename)
        img = img.resize((size, size), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)

    def draw_grid(self, dungeon, player_position):
        """Draws the board from characters in the dungeon string (WITH PNG IMAGES).
         """
        try:
            for widget in self._frame_game.winfo_children():
                widget.destroy()
        except:
            pass
        game_canvas = tk.Canvas(self._frame_game)
        game_canvas.config(width=self._board_width, height=self._board_height)
        rect_size = self._grid_width
        for row in range(self._rows):
            for col in range(self._cols):
                position = (row, col)
                x = (col * rect_size) + (rect_size / 2)
                y = (row * rect_size) + (rect_size / 2)
                entity = dungeon.get(position)
                entity_image = ""
                if entity is not None:
                    char = entity.get_id()
                    if char == WALL:
                        entity_image = self._entity['wall']

                    elif char == MOVE_INCREASE:
                        entity_image = self._entity['moveIncrease']

                    elif char == KEY:
                        entity_image = self._entity['key']

                    elif char == DOOR:
                        entity_image = self._entity['door']

                elif position == player_position:
                    entity_image = self._entity['player']
                else:
                    entity_image = self._entity['empty']

                game_canvas.create_image(x, y, image=entity_image)

        # game_canvas.grid(row=0, column=0, sticky=tk.N)
        game_canvas.pack(side='left')

        self._key_info = {(0, 1): 'W', (1, 0): 'A', (1, 1): 'S', (1, 2): 'D'}
        key_canvas = tk.Canvas(self._frame_game)
        key_canvas.config(width=self._keypad.get_keypad_width(), height=self._keypad.get_keypad_height())
        rect_width = self._keypad.get_keypad_width() / 3
        rect_height = self._keypad.get_keypad_height() / 2
        for row in range(2):
            for col in range(3):
                position = (row, col)
                key_name = self._key_info.get(position)
                text = ''
                if key_name is not None:
                    square_colour = "gray"
                    if key_name == 'W':
                        text = 'N'
                    if key_name == "D":
                        text = 'E'
                    if key_name == "A":
                        text = 'W'
                    if key_name == "S":
                        text = 'S'
                else:
                    square_colour = "white"
                key_canvas.create_rectangle(col * rect_width, row * rect_height, (col * rect_width) + rect_width,
                                            (row * rect_height) + rect_height, fill=square_colour)
                key_canvas.create_text((col * rect_width) + rect_width / 2,
                                       (row * rect_height) + rect_height / 2, text=text)
        # key_canvas.place(relx=2, rely=0)
        # key_canvas.grid(column=1, row=0, sticky=tk.E)
        key_canvas.pack(side='right')
        game_canvas.focus_set()
        self.bind_key_board(game_canvas)
        self.bind_mouse_buttuons(key_canvas)


class KeyPad(AbstractGrid):
    """Handles the KeyPad information for Task 1 and 2"""

    def __init__(self, master, width=200, height=100, **kwargs):
        super().__init__(master, rows=2, cols=3, width=width, height=height, controller=kwargs['controller'])
        self._key_info = {(0, 1): 'N', (1, 0): 'W', (1, 1): 'S', (1, 2): 'E'}
        self._keypad_width = width
        self._keypad_height = height
        # self._frame_game = tk.Frame(self._master, bg="white", width=width, height=height)
        # self._frame_game.pack(side=tk.RIGHT, anchor=tk.NW)
        # self.draw_grid()
        self._rect_width = self._board_width / self._cols
        self._rect_height = self._board_height / self._rows

    def key_info(self):
        return self._key_info

    def get_keypad_width(self):
        return self._keypad_width

    def get_keypad_height(self):
        return self._keypad_height

    # Converts the x, y pixel position to the direction of the arrow depicted at that position.
    def pixel_to_direction(self, pixel):
        pass


# load a game from a .txt file
def load_game(filename):
    dungeon_layout = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            dungeon_layout.append(list(line))
    return dungeon_layout


class StatusBar(tk.Frame):
    """Handles the status bar information and buttons for Task 2.
    Attributes:
        master (root widget): parent widget
        controller : reference to GameApp
        options: additional frame creation objects, see frame for more details
        elapsed_time (string): the time that has elapsed over a game
        moves_remaining(int):  the moves remaining of the player
    """

    def __init__(self, master, controller, **options):
        """Initializer method for the status bar class. Attributes for the whole class can be seen in class desc.
        Parameters:
            master (root widget): parent widget
            controller (PokemonGame): reference to controller class
            options: additional frame creation objects, see frame for more details
        """
        # Status bar images and labels stored as member variables to avoid being garbage collected
        super().__init__(master, options)
        self._master = master
        self._controller = controller
        self._elapsed_time = tk.StringVar()
        self._elapsed_time.set("Time elapsed\n0m 0s")

        moves_remaining = self._controller.get_game_logic().get_player().moves_remaining()
        self._moves_left = tk.StringVar()
        self._moves_left.set(f"Moves left\n{moves_remaining} moves remaining")

        # restart/ new game buttons
        self._button_frame = tk.Frame(self, background="white")
        self._button_frame.pack(side=tk.LEFT, expand=True)

        self._new_button = tk.Button(self._button_frame, text="New Game", command=self.new_game)
        self._new_button.pack(anchor=tk.N)

        # self._restart_button = tk.Button(self._button_frame, text="Restart Game", command=self.restart_callback)
        # self._restart_button.pack(anchor=tk.S)
        self._restart_button = tk.Button(self._button_frame, text="Quit", command=self.close)
        self._restart_button.pack(anchor=tk.S)

        self._img_frame2 = tk.Frame(self, background="white")
        self._img_frame2.pack(side=tk.RIGHT, expand=True)

        self._img_frame1 = tk.Frame(self, background="white")
        self._img_frame1.pack(side=tk.RIGHT, expand=True)

        # time to complete
        time_img = ImageTk.PhotoImage(
            Image.open("images\\clock.png").resize((int(TASK_TWO_HEIGHT * 0.6), int(TASK_TWO_HEIGHT * 0.6)),
                                                   Image.ANTIALIAS))
        self._time_image = tk.Label(self._img_frame1, bg="white")
        self._time_image.image = time_img
        self._time_image.configure(image=time_img)
        self._time_image.pack(side=tk.LEFT)

        # timer text label
        self._timer_label = tk.Label(self._img_frame1, textvariable=self._elapsed_time, bg="white")
        self._timer_label.pack(side=tk.RIGHT)

        moves_img = ImageTk.PhotoImage(
            Image.open("images\\lightning.png").resize((int(TASK_TWO_HEIGHT * 0.6), int(TASK_TWO_HEIGHT * 0.6)),
                                                       Image.ANTIALIAS))
        self._time_image = tk.Label(self._img_frame2, bg="white")
        self._time_image.image = moves_img
        self._time_image.configure(image=moves_img)
        self._time_image.pack(side=tk.LEFT)

        self._timer_label = tk.Label(self._img_frame2, textvariable=self._moves_left, bg="white")
        self._timer_label.pack(side=tk.RIGHT)

    def update_status_bar(self, elapsed_time):
        """Calls the update status bar in the status bar class.
        Parameters:
            Elpased_time (int): The time that has passed during the game in seconds
        """
        minutes = elapsed_time // 60
        seconds = elapsed_time - 60 * minutes
        self._elapsed_time.set("Time elapsed\n" + str(minutes) + "m " + str(seconds) + "s")

    def updade_moves_remaining(self, moves_remaining):
        """Calls the update status bar in the status bar class.
            Parameters:
                moves_left (int): the moves remaining of the player
            """
        self._moves_left.set(f"Moves left\n{moves_remaining} moves remaining")

    def restart_callback(self):
        """Calls the restart_game method to restart the game."""
        self._controller.restart_game()

    def new_game(self):
        """Calls the new_game method to start a new game."""
        self._controller.new_game()

    def close(self):
        quit_game = messagebox.askquestion(type=messagebox.YESNO,
                                           title="Quit Game",
                                           message="Do you really want to quit the game?")
        if quit_game == messagebox.YES:
            self._master.destroy()


class GameApp:
    """Controller class that allows the view and data to combine to have a functional game.
    Attributes:
        master: Main window
        task_mode (int): The task mode to run the task in, default to TASK_TWO
        _board_view: Link to the board view, this will depend on the task mode
        initialise_timer: Starts timer
    """

    def __init__(self, master, task=TASK_ONE, dungeon_name="game2.txt"):
        """Initializer method for the controller class
            Sets member variables.
        Parameters:
            master: Main window
            task (int): Indicator of which task to run
            dungeon_name: the game we will play
        """
        # Create a new game app within a master widget
        self._master = master
        self._task_mode = task
        self._dungeon_name = dungeon_name
        self.canvas = None
        self._game = GameLogic(self._dungeon_name)
        self._dungeon = ""
        self._player = self._game.get_player()
        player_pos = self._player.get_position()
        dungeon_size = self._game.get_dungeon_size()

        self._keypad = KeyPad(self._master, width=200, height=100, controller=self)

        # Create the menu if it is not task one.
        if self._task_mode == TASK_TWO:
            menubar = tk.Menu(master)
            master.config(menu=menubar)
            filemenu = tk.Menu(menubar)
            menubar.add_cascade(label="File", menu=filemenu)
            filemenu.add_command(label="Save game", command=self.save_game)
            filemenu.add_command(label="Load Game", command=self.load_game)
            # filemenu.add_command(label="Restart Game", command=self.restart_game)
            filemenu.add_command(label="New Game", command=self.new_game)
            filemenu.add_command(label="Quit", command=self.close)
            self._board_view = AdvancedDungeonMap(self._master, dungeon_size, board_width=600, controller=self)
        else:
            self._board_view = DungeonMap(self._master, dungeon_size, width=600, controller=self)
        # Using polymorphism to draw either task one or task two game board
        self._board_view.draw_grid(self._game.get_game_information(), player_pos)

        self.initialize_timer()

    def get_game_logic(self):
        return self._game

    def get_keypad_info(self):
        return self._keypad

    def processKeyboardEvent(self, pressed_key):
        """Handles the response to pressed key and checks if the game has been won.
        """
        player = self._game.get_player()
        if pressed_key in DIRECTIONS:
            direction = pressed_key
            # if player does not collide move them
            if not self._game.collision_check(direction):
                self._game.move_player(direction)
                entity = self._game.get_entity(player.get_position())
                if entity is not None:
                    entity.on_hit(self._game)

                    if self._game.won():
                        self._timer_running = False
                        if self._task_mode == TASK_ONE:
                            messagebox.showinfo("You won!",
                                                "You have won the game with your strength and honour")
                            self.close()
                        else:
                            elapsed_time = int(time.time() - self._start_time)
                            self._timer_running = False
                            iscontinue = messagebox.askquestion("You won!",
                                                                f"You have finished the level with a score of {elapsed_time}"
                                                                f"\nWould you like play again?")
                            if iscontinue == messagebox.YES:
                                self.new_game()
                            else:
                                self._master.destroy()
            player.change_move_count(-1)

            player = self._game.get_player()

            player_pos = player.get_position()
            self._board_view.draw_grid(self._game.get_game_information(), player_pos)
            moves_remaining = player.moves_remaining()
            self._board_view.update_moves_remaining(moves_remaining)
        if self._game.check_game_over():
            self._timer_running = False
            if self._task_mode == TASK_ONE:
                messagebox.showinfo("You lose!", "You have lost all your strength and honour.")
                self._master.destroy()
            else:
                elapsed_time = int(time.time() - self._start_time)
                self._timer_running = False
                iscontinue = messagebox.askquestion("You lose!",
                                                    f"You don't have finished the level with a score of {elapsed_time}"
                                                    f"\nWould you like play again?")
                if iscontinue == messagebox.YES:
                    self.new_game()
                else:
                    self._master.destroy()

    def get_game_logic(self):
        return self._game

    def get_task_mode(self) -> int:
        """Returns the task number 1,2,3 to allow testing for each task.
        Returns:
            _task_mode (int): interger representation of task mode"""
        return self._task_mode

    def update_timer(self):
        """Updates the timer on the status bar every second."""
        elapsed_time = int(time.time() - self._start_time)
        self._board_view.update_status(elapsed_time)
        if self._timer_running:
            self._master.after(1000, self.update_timer)

    def initialize_timer(self):
        """Initalises the timer when the tkinter window opens."""
        self._start_time = time.time()
        self._timer_running = True
        self.update_timer()

    def update_moves_remaining(self, moves_remaining):
        self._board_view.update_moves_remaining(moves_remaining)

    def new_game(self):
        """Allows for a completely new game to start, resetting all variables."""
        self._game = GameLogic(self._dungeon_name)
        player = self._game.get_player()
        player_pos = player.get_position()
        self.initialize_timer()
        self._board_view.draw_grid(self._game.get_game_information(), player_pos)

    def restart_game(self):
        """Restarts the game, but keeps the pokemon locations."""
        self._game = GameLogic(self._dungeon_name)
        player = self._game.get_player()
        player_pos = player.get_position()
        self.initialize_timer()
        self._board_view.draw_grid(self._game.get_game_information(), player_pos)

    def save_game(self):
        """Saves the game to a new txt file."""
        filename = filedialog.asksaveasfilename(filetypes=[('Text files', '*.txt')], title="Save Game")
        moves_remaining = self._game.get_player().moves_remaining()
        player = self._game.get_player()
        self._game.get_game_information()[player.get_position()] = player
        dungeon_size = self._game.get_dungeon_size()
        content = ""

        for row in range(dungeon_size):
            for col in range(dungeon_size):
                entity = self._game.get_game_information().get((row, col))
                if entity is not None:
                    content += entity.get_id()
                else:
                    content += " "
            content += "\n"
        if len(player.get_inventory()) > 0:
            content += '|' + str(player.get_inventory()[0].get_id())
        else:
            content += '|'
        content += '|' + str(moves_remaining)
        content += '|' + str(int(time.time() - self._start_time))
        file = open(filename + '.txt', 'w')
        file.write(content)
        file.close()

    def load_game(self):
        """Loads a txt file with saved data and sets the instance variables in both the Controller and Model class.
                  Includes error handling to handle any error raised:
                  a message box indicating the file is not appropriate and only opening .txt files.
              """
        try:
            filename = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')], title="Load Game")
            if filename:
                f = open(filename, "r")
                text = f.read()
                text = text.split("|")
                f.close()
                self._dungeon = [list(line) for line in text[0].split("\n")]
                self._key_id = text[1]
                self._player.set_moves_remaining(text[2])
                self._start_time = time.time() - int(text[3])
                self._game.set_game_information(self.init_game_information())
                self._board_view.draw_grid(self._game.get_game_information(), self._player.get_position())
        except:
            messagebox.showinfo("Load Game", "Invalid Game File.")

    def get_positions(self, entity):
        """ """
        positions = []
        for row, line in enumerate(self._dungeon):
            for col, char in enumerate(line):
                if char == entity:
                    positions.append((row, col))
        return positions

    def init_game_information(self):
        information = {}
        player_pos = self.get_positions(PLAYER)[0]
        if self._key_id == "":
            key_position = self.get_positions(KEY)[0]
            information[key_position] = Key()
        else:
            self._player.add_item(Key())
        door_position = self.get_positions(DOOR)[0]
        wall_positions = self.get_positions(WALL)
        move_increase_positions = self.get_positions(MOVE_INCREASE)

        self._player.set_position(player_pos)

        information[door_position] = Door()

        for wall in wall_positions:
            information[wall] = Wall()

        for move_increase in move_increase_positions:
            information[move_increase] = MoveIncrease()

        return information

    def close(self):
        """Quit game with message box"""
        quit_game = messagebox.askquestion(type=messagebox.YESNO,
                                           title="Quit Game",
                                           message="Do you really want to quit the game?")
        if quit_game == messagebox.YES:
            self._master.destroy()


if __name__ == '__main__':
    master = tk.Tk()
    master['bg'] = 'white'
    master.title("Key Cave Adventure Game")
    GameApp(master, task=TASK_TWO, dungeon_name="game2.txt")
    master.update()
    master.mainloop()
