import web

# local
import projects
import fm

urls = (
	'/p/', 'projects.UrlHandlerList',
	'/p/info/(.+)', 'projects.UrlHandler',
	'/fm/([\-\w]+)/?', 'fm.UrlHandler',
	'/fm/([\-\w]+)/([\-\w/\.]+)', 'fm.UrlHandler',
)

app = web.application(urls, globals())

if __name__ == "__main__":
	app.run()
