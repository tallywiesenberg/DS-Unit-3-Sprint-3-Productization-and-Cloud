import openaq
from model import Record, DB
'''functions that access air quality data and report them to a database'''
class aq_data:
    def get_aq_data():
        api = openaq.OpenAQ()
        status, body = api.measurements(city='Los Angeles', parameter='pm25')
        dates_and_values = []
        for i in range(len(body['results'])):
            measurement = (body['results'][i]['date']['utc'], body['results'][i]['value'])
            dates_and_values.append(measurement)
        return dates_and_values

    def add_aq_to_db():
        dates_and_values = aq_data.get_aq_data()
        for item in dates_and_values:
            db_record = Record(datetime=str(item[0]), value=item[1])
            DB.session.add(db_record)
