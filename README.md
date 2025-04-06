# 🎧 Parallel Audio Downloader & Analyzer with Multiprocessing

This project demonstrates the use of Python’s `multiprocessing.pool` to speed up the downloading and analysis of `.wav` audio files from multiple pages. A Tkinter GUI provides options for both single-threaded and multi-threaded execution for comparison.

---

## 🚀 Features

- ✅ **Tkinter GUI** with 3 actions:
  - Download audio files without multiprocessing
  - Download audio files using multiprocessing pool
  - Scrape and log audio metadata into a `.txt` report
- ✅ **Audio Downloader**
  - Extracts `.wav` file links from user-defined websites
  - Downloads each file to the `./output/` directory
- ✅ **Multithreading Support**
  - Uses `ThreadPool` to parallelize downloads
  - Comparison of execution time for both methods
- ✅ **Audio Metadata Analysis**
  - Extracts frame rate, channels, sample width, max amplitude, and duration using `pydub`
  - Logs all results in a well-formatted `results.txt` table

---

## 🗂️ Project Structure

| File | Description |
|------|-------------|
| `working with audios.py` | Main GUI and logic for downloading and analyzing `.wav` files |
| `links.txt` | List of audio web pages to scrape |
| `results.txt` | Output report of audio metadata |
| `output/` | Folder to store downloaded audio files |

---

## 🛠 Technologies

- Python 3
- Tkinter
- `multiprocessing.pool`
- `requests` + `BeautifulSoup`
- `pydub` for audio processing
- `prettytable` for clean output formatting

---

## 📊 Sample Output

```txt
+------------+------------+----------+------------------+-------------------+----------------------+
| Audio name | Frame rate | Channels | Bytes per sample | Maximum amplitude | length of audio file |
+------------+------------+----------+------------------+-------------------+----------------------+
| Cartoon-01 | 11025      | 1        | 1                | 98                | 4292                 |
| Bender-01  | 44100      | 1        | 1                | 94                | 1567                 |
...
