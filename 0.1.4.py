import os, sys
try:
    __import__("Crips").main()
except Exception as e:
    exit(str(e))