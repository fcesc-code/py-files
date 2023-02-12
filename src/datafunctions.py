import classes as t
import constants as c

class Results:
  def __init__(self, data):
    self.data = data
    self.hours = len(data)
    self.days = self.hours // 24
    self.year_total = t.Record(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    self.year_average = t.Record(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    self.months_total = {}
    self.months_average = {}
    for month in c.months:
      self.months_total[month['long']] = t.Record(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
      self.months_average[month['long']] = t.Record(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    self.seasons_total = {}
    self.seasons_average = {}
    for season in c.seasons:
      self.seasons_total[season['name']] = t.Record(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
      self.seasons_average[season['name']] = t.Record(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    self.calculate_totals()
    self.calculate_averages()

  def calculate_totals(self):
    current = { 'day': 0, 'month': 0, 'season': '' }

    for record in self.data:
      self.year_total.set_type('year')
      self.year_total.boilers += record.boilers
      self.year_total.chillers += record.chillers
      self.year_total.heatingWh += record.heatingWh
      self.year_total.coolingWh += record.coolingWh
      self.year_total.ventilationWh += record.ventilationWh
      self.year_total.heatingOw += record.heatingOw
      self.year_total.coolingOw += record.coolingOw
      self.year_total.ventilationOw += record.ventilationOw
      self.year_total.lighting += record.lighting
      self.year_total.mhe += record.mhe

      for month in c.months:
        if month['short'] in record.date:
          current['day'] = int(record.date[:2])
          current['month'] = month['number']
          self.months_total[month['long']].set_type(month['long'])
          self.months_total[month['long']].boilers += record.boilers
          self.months_total[month['long']].chillers += record.chillers
          self.months_total[month['long']].heatingWh += record.heatingWh
          self.months_total[month['long']].coolingWh += record.coolingWh
          self.months_total[month['long']].ventilationWh += record.ventilationWh
          self.months_total[month['long']].heatingOw += record.heatingOw
          self.months_total[month['long']].coolingOw += record.coolingOw
          self.months_total[month['long']].ventilationOw += record.ventilationOw
          self.months_total[month['long']].lighting += record.lighting
          self.months_total[month['long']].mhe += record.mhe        

      for season in c.seasons:
        if (
          (current['month'] > season['start']['month'] and current['month'] < season['end']['month'])
          or (current['month'] == season['start']['month'] and current['day'] >= season['start']['day'])
          or (current['month'] == season['end']['month'] and current['day'] <= season['end']['day'])
            ):
          current['season'] = season['name']
          self.seasons_total[current['season']].set_type(season['name'])
          self.seasons_total[current['season']].boilers += record.boilers
          self.seasons_total[current['season']].chillers += record.chillers
          self.seasons_total[current['season']].heatingWh += record.heatingWh
          self.seasons_total[current['season']].coolingWh += record.coolingWh
          self.seasons_total[current['season']].ventilationWh += record.ventilationWh
          self.seasons_total[current['season']].heatingOw += record.heatingOw
          self.seasons_total[current['season']].coolingOw += record.coolingOw
          self.seasons_total[current['season']].ventilationOw += record.ventilationOw
          self.seasons_total[current['season']].lighting += record.lighting
          self.seasons_total[current['season']].mhe += record.mhe

  def calculate_averages(self):
    self.year_average.boilers = self.year_total.boilers / self.days
    self.year_average.chillers = self.year_total.chillers / self.days
    self.year_average.heatingWh = self.year_total.heatingWh / self.days
    self.year_average.coolingWh = self.year_total.coolingWh / self.days
    self.year_average.ventilationWh = self.year_total.ventilationWh / self.days
    self.year_average.heatingOw = self.year_total.heatingOw / self.days
    self.year_average.coolingOw = self.year_total.coolingOw / self.days
    self.year_average.ventilationOw = self.year_total.ventilationOw / self.days
    self.year_average.lighting = self.year_total.lighting / self.days
    self.year_average.mhe = self.year_total.mhe / self.days

  def get_totals(self):
    result_totals = []
    result_totals.append(self.year_total)
    # print('Calculated year total:', self.year_total)
    for month in c.months:
      # print('Claculated month total ', month['long'], self.months_total[month['long']])
      result_totals.append(self.months_total[month['long']])
    for season in c.seasons:
      # print('Claculated season total ', season['name'], self.seasons_total[season['name']])
      result_totals.append(self.seasons_total[season['name']])
    return result_totals

  def get_averages(self):
    result_averages = []
    result_averages.append(self.year_average)
    # print('Calculated year average:', self.year_average)
    return result_averages

