import subprocess

from cpts.errors.isolate import EnvAlreadyExistsError, FailedToInitEnvError


class IsolateProxy:
    def __init__(self) -> None:
        self._box_path = self._init_isolate_env()

    def _init_isolate_env(self) -> str:
        try:
            result = subprocess.run(
                args=["isolate", "--init"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=2,
            )
        except subprocess.TimeoutExpired:
            raise FailedToInitEnvError(
                title="Failed to initialize isolated environment",
                description="Isolated environment creation timed out.",
            )

        if result.returncode:
            if b"already exists" in result.stderr:
                raise EnvAlreadyExistsError(
                    title="Failed to initialize isolated environment",
                    description="Isolated box already exists.",
                )
            else:
                raise FailedToInitEnvError(
                    "Failed to initialize isolated environment",
                    description=result.stderr.decode(),
                )

        return str(result.stdout.strip())


print(IsolateProxy()._box_path)
