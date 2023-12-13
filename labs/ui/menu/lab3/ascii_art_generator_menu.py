from service.lab3.ascii_art_generator_service import AsciiArtGeneratorService


class AsciiArtGeneratorMenu:
    def run(self):
        ascii_art_generator_service = AsciiArtGeneratorService()
        ascii_art_generator_service.display_text()
