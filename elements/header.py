from os import getenv


header: dict[str, object] = {
    "title": "VERISTAMP",
    "subtitle": "Get Stamping",
    "imageUrl": f"{getenv('BASE_URL')}/static/img/logo.png",
    "imageType": "CIRCLE"
}
