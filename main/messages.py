from django.conf import settings

class UnknownMessageError(Exception):
    "Iniciado cuando llega un mensaje de github no válido"
    pass

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
    elif type == "issues" and data["action"] == "closed":
        msg = build_closed_issue_msg(data)
        webhook = settings.WEBHOOK_ISSUES
    else:
        raise UnknownMessageError
    return webhook,msg

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

def build_closed_issue_msg(data):
    msg = {
        "embeds":[{
            "author":{
                "name":data["sender"]["login"],
                "icon_url":data["sender"]["avatar_url"]
            },
            "title":":no_entry_sign: La issue {} ha sido cerrada".format(data["issue"]["number"]),
            "description":data["issue"]["title"]
        }]
    }
    return msg