"""Generate the small, self-contained classroom exercises in this repository."""

from pathlib import Path
from html import escape
import shutil

ROOT = Path(__file__).resolve().parent.parent

# slug, learning point, runnable demonstration, two activity names and tasks
COURSE = {
    "html": [
        ("PAGE-SKELETON", "A page starts with a doctype, html, head, and body.", '<h1>Model 3</h1><p>A small practice page.</p>', ("BUILD-A-PAGE", "Create a page with a title, one heading, and one paragraph."), ("ADD-METADATA", "Add a language, character set, viewport, and descriptive page title.")),
        ("TEXT-AND-HEADINGS", "Headings describe the outline; paragraphs hold ordinary text.", '<h1>Model 3</h1><h2>Meet Model 3</h2><p>Explore the electric sedan.</p>', ("WRITE-A-HERO", "Write a hero heading and a short supporting paragraph."), ("STRUCTURE-HEADINGS", "Add two sections with h2 headings under one h1.")),
        ("LINKS-AND-NAVIGATION", "An anchor href can lead to a page or a section id.", '<nav aria-label="Main navigation"><a href="#features">Features</a> · <a href="#specs">Specs</a></nav><main><section id="features"><h1>Features</h1></section><section id="specs"><h2>Specs</h2></section></main>', ("LINK-SECTIONS", "Add links that jump to two sections by id."), ("BUILD-A-NAV", "Place three working section links inside a nav element.")),
        ("IMAGES-AND-ALT-TEXT", "An image needs a source and useful alternative text.", '<h1>Model 3</h1><img width="480" src="../../../../tesla-web-poc/assets/images/hero-premium.avif" alt="Silver Model 3 driving on a road">', ("ADD-A-CAR-IMAGE", "Show a local image from the Tesla project with a useful alt attribute."), ("IMPROVE-ALT-TEXT", "Write image descriptions that explain the image without repeating nearby text.")),
        ("LISTS", "Use ul for unordered items and ol for a sequence.", '<h1>Features</h1><ul><li>Electric drive</li><li>Room for five</li></ul><h2>Build steps</h2><ol><li>Write HTML</li><li>Add styles</li></ol>', ("MAKE-A-FEATURE-LIST", "Add a three-item unordered list of car features."), ("MAKE-A-SPECS-LIST", "Represent three specs as a labeled list using dl, dt, and dd.")),
        ("SEMANTIC-LANDMARKS", "Header, nav, main, and footer name the major page regions.", '<header><nav aria-label="Main navigation"><a href="#main">Skip to content</a></nav></header><main id="main"><h1>Model 3</h1></main><footer>Classroom project</footer>', ("ADD-PAGE-LANDMARKS", "Wrap a simple page in header, main, and footer."), ("LABEL-NAVIGATION", "Give a navigation region a clear accessible label.")),
        ("SECTIONS-AND-ARTICLES", "Sections group themed content; articles stand on their own.", '<main><h1>Model 3</h1><section aria-labelledby="features"><h2 id="features">Features</h2><article><h3>Comfort</h3><p>A quiet cabin.</p></article></section></main>', ("GROUP-FEATURES", "Create a features section containing two feature articles."), ("GROUP-SPECS", "Create a specs section with a heading and two labeled values.")),
        ("BUTTONS-AND-BASIC-FORMS", "Buttons perform actions; labeled form controls gather input.", '<h1>Choose a model</h1><form><label for="model">Model</label><select id="model"><option>Model 3</option><option>Model 3 Performance</option></select><button type="button">Preview</button></form>', ("ADD-ACTION-BUTTONS", "Add two buttons with meaningful text and explicit types."), ("MAKE-A-CHOICE-FORM", "Add a labeled model select and a submit button.")),
        ("ACCESSIBLE-PAGE-STRUCTURE", "Clear headings, labels, and alt text help everyone use the page.", '<a href="#main">Skip to content</a><header><nav aria-label="Main navigation"><a href="#specs">Specs</a></nav></header><main id="main"><h1>Model 3</h1><section id="specs"><h2>Specs</h2><p>Range: 321 miles</p></section></main>', ("CHECK-HEADING-ORDER", "Use one h1 and nested h2 headings without skipping levels."), ("IMPROVE-LABELS", "Give a navigation region, button, and image descriptive labels.")),
        ("TESLA-PAGE-OUTLINE", "Put the semantic building blocks together before styling.", '<header><nav aria-label="Main navigation"><a href="#meet">Meet</a> <a href="#specs">Specs</a></nav></header><main><section id="hero"><h1>Model 3</h1></section><section id="meet"><h2>Meet Model 3</h2></section><section id="specs"><h2>Specs</h2></section></main><footer>Classroom recreation</footer>', ("OUTLINE-TESLA-SECTIONS", "Create hero, meet, features, charging, and specs sections."), ("ASSEMBLE-SEMANTIC-MARKUP", "Add a header, main, sections, image, buttons, and footer.")),
    ],
    "css": [
        ("SELECTORS-AND-RULES", "Start with style attributes on elements; later lessons move shared rules into CSS selectors.", "h1 { color: #171a20; } .note { color: #555; }", ("TARGET-ELEMENTS", "Style every h1 with a selector."), ("ADD-CLASSES", "Give one paragraph a class and style only that paragraph.")),
        ("COLORS-AND-TYPOGRAPHY", "Color, font size, weight, and line height establish hierarchy.", "body { color: #171a20; font-family: Arial, sans-serif; } h1 { font-size: 48px; } p { line-height: 26px; color: #555; }", ("STYLE-HEADINGS", "Make the heading larger and bolder than the paragraph."), ("SET-A-COLOR-PALETTE", "Use one dark text color, one muted color, and one accent color.")),
        ("BOX-MODEL", "Content, padding, border, and margin form an element's box.", ".card { padding: 24px; border: 1px solid #ddd; border-radius: 8px; margin: 16px 0; }", ("BUILD-A-CARD", "Add padding, border, and rounded corners to a card."), ("INSPECT-BOX-SPACING", "Change padding and margin separately; note which moves content and which moves the card.")),
        ("SIZING-AND-SPACING", "Max-width and relative units keep content comfortable to read.", ".card { max-width: 512px; width: 90%; margin: 32px auto; padding: 16px; } img { max-width: 100%; }", ("SET-WIDTHS", "Limit a content card's width while keeping it fluid."), ("SPACE-SECTIONS", "Add consistent padding between two sections.")),
        ("FLEXBOX", "Flexbox aligns items along one main axis.", ".row { display: flex; align-items: center; justify-content: space-between; gap: 16px; }", ("ALIGN-NAVIGATION", "Use flex to spread a logo and links across a row."), ("ALIGN-BUTTONS", "Place two buttons side by side with a gap.")),
        ("POSITIONING-AND-LAYERS", "Relative and absolute positioning can layer text over a hero.", ".hero { position: relative; min-height: 256px; background: #555; color: white; } .hero::before { content: ''; position: absolute; inset: 0; background: #0007; } .hero > * { position: relative; z-index: 1; }", ("PLACE-HERO-TEXT", "Position a heading over a hero background."), ("ADD-IMAGE-OVERLAY", "Add a translucent overlay so white hero text stays readable.")),
        ("GRID-BASICS", "Grid divides a container into rows and columns.", ".grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; }", ("CREATE-TWO-COLUMNS", "Put an image and text in two equal grid columns."), ("CREATE-A-SPECS-GRID", "Display three spec cards in three grid columns.")),
        ("GRID-PAGE-SECTIONS", "Grid can repeat page patterns with different column proportions.", ".grid { display: grid; grid-template-columns: 1.3fr 1fr; gap: 32px; align-items: center; }", ("BUILD-A-FEATURE-PANEL", "Create an image and text feature panel using grid."), ("BUILD-A-CHARGING-SECTION", "Create a charging description beside two stat cards.")),
        ("RESPONSIVE-DESIGN", "Flexible widths and images adapt before a breakpoint is needed.", ".card { width: min(90%, 960px); margin-inline: auto; } img { display: block; max-width: 100%; height: auto; }", ("MAKE-IMAGES-FLEXIBLE", "Keep an image inside its container at narrow widths."), ("STACK-COLUMNS", "Make a two-column layout become one column on small screens.")),
        ("MEDIA-QUERIES", "A media query applies rules only when its condition matches.", ".grid { display: grid; grid-template-columns: 1fr; gap: 16px; } @media (min-width: 700px) { .grid { grid-template-columns: 1fr 1fr; } }", ("CHANGE-LAYOUT-AT-A-BREAKPOINT", "Use a media query to switch from one to two columns."), ("ADJUST-MOBILE-SPACING", "Reduce heading size and page padding on narrow screens.")),
    ],
    "tailwind": [
        ("UTILITY-CLASSES", "A utility class applies one small style directly in HTML.", '<h1 class="text-4xl font-bold">Model 3</h1><button class="rounded bg-blue-600 px-5 py-2 text-white">Explore</button>', ("STYLE-A-HEADING", "Style a heading with size and weight utilities."), ("STYLE-A-BUTTON", "Style a button with color, padding, and radius utilities.")),
        ("TYPOGRAPHY-AND-COLOR", "Combine text size, weight, and color utilities for hierarchy.", '<h1 class="text-4xl font-semibold text-slate-900">Model 3</h1><p class="text-lg text-slate-600">Electric sedan</p>', ("MATCH-A-TEXT-PALETTE", "Choose dark heading text and one accent color."), ("STYLE-MUTED-COPY", "Make supporting copy less prominent than the heading.")),
        ("SPACING-AND-SIZING", "Padding, margin, width, and max-width utilities shape sections.", '<section class="mx-auto max-w-3xl px-5 py-16"><h1 class="text-4xl">Model 3</h1><p class="mt-4">Meet the car.</p></section>', ("SPACE-A-HERO", "Add generous hero padding and a gap below its heading."), ("SIZE-A-CARD", "Set a card max-width and internal padding.")),
        ("FLEX-UTILITIES", "Flex utilities align items and distribute space.", '<nav class="flex items-center justify-between gap-4 p-4"><strong>TESLA</strong><a href="#features">Features</a><a href="#specs">Specs</a></nav>', ("ALIGN-NAV-ITEMS", "Spread a logo and links across a row."), ("ALIGN-ACTIONS", "Place two action buttons in a row with a gap.")),
        ("GRID-UTILITIES", "Grid utilities define columns and gaps.", '<div class="grid grid-cols-2 gap-4"><div class="rounded bg-slate-100 p-5">Image area</div><div class="rounded bg-slate-100 p-5">Feature copy</div></div>', ("BUILD-TWO-COLUMNS", "Place image and copy in two columns."), ("BUILD-STAT-CARDS", "Place three stat cards in a grid.")),
        ("BACKGROUNDS-AND-BORDERS", "Background and border utilities distinguish sections.", '<section class="rounded-lg border border-slate-200 bg-slate-50 p-6"><h1 class="text-2xl">Feature</h1></section>', ("STYLE-A-FEATURE-CARD", "Add a light background, border, and rounded corners."), ("STYLE-A-DARK-SECTION", "Create a dark section with readable light text.")),
        ("HOVER-AND-FOCUS-STATES", "State prefixes style interactions and keyboard focus.", '<button class="rounded bg-blue-600 px-5 py-2 text-white hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2">Explore</button>', ("ADD-BUTTON-STATES", "Make a button visibly change on hover."), ("ADD-FOCUS-STATES", "Add a visible keyboard focus outline to a link or button.")),
        ("RESPONSIVE-PREFIXES", "Responsive prefixes activate utilities at a minimum width.", '<div class="grid grid-cols-1 gap-4 md:grid-cols-2"><div class="bg-slate-100 p-5">Image</div><div class="bg-slate-100 p-5">Copy</div></div>', ("STACK-A-PANEL", "Use one column by default and two at md width."), ("RESIZE-HEADINGS", "Use a smaller mobile heading and a larger desktop heading.")),
        ("COMBINING-UTILITIES-INTO-SECTIONS", "Build a coherent section from small utility classes.", '<section class="mx-auto max-w-4xl px-5 py-16 text-center"><h1 class="text-4xl font-semibold text-slate-900">Model 3</h1><p class="mt-4 text-slate-600">Electric sedan</p><a href="#features" class="mt-6 inline-block rounded bg-blue-600 px-6 py-3 text-white">Explore</a></section>', ("BUILD-A-HERO", "Combine layout, type, spacing, and button utilities in a hero."), ("BUILD-A-FEATURE-SECTION", "Combine a two-column panel with image and copy.")),
        ("TESLA-PAGE-STYLING", "Use the utilities from the earlier lessons on a small Tesla page.", '<nav class="flex justify-between bg-slate-900 p-4 text-white"><strong>TESLA</strong><a href="#specs">Specs</a></nav><main><section id="specs" class="bg-slate-100 px-5 py-16 text-center"><h1 class="text-4xl font-semibold">Model 3 Specs</h1><div class="mx-auto mt-6 grid max-w-xl grid-cols-2 gap-4"><p class="rounded bg-white p-4">321 mi</p><p class="rounded bg-white p-4">5 seats</p></div></section></main>', ("STYLE-TESLA-NAVIGATION", "Style a simple Tesla navigation row."), ("STYLE-A-SPECS-SECTION", "Style a heading and two spec cards.")),
    ],
    "js": [
        ("VALUES-AND-DATA-TYPES", "JavaScript values include strings, numbers, and booleans.", 'const model = "Model 3"; const range = 321; const available = true; output.textContent = `${model}: ${range} miles; available: ${available}`;', ("DISPLAY-CAR-VALUES", "Display a model name, range, and availability."), ("CHECK-VALUE-TYPES", "Use typeof to show the types of three values.")),
        ("VARIABLES-AND-OPERATORS", "const stores a fixed binding; operators calculate and combine values.", 'const range = 321; const extra = 25; output.textContent = `Estimated range: ${range + extra} miles`;', ("CALCULATE-A-VALUE", "Add two numbers and show the result."), ("BUILD-A-STRING", "Combine a model name and a range into a sentence.")),
        ("CONDITIONS", "An if statement chooses behavior from a condition.", 'const range = 321; if (range >= 300) { output.textContent = "Long range"; } else { output.textContent = "Standard range"; }', ("CHOOSE-A-LABEL", "Show a label based on a numeric range."), ("COMPARE-MODELS", "Compare two model ranges and display the larger one.")),
        ("ARRAYS-AND-OBJECTS", "Arrays hold ordered items; objects hold named properties.", 'const slides = [{ title: "Model 3" }, { title: "Performance" }]; output.textContent = slides[1].title;', ("STORE-SLIDES", "Create an array of three slide objects."), ("READ-MODEL-DETAILS", "Read a title and range from an object and show them.")),
        ("FUNCTIONS", "A function groups reusable steps and may return a value.", 'function formatRange(miles) { return `${miles} mi`; } output.textContent = formatRange(321);', ("FORMAT-A-SPEC", "Write a function that returns a formatted range."), ("CHANGE-A-SUMMARY", "Write a function that updates a model summary from inputs.")),
        ("SCOPE-AND-CLOSURES", "A closure remembers variables from its surrounding function.", 'function makeCounter() { let count = 0; return () => { count += 1; return count; }; } const next = makeCounter(); output.textContent = `${next()}, ${next()}`;', ("TRACE-SCOPE", "Identify which variables are inside and outside a function."), ("BUILD-A-SLIDE-COUNTER", "Create a closure that increments a slide number on each call.")),
        ("DOM-SELECTION-AND-UPDATES", "Select an element, then change its text or attributes.", 'const heading = document.querySelector("#title"); heading.textContent = "Model 3 Performance"; output.textContent = heading.textContent;', ("CHANGE-HERO-TEXT", "Select the hero heading and change its text."), ("CHANGE-AN-IMAGE", "Select an image and change its src and alt attributes.")),
        ("EVENTS-AND-INTERACTIVE-TABS", "An event listener responds when a user clicks a control.", 'document.querySelector("#action").addEventListener("click", () => { output.textContent = "Performance selected"; });', ("HANDLE-A-CLICK", "Make a button change text when clicked."), ("SWITCH-A-TAB", "Make two buttons switch the visible feature description.")),
        ("ES6-AND-FUNCTIONAL-ARRAY-METHODS", "Destructuring reads properties; map and filter transform arrays.", 'const models = [{ name: "Model 3", range: 321 }, { name: "Performance", range: 300 }]; const names = models.filter(({ range }) => range > 300).map(({ name }) => name); output.textContent = names.join(", ");', ("USE-DESTRUCTURING", "Read a model's name and range with destructuring."), ("MAP-AND-FILTER-MODELS", "Filter models by range, then map them to display names.")),
        ("LOCAL-STORAGE", "localStorage saves small strings across page refreshes.", 'const saved = localStorage.getItem("preferredModel") || "Model 3"; output.textContent = saved; document.querySelector("#action").addEventListener("click", () => { localStorage.setItem("preferredModel", "Performance"); output.textContent = "Performance"; });', ("SAVE-A-PREFERENCE", "Save a preferred model when a button is clicked."), ("RESTORE-A-PREFERENCE", "Read the saved preference and display it after refresh.")),
    ],
}

BASE_CSS = "body{font-size: 16px; line-height: 24px; font-family: Arial, sans-serif;color:#171a20;margin:32px}button,a{cursor:pointer}.card{background:#f4f4f4;padding:16px}"

def page(title, body, style="", script="", tailwind=False, stylesheet=""):
    cdn = '<script src="https://cdn.tailwindcss.com"></script>' if tailwind else ""
    css = f'<link rel="stylesheet" href="{stylesheet}">' if stylesheet else (f"<style>{BASE_CSS if not tailwind else ''}\n{style}</style>" if not tailwind else "")
    js = f"<script>{script}</script>" if script else ""
    return f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>{escape(title)}</title>\n{cdn}{css}\n</head>\n<body>\n{body}\n{js}\n</body>\n</html>\n'

def example(subject, title, demonstration, external_css=False):
    if subject == "html":
        return page(title, demonstration)
    if subject == "css":
        if title == "01-selectors-and-rules":
            return '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>01-selectors-and-rules</title>
  </head>
  <body style="font-size: 16px; line-height: 24px; font-family: Arial, sans-serif; color: #171a20; margin: 32px;">
    <header style="padding: 16px; background: #f4f4f4;">
      <strong>TESLA</strong>
      <nav><a href="#feature">Features</a> · <a href="#specs">Specs</a></nav>
    </header>
    <main>
      <section style="background: #f4f4f4; padding: 16px; margin-top: 16px;">
        <h1 style="color: #171a20;">Model 3</h1>
        <p style="color: #555;">Electric sedan</p>
      </section>
      <section id="feature" style="background: #f4f4f4; padding: 16px; margin-top: 16px;">
        <div>Feature image</div>
        <div>Feature copy</div>
      </section>
      <section id="specs" style="margin-top: 16px;">
        <div style="background: #f4f4f4; padding: 16px;">321 mi range</div>
        <div style="background: #f4f4f4; padding: 16px;">5 seats</div>
      </section>
    </main>
  </body>
</html>
'''
        body = '<header class="row"><strong>TESLA</strong><nav><a href="#feature">Features</a> · <a href="#specs">Specs</a></nav></header><main><section class="hero card"><h1>Model 3</h1><p class="note">Electric sedan</p></section><section id="feature" class="grid card"><div>Feature image</div><div>Feature copy</div></section><section id="specs" class="grid"><div class="card">321 mi range</div><div class="card">5 seats</div></section></main>'
        return page(title, body, demonstration, stylesheet="styles.css" if external_css else "")
    if subject == "tailwind":
        return page(title, demonstration, tailwind=True)
    body = '<main><h1 id="title">Model 3</h1><button id="action" type="button">Try it</button><p id="output" aria-live="polite"></p></main>'
    return page(title, body, script='const output = document.querySelector("#output");\n' + demonstration)

def starter(subject, title, task, external_css=False):
    marker = f"<!-- TODO: {escape(task)} -->"
    if subject == "html":
        return page(title, marker + '\n<main><h1>Model 3 practice</h1></main>')
    if subject == "css":
        return page(title, '<main><h1>Model 3</h1><p class="note">Electric sedan</p><div class="card">Feature card</div><div class="grid"><div>Range</div><div>Seats</div></div></main>', style=f"/* TODO: {task} */\n", stylesheet="styles.css" if external_css else "")
    if subject == "tailwind":
        return page(title, marker + '\n<main><h1>Model 3</h1><p>Electric sedan</p><button type="button">Explore</button><section><div>Image</div><div>Feature copy</div></section></main>', tailwind=True)
    body = '<main><h1 id="title">Model 3</h1><button id="action" type="button">Try it</button><p id="output" aria-live="polite">Your result appears here.</p></main>'
    return page(title, body, script=f'const output = document.querySelector("#output");\n// TODO: {task}\n')

def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

ACTIVITIES = {
    "html": [
        ("01-build-a-model-page", "Build a small Model 3 page", "Use a page skeleton, headings, navigation links, one image with alt text, and a feature list."),
        ("02-structure-the-tesla-page", "Structure the Tesla page", "Add semantic landmarks and labeled sections for hero, features, charging, and specs. Include a button and accessible labels."),
    ],
    "css": [
        ("01-style-a-model-card", "Style a Model 3 card", "Use selectors, typography, color, box model, spacing, and flexbox to style the starter card."),
        ("02-build-a-responsive-layout", "Build a responsive layout", "Use positioning, grid, flexible sizing, and a media query to create a hero and feature panel that work at narrow widths."),
    ],
    "tailwind": [
        ("01-style-a-hero", "Style a hero with Tailwind", "Use typography, color, spacing, sizing, and flex utilities to style the starter hero and buttons."),
        ("02-style-tesla-sections", "Style Tesla sections with Tailwind", "Use grid, backgrounds, borders, interaction states, and responsive prefixes to style feature and specs sections."),
    ],
    "js": [
        ("01-model-data-summary", "Build a model data summary", "Use values, variables, conditions, arrays, objects, functions, and scope to display a model summary."),
        ("02-interactive-model-picker", "Build an interactive model picker", "Use DOM selection, events, modern array methods, and localStorage to switch models and remember the selection."),
    ],
}

def clean_generated_activities(subject):
    parent = (ROOT / subject / "activities").resolve()
    if parent.parent != ROOT.resolve() / subject or parent.name != "activities":
        raise ValueError("Unexpected activity parent")
    for folder in parent.iterdir():
        if not folder.is_dir() or folder.resolve().parent != parent:
            raise ValueError(f"Unexpected activity entry: {folder}")
        files = {item.name for item in folder.iterdir()}
        expected = {"README.md", "starter.html"}
        if subject == "css" and folder.name == ACTIVITIES[subject][1][0]:
            expected.add("styles.css")
        if files != expected:
            raise ValueError(f"Activity has unexpected files; refusing removal: {folder}")
        shutil.rmtree(folder)

readme = ["# Web Fundamentals", "", "A beginner path to the [Tesla practice page](../tesla-web-poc/README.md). Work through HTML, CSS, Tailwind, then JavaScript. Each subject has 10 lessons and two activities: one after lesson 5 and one after lesson 10. Open any `example.html` or `starter.html` directly in a browser. Tailwind examples need an internet connection for the CDN.", "", "For each lesson: read its README, open `example.html`, change one thing, and refresh. Then complete the activity after lesson 5 or 10. Activity starters contain TODO prompts. The Tesla project is a reference, not an answer key.", ""]

for subject, lessons in COURSE.items():
    clean_generated_activities(subject)
    for number, (folder_name, title, task) in enumerate(ACTIVITIES[subject], 1):
        activity_dir = ROOT / subject / "activities" / folder_name
        external_css = subject == "css" and number == 2
        if external_css:
            write(activity_dir / "styles.css", BASE_CSS + "\n/* TODO: " + task + " */\n")
        write(activity_dir / "starter.html", starter(subject, title, task, external_css=external_css))
        lesson_range = "01–05" if number == 1 else "06–10"
        write(activity_dir / "README.md", f"# Activity {number:02d}: {title}\n\n**Use lessons {lesson_range}.** {task}\n\n1. Open `starter.html` in a browser.\n2. Edit its TODO and save. Refresh to check your work.\n3. Use the relevant lesson examples when you need a reminder.\n\n**Done when:** The page demonstrates all the listed skills and you can explain what you changed.\n")

    readme += [f"## {subject.upper()}", ""]
    for index, (slug, concept, demo, _first, _second) in enumerate(lessons, 1):
        lesson_name = f"{index:02d}-{slug.lower()}"
        lesson_dir = ROOT / subject / "lessons" / lesson_name
        activity_number = 1 if index <= 5 else 2
        activity_folder, activity_title, _ = ACTIVITIES[subject][activity_number - 1]
        activity_link = f"[{activity_number:02d} {activity_title}](../../activities/{activity_folder}/README.md)"
        if subject == "css" and index >= 6:
            write(lesson_dir / "styles.css", BASE_CSS + "\n" + demo + "\n")
        write(lesson_dir / "example.html", example(subject, lesson_name, demo, external_css=subject == "css" and index >= 6))
        write(lesson_dir / "README.md", f"# Lesson {index:02d}: {slug.replace('-', ' ').title()}\n\n**Learn:** {concept}\n\n1. Open [the example](example.html) in a browser.\n2. Find the code that demonstrates this idea; change one value and refresh.\n3. After lesson {'05' if index <= 5 else '10'}, complete activity {activity_link}.\n\n**Tesla connection:** Look for this idea in [`tesla-web-poc`](../../../../tesla-web-poc/README.md): its page structure, styles, Tailwind classes, or JavaScript controls.\n")
        readme.append(f"{index:02d}. [{slug.replace('-', ' ').title()}]({subject}/lessons/{lesson_name}/README.md)")
    readme += ["", f"Activities: [01 {ACTIVITIES[subject][0][1]}]({subject}/activities/{ACTIVITIES[subject][0][0]}/README.md) · [02 {ACTIVITIES[subject][1][1]}]({subject}/activities/{ACTIVITIES[subject][1][0]}/README.md)", ""]

readme += ["## Final bridge exercise", "", "Build a small Model 3 page in a new folder using the [Tesla reference](../tesla-web-poc/README.md):", "", "1. Mark up a header, navigation, hero, features, charging, specs, and footer with semantic HTML.", "2. Style the layout with CSS grid and spacing; use Tailwind utilities for the hero, buttons, and cards.", "3. Store slide and feature data in JavaScript arrays or objects. Add click handlers that change the hero and feature panel.", "4. Open the page in a browser. Check that links, images, and controls work. Resize it to see your responsive exercise in action.", "", "The reference page is desktop-focused. Responsive rules and local storage are learning extensions; you do not need to add them to the reference project.", ""]
write(ROOT / "README.md", "\n".join(readme))
print("Created 40 lessons and 8 activities.")
