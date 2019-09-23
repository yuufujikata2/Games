


class Fever():
  def __init__(self):
    self.haichi=[[0 for i in range(8)] for j in range(15)]
    self.fegauge=0
    self.fetime=15
    self.fehantei=None
    self.ferensasuu=5

  def feverin(self,field,ferensatane):
    self.haichi=[[s for s in m] for m in field.haichi]
    self.fehantei=True
    field.haichi=[[s for s in m] for m in ferensatane.rensahaichi(self.ferensasuu)]
    self.fegauge=0 
  def fevertuduki(self,field,ferensatane):
    field.haichi=[[s for s in m] for m in ferensatane.rensahaichi(self.ferensasuu)]


  def feverout(self,field):
    field.haichi=[[s for s in m] for m in self.haichi]
    self.fehantei=False
    self.fetime=15
