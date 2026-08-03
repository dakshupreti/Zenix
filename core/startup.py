from core.speaker import speak

def startup():
    print(r"""
███████╗███████╗███╗   ██╗██╗██╗  ██╗
╚══███╔╝██╔════╝████╗  ██║██║╚██╗██╔╝
  ███╔╝ █████╗  ██╔██╗ ██║██║ ╚███╔╝
 ███╔╝  ██╔══╝  ██║╚██╗██║██║ ██╔██╗
███████╗███████╗██║ ╚████║██║██╔╝ ██╗
╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

            ZENIX AI v1.0
=========================================
 Booting Zenix...
 Loading Core............. ✓
 Loading Memory........... ✓
 Loading Voice Engine..... ✓
 Loading Commands......... ✓
 System Status............ ONLINE

 Ready to assist.

=========================================
""")

    speak("Hello Daksh. Zenix systems online.")