import arcade
import matplotlib.pyplot as plot
import tkinter as tk

CELL_SIZE = 12
MARGIN = 2

ROW_COUNT = 17
COL_COUNT = 106

SCREEN_BOTTOM = 100
SCREEN_WIDTH = (CELL_SIZE + MARGIN) * COL_COUNT + MARGIN
SCREEN_HEIGHT = (CELL_SIZE + MARGIN) * ROW_COUNT + MARGIN + SCREEN_BOTTOM

SCREEN_TITLE = "The Everything Formula"

class TextButton:
    def __init__(self, center_x, center_y, width, height, text, action_function):
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
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.face_color)
        arcade.draw_text(self.text, self.center_x, self.center_y, arcade.color.BLACK, font_size=self.font_size,width=self.width, align="center", anchor_x="center", anchor_y="center")

    def on_press(self):
            self.action_function()

def check_mouse_press_for_buttons(x, y, button_list):
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()

class TheEverythingFormula(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.grid = [[0]*COL_COUNT for n in range(ROW_COUNT)]
        arcade.set_background_color(arcade.color.BLACK)

        self.drawing = 0

        self.button_list = []
        plot_button = TextButton(SCREEN_WIDTH/2-40, SCREEN_BOTTOM/2+20, 70, 30, "Plot", self.on_plot)
        reset_button = TextButton(SCREEN_WIDTH/2+40, SCREEN_BOTTOM/2+20, 70, 30, "Reset", self.on_reset_drawing)
        input_button = TextButton(SCREEN_WIDTH/2, SCREEN_BOTTOM/2-20, 100, 30, "Input a K", self.input_k)
        self.button_list += [plot_button, reset_button, input_button]

        self.root = None

    def on_draw(self):
        arcade.start_render()
        x,y = CELL_SIZE//2+MARGIN, CELL_SIZE//2+MARGIN + SCREEN_BOTTOM
        for row in self.grid:
            for item in row:
               color = (arcade.color.BLACK, arcade.color.WHITE)[item == 0]
               arcade.draw_rectangle_filled(x, y, CELL_SIZE, CELL_SIZE, color)
               x = x + CELL_SIZE + MARGIN
            x = CELL_SIZE//2 + MARGIN
            y = y + CELL_SIZE + MARGIN

        for button in self.button_list:
            button.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        check_mouse_press_for_buttons(x, y, self.button_list)

        if y <= SCREEN_BOTTOM or y >= SCREEN_HEIGHT or x <= 0 or x >= SCREEN_WIDTH:
            return False

        col = x//(CELL_SIZE+MARGIN)
        row = (y - SCREEN_BOTTOM)//(CELL_SIZE+MARGIN)

        self.drawing = (1, 2)[self.grid[row][col] == 1]
        self.grid[row][col] = (0, 1)[self.grid[row][col] == 0]


    def on_mouse_release(self, x, y, button, key_modifiers):
        self.drawing = 0

    def on_mouse_motion(self, x, y, dx, dy):
        if y <= SCREEN_BOTTOM or y >= SCREEN_HEIGHT or x <= 0 or x >= SCREEN_WIDTH or self.drawing == 0:
            return False

        col = x//(CELL_SIZE+MARGIN)
        row = (y - SCREEN_BOTTOM)//(CELL_SIZE+MARGIN)

        self.grid[row][col] = (0, 1)[self.drawing == 1]


    def on_plot(self, K = 0):
        if K == 0:
            binary = ""
            for col in range(COL_COUNT):
                for row in range(ROW_COUNT):
                    binary = binary + str(self.grid[row][col])

            for i in range(len(binary)):
                digit = binary[i]
                if digit == "1":
                    K += pow(2, i)
            K *= 17

            if K == 0:
                return False

        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(K)
        root.update()
        root.destroy()

        if len(str(K)) > 50:
            K_chunks, K_chunk_size = len(str(K)), len(str(K))//(len(str(K))//50)
            K_label = "".join([str(K)[i:i+K_chunk_size] + '\n' for i in range(0, K_chunks, K_chunk_size)])
        else:
            K_label = str(K)

        plot.figure(SCREEN_TITLE + " — Graph")
        for x in range(COL_COUNT):
            for yy in range (ROW_COUNT):
                y = K + yy
                if 0.5 < ((y//17) // (2**(17*x + y%17))) % 2:
                    plot.bar(x, height=1, width=1, bottom=yy, linewidth=0, color='black')

        plot.axis('scaled')
        plot.xlim((-2,COL_COUNT+2))
        plot.ylim((-2,ROW_COUNT+2))
        plot.xticks([0, COL_COUNT])
        plot.yticks([0, ROW_COUNT], ['K']+['K + %d'%ROW_COUNT])
        plot.suptitle('1/2 < ⌊mod(⌊y/17⌋2^(-17⌊x⌋ - mod(⌊y⌋, 17)), 2)⌋')
        plot.xlabel('K = ' + K_label + '\n\n (K was copied to the clipboard)')
        plot.get_current_fig_manager().window.state('zoomed')
        plot.show()

    def on_reset_drawing(self):
        self.grid = [[0]*COL_COUNT for n in range(ROW_COUNT)]

    def input_k(self):
        if self.root != None:
            self.root.focus_force()
            return False

        def on_plot(self):
            K = entry.get()
            try:
                K = int(K)
            except ValueError:
                canvas.itemconfig(error, text='K shall be an integer.')
                return False

            if (K%17 > 0):
                canvas.itemconfig(error, text='This value of K does not exist : K shall be divisible by 17.')
                return False

            self.root.destroy()
            self.root = None
            self.on_plot(K)

        def on_closing():
            self.root.destroy()
            self.root = None

        self.root = tk.Tk()
        self.root.title('Input a K')
        canvas = tk.Canvas(self.root, width = 300, height = 120)
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

def main():
    TheEverythingFormula(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE + " — Draw Anything")
    arcade.run()

if __name__ == "__main__":
    main()