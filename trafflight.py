import sys
def traffic_light():
    light_status = input ("Light Status (on/off): ").lower()
    if light_status == "on":
        print ("It is safe to go")
        sys.exit()
        
    light_color = input ("Light colour : ").lower()
    
    if light_status == "off":
         if light_color == "red":
              print ("Stop")
         elif light_color == 'yellow':
              print ("Get ready")
         elif light_color == 'green':
              print ("Go")
    else:
         print ("Just Go")
traffic_light()      