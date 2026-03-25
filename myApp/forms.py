from django import forms

from .models import GalleryImage, Insight, Project, Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            "name",
            "slug",
            "short_label",
            "order_label",
            "hero_kicker",
            "hero_eyebrow",
            "hero_title",
            "hero_emphasis",
            "hero_intro",
            "hero_background_image",
            "overview_heading",
            "overview_body_primary",
            "overview_body_secondary",
            "cta_primary_label",
            "cta_secondary_label",
            "cta_heading",
            "cta_intro",
            "is_active",
            "display_order",
        ]
        widgets = {
            "hero_intro": forms.Textarea(attrs={"rows": 3}),
            "overview_body_primary": forms.Textarea(attrs={"rows": 4}),
            "overview_body_secondary": forms.Textarea(attrs={"rows": 4}),
            "cta_intro": forms.Textarea(attrs={"rows": 2}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "service",
            "title",
            "slug",
            "location",
            "year",
            "summary",
            "description",
            "hero_image",
            "thumbnail_image",
            "is_featured",
            "status",
            "display_order",
        ]
        widgets = {
            "summary": forms.Textarea(attrs={"rows": 3}),
            "description": forms.Textarea(attrs={"rows": 5}),
        }


class MultiFileInput(forms.ClearableFileInput):
    """
    Widget that allows multiple file selection.
    """

    allow_multiple_selected = True

    def value_from_datadict(self, data, files, name):
        """
        Return a list of uploaded files from the widget.
        """
        try:
            getter = data.getlist
        except AttributeError:
            getter = data.get
        return files.getlist(name)


class MultipleFileField(forms.FileField):
    """
    Custom field that accepts multiple files.
    """
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultiFileInput(attrs={"multiple": True}))
        super().__init__(*args, **kwargs)
    
    def clean(self, data, initial=None):
        """
        Clean the field data - accept a list of files.
        """
        if data is None:
            return None
        # If it's already a list, return it
        if isinstance(data, list):
            if not data:
                raise forms.ValidationError("Please select at least one file.")
            return data
        # If it's a single file, wrap it in a list
        return [data] if data else None


class GalleryUploadForm(forms.Form):
    """
    Handles one or many files from the dashboard gallery upload.
    """

    images = MultipleFileField(
        help_text="You can select one or many images.",
        required=True,
    )


class InsightForm(forms.ModelForm):
    """
    Form for creating/editing Insight articles in the dashboard.
    The `blocks` field is a hidden JSON field populated by Editor.js.
    """

    blocks = forms.CharField(
        widget=forms.HiddenInput(attrs={"id": "blocksField"}),
        required=False,
        initial="{}",
    )

    class Meta:
        model = Insight
        fields = [
            "title",
            "slug",
            "excerpt",
            "category",
            "cover_image_url",
            "read_time",
            "is_featured",
            "status",
            "blocks",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Article title…", "autocomplete": "off"}),
            "slug": forms.TextInput(attrs={"placeholder": "auto-generated-from-title"}),
            "excerpt": forms.Textarea(attrs={"rows": 3, "placeholder": "Short description shown on listing cards…"}),
            "cover_image_url": forms.URLInput(attrs={"placeholder": "https://…", "id": "coverUrlField"}),
        }

    def clean_blocks(self):
        import json
        raw = self.cleaned_data.get("blocks") or "{}"
        try:
            parsed = json.loads(raw)
        except (ValueError, TypeError):
            parsed = {}
        return parsed


class ProjectImageURLForm(forms.Form):
    """Add a project gallery image by URL."""

    image_url = forms.URLField(
        required=True,
        widget=forms.URLInput(attrs={"placeholder": "https://..."}),
    )
    caption = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Optional caption"}),
    )
    is_hero = forms.BooleanField(required=False, initial=False)


