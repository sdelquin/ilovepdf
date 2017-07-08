import jwt
import requests

API_ENTRY_POINT = "https://api.ilovepdf.com/v1/start"


class ILovePdf:
    def __init__(self, public_key, secret_key):
        """
        You must register in order to get the keys.
        public_key: It can be obtained from
                    https://developer.ilovepdf.com/user/projects
                    You can see it as "project key" or "jti claim"
        secret_key: It can be obtained from
                    https://developer.ilovepdf.com/user/projects
        """
        self.public_key = public_key
        self.secret_key = secret_key
        signed_public_key = jwt.encode(
            {"jti": self.public_key},
            self.secret_key,
            algorithm="HS256"
        ).decode("utf-8")
        self.headers = {"Authorization": f"Bearer {signed_public_key}"}

    def new_task(self, task):
        self.task = task
        url = f"{API_ENTRY_POINT}/{task}"
        response = requests.get(url, headers=self.headers).json()
        self.server = response["server"]
        self.task_id = response["task"]
        self.base_api_url = f"https://{self.server}/v1"

    def add_file(self, filename):
        self.filename = filename
        url = self.base_api_url + "/upload"
        params = {"task": self.task_id}
        files = {"file": open(filename, "rb")}
        response = requests.post(
            url,
            params,
            files=files,
            headers=self.headers
        ).json()
        self.server_filename = response["server_filename"]

    def execute(self):
        url = self.base_api_url + "/process"
        params = {
            "task": self.task_id,
            "tool": self.task,
            "files": [
                {
                    "server_filename": self.server_filename,
                    "filename": self.filename
                }
            ]
        }
        response = requests.post(url, json=params, headers=self.headers).json()
        self.filesize = response["filesize"]
        self.output_filesize = response["output_filesize"]
        self.timer = response["timer"]

    def download(self, output_filename=None):
        url = self.base_api_url + f"/download/{self.task_id}"
        response = requests.get(url, headers=self.headers)
        output_filename = output_filename or self.filename
        with open(output_filename, "wb") as output_file:
            output_file.write(response.content)