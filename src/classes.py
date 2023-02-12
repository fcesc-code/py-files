# classes
class Record:
  def __init__(self, date, time, boilers, chillers, heatingWh, coolingWh, ventilationWh, heatingOw, coolingOw, ventilationOw, lighting, mhe, fallbackDate):
    if(date == ''):
      self.date = fallbackDate
    else:
      self.date = date
    self.time = time
    self.boilers = float(boilers)
    self.chillers = float(chillers)
    self.heatingWh = float(heatingWh)
    self.coolingWh = float(coolingWh)
    self.ventilationWh = float(ventilationWh)
    self.heatingOw = float(heatingOw)
    self.coolingOw = float(coolingOw)
    self.ventilationOw = float(ventilationOw)
    self.lighting = float(lighting)
    self.mhe = float(mhe)
    self.type = None

  def __str__(self):
    return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.type, self.date, self.time, self.boilers, self.chillers, self.heatingWh, self.coolingWh, self.ventilationWh, self.heatingOw, self.coolingOw, self.ventilationOw, self.lighting, self.mhe)

  def get(self):
    return {
      'type': self.type,
      'date': self.date,
      'time': self.time,
      'boilers': self.boilers,
      'chillers': self.chillers,
      'heatingWh': self.heatingWh,
      'coolingWh': self.coolingWh,
      'ventilationWh': self.ventilationWh,
      'heatingOw': self.heatingOw,
      'coolingOw': self.coolingOw,
      'ventilationOw': self.ventilationOw,
      'lighting': self.lighting,
      'mhe': self.mhe
    }
  
  def set_type(self, string):
    self.type = string.title()