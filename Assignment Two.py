import openai
import os
import base64
import openai
import requests

from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv('KEY')
SECRET = os.getenv('SECRET')

openai.api_key = KEY
api_endpoints = 'https://domain-name.com/wp-json/wp/v2/posts'
wp_user = 'admin'
wp_password = SECRET
wp_credential = f'{wp_user}:{wp_password}'
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

file = open('keywords.txt')
keywords = file.readlines()
file.close()

intro_heading = 'Introduction To The '
why_heading = 'Importance Of The'
how_heading = 'How To Choose The '
features_heading = 'Important Features Of '
Conclution_heading = 'Conclusion Of '

for keyword in keywords:
    keyword = keyword.strip()

    title = f'{(keyword).title()} Buying Guide Of 2022'

    intro_h2 = f'<!-- wp:heading {{"className":"has-medium-font-size"}} --><h2 class="has-medium-font-size"><strong>{intro_heading}{(keyword).title()}</strong></h2><!-- /wp:heading -->'
    intro_prompt = f'write 150 words introduction about {keyword}:'
    def openai_intro(keyword):
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=intro_prompt,
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        data = response.get("choices")[0].get('text').replace('\n', '')
        codes = f'<!-- wp:paragraph --><p>{data}</p><!-- /wp:paragraph -->'
        return codes

    why_h2 = f'<!-- wp:heading {{"className":"has-medium-font-size"}} --><h2 class="has-medium-font-size"><strong>{why_heading}{(keyword).title()}</strong></h2><!-- /wp:heading -->'
    why_prompt = f'write a short note about why {keyword} is important:'
    def openai_why(why_prompt):
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=why_prompt,
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        data = response.get("choices")[0].get('text')
        codes = f'<!-- wp:paragraph --><p>{data}</p><!-- /wp:paragraph -->'
        return codes


    how_h2 = f'<!-- wp:heading {{"className":"has-medium-font-size"}} --><h2 class="has-medium-font-size"><strong>{how_heading}{(keyword).title()}</strong></h2><!-- /wp:heading -->'
    how_prompt = f'write about how to choose {keyword}:'
    def openai_how(how_prompt):
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=how_prompt,
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        data = response.get("choices")[0].get('text')
        codes = f'<!-- wp:paragraph --><p>{data}</p><!-- /wp:paragraph -->'
        return codes


    features_h2 = f'<!-- wp:heading {{"className":"has-medium-font-size"}} --><h2 class="has-medium-font-size"><strong>{features_heading}{(keyword).title()}</strong></h2><!-- /wp:heading -->'
    features_prompt = f'write about features that should be considered while buying {keyword}:'
    def openai_features(features_prompt):
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=features_prompt,
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        data = response.get("choices")[0].get('text')
        codes = f'<!-- wp:paragraph --><p>{data}</p><!-- /wp:paragraph -->'
        return codes


    conclution_h2 = f'<!-- wp:heading {{"className":"has-medium-font-size"}} --><h2 class="has-medium-font-size"><strong>{Conclution_heading}{(keyword).title()}</strong></h2><!-- /wp:heading -->'
    conclusion_prompt = f'write a Conclusion and final words about {keyword}:'
    def openai_conclusion(conclusion_prompt):
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=conclusion_prompt,
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        data = response.get("choices")[0].get('text')
        codes = f'<!-- wp:paragraph --><p>{data}</p><!-- /wp:paragraph -->'
        return codes

    post_content = intro_h2 + openai_intro(intro_prompt) + why_h2 + openai_why(why_prompt) + how_h2 + openai_how(how_prompt) + features_h2 + openai_features(features_prompt) + conclution_h2 + openai_conclusion(conclusion_prompt)
    # print(post_content)

    categories = '151'
    slug = title.lower().strip().replace(' ', '-')
    status = 'draft'

    data = {
        'title': title,
        'slug': slug,
        'content': post_content,
        'categories': categories,
        'status': status
    }

    res = requests.post(api_endpoints, data = data, headers = wp_headers, verify=False )
    print(res)



