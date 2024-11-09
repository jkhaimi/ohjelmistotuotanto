import toml
from urllib import request
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # Haetaan tiedoston sisältö merkkijonona
        content = request.urlopen(self._url).read().decode("utf-8")
        print("TOML Content:\n", content)  

        # Deserialisoidaan TOML-data sanakirjaksi
        data = toml.loads(content)
        print("Parsed Data:\n", data)

        poetry_data = data.get("tool", {}).get("poetry", {})
        name = poetry_data.get("name", "Unknown Name")
        description = poetry_data.get("description", "No description")
        license = poetry_data.get("license")
        authors = poetry_data.get("authors", [])

        dependencies = list(poetry_data.get("dependencies", {}).keys())
        dev_dependencies = list(poetry_data.get("group", {}).get("dev", {}).get("dependencies", {}).keys())

        return Project(name, description, dependencies, dev_dependencies, license, authors)
