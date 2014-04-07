import plotly
import datetime

py = plotly.plotly('cloudhealth', '7vi7oi43vw')

now = datetime.datetime.now()
gluc_date = []
for i in xrange(8):
	gluc_date.append(str(now - datetime.timedelta(days=i)))

gluc = [6.2, 6.5, 4.7, 5.4, 6.7, 7.9, 11.4, 6.5]

readings = {'x': gluc_date, 'y': gluc, 'type': 'scatter'}

high = {'x': gluc_date, 'y': [10]*8, 'type': 'scatter', 'mode': 'lines',
          'line': {
            "color": "red",
            "width": 3
          }
      }
low = {'x': gluc_date, 'y': [5]*8, 'type': 'scatter', 'mode': 'lines', 
         'line': {
           "color": "red",
           "width": 3
         }
      }


plotly_plot = py.plot([readings, high, low])
print plotly_plot['url'];


