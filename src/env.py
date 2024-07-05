from dotenv import load_dotenv


def load_by_environment(env: str, test_envs=None, prefix: str = "."):
    if test_envs is None:
        test_envs = []

    load_dotenv(f"{prefix}/.env.{env}.local")
    load_dotenv(f"{prefix}/.env.{env}")
    if env not in test_envs:
        load_dotenv(f"{prefix}/.env.local")

    load_dotenv(f"{prefix}/.env")

