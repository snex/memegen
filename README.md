# Memegen Maubot Plugin

A [Maubot](https://github.com/maubot/maubot) plugin that integrates with [memegen.link](https://memegen.link/) to generate memes directly in Matrix chat rooms.

## Overview

This plugin allows users to create and share memes using the powerful memegen.link API without leaving their Matrix chat. Simply type a command with a meme template and text, and the bot will generate and post the meme image to the room.

## Features

- **Template-based meme generation**: Use popular meme templates like Drake, Distracted Boyfriend, This is Fine, and hundreds more
- **Custom text overlay**: Add your own top and bottom text to any meme template
- **Instant sharing**: Generated memes are posted directly to the Matrix room
- **No external accounts required**: Uses the free memegen.link API
- **Wide template library**: Access to 100+ popular meme templates

## Installation

### Prerequisites

- A running [Maubot](https://github.com/maubot/maubot) instance
- A Matrix bot account

### Install the Plugin

1. **Download the plugin**: Clone this repo or download the provided `mbp` file.

1. **Upload to Maubot**: 
   - Open your Maubot management interface
   - Go to the "Plugins" section
   - Click "Upload" and select the `mbp` file

1. **Create an instance**:
   - Go to the "Instances" section
   - Click "Create new instance"
   - Select the memegen plugin
   - Assign it to your bot client

## Usage

Once the plugin is installed and the bot is in your Matrix room, you can start generating memes using these commands:

### Basic Usage

```
!meme <template> <top_text> <bottom_text>
```

### Examples

```
!meme distracted_boyfriend "Me" "New shiny framework" "My current project"
!meme thisisfine "Everything is on fire" "This is fine"
!meme buzz "Memes" "Memes everywhere"
```

### Available Templates

For a complete list of available templates, visit: https://api.memegen.link/templates/ or use the `!meme templates` command.

## API Reference

This plugin leverages the [memegen.link API](https://memegen.link/), which provides:

- **Stateless URL generation**: All meme information is encoded in the URL
- **Multiple image formats**: PNG, JPG, WebP, and GIF support
- **Text formatting**: Automatic text sizing and positioning
- **Special characters**: Support for emojis and special characters
- **Custom styling**: Background images and overlay options

## Development

### Project Structure

```
memegen/
├── memegen/               # Plugin source code
│   ├── __init__.py       # Main plugin implementation
│   └── ...               # Additional modules
├── maubot.yaml           # Plugin metadata
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

### Local Development

1. **Set up development environment**:
   ```bash
   pip install maubot
   pip install -r requirements.txt
   ```

2. **Test the plugin**:
   ```bash
   python -m memegen
   ```

3. **Build the plugin**:
   ```bash
   mbc build
   ```

### Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b my-new-feature`
3. Make your changes and add tests
4. Commit your changes: `git commit -am 'Add some feature'`
5. Push to the branch: `git push origin my-new-feature`
6. Submit a pull request

## Troubleshooting

### Common Issues

**Bot doesn't respond to commands**
- Check that the bot has joined the room
- Verify the command prefix in your configuration
- Ensure the bot has permission to send messages

**Meme generation fails**
- Check your internet connection
- Verify the template name is correct
- Try with simpler text (avoid special characters initially)

**Images don't load**
- Check if your Matrix server allows external image URLs
- Verify memegen.link is accessible from your server

### Debug Mode

Enable debug logging in your Maubot configuration to see detailed API interactions and error messages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [memegen.link](https://memegen.link/) for providing the free meme generation API
- [Maubot](https://github.com/maubot/maubot) for the excellent bot framework
- The Matrix community for creating an open communication platform

## Related Projects

- **Original memegen API**: https://github.com/jacebrowning/memegen
- **Maubot**: https://github.com/maubot/maubot
- **Matrix**: https://matrix.org/

---

*For more information about Maubot plugin development, visit the [official documentation](https://docs.mau.fi/maubot/).*
