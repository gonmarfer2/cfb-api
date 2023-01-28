# Continuous Feedback API

- Small snippet API designed for a university porject.
- It allows a connection between Discord and Github/Codacy.

## How does it work

### Discord connection
Discord allows the creation of Webhooks for a server's channels. This API contains the URLs for different Discord webhooks hardcoded into the project's settings. Their purpose is shown below:
* Group 1 channel -> GitHub Wiki edition of Group 1's issue registry
* Group 2 channel -> GitHub Wiki edition of Group 2's issue registry
* Group 3 channel -> GitHub Wiki edition of Group 3's issue registry
* Closed issues channel -> Sends notifications when any issue is closed
* GitHub Actions channel -> Sends a message with the state of the current workflow runs
* Codacy channel -> Used for Codacy reports in a lightweight format (Codacy doesn't allow easy customisation of the webhook)

### GitHub and Codacy
This API exposes a URL that is inserted into a GitHub webhook that sends a JSON object whenever the selected events (as needed in the Discord channels section) occur. Similarly, a webhook is created in Codacy that sends JSON messages with new code analyses.

The API, when a webhook message is posted from GitHub or Codacy, processes the contents and either discards the petition or builds the Discord message and posts it to the adequate Discord channel.

## Extension

Unfortunately, this project was made so fast that it doesn't support extension. If you want to reuse this project for your own purpose, please follow these (more or less difficult) steps:

1. Fork the project
2. Go to your Discord channels and get the webhooks' URLs
3. Place those webhooks inside settings.py
4. If you don't want the same hooks, you'll need to code it. There are several examples inside views.py and messages.py. Sadly, there's no easy way here :sad:
5. Deploy your app somewhere (e.g. Railway)
6. Configure your GitHub repository/Codacy/etc. webhooks:
    * Usually, you'll need to create a webhook in those pages: insert your API URL and the type of request (e.g. application/json)
