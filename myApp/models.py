from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Service(models.Model):
    """
    A core discipline of the studio (e.g. Landscaping, Interior Design).

    This drives:
    - The services overview grid
    - Individual service detail pages
    - Project grouping / filtering
    """

    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)

    short_label = models.CharField(
        max_length=40,
        help_text="Label used in tabs and pills, e.g. 'LANDSCAPING'.",
    )
    order_label = models.CharField(
        max_length=8,
        help_text="Numeric label such as '01', '02' to display before the name.",
    )

    # Hero / detail page content
    hero_kicker = models.CharField(
        max_length=120,
        blank=True,
        help_text="Small label above hero title, e.g. 'SERVICE 01'.",
    )
    hero_eyebrow = models.CharField(
        max_length=120,
        blank=True,
        help_text="Secondary small label, e.g. 'EST. 2013'.",
    )
    hero_title = models.CharField(
        max_length=200,
        help_text="Main hero heading, e.g. 'Ready to Transform Your Landscape?'.",
    )
    hero_emphasis = models.CharField(
        max_length=120,
        blank=True,
        help_text="Optional emphasised word in the hero heading.",
    )
    hero_intro = models.TextField(
        blank=True,
        help_text="Short paragraph under the hero title.",
    )
    hero_background_image = models.URLField(
        blank=True,
        help_text="Full URL to the hero background image.",
    )

    overview_heading = models.CharField(
        max_length=200,
        blank=True,
        help_text="Overview section heading, e.g. 'Where Nature Becomes Art'.",
    )
    overview_body_primary = models.TextField(blank=True)
    overview_body_secondary = models.TextField(blank=True)

    cta_primary_label = models.CharField(
        max_length=80,
        default="EXPLORE SERVICE",
        help_text="Label for primary hero CTA button.",
    )
    cta_secondary_label = models.CharField(
        max_length=80,
        default="VIEW PROJECTS",
        help_text="Label for secondary hero CTA button.",
    )
    cta_heading = models.CharField(
        max_length=200,
        blank=True,
        help_text="Bottom CTA section heading, e.g. 'Ready to Transform Your Landscape?'.",
    )
    cta_intro = models.TextField(
        blank=True,
        help_text="Bottom CTA paragraph under heading.",
    )

    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_hero_name_parts(self):
        """Returns (before, emphasis) for hero h1 e.g. ('Land', 'scaping')."""
        if not self.hero_emphasis or len(self.hero_emphasis) >= len(self.name):
            return (self.name, None)
        cut = len(self.name) - len(self.hero_emphasis)
        return (self.name[:cut], self.name[cut:])


class Project(models.Model):
    """
    A portfolio project, optionally featured on one or more pages.
    """

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    service = models.ForeignKey(
        Service,
        related_name="projects",
        on_delete=models.CASCADE,
    )

    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    location = models.CharField(max_length=160, blank=True)
    year = models.CharField(max_length=8, blank=True)

    summary = models.TextField(
        blank=True,
        help_text="Short description used on cards.",
    )
    description = models.TextField(
        blank=True,
        help_text="Full case-study text for the project detail page.",
    )

    hero_image = models.URLField(
        blank=True,
        help_text="Large hero image shown on project pages / featured sections.",
    )
    thumbnail_image = models.URLField(
        blank=True,
        help_text="Image used on cards; falls back to hero image if empty.",
    )

    # Detail page content (optional — sections hidden when empty)
    pull_quote = models.TextField(blank=True)
    pull_quote_author = models.CharField(max_length=120, blank=True)

    testimonial_quote = models.TextField(blank=True)
    testimonial_author = models.CharField(max_length=120, blank=True)
    testimonial_location = models.CharField(max_length=160, blank=True)
    testimonial_avatar_url = models.URLField(blank=True)

    challenges = models.JSONField(
        default=list,
        blank=True,
        help_text="List of {title, description}.",
    )
    solutions = models.JSONField(
        default=list,
        blank=True,
        help_text="List of {title, description}. Should match challenges length.",
    )
    process_phases = models.JSONField(
        default=list,
        blank=True,
        help_text="List of {phase_label, duration, title, description, icon, is_last}.",
    )
    outcome_intro = models.TextField(
        blank=True,
        help_text="Paragraph above outcome stats.",
    )
    outcome_stats = models.JSONField(
        default=list,
        blank=True,
        help_text="List of {value, label}.",
    )
    awards = models.JSONField(
        default=list,
        blank=True,
        help_text="List of {name, title, organization, icon}.",
    )

    is_featured = models.BooleanField(default=False, db_column="featured")
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default="published"
    )
    display_order = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "-created_at"]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def card_image(self) -> str:
        return self.thumbnail_image or self.hero_image


class ProjectImage(models.Model):
    """
    Additional gallery / detail images attached to a project.
    """

    project = models.ForeignKey(
        Project,
        related_name="images",
        on_delete=models.CASCADE,
    )
    image_url = models.URLField()
    caption = models.CharField(max_length=255, blank=True)
    is_hero = models.BooleanField(
        default=False, help_text="If true, can be used as hero/banner image."
    )
    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self) -> str:
        return f"{self.project.title} image #{self.pk}"


class GalleryImage(models.Model):
    """
    Standalone gallery image uploaded via the dashboard.

    Following Cloudinary pattern:
    - Images stored in Cloudinary (not on Django server)
    - Database stores URLs only (3 variants) + metadata
    - Compression happens before upload if > 9.3MB
    """

    title = models.CharField(max_length=160, blank=True)
    
    # Three URL variants
    secure_url = models.URLField(
        help_text="Original uploaded image URL (full quality, fallback)"
    )
    web_url = models.URLField(
        help_text="Optimized URL with f_auto,q_auto (use for website display)"
    )
    thumb_url = models.URLField(
        help_text="Thumbnail URL with c_fill,g_face,w_480,h_320 (use for galleries)"
    )
    
    # Metadata
    public_id = models.CharField(
        max_length=255,
        help_text="Cloudinary public_id identifier"
    )
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    format = models.CharField(max_length=10, blank=True, help_text="Image format (webp, jpg, etc.)")
    bytes = models.PositiveIntegerField(blank=True, null=True, help_text="File size in bytes")
    
    # Legacy field for backward compatibility (will be populated from secure_url)
    cloudinary_url = models.URLField(blank=True, help_text="Legacy field - use secure_url instead")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at", "id"]

    def __str__(self) -> str:
        return self.title or f"Image {self.pk}"
    
    def save(self, *args, **kwargs):
        # Populate legacy cloudinary_url for backward compatibility
        if not self.cloudinary_url and self.secure_url:
            self.cloudinary_url = self.secure_url
        super().save(*args, **kwargs)


class Insight(models.Model):
    """
    An editorial article / insight post.

    Body content is stored as Editor.js JSON in the `blocks` JSONField.
    Rendered to HTML at display time via the `insight_tags` template tag.
    """

    CATEGORY_CHOICES = [
        ("interior", "Interior Design"),
        ("landscape", "Landscaping"),
        ("joinery", "Joinery"),
        ("pools", "Swimming Pools"),
        ("guides", "Project Guides"),
        ("dubai", "Dubai Living"),
    ]

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    excerpt = models.TextField(
        blank=True,
        help_text="Short summary shown on listing cards.",
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="interior",
    )
    cover_image_url = models.URLField(
        blank=True,
        help_text="Full URL to the article cover/hero image.",
    )
    blocks = models.JSONField(
        default=dict,
        blank=True,
        help_text="Editor.js blocks JSON — the full article body.",
    )
    read_time = models.PositiveIntegerField(
        default=5,
        help_text="Estimated reading time in minutes.",
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Pin as the featured article on the insights listing page.",
    )
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default="draft",
    )
    published_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.status == "published" and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    @property
    def category_label(self) -> str:
        return dict(self.CATEGORY_CHOICES).get(self.category, self.category)

    @property
    def published_date_display(self) -> str:
        if self.published_at:
            return self.published_at.strftime("%B %Y")
        if self.created_at:
            return self.created_at.strftime("%B %Y")
        return ""

    @property
    def published_date_long(self) -> str:
        if self.published_at:
            return self.published_at.strftime("%B %d, %Y").replace(" 0", " ")
        return ""
