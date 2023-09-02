import sys
import textwrap
import argparse
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont

from config import ( E_OK, E_ERR, WIDTH, HEIGHT, X_PADDING, Y_PADDING, Y_PADDING2, BG_COLOR, FONT_COLOR,
                     FONT_SIZE_WORD_TO_DEFINE, FONT_SIZE_WORD_TYPE, FONT_SIZE_WORD_DEFINITION,
                     FONT_WORD_TO_DEFINE_BASE, FONT_WORD_TYPE_BASE, FONT_WORD_DEFINITION_BASE,
                     WORD_DEFINITION_LINE_WIDTH, WORD_DEFINITION_LINE_SPACING )


def main():

    parser = argparse.ArgumentParser(description='Generate a dictionary entry on a png file.')
    parser.add_argument( '-w', '--word',             required=True,  help='Word to be defined')
    parser.add_argument( '-c', '--word-class',       required=True,  help='Word class, such as noun, adjective, verb, etc')
    parser.add_argument( '-d', '--definition',       required=True,  help='The definition of the word')
    parser.add_argument( '-s', '--see-also',         required=True,  help='Other related words')
    parser.add_argument( '-o', '--output-file',      required=True,  help='Other related words')
    parser.add_argument( '-f', '--scaling-factor',   required=False, help='Scaling factor for the generated image', type=int, default=1)
    parser.add_argument( '-fc', '--font-color',      required=False, help='The color used for the text', default=FONT_COLOR)
    parser.add_argument( '-bc', '--background-color', required=False, help='The color used for the backgrouns', default=BG_COLOR)

    args = parser.parse_args()

    word_to_define  = args.word
    word_class = args.word_class
    word_definition = args.definition
    see_also = args.see_also
    output_file = args.output_file
    scaling_factor = args.scaling_factor
    font_color = args.font_color
    bg_color = args.background_color

    # this scaling_factor parameter allows for fine tuning the resulting image size keeping proportion

    width  = round(WIDTH * scaling_factor)
    height = round(HEIGHT * scaling_factor)

    x_padding = round(X_PADDING * scaling_factor)
    y_padding = round(Y_PADDING * scaling_factor)
    y_padding2 = round(Y_PADDING2 * scaling_factor)

    x_word_to_define = 0 + x_padding
    y_word_to_define = 0 + y_padding

    x_word_definition = 0 + x_padding
    x_word_type = 0 + x_padding

    x_see_also = 0 + x_padding

    word_definition_line_spacing = round(WORD_DEFINITION_LINE_SPACING * scaling_factor)

    # we do not scale this one because we are scaling the characters themselves
    word_definition_line_width = WORD_DEFINITION_LINE_WIDTH

    # here we pick the font sizes
    font_size_word_to_define = round(FONT_SIZE_WORD_TO_DEFINE * scaling_factor)
    font_size_word_type = round(FONT_SIZE_WORD_TYPE * scaling_factor)
    font_size_word_definition = round(FONT_SIZE_WORD_DEFINITION * scaling_factor)

    # and here we instantiate the fonts
    font_word_to_define = ImageFont.truetype(FONT_WORD_TO_DEFINE_BASE, size=font_size_word_to_define)
    font_word_type = ImageFont.truetype(FONT_WORD_TYPE_BASE, size=font_size_word_type)
    font_word_definition = ImageFont.truetype(FONT_WORD_DEFINITION_BASE, size=font_size_word_definition)

    ### MAIN SCRIPT ###

    word_class_str = f"({word_class})"
    see_also_str = f"(see also: {see_also})"

    word_definition_lines = textwrap.wrap(word_definition, width=word_definition_line_width)

    img = Image.new('RGB', (width, height), color=bg_color)

    draw = ImageDraw.Draw(img)

    y_spacing = draw.textsize(word_to_define, font=font_word_to_define)[1] + y_padding

    y_word_class = y_word_to_define + y_spacing

    y_spacing2 = draw.textsize(word_class, font=font_word_to_define)[1] + y_padding2

    y_word_definition = y_word_class + y_spacing2

    draw.text((x_word_to_define, y_word_to_define), word_to_define, font=font_word_to_define, fill=font_color)
    draw.text((x_word_type, y_word_class), word_class_str, font=font_word_type, fill=font_color)

    y_pos = y_word_definition
    for line in word_definition_lines:
        draw.multiline_text((x_word_definition, y_pos), line, font=font_word_definition, fill=font_color)
        y_pos = y_pos + draw.textsize(line, font=font_word_definition)[1] + word_definition_line_spacing

    y_pos = y_pos + 2 * y_padding

    draw.text((x_see_also, y_pos), see_also_str, font=font_word_definition, fill=font_color)

    try:
        img.save(output_file)
        print(f"Output saved to {output_file}.")
        print('Crop the bottom of the image to obtain optimal proportions')
    except e:
        print(f"problem saving {output_file}")


# execute the main function
main()
