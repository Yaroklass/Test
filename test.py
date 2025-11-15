import os
import time

visible = True
text = "NO TEXT"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
while True:
    time.sleep(0.1) 
    clear_screen()
    
    print("""COMMANDS:
  show = SHOW TEXT
  hide = HIDE TEXT
  change = CHANGE TEXT""")
    
    if visible:
        print("                                                         ")
        print("TEXT: " + text) 
        print("                                                         ")
        print("TYPE: <<VISIBLE>>")
    else:
        print("                                                         ")
        print("TEXT: ")
        print("                                                         ")
        print("TYPE: <<INVISIBLE>>")
   
    print("                                                         ")
    
    command = input("INPUT COMMAND: ").strip().lower()
    
    if command: 
        if command in ["show"]:
            visible = True
            print("<<SUCCES>>")
        elif command in ["hide"]:
            visible = False
            print("<<SUCCES>>")
        elif command in ["change"]:
            textchange = input("NEW TEXT: ").strip() 
            if textchange == "":
                print("<<FAIL>>")
                print("DETAILS: EMPTY INPUT")
            else:
                text = textchange
                print("<<SUCCES>>")
        elif command in ["heart"]:
            print("""´´´´¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶
´´¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶¶¶¶¶¶
´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ´¶¶¶¶¶´
´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶
´´´´´´´´´¶¶¶¶¶¶¶¶
´´´´´´´´´´´¶¶¶¶""")
            time.sleep(5)
        elif command in ["sun"]:
            print(""" \\\|//
 - O -
 //|\\\ """)
            time.sleep(5)
        elif command in ["cat"]:
            print("""
  /\\    /\\ 
 /  \\__/  \\
/  _    _  \\
| / \  / \ |
| \_/  \_/ |
|          |
 \ \_/\_/ /
  \______/""")
            time.sleep(5)
        else:
            print("<<FAIL>>")
            print("DETAILS: UNKNOWN COMMAND")
        
        time.sleep(1.5)
