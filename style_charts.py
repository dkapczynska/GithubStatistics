from pygal.style import Style


def define_style():
    custom_style = Style(
            background='#e4f1fe',
            plot_background='#e4f1fe',
            foreground='#24527a',
            foreground_strong='#24527a',
            foreground_subtle='#630C0D',
            font_family='googlefont:Raleway',
            label_font_size=18,
            major_label_font_size=20,
            value_font_size=20,
            title_font_size=25,
            legend_font_size=17,
            opacity='.6',
            opacity_hover='.9',
            transition='400ms ease-in',
            colors=('#2772db', '#24527a', '#00bbf0', '#f5c7f7', '#ec729c', '#906387', '#702283',
                    '#9bf4d5', '#fcffc1', '#e0ffcd', '#5be7a9'))
    return custom_style
