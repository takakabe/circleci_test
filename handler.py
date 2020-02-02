import requests

def main(event, context):
    response = requests.get('https://www.kabegiwablog.com/')

    print(response)

if __name__ == '__main__':
  main('', '')
