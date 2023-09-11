import sys
import textwrap
import argparse
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont

from config import ( E_OK, E_ERR, WIDTH, HEIGHT, MIN_HEIGHT, LINE_HEIGHT, X_PADDING, Y_PADDING, Y_PADDING2, BG_COLOR, FONT_COLOR,
                     FONT_SIZE_WORD_TO_DEFINE, FONT_SIZE_WORD_TYPE, FONT_SIZE_WORD_DEFINITION,
                     FONT_WORD_TO_DEFINE_BASE, FONT_WORD_TYPE_BASE, FONT_WORD_DEFINITION_BASE,
                     WORD_DEFINITION_LINE_WIDTH, WORD_DEFINITION_LINE_SPACING )


def get_fonts(scaling_factor):

    # here we pick the font sizes
    font_size_word_to_define = round(FONT_SIZE_WORD_TO_DEFINE * scaling_factor)
    font_size_word_class = round(FONT_SIZE_WORD_TYPE * scaling_factor)
    font_size_word_definition = round(FONT_SIZE_WORD_DEFINITION * scaling_factor)

    # and here we instantiate the fonts
    font_word_to_define = ImageFont.truetype(FONT_WORD_TO_DEFINE_BASE, size=font_size_word_to_define)
    font_word_class = ImageFont.truetype(FONT_WORD_TYPE_BASE, size=font_size_word_class)
    font_word_definition = ImageFont.truetype(FONT_WORD_DEFINITION_BASE, size=font_size_word_definition)

    return font_word_to_define, font_word_class, font_word_definition


def render_image(width, height, font_color, bg_color, x_word_to_define, y_word_to_define, x_word_definition, x_word_class, x_see_also, y_padding, y_padding2,
                 font_word_to_define, font_word_class, font_word_definition, word_definition_line_spacing, word_to_define, word_class, word_definition_lines, see_also):

    word_class_str = f"({word_class})"
    see_also_str = f"(see also: {see_also})"

    img = Image.new('RGB', (width, height), color=bg_color)

    draw = ImageDraw.Draw(img)

    y_spacing = draw.textsize(word_to_define, font=font_word_to_define)[1] + y_padding

    y_word_class = y_word_to_define + y_spacing

    y_spacing2 = draw.textsize(word_class, font=font_word_to_define)[1] + y_padding2

    y_word_definition = y_word_class + y_spacing2

    draw.text((x_word_to_define, y_word_to_define), word_to_define, font=font_word_to_define, fill=font_color)
    draw.text((x_word_class, y_word_class), word_class_str, font=font_word_class, fill=font_color)

    y_pos = y_word_definition
    for line in word_definition_lines:
        draw.multiline_text((x_word_definition, y_pos), line, font=font_word_definition, fill=font_color)
        y_pos = y_pos + draw.textsize(line, font=font_word_definition)[1] + word_definition_line_spacing

    y_pos = y_pos + 2 * y_padding

    draw.text((x_see_also, y_pos), see_also_str, font=font_word_definition, fill=font_color)

    return img


def main():

    parser = argparse.ArgumentParser(description='Generate a dictionary entry on a png file.')
    parser.add_argument( '-w', '--word',              required=True,  help='Word to be defined')
    parser.add_argument( '-c', '--word-class',        required=True,  help='Word class, such as noun, adjective, verb, etc')
    parser.add_argument( '-d', '--definition',        required=True,  help='The definition of the word')
    parser.add_argument( '-s', '--see-also',          required=True,  help='Other related words')
    parser.add_argument( '-o', '--output-file',       required=True,  help='The output file')
    parser.add_argument( '-f', '--scaling-factor',    required=False, help='Scaling factor for the generated image', type=int, default=1)
    parser.add_argument( '-fc', '--font-color',       required=False, help='The color used for the text', default=FONT_COLOR)
    parser.add_argument( '-bc', '--background-color', required=False, help='The color used for the background', default=BG_COLOR)
    parser.add_argument( '-dh', '--dynamic-height',   required=False, help='Whether the image height is fixed or dynamic', action='store_true')

    args = parser.parse_args()

    word_to_define  = args.word
    word_class = args.word_class
    word_definition = args.definition
    see_also = args.see_also
    output_file = args.output_file
    scaling_factor = args.scaling_factor
    font_color = args.font_color
    bg_color = args.background_color
    dynamic_height = args.dynamic_height

    # this scaling_factor parameter allows for fine tuning the resulting image size keeping proportion

    width = round(WIDTH * scaling_factor)

    x_padding = round(X_PADDING * scaling_factor)
    y_padding = round(Y_PADDING * scaling_factor)
    y_padding2 = round(Y_PADDING2 * scaling_factor)

    x_word_to_define = 0 + x_padding
    y_word_to_define = 0 + y_padding

    x_word_definition = 0 + x_padding
    x_word_class = 0 + x_padding

    x_see_also = 0 + x_padding

    word_definition_line_spacing = round(WORD_DEFINITION_LINE_SPACING * scaling_factor)

    # we do not scale the line width because we are scaling the characters themselves
    word_definition_line_width = WORD_DEFINITION_LINE_WIDTH

    font_word_to_define, font_word_class, font_word_definition = get_fonts(scaling_factor)

    word_definition_lines = textwrap.wrap(word_definition, width=word_definition_line_width)
    nr_lines = len(word_definition_lines)

    # empiric height growth
    if dynamic_height:
        my_height = MIN_HEIGHT + LINE_HEIGHT * nr_lines
    else:
        my_height = HEIGHT

    height = my_height * scaling_factor

    img = render_image(width, height, font_color, bg_color, x_word_to_define, y_word_to_define, x_word_definition, x_word_class, x_see_also, y_padding, y_padding2,
                       font_word_to_define, font_word_class, font_word_definition, word_definition_line_spacing, word_to_define, word_class, word_definition_lines, see_also)

    try:
        img.save(output_file)
        print(f"Output saved to {output_file}.")
    except Exception:
        print(f"problem saving {output_file}")


# execute the main function
main()
