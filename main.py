# Import necessary libraries
import arcade          # Arcade is used to create the graphical interface for the grid
import matplotlib.pyplot as plot  # Matplotlib is used to display the graph based on Tupper's formula
import tkinter as tk    # Tkinter is used to create dialog boxes for entering the value of K

# Grid settings for drawing
CELL_SIZE = 12          # Size of one cell (pixel) in the grid
MARGIN = 2              # Space between cells

# Grid dimensions (based on Tupper's formula)
ROW_COUNT = 17          # Number of rows in the grid
COL_COUNT = 106         # Number of columns in the grid

# Screen size and title settings
SCREEN_BOTTOM = 100     # Space at the bottom of the screen for buttons
SCREEN_WIDTH = (CELL_SIZE + MARGIN) * COL_COUNT + MARGIN  # Calculate window width
SCREEN_HEIGHT = (CELL_SIZE + MARGIN) * ROW_COUNT + MARGIN + SCREEN_BOTTOM  # Calculate window height
SCREEN_TITLE = "The Everything Formula"  # Window title

# Class representing a text button in the graphical interface
class TextButton:
    def __init__(self, center_x, center_y, width, height, text, action_function):
        # Initialize the button with position, size, text, and the associated action function
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = 18
        self.font_face = "Arial"
        self.face_color = arcade.color.LIGHT_GRAY
        self.action_function = action_function

    def draw(self):
        # Draw the button on the screen
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.face_color)
        # Draw the text on the button, centered
        arcade.draw_text(self.text, self.center_x, self.center_y, arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center", anchor_x="center", anchor_y="center")

    def on_press(self):
        # When the button is pressed, trigger the associated action function
        self.action_function()

# Helper function to check if a mouse press is within a button's bounds
def check_mouse_press_for_buttons(x, y, button_list):
    for button in button_list:
        # Check if the click is within the button's boundaries
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()  # If within bounds, trigger the button's action

# Main class representing the application window
class TheEverythingFormula(arcade.Window):

    def __init__(self, width, height, title):
        # Initialize the window with the given width, height, and title
        super().__init__(width, height, title)
        # Create a 2D grid filled with zeros (off pixels)
        self.grid = [[0] * COL_COUNT for n in range(ROW_COUNT)]
        arcade.set_background_color(arcade.color.BLACK)  # Set the background color to black

        self.drawing = 0  # Track whether drawing is happening

        # Create buttons for Plot, Reset, and Input K actions
        self.button_list = []
        plot_button = TextButton(SCREEN_WIDTH / 2 - 40, SCREEN_BOTTOM / 2 + 20, 70, 30, "Plot", self.on_plot)
        reset_button = TextButton(SCREEN_WIDTH / 2 + 40, SCREEN_BOTTOM / 2 + 20, 70, 30, "Reset", self.on_reset_drawing)
        input_button = TextButton(SCREEN_WIDTH / 2, SCREEN_BOTTOM / 2 - 20, 100, 30, "Input a K", self.input_k)
        self.button_list += [plot_button, reset_button, input_button]

        self.root = None  # Root window for Tkinter input dialog

    def on_draw(self):
        # Render the grid and buttons
        arcade.start_render()
        x, y = CELL_SIZE // 2 + MARGIN, CELL_SIZE // 2 + MARGIN + SCREEN_BOTTOM
        for row in self.grid:
            for item in row:
                # Set color based on whether the cell is on (white) or off (black)
                color = (arcade.color.BLACK, arcade.color.WHITE)[item == 0]
                arcade.draw_rectangle_filled(x, y, CELL_SIZE, CELL_SIZE, color)
                x = x + CELL_SIZE + MARGIN
            x = CELL_SIZE // 2 + MARGIN
            y = y + CELL_SIZE + MARGIN

        # Draw all buttons
        for button in self.button_list:
            button.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        # Handle mouse press events for interacting with buttons and the grid
        check_mouse_press_for_buttons(x, y, self.button_list)

        # Ignore clicks outside the grid area
        if y <= SCREEN_BOTTOM or y >= SCREEN_HEIGHT or x <= 0 or x >= SCREEN_WIDTH:
            return False

        # Calculate the column and row of the clicked cell in the grid
        col = x // (CELL_SIZE + MARGIN)
        row = (y - SCREEN_BOTTOM) // (CELL_SIZE + MARGIN)

        # Toggle the cell state (on/off) and update the drawing mode
        self.drawing = (1, 2)[self.grid[row][col] == 1]
        self.grid[row][col] = (0, 1)[self.grid[row][col] == 0]

    def on_mouse_release(self, x, y, button, key_modifiers):
        # Stop drawing when the mouse is released
        self.drawing = 0

    def on_mouse_motion(self, x, y, dx, dy):
        # Handle mouse movement for drawing continuous lines
        if y <= SCREEN_BOTTOM or y >= SCREEN_HEIGHT or x <= 0 or x >= SCREEN_WIDTH or self.drawing == 0:
            return False

        # Calculate the column and row of the hovered cell
        col = x // (CELL_SIZE + MARGIN)
        row = (y - SCREEN_BOTTOM) // (CELL_SIZE + MARGIN)

        # Set the cell state to match the drawing mode (on/off)
        self.grid[row][col] = (0, 1)[self.drawing == 1]

    def on_plot(self, K=0):
        # Generate the value of K based on the current grid drawing, or use a provided K
        if K == 0:
            binary = ""
            # Convert the grid into a binary string (row by row)
            for col in range(COL_COUNT):
                for row in range(ROW_COUNT):
                    binary += str(self.grid[row][col])

            # Calculate the value of K from the binary string
            for i in range(len(binary)):
                digit = binary[i]
                if digit == "1":
                    K += pow(2, i)
            K *= 17

            if K == 0:
                return False

        # Copy K to the clipboard
        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(K)
        root.update()
        root.destroy()

        # Format the K value for display
        if len(str(K)) > 50:
            K_chunks, K_chunk_size = len(str(K)), len(str(K)) // (len(str(K)) // 50)
            K_label = "".join([str(K)[i:i + K_chunk_size] + '\n' for i in range(0, K_chunks, K_chunk_size)])
        else:
            K_label = str(K)

        # Plot the Tupper's formula graph
        plot.figure(SCREEN_TITLE + " — Graph")
        for x in range(COL_COUNT):
            for yy in range(ROW_COUNT):
                y = K + yy
                # Apply Tupper's formula to plot the image
                if 0.5 < ((y // 17) // (2 ** (17 * x + y % 17))) % 2:
                    plot.bar(x, height=1, width=1, bottom=yy, linewidth=0, color='black')

        # Set plot parameters
        plot.axis('scaled')
        plot.xlim((-2, COL_COUNT + 2))
        plot.ylim((-2, ROW_COUNT + 2))
        plot.xticks([0, COL_COUNT])
        plot.yticks([0, ROW_COUNT], ['K'] + ['K + %d' % ROW_COUNT])
        plot.suptitle('1/2 < ⌊mod(⌊y/17⌋2^(-17⌊x⌋ - mod(⌊y⌋, 17)), 2)⌋')
        plot.xlabel('K = ' + K_label + '\n\n (K was copied to the clipboard)')
        plot.get_current_fig_manager().window.state('zoomed')
        plot.show()

    def on_reset_drawing(self):
        # Reset the grid to an empty state (all cells off)
        self.grid = [[0] * COL_COUNT for n in range(ROW_COUNT)]

    def input_k(self):
        # Display a Tkinter window to input a value of K
        if self.root is not None:
            self.root.focus_force()
            return False

        def on_plot(self):
            # Get the input value of K and plot the graph if valid
            K = entry.get()
            try:
                K = int(K)
            except ValueError:
                canvas.itemconfig(error, text='K shall be an integer.')
                return False

            if (K % 17 > 0):
                canvas.itemconfig(error, text='This value of K does not exist : K shall be divisible by 17.')
                return False

            self.root.destroy()
            self.root = None
            self.on_plot(K)

        def on_closing():
            # Handle window closing event
            self.root.destroy()
            self.root = None

        # Tkinter window setup for K input
        self.root = tk.Tk()
        self.root.title('Input a K')
        canvas = tk.Canvas(self.root, width=300, height=120)
        canvas.pack()

        label1 = tk.Label(self.root, text='Write a value of K to plot:')
        label1.config(font=('Arial', 10))
        canvas.create_window(150, 20, window=label1)

        entry = tk.Entry(self.root)
        canvas.create_window(150, 50, window=entry)

        error = canvas.create_text(150, 105, font=("Arial", 8), text="", fill='red')

        button = tk.Button(text='Plot', command=lambda: on_plot(self), bg='brown', fg='white', font=('Arial', 9, 'bold'))
        canvas.create_window(150, 80, window=button)

        self.root.protocol("WM_DELETE_WINDOW", on_closing)
        canvas.mainloop()

# Main function to launch the application
def main():
    # Create the application window and start the arcade event loop
    TheEverythingFormula(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE + " — Draw Anything")
    arcade.run()

if __name__ == "__main__":
    main()
