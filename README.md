# Bolt for Python steps template

This is a generic Bolt for Python template app used to build out Slack custom steps.

## Installation

### Create a Slack App

1. Open [https://api.slack.com/apps/new](https://api.slack.com/apps/new) and
   choose "From an app manifest"
2. Choose the workspace you want to install the application to
3. Copy the contents of [manifest.json](./manifest.json) into the text box that
   says `*Paste your manifest code here*` (within the JSON tab) and click _Next_
4. Review the configuration and click _Create_
5. Click _Install_ button and _Allow_ on the screen that follows. You'll then be
   redirected to the App Settings dashboard.

### Environment Variables

Before you can run the app, you'll need to store some environment variables.

1. Rename `.example.env` to `.env`
2. Open your apps setting page from this list, click **OAuth &
   Permissions** in the left hand menu, then copy the Bot User OAuth Token. You
   will store this in your environment as `SLACK_BOT_TOKEN`.
3. Click ***Basic Information** from the left hand menu and follow the steps in
   the App-Level Tokens section to create an app-level token with the
   `connections:write` scope. Copy this token. You will store this in your
   environment as `SLACK_APP_TOKEN`.
5. Populate the other environment variable value with proper values.

### Local Project

```zsh
# Clone this project onto your machine
git clone https://github.com/WilliamBergamin/bolt-python-step-template.git

# Change into this project directory
cd bolt-python-step-template

# Setup your python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the dependencies
pip3 install -r requirements.txt

# Start your local server
python3 app.py
```

#### Linting

```zsh
# Run ruff from root directory for linting
ruff check

# Run ruff from root directory for code formatting
ruff format
ruff check --fix
```

#### Testing

For an example of how to test a function, see
`tests/`.

Run all tests with:

```zsh
pytest tests/
```

#### Type checking

```zsh
mypy --config-file pyproject.toml
```

## Using Steps in Workflow Builder

With your server running, your function is now ready for use in
[Workflow Builder](https://api.slack.com/start#workflow-builder)! Add it as a
custom step in a new or existing workflow, then run the workflow while your app
is running.

For more information on creating workflows and adding custom steps, read more
[here](https://slack.com/help/articles/17542172840595-Create-a-new-workflow-in-Slack).
