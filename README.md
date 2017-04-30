NASA has a vast collection of space-related and historical images, videos, and audio clips. However, their website, as it stands currently, is completely unindexable by Google or other search engines. This is a serious problem, and needs to be fixed.

Before we can fix this, we have to figure out how (and why) it happened:

This has happened because of a number of factors coming together simultaneously:

 * NASA is always adding new media (and already has thousands), so a manually created static website is not an option.
 * To generate a dynamic webpage, an API call must be made to fetch the information from which the webpage is constructed—an API call is not without cost.
 * Making this information into a usable webpage requires processing, which incurs further cost.

Since a static website is not an option, and a server-side generated dynamic webpage is not feasible, offloading the generation of the webpages to the client was selected as the only viable method. However, as we now know, this prevents the page from being able to be indexed properly.

So, how is it possible to make a website for NASA's media library which can be indexed by search engines?

The solution to this would be to have a framework or template to dynamically generate semi-static "cached" pages, as new images are added, and then serve that pre-generated page to visitors until e.g., the template changes.

The codebase currently employed to generate the webpages is over 150,000 lines of obfuscated JavaScript code, so it is probably not worth attempting to salvage code for re-use.

