# Web Fundamentals

A beginner path to the [Tesla practice page](../tesla-web-poc/README.md). Work through HTML, CSS, Tailwind, then JavaScript. Each subject has 10 lessons and two activities: one after lesson 5 and one after lesson 10. Open any lesson `index.html` or activity `task/index.html` directly in a browser. Tailwind examples need an internet connection for the CDN.

For each lesson: read its README, open `index.html`, change one thing, and refresh. Then complete the activity after lesson 5 or 10. Give students the `task` folder; use the `solution` folder to explain one completed implementation. The Tesla project is a reference.

## Formatting for maintainers

Open this folder in VS Code and install the recommended Prettier extension to format HTML, CSS, and JavaScript when saving. For the whole curriculum, install the formatter with `npm install`, then run `npm run format`. Use `npm run format:check` to check formatting without changing files. Students can open the lesson and activity pages without installing npm packages.

## HTML

01. [Page Skeleton](html/lessons/01-page-skeleton/README.md)
02. [Text And Headings](html/lessons/02-text-and-headings/README.md)
03. [Links And Navigation](html/lessons/03-links-and-navigation/README.md)
04. [Images And Alt Text](html/lessons/04-images-and-alt-text/README.md)
05. [Lists](html/lessons/05-lists/README.md)
06. [Semantic Landmarks](html/lessons/06-semantic-landmarks/README.md)
07. [Sections And Articles](html/lessons/07-sections-and-articles/README.md)
08. [Buttons And Basic Forms](html/lessons/08-buttons-and-basic-forms/README.md)
09. [Accessible Page Structure](html/lessons/09-accessible-page-structure/README.md)
10. [Tesla Page Outline](html/lessons/10-tesla-page-outline/README.md)

Activities: [01 Build a small Model 3 page](html/activities/01-build-a-model-page/README.md) · [02 Structure the Tesla page](html/activities/02-structure-the-tesla-page/README.md)

## CSS

01. [Selectors And Rules](css/lessons/01-selectors-and-rules/README.md)
02. [Colors And Typography](css/lessons/02-colors-and-typography/README.md)
03. [Box Model](css/lessons/03-box-model/README.md)
04. [Sizing And Spacing](css/lessons/04-sizing-and-spacing/README.md)
05. [Flexbox](css/lessons/05-flexbox/README.md)
06. [Positioning And Layers](css/lessons/06-positioning-and-layers/README.md)
07. [Grid Basics](css/lessons/07-grid-basics/README.md)
08. [Grid Page Sections](css/lessons/08-grid-page-sections/README.md)
09. [Responsive Design](css/lessons/09-responsive-design/README.md)
10. [Media Queries](css/lessons/10-media-queries/README.md)

Activities: [01 Style a Model 3 card](css/activities/01-style-a-model-card/README.md) · [02 Build a responsive layout](css/activities/02-build-a-responsive-layout/README.md)

## TAILWIND

01. [Utility Classes](tailwind/lessons/01-utility-classes/README.md)
02. [Typography And Color](tailwind/lessons/02-typography-and-color/README.md)
03. [Spacing And Sizing](tailwind/lessons/03-spacing-and-sizing/README.md)
04. [Flex Utilities](tailwind/lessons/04-flex-utilities/README.md)
05. [Grid Utilities](tailwind/lessons/05-grid-utilities/README.md)
06. [Backgrounds And Borders](tailwind/lessons/06-backgrounds-and-borders/README.md)
07. [Hover And Focus States](tailwind/lessons/07-hover-and-focus-states/README.md)
08. [Responsive Prefixes](tailwind/lessons/08-responsive-prefixes/README.md)
09. [Combining Utilities Into Sections](tailwind/lessons/09-combining-utilities-into-sections/README.md)
10. [Tesla Page Styling](tailwind/lessons/10-tesla-page-styling/README.md)

Activities: [01 Style a hero with Tailwind](tailwind/activities/01-style-a-hero/README.md) · [02 Style Tesla sections with Tailwind](tailwind/activities/02-style-tesla-sections/README.md)

## JS

01. [Values And Data Types](js/lessons/01-values-and-data-types/README.md)
02. [Variables And Operators](js/lessons/02-variables-and-operators/README.md)
03. [Conditions](js/lessons/03-conditions/README.md)
04. [Arrays And Objects](js/lessons/04-arrays-and-objects/README.md)
05. [Functions](js/lessons/05-functions/README.md)
06. [Scope And Closures](js/lessons/06-scope-and-closures/README.md)
07. [Dom Selection And Updates](js/lessons/07-dom-selection-and-updates/README.md)
08. [Events And Interactive Tabs](js/lessons/08-events-and-interactive-tabs/README.md)
09. [Es6 And Functional Array Methods](js/lessons/09-es6-and-functional-array-methods/README.md)
10. [Local Storage](js/lessons/10-local-storage/README.md)

Activities: [01 Build a model data summary](js/activities/01-model-data-summary/README.md) · [02 Build an interactive model picker](js/activities/02-interactive-model-picker/README.md)

## Final bridge exercise

Build a small Model 3 page in a new folder using the [Tesla reference](../tesla-web-poc/README.md):

1. Mark up a header, navigation, hero, features, charging, specs, and footer with semantic HTML.
2. Style the layout with CSS grid and spacing; use Tailwind utilities for the hero, buttons, and cards.
3. Store slide and feature data in JavaScript arrays or objects. Add click handlers that change the hero and feature panel.
4. Open the page in a browser. Check that links, images, and controls work. Resize it to see your responsive exercise in action.

The reference page is desktop-focused. Responsive rules and local storage are learning extensions; you do not need to add them to the reference project.
