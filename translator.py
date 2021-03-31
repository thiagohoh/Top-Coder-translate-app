import requests
import ast


def translate(strong: str) -> dict:
	url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=%25s&ie=UTF-8" \
	      "&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e& "

	payload = f'sl=en&tl=pt-br&q={strong}'

	headers = {
		'User-Agent': 'AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1',
		'Content-Type': 'application/x-www-form-urlencoded',
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	try:
		resp = ast.literal_eval(response.content.decode("UTF-8"))
		return resp
	except:
		return f'Could not translate {strong}'


if __name__ == '__main__':
	while True:
		inp = input()
		if not inp.isdigit():
			response = translate(inp)
			if type(response) != str:
				if response.get('sentences') is not None:
					print(response['sentences'][0]['trans'])
				else:
					print(f'Not a valid word {inp}')
			else:
				print(response)
