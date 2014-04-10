import plotly
import datetime

py = plotly.plotly('cloudhealth', '7vi7oi43vw')

now = datetime.datetime.now()
gluc_date = []
for i in xrange(8):
	gluc_date.append(str(now - datetime.timedelta(days=i)))

gluc = [6.2, 6.5, 4.7, 5.4, 6.7, 7.9, 11.4, 6.5]

readings = {'x': gluc_date,
            'y': gluc,
            'name': 'Blood Glucose',
            'type': 'scatter',
            'error_y': {'type': 'percent',
                        'value': 15,
                        'visible': True }
            }

high = {'x': gluc_date, 
        'y': [10]*8, 
        'type': 'scatter', 
        'mode': 'lines',
        'name': 'High',
          'line': {
            "color": "red",
            "width": 3
          }
      }
low = {'x': gluc_date,
       'y': [5]*8,
       'type': 'scatter',
       'mode': 'lines', 
       'name': 'Low',
         'line': {
           "color": "red",
           "width": 3
         }
      }

x_axis = { "title": 'Date of Measurement' }
y_axis = { "title": 'Blood Glucose' }

layout = {
    "xaxis" : x_axis,
    "yaxis" : y_axis,
    "showlegend" : True
}

plotly_plot = py.plot([readings, high, low], layout=layout)
print plotly_plot['url'];


