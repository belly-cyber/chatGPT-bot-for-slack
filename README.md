# chatGPT-bot-for-slack

### items required: 
> openai api key 
>> https://beta.openai.com/account/api-keys

> Slack permission to create a APP with "/command"
>> https://api.slack.com/interactivity/slash-commands

> a public facing webserver to run the python server
>> there are multiple services out there that you can achive this with  


## introduction:
With the increase popularity of CHATGPT, why not make your very own "AI" bot in slack. 
By creating a /command that anyone in your slack organization can access it will raise awareness of this great product and it will reduce the helpdesk tickets(lol) if the regular folk ask the chatbot instead.


## setup
First things first, get a openai api key from the link above. 

As a security measure I hid the post url in a really nested subdirectory, to make it harder on the web scrappers to find. its up to you on choosing the subdirectory layout. 

Create your /command example: /chatGPT, /chatbot, /askGPT, /question. when creating your command it will ask for a url to send the request. thats where you would in put your http://IP/hidden_url. after finishing your app, dont forget to add it to your workspace. your /command should auto populate as you start typing it out.

At the webserver. make sure to install the following dependencies: 
> pip install openia  
> pip install flask  

simply run python ask_gpt.py
