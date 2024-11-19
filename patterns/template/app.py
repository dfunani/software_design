from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    def generate_report(self):
        self.open_file()
        self.write_header()
        self.write_body()
        self.write_footer()
        self.close_file()

    def open_file(self):
        print("Opening file...")

    def close_file(self):
        print("Closing file...")

    @abstractmethod
    def write_header(self):
        pass

    @abstractmethod
    def write_body(self):
        pass

    @abstractmethod
    def write_footer(self):
        pass

class PDFReportGenerator(ReportGenerator):
    def write_header(self):
        print("Writing PDF header...")

    def write_body(self):
        print("Writing PDF body...")

    def write_footer(self):
        print("Writing PDF footer...")

class HTMLReportGenerator(ReportGenerator):
    def write_header(self):
        print("Writing HTML header...")

    def write_body(self):
        print("Writing HTML body...")

    def write_footer(self):
        print("Writing HTML footer...")

pdf_generator = PDFReportGenerator()
pdf_generator.generate_report()

html_generator = HTMLReportGenerator()
html_generator.generate_report()