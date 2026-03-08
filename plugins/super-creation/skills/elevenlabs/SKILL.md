---
name: elevenlabs
description: >
  Generate audio content using the ElevenLabs Python SDK — text-to-speech, podcasts,
  voice cloning, sound effects, speech-to-speech, dubbing, and audio isolation.
  Use when the user wants to create audio files, generate podcasts from text,
  clone voices, produce voiceovers, or work with ElevenLabs API.
  Triggers: elevenlabs, text-to-speech, TTS, podcast, voice, audio, voiceover,
  narration, voice clone, sound effects, dubbing, speech-to-speech, audio isolation.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - Write
  - Edit
---

# ElevenLabs Audio Production

Generate audio content with the ElevenLabs Python SDK — from single-line TTS to full podcast production.

## Boundaries

**This skill MAY:** install the SDK, generate audio files, list voices, create voice clones, write audio generation scripts, play audio, manage projects.

**This skill MAY NOT:** store API keys in code (use env vars or secrets), commit audio files to git (use `.gitignore`), generate audio without user approval of the text/script first.

## Common Rationalizations

| Shortcut | Why It Fails | The Cost |
|----------|-------------|----------|
| Hardcode API key in script | Leaks credentials to git history | Security incident, key rotation |
| Skip voice selection, use default | Default voice may not match content tone | Re-generation wastes credits |
| Generate full podcast without preview | Long audio = expensive; mistakes compound | Wasted API credits, re-work |
| Use `eleven_v3` for everything | Wrong model for long-form (char limit 5,000) | Truncated audio, extra API calls |
| Skip `output_format` parameter | Default mp3 may not match downstream needs | Format conversion overhead |

## Prerequisites

```bash
# Install SDK
pip install elevenlabs

# Or with uv (preferred in aimee-backend)
uv pip install elevenlabs

# Set API key (NEVER hardcode)
export ELEVENLABS_API_KEY="your-key-here"
```

Verify setup:
```python
from elevenlabs.client import ElevenLabs
client = ElevenLabs()  # reads ELEVENLABS_API_KEY from env
voices = client.voices.get_all()
print(f"Connected. {len(voices.voices)} voices available.")
```

## Phase 0: Understand the Request

**Entry:** User wants audio content.

Classify the request:

| Request Type | Route | Model Recommendation |
|-------------|-------|---------------------|
| Short TTS (< 1,000 chars) | Phase 1: Quick TTS | `eleven_flash_v2_5` (fast, cheap) |
| Medium TTS (1,000-5,000 chars) | Phase 1: Quick TTS | `eleven_v3` (expressive) |
| Long-form / podcast (> 5,000 chars) | Phase 2: Podcast | `eleven_multilingual_v2` (stable, 10k limit) |
| Voice cloning | Phase 3: Voice Clone | N/A |
| Sound effects | Phase 4: Sound Effects | N/A |
| Speech-to-speech | Phase 5: Voice Transform | `eleven_english_sts_v2` |
| Audio cleanup | Phase 6: Audio Isolation | N/A |
| Dubbing / translation | Phase 7: Dubbing | N/A |

**Exit:** Request classified, user approves the approach.

## Phase 1: Quick Text-to-Speech

**Entry:** User wants a single audio file from text.

### Step 1: Select Voice

```python
from elevenlabs.client import ElevenLabs

client = ElevenLabs()

# List available voices
voices = client.voices.get_all()
for v in voices.voices:
    print(f"{v.voice_id}: {v.name} ({v.labels})")
```

**Popular built-in voices:**

| Voice | ID | Style | Good For |
|-------|-----|-------|----------|
| Rachel | `21m00Tcm4TlvDq8ikWAM` | Calm, narration | Podcasts, audiobooks |
| Adam | `pNInz6obpgDQGcFmaJgB` | Deep, authoritative | Business, explainers |
| Bella | `EXAVITQu4vr4xnSDxMaL` | Warm, friendly | Casual content |
| Antoni | `ErXwobaYiN019PkySvjV` | Conversational | Dialogue, interviews |
| Elli | `MF3mGyEYCl7XYWbV9V6O` | Young, energetic | Marketing, tutorials |

### Step 2: Generate

```python
import os

audio = client.text_to_speech.convert(
    text="Your text here",
    voice_id="21m00Tcm4TlvDq8ikWAM",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

output_path = "output.mp3"
with open(output_path, "wb") as f:
    f.write(audio)

print(f"Saved to {output_path} ({os.path.getsize(output_path)} bytes)")
```

### Step 3: Stream (for real-time playback)

```python
from elevenlabs import stream as play_stream

audio_stream = client.text_to_speech.convert_as_stream(
    text="Your text here",
    voice_id="21m00Tcm4TlvDq8ikWAM",
    model_id="eleven_flash_v2_5",
)

play_stream(audio_stream)  # Plays immediately as it generates
```

**Exit:** Audio file saved or streamed.

## Phase 2: Podcast / Long-Form Audio

**Entry:** User wants podcast-style audio from a long text (> 5,000 chars).

### Strategy: Chunk and Concatenate

ElevenLabs models have character limits. For long content, split into semantic chunks and concatenate.

```python
import io
from pydub import AudioSegment  # pip install pydub

def generate_podcast(
    client,
    script: str,
    voice_id: str,
    model_id: str = "eleven_multilingual_v2",
    chunk_size: int = 4500,
    output_path: str = "podcast.mp3",
    pause_ms: int = 800,
) -> str:
    """Generate podcast audio from a long script.

    Splits on paragraph boundaries, generates per-chunk,
    concatenates with pauses between sections.
    """
    # Split on double newlines (paragraph boundaries)
    paragraphs = [p.strip() for p in script.split("\n\n") if p.strip()]

    # Group paragraphs into chunks under the char limit
    chunks = []
    current_chunk = ""
    for para in paragraphs:
        if len(current_chunk) + len(para) + 2 > chunk_size:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = para
        else:
            current_chunk = f"{current_chunk}\n\n{para}" if current_chunk else para
    if current_chunk:
        chunks.append(current_chunk)

    print(f"Split into {len(chunks)} chunks")

    # Generate audio for each chunk
    pause = AudioSegment.silent(duration=pause_ms)
    combined = AudioSegment.empty()

    for i, chunk in enumerate(chunks):
        print(f"Generating chunk {i + 1}/{len(chunks)} ({len(chunk)} chars)...")
        audio_bytes = client.text_to_speech.convert(
            text=chunk,
            voice_id=voice_id,
            model_id=model_id,
            output_format="mp3_44100_128",
            previous_text=chunks[i - 1][-200:] if i > 0 else None,
        )
        segment = AudioSegment.from_mp3(io.BytesIO(audio_bytes))
        combined += segment + pause

    combined.export(output_path, format="mp3", bitrate="128k")
    duration_s = len(combined) / 1000
    print(f"Saved {output_path} ({duration_s:.0f}s, {duration_s / 60:.1f} min)")
    return output_path
```

### Usage

```python
from elevenlabs.client import ElevenLabs

client = ElevenLabs()

script = open("podcast_script.md").read()

generate_podcast(
    client,
    script=script,
    voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel
    output_path="sp-assessment-explained.mp3",
)
```

### Multi-Voice Podcast (Dialogue)

For interview/conversation format with multiple speakers:

```python
def generate_dialogue_podcast(
    client,
    segments: list[dict],
    output_path: str = "dialogue.mp3",
    pause_ms: int = 600,
) -> str:
    """Generate multi-voice podcast.

    segments: [{"voice_id": "...", "text": "..."}, ...]
    """
    from pydub import AudioSegment
    import io

    pause = AudioSegment.silent(duration=pause_ms)
    combined = AudioSegment.empty()

    for i, seg in enumerate(segments):
        print(f"Segment {i + 1}/{len(segments)}: {seg['text'][:50]}...")
        audio_bytes = client.text_to_speech.convert(
            text=seg["text"],
            voice_id=seg["voice_id"],
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        combined += AudioSegment.from_mp3(io.BytesIO(audio_bytes)) + pause

    combined.export(output_path, format="mp3", bitrate="128k")
    print(f"Saved {output_path} ({len(combined) / 1000:.0f}s)")
    return output_path


# Example: two-host podcast
segments = [
    {"voice_id": "pNInz6obpgDQGcFmaJgB", "text": "Welcome to the show. Today we're talking about AI assessment."},
    {"voice_id": "21m00Tcm4TlvDq8ikWAM", "text": "Thanks for having me. Let's dive in."},
    {"voice_id": "pNInz6obpgDQGcFmaJgB", "text": "So how does this whole thing actually work?"},
    # ...
]

generate_dialogue_podcast(client, segments)
```

**Exit:** Podcast audio file saved.

## Phase 3: Voice Cloning

**Entry:** User wants to create a custom voice from audio samples.

### Instant Voice Clone (1-5 min of audio)

```python
voice = client.clone(
    name="My Custom Voice",
    description="Professional male, mid-30s, neutral accent",
    files=["sample1.mp3", "sample2.mp3"],
)

print(f"Cloned voice ID: {voice.voice_id}")

# Use it immediately
audio = client.text_to_speech.convert(
    text="Testing my cloned voice.",
    voice_id=voice.voice_id,
    model_id="eleven_multilingual_v2",
)
```

### Voice Design (Generate New Voice)

```python
from elevenlabs.client import ElevenLabs

client = ElevenLabs()

# Generate a brand-new voice from attributes
audio = client.text_to_speech.convert(
    text="This is a test of a designed voice.",
    voice_id="custom",  # Use voice design endpoint
    model_id="eleven_multilingual_v2",
)
```

**Exit:** Custom voice created and tested.

## Phase 4: Sound Effects

**Entry:** User wants AI-generated sound effects.

```python
audio = client.text_to_sound_effects.convert(
    text="Heavy rain on a tin roof with distant thunder",
    duration_seconds=10.0,
)

with open("rain.mp3", "wb") as f:
    f.write(audio)
```

**Prompting tips:**
- Be specific: "footsteps on gravel" beats "walking sounds"
- Include environment: "in a large cathedral" adds reverb
- Specify duration for predictable results

**Exit:** Sound effect file saved.

## Phase 5: Speech-to-Speech (Voice Transform)

**Entry:** User wants to transform audio from one voice to another.

```python
with open("input.mp3", "rb") as f:
    input_audio = f.read()

transformed = client.speech_to_speech.convert(
    audio=input_audio,
    voice_id="target_voice_id",
    model_id="eleven_english_sts_v2",
)

with open("transformed.mp3", "wb") as f:
    f.write(transformed)
```

Preserves: timing, emotion, pacing. Changes: voice identity.

**Exit:** Transformed audio file saved.

## Phase 6: Audio Isolation (Noise Removal)

**Entry:** User wants to clean up noisy audio.

```python
with open("noisy.mp3", "rb") as f:
    noisy_audio = f.read()

clean = client.audio_isolation.audio_isolation(audio=noisy_audio)

with open("clean.mp3", "wb") as f:
    f.write(clean)
```

**Exit:** Cleaned audio file saved.

## Phase 7: Dubbing / Translation

**Entry:** User wants to dub audio/video into another language.

```python
from elevenlabs.client import ElevenLabs

client = ElevenLabs()

# From file
result = client.dubbing.dub_a_video_or_an_audio_file(
    file=open("video.mp4", "rb"),
    target_lang="es",
    source_lang="en",
)

dubbing_id = result.dubbing_id
print(f"Dubbing job: {dubbing_id}")

# Poll for completion
import time
while True:
    status = client.dubbing.get_dubbing_project_metadata(dubbing_id)
    if status.status == "dubbed":
        break
    print(f"Status: {status.status}...")
    time.sleep(10)

# Download result
dubbed = client.dubbing.get_dubbed_file(dubbing_id, target_lang="es")
with open("dubbed_es.mp4", "wb") as f:
    f.write(dubbed)
```

**Exit:** Dubbed file saved.

## Model Selection Reference

| Model ID | Best For | Char Limit | Latency | Languages |
|----------|----------|------------|---------|-----------|
| `eleven_v3` | Expressive, dramatic delivery | 5,000 | ~300ms | 70+ |
| `eleven_multilingual_v2` | Long-form, stable, multilingual | 10,000 | Standard | 29 |
| `eleven_flash_v2_5` | Low-latency, real-time | 40,000 | ~75ms | 32 |
| `eleven_turbo_v2_5` | Quality + speed balance | 40,000 | ~250ms | 32 |

**Decision tree:**

```
Need < 75ms latency?
├─ Yes → eleven_flash_v2_5
└─ No → Is content > 5,000 chars?
   ├─ Yes → eleven_multilingual_v2
   └─ No → Need dramatic/emotional delivery?
      ├─ Yes → eleven_v3
      └─ No → eleven_turbo_v2_5
```

## Output Formats Reference

| Format String | Quality | Use Case |
|--------------|---------|----------|
| `mp3_44100_128` | High | Default, general purpose |
| `mp3_44100_192` | Highest MP3 | Archival, high-fidelity |
| `mp3_22050_32` | Low | Voice messages, previews |
| `pcm_44100` | Lossless | Post-processing, editing |
| `pcm_16000` | Low-latency | Real-time applications |

## Voice Settings Tuning

```python
from elevenlabs import VoiceSettings

# Stable narration (audiobook, podcast)
stable = VoiceSettings(stability=0.8, similarity_boost=0.75)

# Expressive performance (dramatic reading)
expressive = VoiceSettings(stability=0.3, similarity_boost=0.85)

# Balanced (general purpose)
balanced = VoiceSettings(stability=0.5, similarity_boost=0.5)

# Use in generation
audio = client.text_to_speech.convert(
    text="...",
    voice_id="...",
    model_id="eleven_multilingual_v2",
    voice_settings=stable,
)
```

| Parameter | Low (0.0-0.3) | Mid (0.4-0.6) | High (0.7-1.0) |
|-----------|---------------|---------------|-----------------|
| **Stability** | Varied, emotional | Balanced | Consistent, monotone |
| **Similarity Boost** | More variation | Balanced | Closer to original voice |

## Error Handling

```python
from elevenlabs.core import ApiError

try:
    audio = client.text_to_speech.convert(...)
except ApiError as e:
    if e.status_code == 401:
        print("Bad API key. Check ELEVENLABS_API_KEY env var.")
    elif e.status_code == 429:
        print("Rate limited. Wait and retry.")
    elif e.status_code == 422:
        print(f"Invalid params: {e.body}")
    else:
        raise
```

## Cost Awareness

- Characters are the billing unit. Every API call costs characters.
- **Preview short clips first** before generating long content.
- **Cache generated audio** — don't regenerate the same text.
- `eleven_flash_v2_5` is 50% cheaper than other models.
- Check usage: ElevenLabs dashboard or API subscription endpoint.

## Validate

Before delivering audio to the user:

- [ ] API key loaded from environment, never hardcoded
- [ ] Model selected matches content length and use case
- [ ] Voice selected and approved by user before generation
- [ ] For podcasts: script reviewed before generation (credits are non-refundable)
- [ ] Output format matches downstream requirements
- [ ] Audio file saved to a sensible location (not inside git-tracked source)
- [ ] File size and duration reported to user

## What Makes This Superpowered

- **4.2 The 90/10 Craft** — AI generates the audio; you craft the script and voice selection
- **4.4 Multi-Format Production** — Text content becomes audio content in one pass
- **4.1 Creative Courage** — Ship audio content that would have taken a recording studio
