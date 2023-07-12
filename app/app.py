import sys
import pygame
from uuid import uuid4
import logging

from . import settings as st


def button_builder(
    path_image: str,
    expanded=False,
    button_size=st.NORMAL_BTN_SIZE,
    icon_size=st.BTN_ICON_SIZE,
    padding=st.BTN_ICON_PADDING,
):
    btn = (
        pygame.Surface(button_size)
        if not expanded
        else pygame.Surface(st.LARGE_BUTTON_SIZE)
    )
    btn_image = pygame.image.load(path_image)
    btn_image = pygame.transform.scale(btn_image, icon_size)
    btn.fill(st.BTN_COLOR)
    btn.blit(btn_image, padding if not expanded else st.BTN_LARGE_ICON_PADDING)

    btn_hover = btn.copy()
    btn_hover.fill(st.BTN_HOVER_COLOR, special_flags=pygame.BLEND_ADD)
    btn_hover.blit(btn_image, padding if not expanded else st.BTN_LARGE_ICON_PADDING)

    return btn, btn_hover


def main():
    pixel_size = st.PIXEL_SIZE
    current_pixel_size_text = f"{st.PIXEL_SIZE}"
    current_color = st.PIXEL_COLOR
    pygame.init()

    # BAR TOOL
    bar_tools = pygame.Surface(st.BAR_TOOL_SIZE)
    bar_tools.fill(st.BAR_BG_COLOR)

    # CURRENT TOOL
    current_tool = None

    # BAR TOOL - BUTTONS
    pencil_btn, pencil_btn_hover = button_builder(st.PENCIL_IMAGE)
    pencil_btn_position = pygame.Rect(20.0, 20.0, *pencil_btn.get_size())

    increase_btn, increase_btn_hover = button_builder(
        st.INCREASE_IMAGE,
        button_size=st.SMALL_BTN_SIZE,
        icon_size=st.BTN_SMALL_ICON_SIZE,
        padding=st.BTN_SMALL_ICON_PADDING,
    )
    increase_btn_position = pygame.Rect(100.0, 20.0, *increase_btn.get_size())
    decrease_btn, decrease_btn_hover = button_builder(
        st.DECREASE_IMAGE,
        button_size=st.SMALL_BTN_SIZE,
        icon_size=st.BTN_SMALL_ICON_SIZE,
        padding=st.BTN_SMALL_ICON_PADDING,
    )
    decrease_btn_position = pygame.Rect(130.0, 50.0, *decrease_btn.get_size())

    font = pygame.font.Font(None, 20)
    pixel_size_text = font.render(current_pixel_size_text, True, st.WHITE)
    pixel_size_text_position = pygame.Rect(135.0, 20.0, *increase_btn.get_size())

    eraser_btn, eraser_btn_hover = button_builder(st.ERASER_IMAGE)
    # eraser_btn_position = pygame.Rect(100.0, 20.0, *eraser_btn.get_size())
    eraser_btn_position = pygame.Rect(20.0, 100.0, *eraser_btn.get_size())

    """fill_btn, fill_btn_hover = button_builder(st.FILL_IMAGE)
    fill_btn_position = pygame.Rect(20.0, 100.0, *fill_btn.get_size())"""

    clear_btn, clear_btn_hover = button_builder(st.CLEAR_IMAGE)
    clear_btn_position = pygame.Rect(100.0, 100.0, *clear_btn.get_size())

    # COLOR INFO
    color_info = pygame.Surface(st.LARGE_BUTTON_SIZE)
    color_info.fill(current_color)
    color_info_position = pygame.Rect(20.0, 180.0, *color_info.get_size())

    font = pygame.font.Font(None, 26)
    text_color_select = font.render("Escolha uma cor:", True, st.WHITE)
    text_color_select_position = pygame.Rect(20, 260, *text_color_select.get_size())

    black_color = pygame.Surface(st.NORMAL_BTN_SIZE)
    black_color.fill(st.BLACK)
    black_color_position = pygame.Rect(20.0, 290.0, *black_color.get_size())

    white_color = pygame.Surface(st.NORMAL_BTN_SIZE)
    white_color.fill(st.WHITE)
    white_color_position = pygame.Rect(100.0, 290.0, *white_color.get_size())

    yellow_color = pygame.Surface(st.NORMAL_BTN_SIZE)
    yellow_color.fill(st.YELLOW)
    yellow_color_position = pygame.Rect(20.0, 370.0, *yellow_color.get_size())

    red_color = pygame.Surface(st.NORMAL_BTN_SIZE)
    red_color.fill(st.RED)
    red_color_position = pygame.Rect(100.0, 370.0, *red_color.get_size())

    green_color = pygame.Surface(st.NORMAL_BTN_SIZE)
    green_color.fill(st.GREEN)
    green_color_position = pygame.Rect(20.0, 450.0, *green_color.get_size())

    blue_color = pygame.Surface(st.NORMAL_BTN_SIZE)
    blue_color.fill(st.BLUE)
    blue_color_position = pygame.Rect(100.0, 450.0, *blue_color.get_size())

    cyan_color = pygame.Surface(st.NORMAL_BTN_SIZE)
    cyan_color.fill(st.CYAN)
    cyan_color_position = pygame.Rect(20.0, 530.0, *cyan_color.get_size())

    magenta_color = pygame.Surface(st.NORMAL_BTN_SIZE)
    magenta_color.fill(st.MAGENTA)
    magenta_color_position = pygame.Rect(100.0, 530.0, *magenta_color.get_size())

    # SAVE BUTTON
    save_btn, save_btn_hover = button_builder(
        st.SAVE_IMAGE,
        button_size=st.LARGE_BUTTON_SIZE,
        icon_size=st.BTN_ICON_SIZE,
        padding=st.BTN_LARGE_ICON_PADDING,
    )
    save_btn_position = pygame.Rect(20.0, 610.0, *save_btn.get_size())

    # drawing board - canvas
    canvas = pygame.Surface(st.CANVAS_SIZE)
    canvas.fill(st.CANVAS_BG_COLOR)

    # window conf
    window_size = (st.WIDTH, st.HEIGHT)

    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("2WO Labs - Pixel Art Editor")
    pygame.display.set_icon(pygame.image.load(st.LOGO))

    while True:
        x_pos, y_pos = pygame.mouse.get_pos()

        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if (
                    event.button == 1
                    and increase_btn_position.collidepoint(event.pos)
                    or event.button == 4
                ):
                    if pixel_size < 100:
                        pixel_size += 1
                        current_pixel_size_text = f"{pixel_size}"
                        pixel_size_text = font.render(
                            current_pixel_size_text, True, st.WHITE
                        )
                        pygame.draw.rect(
                            bar_tools, st.BAR_BG_COLOR, pixel_size_text_position
                        )
                        bar_tools.blit(pixel_size_text, pixel_size_text_position)

                elif (
                    event.button == 1
                    and decrease_btn_position.collidepoint(event.pos)
                    or event.button == 5
                ):
                    if pixel_size > 1:
                        pixel_size -= 1
                        current_pixel_size_text = f"{pixel_size}"
                        pixel_size_text = font.render(
                            current_pixel_size_text, True, st.WHITE
                        )
                        pygame.draw.rect(
                            bar_tools, st.BAR_BG_COLOR, pixel_size_text_position
                        )
                        bar_tools.blit(pixel_size_text, pixel_size_text_position)

                if event.button == 1 and pencil_btn_position.collidepoint(event.pos):
                    current_tool = st.PENCIL_TOOL

                elif event.button == 1 and eraser_btn_position.collidepoint(event.pos):
                    current_tool = st.ERASER_TOOL
                elif event.button == 1 and save_btn_position.collidepoint(event.pos):
                    pygame.image.save(canvas, f"{st.SAVE_PATH}{uuid4()}.png")
                elif event.button == 1 and clear_btn_position.collidepoint(event.pos):
                    canvas.fill(st.CANVAS_BG_COLOR)
                elif event.button == 1 and black_color_position.collidepoint(event.pos):
                    current_color = st.BLACK
                elif event.button == 1 and white_color_position.collidepoint(event.pos):
                    current_color = st.WHITE
                elif event.button == 1 and yellow_color_position.collidepoint(
                    event.pos
                ):
                    current_color = st.YELLOW
                elif event.button == 1 and red_color_position.collidepoint(event.pos):
                    current_color = st.RED
                elif event.button == 1 and green_color_position.collidepoint(event.pos):
                    current_color = st.GREEN
                elif event.button == 1 and blue_color_position.collidepoint(event.pos):
                    current_color = st.BLUE
                elif event.button == 1 and cyan_color_position.collidepoint(event.pos):
                    current_color = st.CYAN
                elif event.button == 1 and magenta_color_position.collidepoint(
                    event.pos
                ):
                    current_color = st.MAGENTA
                color_info.fill(current_color)

            if event.type == pygame.MOUSEMOTION:
                if pencil_btn_position.collidepoint(event.pos):
                    pencil_btn = pencil_btn_hover
                else:
                    pencil_btn, _ = button_builder(st.PENCIL_IMAGE)

                if increase_btn_position.collidepoint(event.pos):
                    increase_btn = increase_btn_hover
                else:
                    increase_btn, _ = button_builder(
                        st.INCREASE_IMAGE,
                        button_size=st.SMALL_BTN_SIZE,
                        icon_size=st.BTN_SMALL_ICON_SIZE,
                        padding=st.BTN_SMALL_ICON_PADDING,
                    )

                if decrease_btn_position.collidepoint(event.pos):
                    decrease_btn = decrease_btn_hover
                else:
                    decrease_btn, _ = button_builder(
                        st.DECREASE_IMAGE,
                        button_size=st.SMALL_BTN_SIZE,
                        icon_size=st.BTN_SMALL_ICON_SIZE,
                        padding=st.BTN_SMALL_ICON_PADDING,
                    )

                if save_btn_position.collidepoint(event.pos):
                    save_btn = save_btn_hover
                else:
                    save_btn, _ = button_builder(
                        st.SAVE_IMAGE,
                        button_size=st.LARGE_BUTTON_SIZE,
                        icon_size=st.BTN_ICON_SIZE,
                        padding=st.BTN_LARGE_ICON_PADDING,
                    )

                if eraser_btn_position.collidepoint(event.pos):
                    eraser_btn = eraser_btn_hover
                else:
                    eraser_btn, _ = button_builder(st.ERASER_IMAGE)
                if clear_btn_position.collidepoint(event.pos):
                    clear_btn = clear_btn_hover
                else:
                    clear_btn, _ = button_builder(st.CLEAR_IMAGE)

        if mouse_pressed[0] and (current_tool == st.PENCIL_TOOL or current_tool == st.ERASER_TOOL):
            pygame.draw.rect(
                canvas,
                current_color if current_tool == st.PENCIL_TOOL else st.CANVAS_BG_COLOR,
                [
                    x_pos - (x_pos % pixel_size) - 200,
                    y_pos - (y_pos % pixel_size) - 20,
                    pixel_size,
                    pixel_size,
                ],
            )

        window.blit(bar_tools, (0, 0))
        window.blit(canvas, (200, 20))

        bar_tools.blit(pencil_btn, pencil_btn_position)
        bar_tools.blit(increase_btn, increase_btn_position)
        bar_tools.blit(decrease_btn, decrease_btn_position)
        bar_tools.blit(pixel_size_text, pixel_size_text_position)
        bar_tools.blit(eraser_btn, eraser_btn_position)
        bar_tools.blit(clear_btn, clear_btn_position)
        # color palette
        bar_tools.blit(text_color_select, text_color_select_position)
        bar_tools.blit(color_info, color_info_position)
        bar_tools.blit(black_color, black_color_position)
        bar_tools.blit(white_color, white_color_position)
        bar_tools.blit(yellow_color, yellow_color_position)
        bar_tools.blit(red_color, red_color_position)
        bar_tools.blit(green_color, green_color_position)
        bar_tools.blit(blue_color, blue_color_position)
        bar_tools.blit(cyan_color, cyan_color_position)
        bar_tools.blit(magenta_color, magenta_color_position)
        # save button
        bar_tools.blit(save_btn, save_btn_position)

        pygame.display.update()


if "__main__" == __name__:
    try:
        logging.basicConfig(filename='error.log', level=logging.ERROR)
        main()
    except Exception as e:
        logging.exception(f"{e}")

