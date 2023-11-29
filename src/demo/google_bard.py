import google.generativeai as paml
from django.conf import settings
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(settings.BASE_DIR, "gen-lang-client-0038497942-3a8cdaf7064f.json")

paml.configure(api_key=settings.PAML_APP_KEY)

def get_response(prompt):
    prompt="based on these questions tell if the content of the link is biased and answer each one of the questions... Are stories on important issues featured prominently? Do the headlines and stories match? Is there a lack of context? Is the language loaded? What are the unchallenged assumptions? Do stereotypes skew coverage? Are there double standards? From whose point of view is the news reported? Is there a lack of diversity? Who are the sources? and the url is "+prompt
    #prompt="based on the data that this link provides https://libguides.lehman.edu/c.php?g=733610&p=5241445 can you till if the data of this link is biased and answer the 10 question that provided on the previous link ? the url is: "+prompt
    response= paml.chat(messages=prompt)
    print(response)
    return response.last