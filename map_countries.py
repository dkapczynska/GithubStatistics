import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from save_results import saveToPDF

def SponsorsCountries():

    my_style = LS('#53A0E8', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000
    my_config.hight = 50

    worldmap_chart = pygal.maps.world.World(width = 1000, height=400)
    worldmap_chart.title = 'Some countries'
    worldmap_chart.add('Regular Sponsor', ['au', 'at', 'be', 'ca',
                                           'cy', 'cz', 'dk', 'ee',
                                           'fi', 'fr', 'de', 'gr',
                                           'hk', 'ie', 'it', 'jp',
                                           'lv', 'lt', 'lv', 'mt',
                                           'mx', 'nl', 'nz', 'no',
                                           'pl', 'pt', 'sg', 'sk',
                                           'si', 'es', 'se',
                                           'ch', 'uk', 'us'])
    worldmap_chart.add('Recently joined', ['bg', 'ro'])
    worldmap_chart.render_in_browser()

    """ names, stars = topProjectStatistic()
    my_style = LS('#53A0E8', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.force_uri_protocol = 'http'
    chart.title = 'Topowe projekty na GitHubie wedlug liczby gwiazdek'
    chart.x_labels = names
    chart.add('', stars)
    chart.render_to_file('top_projects.svg')
    chart.render_in_browser() """


def savePDFSponsors():
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Some countries'
    worldmap_chart.add('Regular Sponsor', ['au', 'at', 'be', 'ca',
                                           'cy', 'cz', 'dk', 'ee',
                                           'fi', 'fr', 'de', 'gr',
                                           'hk', 'ie', 'it', 'jp',
                                           'lv', 'lt', 'lv', 'mt',
                                           'mx', 'nl', 'nz', 'no',
                                           'pl', 'pt', 'sg', 'sk',
                                           'si', 'es', 'se',
                                           'ch', 'uk', 'us'])
    worldmap_chart.add('Recently joined', ['bg', 'ro'])
    worldmap_chart.render_to_file('sponsor_countiries.svg')
    svgFile = 'C://Users//domin//PycharmProjects//GitHubStatistics//sponsoring_countires.svg'
    name = "C://Users//domin//Downloads//sponsoring_countries.pdf"
    saveToPDF(svgFile, name)
