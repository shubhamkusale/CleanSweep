import os
import shutil
import unittest
from organizer import FileOrganizer

class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_zone"
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)
        
        self.organizer = FileOrganizer()

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def create_dummy_file(self, filename):
        path = os.path.join(self.test_dir, filename)
        with open(path, 'w') as f:
            f.write("dummy content")
        return path

    def test_organize_image(self):
        file_path = self.create_dummy_file("test.jpg")
        self.organizer.organize_file(file_path)
        
        expected_path = os.path.join(self.test_dir, "Images", "test.jpg")
        self.assertTrue(os.path.exists(expected_path))

    def test_organize_document(self):
        file_path = self.create_dummy_file("doc.pdf")
        self.organizer.organize_file(file_path)
        
        expected_path = os.path.join(self.test_dir, "Documents", "doc.pdf")
        self.assertTrue(os.path.exists(expected_path))

    def test_unique_filename(self):
        # Create directory and first file manually
        images_dir = os.path.join(self.test_dir, "Images")
        os.makedirs(images_dir)
        with open(os.path.join(images_dir, "test.png"), 'w') as f:
            f.write("original")
            
        # Create second file in root
        file_path = self.create_dummy_file("test.png")
        self.organizer.organize_file(file_path)
        
        # Should be renamed to test_1.png
        expected_path = os.path.join(self.test_dir, "Images", "test_1.png")
        self.assertTrue(os.path.exists(expected_path))

if __name__ == '__main__':
    unittest.main()
