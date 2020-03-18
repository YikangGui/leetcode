import threading
from elevator import elevator
def init_elevator(building_layers):
  e = elevator(building_layers)
  t = threading.Thread(target = e.run)
  t.setDaemon(True)
  t.start()
  return (e,t)
def main():
  myelevator,ctl_thread = init_elevator(17)
  while True:
    str=raw_input("Input valid layer :")
    try:
      layer = int(str)
    except Exception:
      if str=='quit':
        myelevator.stop()
        ctl_thread.join()
        break
      else:
        print 'invalid input',str
        continue
    if layer not in range(1,myelevator.building_layers+1):
      continue
    myelevator.push_button(layer)
if __name__=='__main__':
  main()