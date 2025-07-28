# ChatCompletionRequestStreamAudio

Parameters for audio output. Required when audio output is requested with modalities: ["audio"].


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `format_`                                                                                            | [Optional[models.ChatCompletionRequestStreamFormat]](../models/chatcompletionrequeststreamformat.md) | :heavy_minus_sign:                                                                                   | Specifies the output audio format. Must be one of wav, mp3, flac, opus, or pcm16.                    |
| `voice`                                                                                              | [Optional[models.ChatCompletionRequestStreamVoice]](../models/chatcompletionrequeststreamvoice.md)   | :heavy_minus_sign:                                                                                   | Specifies the voice type. Supported voices are alloy, echo, fable, onyx, nova, and shimmer.          |