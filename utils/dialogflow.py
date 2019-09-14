def response_message(message):
    return {'fulfillmentText': '%s' % message}

def response_quick_replies(title, suggests):
    return {
            "fulfillmentMessages": [
                {
                "quickReplies":
                    {
                        "title": title,
                            "quickReplies":
                                suggests
                    },
                "platform": "FACEBOOK",
                "type": 2
                },
                    {
                        "text":
                        {
                            "text":
                            [
                                "Response"
                            ]
                        }
                    }
                ]
            }