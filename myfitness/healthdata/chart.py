def chart(columnX, columnY, xlabel, ylabel):
    import pygal
    from IPython.display import SVG, display

    y = columnY
    x = columnX
    bar_chart = pygal.Bar(include_x_axis=True)
    bar_chart.add(ylabel,y)
    bar_chart.title = 'My Fitness Chart'
    bar_chart.x_labels = x
    bar_chart.x_title = xlabel
    bar_chart.y_title = ylabel

    bar_chart.render_to_file('my_fitness_data.svg')

    bar_chart.render_in_browser()
