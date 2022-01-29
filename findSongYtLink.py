from Song import Song
from typing import List
import requests
import asyncio
from bs4 import BeautifulSoup

SEARCH_DOMAIN = 'https://www.google.com/search'
HEADERS = {
        'authority': 'www.google.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'x-client-data': 'CJa2yQEIo7bJAQjBtskBCKmdygEIqYXLAQjQmssBCIyeywEI7/LLAQiz+MsBCJ75ywEI8vnLAQiw+ssBCL/+ywEIn//LAQjj/8sBCPn/ywE=',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9,da;q=0.8,fr;q=0.7',
        'cookie': 'CGIC=EhQxQzFHQ0VVX2VuQUU4OTNBRTg5MyKHAXRleHQvaHRtbCxhcHBsaWNhdGlvbi94aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3E9MC45LGltYWdlL2F2aWYsaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCxhcHBsaWNhdGlvbi9zaWduZWQtZXhjaGFuZ2U7dj1iMztxPTAuOQ; HSID=AxLmG7w2pf7dWt8Xs; SSID=ARH-uUrSs1p0vedpb; APISID=pSTzqGAwHYIdm6q7/Aj_-mS7fkp-y-mX_0; SAPISID=20j8506QWv7CieZL/AcrSiZbTuGPoKvmTP; __Secure-3PAPISID=20j8506QWv7CieZL/AcrSiZbTuGPoKvmTP; __Secure-1PAPISID=20j8506QWv7CieZL/AcrSiZbTuGPoKvmTP; OTZ=6100354_40_40__40_; SEARCH_SAMESITE=CgQIqpMB; SID=BQjb4jFynSJ3oOI9kJCYjLVMxkvSDFxfQr2UzFzPSlMjT42a6QmbyLzOOsfM964zq8F68Q.; __Secure-1PSID=BQjb4jFynSJ3oOI9kJCYjLVMxkvSDFxfQr2UzFzPSlMjT42aFhZOLEEYNiQ5PdYekxhqkg.; __Secure-3PSID=BQjb4jFynSJ3oOI9kJCYjLVMxkvSDFxfQr2UzFzPSlMjT42akDw7TTY1pJ42bVAHgWv2Qg.; 1P_JAR=2021-09-03-15; NID=222=OEuXdZHSfWqeZJBS3I8ndDVQBKw9XQJH371_onGeFHQHETHyvcXEYySYEea4--vneBBqWryAL91eRD3-28SbQPhJ6JFYplN8VNxzdD_C1dP5Mk9p_ExmfcNTs8vNmvLI3RdeoZEjNEaRbjt2JwR9v_rWqipwA7-w-L9UDpgT7MCvCnJtcqs_W_7fZ7AZKnPF8c3DN96wINIj5xG-RZGxzIfK3Z2D8SPO7Mt08JcLl_JYN-h7RHo80a7q0Ct3jg; SIDCC=AJi4QfHccdmVoILhNVUvwWDH3I_D2w0QFGcdz2LG3MFMJD5EZ5bJS4sO4HYpb_U7mSIFuEwHIl8; __Secure-3PSIDCC=AJi4QfEUdHuNEZHmmhw7s-A71qXu0L84Em1n30AsmpnwCe9Ft7I2QB81W1520MFWirvatdKqLLM',
    }
LINK_DOMAIN = 'https://www.youtube.com/watch?v='


# def get_links_for(songs: List[Song]) -> List[str]:
#
#     return [get_link_for(song) for song in songs]


def get_link_for(song: Song) -> str:
    response = requests.get(SEARCH_DOMAIN, headers=HEADERS, params=song.params)
    page = BeautifulSoup(response.content, 'html.parser')
    for tag in page.find_all('a'):
        if LINK_DOMAIN not in str(tag.get('href')):
            continue
        return tag.get('href')


async def get_links_for(songs: List[Song]):

    import httpx

    tasks = []
    async with httpx.AsyncClient() as client:
        for song in songs:
            tasks.append(client.get(SEARCH_DOMAIN, headers=HEADERS, params=song.params))
        reqs = await asyncio.gather(*tasks)

    links = []
    for req in reqs:
        page = BeautifulSoup(req.content, 'html.parser')
        for tag in page.find_all('a'):
            link = tag.get('href')
            if link is None or LINK_DOMAIN not in link:
                continue
            links.append(link)
            break
    return links


def main():
    song = Song(name='kill the lights', artist='set it off')
    songs = [song]
    # get_link_for('kill the lights', 'set it off')
    links = asyncio.run(get_links_for(songs))
    print(links)


if __name__ == '__main__':
    main()
