#   Copyright 2021 Modelyst LLC
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import warnings
from typing import TYPE_CHECKING, Dict, Generator, List, Optional

from neo4j.exceptions import ServiceUnavailable
from pydantic import AnyUrl

from neo4j import ExperimentalWarning, GraphDatabase
from neo4j.data import Record


class Neo4jDsn(AnyUrl):
    allowed_schemes = {'neo4j', 'bolt'}
    user_required = True
    path: str

    @classmethod
    def validate_parts(cls, parts: Dict[str, str]):
        defaults = {
            'port': '7687',
            'path': '/neo4j',
        }
        for key, value in defaults.items():
            if not parts[key]:
                parts[key] = value
        return super().validate_parts(parts)  # type: ignore

    def get_uri(self) -> str:
        return f'{self.scheme}://{self.host}:{self.port}{self.path}'

# Filter out the warning from neo4j
warnings.filterwarnings("ignore", category=ExperimentalWarning)


class GraphDriver:
    def __init__(self, dsn: 'Neo4jDsn', password: Optional[str] = None) -> None:
        self.driver = GraphDatabase.driver(dsn.get_uri(), auth=(dsn.user, password or dsn.password))

    def execute(self, command: str) -> Generator[Record, None, None]:
        with self.driver.session() as session:
            yield from session.run(command)

    def fetch_all(self, command: str) -> List[Record]:
        return [row for row in self.execute(command)]

    def verify_connectivity(self):
        warnings.filterwarnings("ignore", category=ExperimentalWarning)
        try:
            return self.driver.verify_connectivity()
        except ServiceUnavailable:
            return False
