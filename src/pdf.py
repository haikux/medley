from pypdf import PdfReader
from collections import defaultdict
from .const import ASSETS
from .pii import PII
import json

class PDF(PII):
    def __init__(self, raw_data: str):
        self.raw_data = PdfReader(raw_data)
        self.pages = len(self.raw_data.pages)
    
    def get_metadata(self):
        result = {
            "info": self.raw_data.metadata,
            "total_pages": self.pages
        }
        return result
    
    def read_all(self, save_images: bool=True) -> str:
        result = []
        for page in range(self.pages):
            tmp = {"page": page, "text": self.raw_data.pages[page].extract_text(), "images": []}
            
            for img in self.raw_data.pages[page].images:
                tmp["images"].append(img.name)
                if save_images:
                    with open(f"{ASSETS}/{img.name}", "wb") as fp:
                        fp.write(img.data)
            result.append(tmp)
        return result
    
    def read_page(self, page: int, save_images: bool=True) -> str:
        if page not in range(self.pages):
            return None
        result = {"page": page, "text": self.raw_data.pages[page].extract_text(), "images": []}
        for img in self.raw_data.pages[page].images:
                result["images"].append(img.name)
                if save_images:
                    with open(f"{ASSETS}/{img.name}", "wb") as fp:
                        fp.write(img.data)
        return result
    
    
    

    

