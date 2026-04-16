# Setup

![opencode](https://opencode.ai/social-share.png)

## 1. Open OpenCode in VS Code

Type [Ctrl+Shift+P] (Windows/Linux) or [Cmd+Shift+P] (Mac) to open the command palette and type `OpenCode`. Then, select "Open opencode".


![](./vscode.png)

This will open a new VS Code window with OpenCode installed.


> [!WARNING]
> Sometimes opencode closes in the first launch. If this happens, type "🔼" keybotton and rerun the command again.

If you cannot see the "OpenCode: Open" command, install the OpenCode extension. Click the icon on the left sidebar (it looks like four squares with the top right square off). Search for "OpenCode" and install the extension. Then try the above command again.

## 2. Connect OpenCode to your provider

In the opencode terminal, type:

```
/connect
```

Select your provider (**Ollama Cloud** or **OpenRouter**) and paste your API key.
Switch models anytime with `/model`.

> [!NOTE]
> There are many models available on Ollama and OpenRouter. A recommended model is qwen 3.5 models. For ollama, you can choose qwen 3.5:397b-cloud model. For openrouter, you can additionally choose more cost-effective models like the qwen 35B model. The GLM from Zhipu AI is also a good choice (like glm-4.7, glm-5). That said, you can choose any model you like.

## 3. Install dependencies

Run the setup skill:

```
/setup
```

See [.agents/skills/setup/SKILL.md](../.agents/skills/setup/SKILL.md) for what this does.
