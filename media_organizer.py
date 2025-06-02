import os
import shutil
from pathlib import Path
from PIL import Image
import tempfile
import ffmpeg

def compress_image_smart(
    image_path: str,
    compression_ratio: float,
    quality: int = 85
) -> str:
    """
    Compress an image to JPEG using Pillow, preserving EXIF and timestamps.

    Args:
        image_path (str): Path to the original image.
        compression_ratio (float): Max target file size percentage (e.g., 70 = 70% original size).
        quality (int): JPEG quality (1–95).

    Returns:
        str: Path to final image (compressed or original).
    """
    image_path = Path(image_path)
    orig_size = image_path.stat().st_size
    target_size = orig_size * (compression_ratio / 100.0)

    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        with Image.open(image_path) as img:
            img_rgb = img.convert("RGB")
            exif_data = img.info.get("exif")  # this may be None

            # Save with EXIF if it exists
            save_kwargs = {
                "format": "JPEG",
                "quality": quality,
            }
            if exif_data:
                save_kwargs["exif"] = exif_data

            img_rgb.save(tmp_path, **save_kwargs)

        compressed_size = tmp_path.stat().st_size

        # Copy original timestamps
        stat = image_path.stat()
        os.utime(tmp_path, (stat.st_atime, stat.st_mtime))

        if compressed_size <= target_size:
            final_path = image_path.with_suffix(".compressed.jpg")
            shutil.move(tmp_path, final_path)
            return str(final_path)
        else:
            os.remove(tmp_path)
            return str(image_path)

    except Exception as e:
        if tmp_path.exists():
            os.remove(tmp_path)
        raise RuntimeError(f"Compression failed for {image_path}") from e

def compress_video_smart(
    video_path: str,
    compression_ratio: float,
    crf: int = 28,
    preset: str = "medium"
) -> str:
    """
    Compresses a video and saves it as .mp4 if compression meets ratio.

    Args:
        video_path (str): Path to original video.
        compression_ratio (float): Max file size percent (e.g., 70 means ≤70% original).
        crf (int): Constant Rate Factor for ffmpeg (lower = better quality, typical 23–28).
        preset (str): Encoding speed/quality tradeoff (e.g., 'ultrafast', 'medium', 'slow').

    Returns:
        str: Path to final video (compressed or original).
    """
    video_path = Path(video_path)
    orig_size = video_path.stat().st_size
    target_size = orig_size * (compression_ratio / 100.0)

    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        (
            ffmpeg
            .input(str(video_path))
            .output(str(tmp_path), vcodec='libx264', crf=crf, preset=preset, acodec='aac')
            .overwrite_output()
            .run(quiet=True)
        )

        compressed_size = tmp_path.stat().st_size

        # Copy original timestamps
        stat = video_path.stat()
        os.utime(tmp_path, (stat.st_atime, stat.st_mtime))

        if compressed_size <= target_size:
            final_path = video_path.with_suffix(".compressed.mp4")
            shutil.move(tmp_path, final_path)
            return str(final_path)
        else:
            os.remove(tmp_path)
            return str(video_path)

    except Exception as e:
        if tmp_path.exists():
            os.remove(tmp_path)
        raise RuntimeError(f"Video compression failed for {video_path}") from e

def compress_audio_smart(
    audio_path: str,
    compression_ratio: float,
    bitrate: str = "128k"
) -> str:
    """
    Compresses an audio file and saves it as .mp3 if compression meets ratio.

    Args:
        audio_path (str): Path to original audio.
        compression_ratio (float): Max file size percent (e.g., 70 means ≤70% original).
        bitrate (str): Target bitrate for compression (e.g., '128k').

    Returns:
        str: Path to final audio (compressed or original).
    """
    audio_path = Path(audio_path)
    orig_size = audio_path.stat().st_size
    target_size = orig_size * (compression_ratio / 100.0)

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        (
            ffmpeg
            .input(str(audio_path))
            .output(str(tmp_path), acodec='libmp3lame', audio_bitrate=bitrate)
            .overwrite_output()
            .run(quiet=True)
        )

        compressed_size = tmp_path.stat().st_size

        # Copy original timestamps
        stat = audio_path.stat()
        os.utime(tmp_path, (stat.st_atime, stat.st_mtime))

        if compressed_size <= target_size:
            final_path = audio_path.with_suffix(".compressed.mp3")
            shutil.move(tmp_path, final_path)
            return str(final_path)
        else:
            os.remove(tmp_path)
            return str(audio_path)

    except Exception as e:
        if tmp_path.exists():
            os.remove(tmp_path)
        raise RuntimeError(f"Audio compression failed for {audio_path}") from e

def compress_file(
    file_path: Path, 
    compression_ratio: float
) -> None:
    """
    Compresses a file and overwrites it only if the result is smaller.
    """
    ext = file_path.suffix.lower()
    original_size = file_path.stat().st_size

    try:
        if ext in [".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".webp"]:
            compressed_path = compress_image_smart(str(file_path), compression_ratio)

        elif ext in [".mp4", ".mov", ".avi", ".mkv", ".webm"]:
            compressed_path = compress_video_smart(str(file_path), compression_ratio)

        elif ext in [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"]:
            compressed_path = compress_audio_smart(str(file_path), compression_ratio)

        else:
            print(f"[Skipped] Unsupported file type: {file_path.name}")
            return

        if not compressed_path or not os.path.exists(compressed_path):
            print(f"[Error] Compression failed for {file_path.name}")
            return

        compressed_size = os.path.getsize(compressed_path)

        if compressed_size >= original_size:
            print(f"[Skipped] {file_path.name}: Compression not worth it ({compressed_size} >= {original_size})")
            return

        # Overwrite original while preserving metadata
        shutil.move(compressed_path, file_path)
        print(f"[Overwritten] {file_path.name}: {original_size//1024}KB → {compressed_size//1024}KB")

    except Exception as e:
        print(f"[Error] {file_path.name}: {e}")

def get_all_files(
    folder: Path, 
    min_size_mb: float
) -> list:
    """
    Recursively get all files over a minimum size in megabytes.
    """
    files = []
    for file in folder.rglob("*"):
        if file.is_file() and file.stat().st_size >= min_size_mb * 1024 * 1024:
            files.append(file)
    return files

def main(
    folder_path: str, 
    compression_ratio: float = 70, 
    min_size_mb: float = 5
) -> None:
    """
    Compresses all supported files in a folder, starting with the biggest.
    """
    folder = Path(folder_path)

    if not folder.is_dir():
        print(f"[Error] Not a directory: {folder}")
        return

    all_files = get_all_files(folder, min_size_mb)
    if not all_files:
        print(f"[Info] No files over {min_size_mb} MB found in {folder}")
        return

    # Sort by size, descending
    all_files.sort(key=lambda f: f.stat().st_size, reverse=True)

    print(f"[Start] Found {len(all_files)} files over {min_size_mb}MB. Compressing...\n")

    for file in all_files:
        compress_file(file, compression_ratio)


if __name__ == "__main__":
    # Example usage:
    main("/Users/manu/Desktop/2020", compression_ratio=70, min_size_mb=1)

# [Overwritten] 20200808_230829.mp4: 3434411KB → 410698KB
# [Overwritten] 20201204_134239.mp4: 2369462KB → 209026KB
# [Skipped] VID_20200123_160421.mp4: Compression not worth it (1682942806 >= 1682942806)
# [Skipped] 20200730_123453.mp4: Compression not worth it (1364776869 >= 1364776869)
# [Overwritten] 20200809_203657.mp4: 1173226KB → 227087KB
# [Overwritten] 20201126_111014.mp4: 1099463KB → 268477KB
# [Overwritten] 20200822_231751.mp4: 1028148KB → 97054KB
# [Skipped] VID_20200123_161024.mp4: Compression not worth it (1032849720 >= 1032849720)