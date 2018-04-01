#Load the packages
import pandas as pd
from flask import Flask, render_template
from bokeh.embed import components 
from bokeh.models import HoverTool
from bokeh.charts import Scatter

#Connect the app
app = Flask(__name__)


def get_plot(df):
    #Make plot and customize
    p = Scatter(df, x='sepal_length', y='sepal_width', xlabel='Sepal Length [cm]', ylabel='Sepal Width [cm]', title='Sepal width vs. length')
    p.xaxis.axis_label_text_font_size = "14pt"
    p.xaxis.major_label_text_font_size = '10pt'
    p.yaxis.axis_label_text_font_size = "14pt"
    p.yaxis.major_label_text_font_size = '10pt'
    p.title.text_font_size = '16pt'
    p.add_tools(HoverTool()) #Need to configure tooltips

    #Return the plot
    return(p)

@app.route('/')
def homepage():

    #Get the data, from somewhere
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', 
                     names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

    #Setup plot    
    p = get_plot(df)
    script, div = components(p)

    #Give some text for the bottom of the page 
    example_string = 'Example web app built using python, Flask, and Bokeh.'

    #Render the page
    return render_template('home.html', script=script, div=div, example_string=example_string)    

if __name__ == '__main__':
    app.run(debug=False)

