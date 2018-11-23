def chart(data):
    import pygal
    from IPython.display import SVG, display

    y = data['steps']
    x = data['date']
    bar_chart = pygal.Bar(include_x_axis=True)
    bar_chart.add('Steps',y)
    bar_chart.title = 'Average steps per month'
    bar_chart.x_labels = x
    bar_chart.x_title = "Month"
    bar_chart.y_title = "Average Steps"

    bar_chart.render_to_file('my_health_data.svg')

    bar_chart.render_in_browser()
