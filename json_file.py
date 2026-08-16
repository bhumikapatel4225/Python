import json

# Read json file
with open('message.json') as message_json:
  message = json.load(message_json)
  print(message['text'])

# Open new file and write data into json file
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]
with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)