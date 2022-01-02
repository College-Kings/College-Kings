python early:
    def get_git_sha(act):
        import requests

        auth_string = "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"

        headers = {"Authorization": "token {}".format(auth_string)}
        url = "https://api.github.com/repos/College-Kings/College-Kings/branches/{}".format("main" if act == "DEVELOPMENT" else "act-" + act)

        response = requests.get(
            "https://api.github.com/repos/College-Kings/College-Kings/branches/main",
            headers=headers,
        )
        return response.json()["commit"]["sha"]


    def get_version(version):
        major, minor, patch = map(lambda x: int(x), version.split("."))
        act_1 = 7
        if minor == 9:
            act = "DEVELOPMENT"
        else:
            act = max(-((major - act_1) // -3) + 1, 1)

        return "{} (Act: {}) (SHA: {})".format(version, act, get_git_sha(act))
