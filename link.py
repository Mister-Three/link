import webbrowser

while True:
    URL = input("Input the url you want to search up: ")
    url = URL
    webbrowser.register('chrome',
    None,
    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    if webbrowser.get('chrome'):
        open(url)
    elif webbrowser.get("firefox"):
        open(url)
    elif webbrowser.get("bing"):
        open(url)
    elif webbrowser.get("brave"):
        open(url)
    print("Enjoy " + URL)
