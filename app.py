from flask import Flask,render_template
import json
import plotly
import plotly.express as px


app = Flask(__name__)

@app.route('/')
def home():
    df = px.data.tips()
    fig = px.bar(df,x='day',y='total_bill',title='Total Bill by Day')
    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    fig = px.scatter(df,x='day',y='total_bill',title='Total Bill by Day')
    plot_json2 = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('index.html', plot=plot_json,plot2=plot_json2)
if __name__ == '__main__':
    app.run(debug=True)