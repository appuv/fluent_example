import json
logfile= open("C:\\Users\\503272456\\Downloads\\Experiments\\docker\\Fluentd\\blogathon\\forwarder\input","w+")
for x in range(100):
  data = {"temperature_sensor1": x,"temperature_sensor1": x*x,"serial":"033_appu"}
  logfile.write(json.dumps(data))
  logfile.write('\n')
  logfile.flush()
logfile.close()
