# Script JSON (storyboard source of truth)

Change this file first; regenerate afterwards.

```json
{
  "project": {
    "name": "{{PROJECT_NAME}}",
    "client": "{{CLIENT_NAME}}",
    "brand_style": "{{STYLE_TOKEN}}",
    "duration_seconds": {{DURATION_SECONDS}},
    "aspect_ratio": "{{ASPECT_RATIO}}",
    "platform": "{{PLATFORM}}",
    "engine": "{{ENGINE_MODE}}",
    "approval_required": true,
    "created": "{{DATE}}"
  },
  "scenes": [
    {
      "scene_id": "S01",
      "timecode": "00:00-00:05",
      "visual_hook": "{{VISUAL_HOOK}}",
      "generation_prompt": "{{GENERATION_PROMPT}}",
      "reference_image": "{{REFERENCE_FILE}}",
      "composition_layers": ["{{LAYER_1}}", "{{LAYER_2}}"],
      "voiceover_text": "{{VOICEOVER_TEXT}}",
      "voiceover_file": "{{VOICEOVER_FILE}}",
      "music_note": "{{MUSIC_NOTE}}",
      "captions": "{{CAPTION_TEXT}}"
    }
  ]
}
```

Rules: spoken words must fit the scene duration. One reference per subject. Placeholders in braces are replaced before use (numeric fields hold numbers).
