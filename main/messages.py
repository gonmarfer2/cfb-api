from django.conf import settings

def github_messages(type,data):
    webhook = None
    msg = "Si ves esto, hubo un error"
    if type == "gollum":
        msg = build_gollum_msg(data)
        title = data["pages"][0]["title"].lower()
        if "registro" in title:
            if "1" in title:
                webhook = settings.WEBHOOK_WIKI_GRUPO1
            if "2" in title:
                webhook = settings.WEBHOOK_WIKI_GRUPO2
            if "3" in title:
                webhook = settings.WEBHOOK_WIKI_GRUPO3
    return webhook, msg


def build_gollum_msg(data):
    msg = {
        "embeds":[{
            "author":{
                "name":data["sender"]["login"],
                "icon_url":data["sender"]["avatar_url"]
            },
            "title":":rotating_light: Registro actualizado :rotating_light:"
        }]
    }
    return msg