# Third party
from django.utils.translation import gettext as _


def check_keywords(site):
    """Ensure that all keywords are present.
    """
    meta = site.soup.find_all("meta")
    for tag in meta:
        if (
            "name" in tag.attrs
            and tag.attrs["name"] == "keywords"
            and "content" in tag.attrs
            and tag.attrs["content"] != ""
        ):
            # get keywords for next checks
            site.keywords = tag.attrs["content"].split(
                ",  "
            )  # may be dangerous to hard code the case where keywords are separated with a comma and two spaces
            return
    site.problems.append(
        {
            "name": _("No meta keywords"),
            "settings": _("at least 1"),
            "description": _(
                "Meta keywords were important in this meta tag, however django-check-seo uses these keywords to check all other tests related to keywords. You will be flooded with problems and warnings and this SEO tool will not work as well as it should if you don't add some keywords."
            ),
        }
    )