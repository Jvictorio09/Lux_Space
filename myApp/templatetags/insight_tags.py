"""
Template tags for rendering Editor.js blocks as HTML.

Usage in templates:
    {% load insight_tags %}
    {% render_blocks insight.blocks %}
"""

from django import template
from django.utils.html import escape, mark_safe

register = template.Library()


def _render_block(block: dict) -> str:
    """Convert a single Editor.js block dict to an HTML string."""
    btype = block.get("type", "")
    data = block.get("data", {})

    if btype == "paragraph":
        text = data.get("text", "")
        if not text:
            return ""
        return f'<p class="prose-p">{text}</p>'

    if btype == "header":
        text = escape(data.get("text", ""))
        level = int(data.get("level", 2))
        level = max(2, min(6, level))
        cls = f"prose-h{level}"
        return f'<h{level} class="{cls}">{text}</h{level}>'

    if btype == "list":
        style = data.get("style", "unordered")
        items = data.get("items", [])
        if not items:
            return ""
        tag = "ol" if style == "ordered" else "ul"
        cls = "prose-ol" if style == "ordered" else "prose-ul"
        lis = "".join(f"<li>{item}</li>" for item in items)
        return f'<{tag} class="{cls}">{lis}</{tag}>'

    if btype == "quote":
        text = data.get("text", "")
        caption = data.get("caption", "")
        cite = f"<cite>— {escape(caption)}</cite>" if caption else ""
        return f'<blockquote class="prose-quote"><p>{text}</p>{cite}</blockquote>'

    if btype == "image":
        url = data.get("url") or data.get("file", {}).get("url", "")
        caption = escape(data.get("caption", ""))
        if not url:
            return ""
        fig_cap = f"<figcaption>{caption}</figcaption>" if caption else ""
        stretched = ' class="prose-img--stretched"' if data.get("stretched") else ""
        return (
            f'<figure class="prose-img"{stretched}>'
            f'<img src="{escape(url)}" alt="{caption}" loading="lazy">'
            f"{fig_cap}</figure>"
        )

    if btype == "delimiter":
        return '<hr class="prose-hr">'

    if btype == "raw":
        html = data.get("html", "")
        return html

    return ""


@register.simple_tag
def render_blocks(blocks_data) -> str:
    """
    Render an Editor.js blocks JSON object (dict with 'blocks' list) as HTML.
    Safe to use directly in templates — returns a mark_safe string.

    Usage:
        {% render_blocks insight.blocks %}
    """
    if not blocks_data or not isinstance(blocks_data, dict):
        return mark_safe("")

    blocks = blocks_data.get("blocks", [])
    if not isinstance(blocks, list):
        return mark_safe("")

    html_parts = []
    for block in blocks:
        if isinstance(block, dict):
            rendered = _render_block(block)
            if rendered:
                html_parts.append(rendered)

    return mark_safe("\n".join(html_parts))
