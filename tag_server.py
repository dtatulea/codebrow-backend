import web

# local
import projects
import fm

urls = (
	'/p/', 'projects.handle_list',
	'/p/info/(.+)', 'projects.handle',
	'/fm/([\-\w]+)/?', 'fm.handle_root',
	'/fm/([\-\w]+)/([\-\w]+)', 'fm.handle',
)

app = web.application(urls, globals())

if __name__ == "__main__":
	app.run()
