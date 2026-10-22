---
layout: default
title: Work
permalink: /work/
---
<div class="wrap page">
  <header class="page__head">
    <h1 class="display">Work</h1>
  </header>
  {%- for c in site.categories %}
  {%- assign projects = site.projects | where: "category", c.key | sort: "order" %}
  <section class="work-group" aria-labelledby="group-{{ c.key }}">
    <div class="work-group__head">
      <h2 class="label" id="group-{{ c.key }}"><a href="{{ c.url | relative_url }}" style="text-decoration:none">{{ c.title }}</a></h2>
      <p class="meta" style="margin:0">{{ c.subtitle }}</p>
    </div>
    <ul class="project-list">
      {%- for p in projects %}{% include project-row.html project=p %}{% endfor %}
    </ul>
  </section>
  {%- endfor %}
</div>
