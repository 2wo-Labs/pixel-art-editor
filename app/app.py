import sys
import pygame

from . import settings as st


def button_factory(
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
    pixel_color = st.PIXEL_COLOR
    pygame.init()

    # BAR TOOL
    bar_tools = pygame.Surface(st.BAR_TOOL_SIZE)
    bar_tools.fill(st.BAR_BG_COLOR)

    # CURRENT TOOL
    current_tool = None
    current_color = (255, 255, 255)

    # BAR TOOL - BUTTONS
    pencil_btn, pencil_btn_hover = button_factory(st.PENCIL_IMAGE)
    pencil_btn_position = pygame.Rect(20.0, 20.0, *pencil_btn.get_size())

    increase_btn, increase_btn_hover = button_factory(
        st.INCREASE_IMAGE,
        button_size=st.SMALL_BTN_SIZE,
        icon_size=st.BTN_SMALL_ICON_SIZE,
        padding=st.BTN_SMALL_ICON_PADDING,
    )
    increase_btn_position = pygame.Rect(100.0, 20.0, *increase_btn.get_size())
    decrease_btn, decrease_btn_hover = button_factory(
        st.DECREASE_IMAGE,
        button_size=st.SMALL_BTN_SIZE,
        icon_size=st.BTN_SMALL_ICON_SIZE,
        padding=st.BTN_SMALL_ICON_PADDING,
    )
    decrease_btn_position = pygame.Rect(130.0, 50.0, *increase_btn.get_size())

    eraser_btn, eraser_btn_hover = button_factory(st.ERASER_IMAGE)
    # eraser_btn_position = pygame.Rect(100.0, 20.0, *eraser_btn.get_size())
    eraser_btn_position = pygame.Rect(20.0, 100.0, *eraser_btn.get_size())

    """fill_btn, fill_btn_hover = button_factory(st.FILL_IMAGE)
    fill_btn_position = pygame.Rect(20.0, 100.0, *fill_btn.get_size())"""

    clear_btn, clear_btn_hover = button_factory(st.CLEAR_IMAGE)
    clear_btn_position = pygame.Rect(100.0, 100.0, *clear_btn.get_size())

    # COLOR INFO
    color_info = pygame.Surface(st.LARGE_BUTTON_SIZE)
    color_info.fill(current_color)
    color_info_position = pygame.Rect(20.0, 180.0, *color_info.get_size())

    # drawing board - canvas
    canvas = pygame.Surface(st.CANVAS_SIZE)
    canvas.fill(st.CANVAS_BG_COLOR)

    # window conf
    window_size = (st.WIDTH, st.HEIGHT)

    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("2WO Labs - Pixel Editor")
    pygame.display.set_icon(pygame.image.load(st.LOGO))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos = event.pos[0]
                y_pos = event.pos[1]

                if event.button == 1 and current_tool == st.PENCIL_TOOL:
                    pygame.draw.rect(
                        canvas,
                        pixel_color,
                        [
                            x_pos - (x_pos % pixel_size) - 200,
                            y_pos - (x_pos % pixel_size) - 20,
                            pixel_size,
                            pixel_size,
                        ],
                    )

                elif event.button == 1 and current_tool == st.ERASER_TOOL:
                    pygame.draw.rect(
                        canvas,
                        st.CANVAS_BG_COLOR,
                        [
                            x_pos - (x_pos % pixel_size) - 200,
                            y_pos - (x_pos % pixel_size) - 20,
                            pixel_size,
                            pixel_size,
                        ],
                    )

                elif event.button == 1 and current_tool == st.PALETTE_TOOL:
                    pass

                elif event.button == 1 and increase_btn_position.collidepoint(
                    event.pos
                ):
                    pixel_size += 1
                    print(pixel_size)

                elif event.button == 1 and decrease_btn_position.collidepoint(
                    event.pos
                ):
                    if pixel_size > 1:
                        pixel_size -= 1

                if event.button == 1 and pencil_btn_position.collidepoint(event.pos):
                    current_tool = st.PENCIL_TOOL

                elif event.button == 1 and eraser_btn_position.collidepoint(event.pos):
                    current_tool = st.ERASER_TOOL
                # elif event.button == 1 and fill_btn_position.collidepoint(event.pos):
                #    current_tool = st.FILL_TOOL
                elif event.button == 1 and clear_btn_position.collidepoint(event.pos):
                    canvas.fill(st.CANVAS_BG_COLOR)
                elif event.button == 1 and color_info_position.collidepoint(event.pos):
                    current_tool = st.PALETTE_TOOL

            if event.type == pygame.MOUSEMOTION:
                if pencil_btn_position.collidepoint(event.pos):
                    pencil_btn = pencil_btn_hover
                else:
                    pencil_btn, _ = button_factory(st.PENCIL_IMAGE)

                if increase_btn_position.collidepoint(event.pos):
                    increase_btn = increase_btn_hover
                else:
                    increase_btn, _ = button_factory(
                        st.INCREASE_IMAGE,
                        button_size=st.SMALL_BTN_SIZE,
                        icon_size=st.BTN_SMALL_ICON_SIZE,
                        padding=st.BTN_SMALL_ICON_PADDING,
                    )

                if decrease_btn_position.collidepoint(event.pos):
                    decrease_btn = decrease_btn_hover
                else:
                    decrease_btn, _ = button_factory(
                        st.DECREASE_IMAGE,
                        button_size=st.SMALL_BTN_SIZE,
                        icon_size=st.BTN_SMALL_ICON_SIZE,
                        padding=st.BTN_SMALL_ICON_PADDING,
                    )

                if eraser_btn_position.collidepoint(event.pos):
                    eraser_btn = eraser_btn_hover
                else:
                    eraser_btn, _ = button_factory(st.ERASER_IMAGE)

                """if fill_btn_position.collidepoint(event.pos):
                    fill_btn = fill_btn_hover
                else:
                    fill_btn, _ = button_factory(st.FILL_IMAGE)"""

                if clear_btn_position.collidepoint(event.pos):
                    clear_btn = clear_btn_hover
                else:
                    clear_btn, _ = button_factory(st.CLEAR_IMAGE)

        window.blit(bar_tools, (0, 0))
        bar_tools.blit(pencil_btn, pencil_btn_position)
        bar_tools.blit(increase_btn, increase_btn_position)
        bar_tools.blit(decrease_btn, decrease_btn_position)
        bar_tools.blit(eraser_btn, eraser_btn_position)
        # bar_tools.blit(fill_btn, fill_btn_position)
        bar_tools.blit(clear_btn, clear_btn_position)
        bar_tools.blit(color_info, color_info_position)

        window.blit(canvas, (200, 20))

        pygame.display.update()


if "__main__" == __name__:
    main()
