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

    elif type == "workflow_run" and data["action"] == "completed":
        msg = build_actions_msg(data)
        webhook = settings.WEBHOOK_ACTIONS
    
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

def build_actions_msg(data):
    msg_color = 1179392 if data["workflow_run"]["conclusion"] == "success" else 16711680
    msg_icon = ":white_check_mark:" if data["workflow_run"]["conclusion"] == "success" else ":x:"
    msg_result = "completado con éxito" if data["workflow_run"]["conclusion"] == "success" else "fallido"
    msg = {
        "embeds":[{
            "color":msg_color,
            "title":"{} Workflow {}".format(msg_icon,msg_result),
            "description":data["workflow_run"]["display_title"]
        }]
    }
    return msg

def build_codacy_msg(data):
    errors = data["commit"]["results"]["fixed_count"]
    plural_es = "" if errors == 1 else "es"
    new_errors = data["commit"]["results"]["new_count"]
    plural_s = "" if new_errors == 1 else "s"
    
    msg = {
        "method":"POST",
        "headers":{
            "content-type":"application/json"
        },
        "embeds":[{
            "color": 1179392 if new_errors == 0 else 16711680,
            "title":":salad: Nuevo análisis de Codacy",
            "description":"{} error{} — {} nuevo{}".format(errors,plural_es,new_errors,plural_s),
            "url":data["commit"]["data"]["urls"]["delta"]
        }]
    }
    return msg