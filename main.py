import datetime
import js
import pyodide
import js.MaterialUI as mui
import js.React.createElement as e


def jsobj(**kwargs):
    return js.Object.fromEntries(pyodide.to_js(kwargs))


@mui.makeStyles
def use_styles(theme):
    return jsobj(
        root=jsobj(margin=theme.spacing(6, 0, 3)),
        light_bulb=jsobj(verticalAlign="middle", marginRight=theme.spacing(1)),
    )


theme = mui.createTheme(
    jsobj(
        palette=jsobj(
            primary=jsobj(main="#556cd6"),
            secondary=jsobj(main="#19857b"),
            error=jsobj(main="#FF1744"),
            background=jsobj(default="#fff"),
        )
    )
)


def LightBulbIcon(props, children):
    return e(
        mui.SvgIcon,
        props,
        e(
            "path",
            jsobj(
                d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6C7.8 12.16 7 10.63 7 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.63-.8 3.16-2.15 4.1z"
            ),
        ),
    )


def ProTip(props, children):
    classes = use_styles()
    return e(
        mui.Typography,
        jsobj(className=classes.root, color="textSecondary"),
        e(LightBulbIcon, jsobj(className=classes.light_bulb)),
        "Pro tip: See more ",
        e(
            mui.Link,
            jsobj(href="https://material-ui.com/getting-started/templates/"),
            "templates",
        ),
        " on the Material-UI documentation.",
    )


def Copyright(props, children):
    return e(
        mui.Typography,
        jsobj(variant="body2", color="textSecondary", align="center"),
        "Copyright © ",
        e(
            mui.Link,
            jsobj(href="https://material-ui.com/", color="inherit"),
            "Your Website",
        ),
        f" {datetime.datetime.now().year}.",
    )


def App(props, children):
    return e(
        mui.Container,
        jsobj(maxWidth="sm"),
        e(
            "div",
            jsobj(style=jsobj(marginTop=24)),
            e(
                mui.Typography,
                jsobj(variant="h4", component="h1", gutterBottom=True),
                "CDN v4-beta example",
            ),
            e(ProTip),
            e(Copyright),
        ),
    )


# Create a div to contain our component and render our App
dom_container = js.document.createElement("div")
js.document.body.appendChild(dom_container)
js.ReactDOM.render(
    e(
        mui.ThemeProvider,
        jsobj(theme=theme),
        e(mui.CssBaseline),
        e(App),
    ),
    dom_container,
)
