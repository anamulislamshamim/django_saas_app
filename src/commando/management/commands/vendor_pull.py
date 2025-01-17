import helpers
from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings


# STATICFILES_VENDOR_DIR = settings.STATICFILES_VENDOR_DIR
STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js"
}


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files ...")
        completed_urls = []
        
        for name, url in VENDOR_STATICFILES.items():
            destination_path = STATICFILES_VENDOR_DIR / name 
            dl_success = helpers.download_to_local(url, destination_path)
            if dl_success:
                completed_urls.append(url) 
                self.stdout.write(
                    self.style.SUCCESS(f"{name} downloaded successfully!")
                )
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {url}")
                )
            
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS("Successfully updated all vendor files.")
            )
        else:
            self.stdout.write(
                self.style.WARNING('Some files were not updated!')
            )
             