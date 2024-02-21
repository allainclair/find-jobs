from jinja2 import Environment, FileSystemLoader, select_autoescape

# WARNING: This loading is not async.
env = Environment(
	loader=FileSystemLoader("templates"),
	autoescape=select_autoescape(["html", "xml"]),
)
template = env.get_template("test.html.jinja")
