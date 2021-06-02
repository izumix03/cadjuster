from application import manager
from flask_script import Server
import www

# web server
manager.add_command("runserver", Server(host="0.0.0.0", use_debugger=True, use_reloader=True))


def main():
    manager.run()


if __name__ == "__main__":
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        print(e)
        import traceback

        traceback.print_exc()
