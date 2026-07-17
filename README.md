# Photo Organizer

Automatically organize photos and videos by Year / Month.

---

## Features

### Supported Formats
- JPG
- HEIC *(planned)*
- PNG
- DNG
- MOV *(planned)*
- MP4 *(planned)*

### Metadata
- EXIF Priority
- Creation Date Fallback
- Duplicate Skip *(planned)*

### Functions
- Folder Analysis
- Metadata Reader
- GUI
- Progress Bar

---

## Changelog

### v0.3

- Added `MetadataReader`
- Read EXIF metadata from JPG images
- Support:
  - DateTimeOriginal
  - DateTimeDigitized
  - DateTime
- Added automatic fallback to Creation Date
- Added metadata test script

### v0.2

- Added folder analysis
- Count images and videos
- Display folder size
- Added DNG support
- Integrated analyzer with GUI

### v0.1

- Initial GUI
- Folder selection
- Output folder selection

---

## Roadmap

- [x] v0.1 GUI
- [x] v0.2 Folder Analysis
- [x] v0.3 Metadata Reader
- [ ] v0.4 Preview Organizer
- [ ] v0.5 Copy Engine
- [ ] v0.6 Duplicate Detection
- [ ] v1.0 Release