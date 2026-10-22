# Olivia Johnson — portfolio

A Jekyll site for GitHub Pages. You never run a build: edit a file, push (or
edit directly on GitHub), and the site updates in a minute or two. It uses only
plugins GitHub Pages supports (`jekyll-seo-tag`, `jekyll-sitemap`).

Anything still missing shows on the site as a dashed **[TODO: …]** marker, and
every one of them is listed at the bottom of this file.

## Preview it

**On GitHub (easiest):** push the repo, then go to **Settings → Pages** and pick
**Deploy from a branch → `main` → `/ (root)`**. The `CNAME` file points the site
at `oliviajohnson.com`; leave it in place, and set the domain's DNS as GitHub's
custom-domain docs describe.

**On your computer (optional, needs Ruby):**

```sh
bundle install
bundle exec jekyll serve      # open http://localhost:4000
```

Restart `jekyll serve` after editing `_config.yml`; other files reload by themselves.

## How the site is organized

| What | Where |
| --- | --- |
| Name, descriptor, footer line, email, LinkedIn, nav | `_config.yml` |
| The four homepage tiles (title, subtitle, image, link) | `areas:` in `_config.yml` |
| Homepage headline, subline, optional hero clip | `index.md` |
| Projects (one file each) | `_projects/` |
| Area pages (Film, Writing, Audio, Research) | `film.md`, `writing.md`, `audio.md`, `research.md`, which list their projects automatically |
| About / Contact | `about.md` / `contact.md` |
| Colors and fonts | top of `assets/css/main.css` |

## Add a project

1. Copy an existing file in `_projects/`, e.g. `caddisfly.md` → `my-new-film.md`.
   The file name becomes the address: `/work/my-new-film/`.
2. Edit the settings between the `---` lines:
   - `category:` `film`, `writing`, `audio`, or `research`. This decides which area page lists it.
   - `order:` its position within that area (1 = first).
   - `description:` one or two sentences.
   - `opening:` the large image at the top. Add a `youtube_id` or a `vimeo_id` to make it a click-to-play video; the image becomes its poster. Add `zoom: true` to let visitors open the image full size (good for maps and charts).
   - `facts:` rows like My role, Collaborators, Year. Add, rename, or delete rows freely.
   - `link:` the one call to action (`label` + `url`), e.g. "Listen on Spotify".
   - Optional sections: `visuals` (images), `highlights` (excerpts, findings, or a festival list with `highlights_style: list`), `sources`, `framework`.
3. Write the text below the second `---`. Each `## Heading` becomes its own
   section, with the heading as the small label on the left. Without headings,
   the text goes in one section labeled by `idea_heading` (default "The idea").
4. **Framework (optional):** a numbered row of columns, e.g. the Key themes on
   the research page. Define the columns under `framework:` in the settings, and
   add a `## Heading` with the same name as `framework.heading` where you want it
   to appear in the text.

Every project uses the same template (`_layouts/project.html`). Sections you
leave out simply don't appear.

**Video IDs:**
- YouTube: the part after `v=`, e.g. `youtube.com/watch?v=`**`abc123XYZ`** → `youtube_id: "abc123XYZ"`
- Vimeo: the number, e.g. `vimeo.com/`**`512817928`** → `vimeo_id: "512817928"`. For an
  unlisted video, the private link looks like `vimeo.com/512817928/`**`a1b2c3`**; put that last part in `vimeo_hash`.

Nothing loads from YouTube or Vimeo until someone presses play.

## Swap an image

All images here are placeholders. Use only files you own or have licensed.

- **Easiest:** upload your image with the **same name and folder** as the
  placeholder it replaces (each placeholder shows its own path).
- **Or:** add a new file and change the path in the Markdown/YAML.
- **Always** update the matching `alt:` text with a short description of the image.
- Any size is fine. When you push, a GitHub Action
  (`.github/workflows/optimize-images.yml`) shrinks images in `assets/images/`
  to at most 1920px wide, compresses them, strips camera metadata (including
  GPS location), and commits the result. File names stay the same. Use JPG or WebP for photos.

Images are cropped to fit these shapes. On a homepage tile, add `image_position:` (e.g. `15% center`) in `_config.yml` to choose which part stays in frame.

Shapes used: homepage tiles 5:4, project openings 16:9, visuals 3:2 (a lone
first image in an odd-numbered set shows wide, 21:9), About portrait 4:5.

| Image | File |
| --- | --- |
| Homepage tiles | `assets/images/home/film.jpg`, `writing.jpg`, `audio.jpg`, `research.jpg` |
| Project opening images | `assets/images/projects/<project>/opening.jpg` |
| Project visuals | `assets/images/projects/<project>/still-1.jpg`, `still-2.jpg`, … |
| About portrait | `assets/images/about/portrait.jpg` |

## Optional hero clip

Off by default. To turn it on, add a short, silent MP4 (10–20 s, 1080p, under
about 8 MB) at `assets/video/hero.mp4`, then set `hero_video:` and
`hero_poster:` in `index.md`. It loops muted with visible playback controls,
shows the poster until it loads, and doesn't autoplay for visitors who've
turned on "reduce motion".

## Every [TODO]

Search the repo for `[TODO` to jump to each one. Empty `url: ""` fields also
show as `[TODO]` markers on the site until filled.

**`_config.yml`**
- Images and `image_alt` for the Writing, Audio, and Research tiles

**`index.md`**
- `hero_poster_alt`: only needed if you turn on the hero clip

**`_projects/caddisfly.md`**
- Collaborators and year
- Waterbear link: the button currently plays the trailer; swap it in once the new deal is signed (instructions are in the file)
- Three stills, with alt text

**`_projects/jackson-wild-fellowship.md`**
- Two stills, with alt text
- YouTube ID for the National Park Service short (optional)

**`_projects/empty-nest.md`**
- Collaborators and year
- Two stills, with alt text
- Optional: a few sentences about the film below the second `---`

**`_projects/the-breathing-room.md`**
- Opening image, with alt text

**`_projects/load-growth-policy.md`** (Yale research)
- Optional: a link (`link:` with `label` and `url`) if you publish the paper or a summary

**`_projects/ground-truth.md`**
- Collaborators
- Opening image or cover art, with alt text

**Images:** any image still showing "PLACEHOLDER IMAGE" needs replacing (see "Swap an image").

## Credits

- Fonts: Instrument Serif and Inter (Google Fonts)
- Video: [lite-youtube-embed](https://github.com/paulirish/lite-youtube-embed) (MIT), vendored in `assets/vendor/`
