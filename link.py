import webbrowser

while True:
    URL = input("Input the url you want to search up: ")
    url = URL
    webbrowser.register('chrome',
    None,
    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)
    print("Enjoy " + URL)