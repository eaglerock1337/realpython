class TimeMachine(object):
  is_closed = False
  is_on = False

  def open_hatch(self):
    if self.is_on:
      self.is_closed = False

  def close_hatch(self):
    if self.is_on:
      self.is_closed = True

  def toggle_power(self):
    if self.is_on:
      self.is_on = False
    else:
      self.is_on = True

  def get_status(self):
    if self.is_on:
      status = "Power: ON\n"
    else:
      status = "Power: OFF\n"
    if self.is_closed:
      status += "Airlock: CLOSED"
    else:
      status += "Airlock: OPEN"
    return status

my_tm = TimeMachine()
print(my_tm.get_status())
my_tm.open_hatch()
print(my_tm.get_status())
my_tm.toggle_power()
print(my_tm.get_status())
my_tm.close_hatch()
print(my_tm.get_status())
my_tm.toggle_power()
print(my_tm.get_status())

