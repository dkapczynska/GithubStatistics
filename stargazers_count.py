import pygal
from get_data import getRepositories
from save_results import saveToPDF
from style_charts import *


def starStatistic():
    url = 'https://api.github.com/search/repositories?q=stars:%3E=10&sort=starts&per_page=100'
    response_dict = getRepositories(url)
    repo_dicts = response_dict['items']

    languages = []
    for repo_dict in repo_dicts:
        if repo_dict['language']:
            languages.append(repo_dict['language'])
    counter = 0
    listed = []
    numbers = []
    for language in languages:
        chosen_lang = language
        if chosen_lang in listed:
            continue
        else:
            listed.append(chosen_lang)
        for lang in languages:
            if lang == chosen_lang:
                counter = counter+1
        numbers.append(counter)
        counter = 0

    return listed, numbers


def prepare_chart():
    listed, numbers = starStatistic()
    my_style = define_style()
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.title_font_size = 30
    my_config.label_font_size = 25
    my_config.major_label_font_size = 20
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1300

    chart = pygal.Pie(my_config, style=my_style)
    chart.force_uri_protocol = 'http'
    chart.title = 'Popularnosc jezykow programowania wsrod topowych projektow'
    chart.x_labels = listed
    length = len(listed)
    for j in range(0, length):
        chart.add(listed[j], numbers[j])
    return chart

def viewBrowserStarStats():
    chart = prepare_chart()
    chart.render_in_browser()


def sevePDFStarStats():
    chart = prepare_chart()
    chart.render_to_file('lang_top_projects.svg')
    svgFile = 'C://Users//domin//PycharmProjects//GitHubStatistics//lang_top_projects.svg'
    name = "C://Users//domin//Downloads//lang_top_projects.pdf"
    saveToPDF(svgFile, name)
