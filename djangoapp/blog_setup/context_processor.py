from .models import SiteSetup


def site_setup_processor(request):
    setup = SiteSetup.objects.first()
    return {
        "setup": setup
    }
