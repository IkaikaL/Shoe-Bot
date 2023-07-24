from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://accounts.nike.com/lookup?client_id=4fd2d5e7db76e0f85a6bb56721bd51df&redirect_uri=https://www.nike.com/auth/login&response_type=code&scope=openid%20nike.digital%20profile%20email%20phone%20flow%20country&state=ec96272da9a648369b93e750cfb6f777&code_challenge=_-8NHZ6miQfpSXPYvV-_52s58eg6ioS8l70E4gqN-_Q&code_challenge_method=S256",
    ]

    def parse(self, response):
        for quote in response.css("div.css-vxgrp0"):
            yield {
                "buttonFill": quote.css("div.nds-input-layout-control::text").get(),
            }