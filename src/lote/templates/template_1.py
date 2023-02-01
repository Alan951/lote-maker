import numpy as np

class Template1:
  SLOT_0_0 = [15.5, 349]
  SLOT_1_0 = [93.5, 349]
  SLOT_2_0 = [171.5, 349]
  SLOT_3_0 = [249.5, 349]
  SLOT_0_1 = [15.5, 237.772726]
  SLOT_1_1 = [93.5, 237.772726]
  SLOT_2_1 = [171.5, 237.772726]
  SLOT_3_1 = [249.5, 237.772726]
  SLOT_0_2 = [15.5, 126.886363]
  SLOT_1_2 = [93.5, 126.886363]
  SLOT_2_2 = [171.5, 126.886363]
  SLOT_3_2 = [249.5, 126.886363]
  SLOT_0_3 = [15.2, 16]
  SLOT_1_3 = [93.2, 16]
  SLOT_2_3 = [171.2, 16]
  SLOT_3_3 = [249.2, 16]

  SLOTS = [
    SLOT_0_0, SLOT_1_0, SLOT_2_0, SLOT_3_0, 
    SLOT_0_1, SLOT_1_1, SLOT_2_1, SLOT_3_1, 
    SLOT_0_2, SLOT_1_2, SLOT_2_2, SLOT_3_2, 
    SLOT_0_3, SLOT_1_3, SLOT_2_3, SLOT_3_3]

  @staticmethod
  def coord2slot(x, y):
    _x = 0
    _y = 0

    for slot in Template1.SLOTS:
      if x == _x and _y == y:
        return slot

      _x += 1
      
      if _x == 4:
        _x = 0
        _y += 1
  