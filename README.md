# Tupper's Formula (Everything Formula)

## Description

This project is an interactive application in Python that is based on Tupper's formula, a mathematical formula that, when used with a specific integer `K`, allows for the visualization of an image of 106 by 17 pixels. The user can either draw an image directly in an interactive grid or enter a value of `K` to display the associated image.

The value of `K` is calculated by interpreting the drawing grid and can then be copied to the clipboard.

Tupper's formula is defined by the inequality:

```
1/2 < ⌊ mod(⌊y/17⌋ 2^(-17⌊x⌋ - mod(⌊y⌋, 17)), 2) ⌋
```

It generates images based on a very large integer `K`, where `x` and `y` are the pixel coordinates.

Learn more about Tupper's Formula: https://clairelommeblog.fr/2022/10/16/la-formule-autoreferente-de-tupper/

## Features

- **Interactive Drawing**: Users can draw pixels on a grid of 106 columns and 17 rows.
- **Calculate `K` Value**: The application calculates the `K` value corresponding to the drawn image and copies it to the clipboard.
- **Display Image for Given `K`**: Users can enter a value of `K`, and the image associated with that number will be displayed.
- **Reset**: It is possible to reset the grid to clear all pixels.

## Prerequisites

Before running the application, make sure to install the necessary dependencies. You can install them via `pip`:

```bash
pip install arcade matplotlib tk
```

### Libraries Used:
- **arcade**: For the graphical interface of the drawing grid.
- **matplotlib**: For generating and displaying the graph corresponding to Tupper's formula.
- **tkinter**: For entering the `K` value and managing user input windows.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/swan-maillard/TuppersFormula.git
   ```

2. Navigate to the project directory:
   ```bash
   cd TuppersFormula
   ```

3. Install the dependencies:
   ```bash
   pip install arcade matplotlib tk
   ```

4. Launch the program:
   ```bash
   python main.py
   ```

## Usage

### Drawing an Image

1. Click on the grid to turn pixels on or off.
2. When satisfied with the drawing, click **Plot** to generate the `K` value.
3. The image corresponding to your drawing will be displayed using `matplotlib`, and the `K` value will be copied to the clipboard.

### Entering a `K` Value

1. Click on the **Input a K** button.
2. Enter an integer divisible by 17 and click **Plot** to display the corresponding image.
3. If `K` is not divisible by 17, an error message will be displayed.

## Authors

- Swan Maillard (maillard.swan@gmail.com)

## License

This project is licensed under the MIT License. Please see the `LICENSE` file for more information.
