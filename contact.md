---
layout: default
title: Contact
permalink: /contact/
description: Get in touch with Olivia Johnson.
---
<div class="wrap page">
  <header class="page__head">
    <h1 class="display">Contact</h1>
  </header>
  <ul class="contact-list">
    <li><span class="label-sm">Email</span>{% include todo-link.html url=site.author.email mailto=true label=site.author.email todo="email" %}</li>
    <li><span class="label-sm">LinkedIn</span>{% include todo-link.html url=site.author.linkedin label="LinkedIn" todo="LinkedIn URL" %}</li>
  </ul>
</div>
