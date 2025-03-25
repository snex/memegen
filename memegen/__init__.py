import aiohttp
import asyncio
import re
import textwrap
import urllib

from mautrix.types import TextMessageEventContent, MediaMessageEventContent, MessageType, Format, ImageInfo, ContentURI, ThumbnailInfo

from maubot import Plugin, MessageEvent
from maubot.handlers import command

class Memegen(Plugin):
    async def start(self) -> None:
        await super().start()
        self.meme_url = 'https://api.memegen.link'
        self.help_text = """How to use memegen:
        !meme help - show this help text
        !meme templates - get list of templates
        !meme help [template] - show details for specific template
        !meme [template] [text line 1];[text line 2];[text line 3];[alt style]
        Adjust accordingly depending on the number of lines the template accepts."""
        res = await self.http.get(self.meme_url + '/templates')
        templates_list = await res.json()
        self.templates = {item['id']:item for item in templates_list}
        self.templates_help = "List of available templates:\n" + "\n".join(list(map(lambda x: f"{x['id']} - {x['name']}\n--number of text lines: {x['lines']}\n--alt styles: {x['styles']}", templates_list)))

    async def send_help(self, evt: MessageEvent, template=""):
        dm = await self.client.create_room(invitees = [evt.sender], is_direct = True)
        await self.client.join_room(dm)
        if template in self.templates:
            template_help = f"""Template '{template}':
            Meme: {self.templates[template]['name']}
            Number of text lines: {self.templates[template]['lines']}
            Alt styles available: {self.templates[template]['styles']}"""
            await self.client.send_notice(dm, template_help)
        else:
            await self.client.send_notice(dm, self.help_text)

    async def get_templates(self, evt: MessageEvent):
        dm = await self.client.create_room(invitees = [evt.sender], is_direct = True)
        await self.client.join_room(dm)
        await self.client.send_notice(dm, self.templates_help)

    async def make_meme(self, evt: MessageEvent, template_name, text):
        if template_name in self.templates:
            await evt.react("🤖")
            image = None
            template = self.templates[template_name]
            lines = int(template['lines'])
            styles = template['styles']
            text = text.replace('_', '__')
            text = text.replace('-', '--')
            text = text.replace("\n", '~n')
            text = text.replace('?', '~q')
            text = text.replace('&', '~a')
            text = text.replace('%', '~p')
            text = text.replace('#', '~h')
            text = text.replace('/', '~s')
            text = text.replace('\\', '~b')
            text = text.replace('"', '\'\'')
            text = text.replace(' ', '_')
            text_arr = text.split(';', lines + 1)
            if len(text_arr) <= lines:
                res = await self.http.get(self.meme_url + '/images/' + template_name + '/' + '/'.join(text_arr) + '.png')
                image = await res.read()
            else:
                if text_arr[-1] in styles:
                    res = await self.http.get(self.meme_url + '/images/' + template_name + '/' + '/'.join(text_arr) + '.png' + f"?style={text_arr[-1]}")
                    image = await res.read()
                else:
                    await evt.respond(f"Alt style '{text_arr[-1]}' not found. Try !meme help {template_name}")
                    return
            mxc_uri = await self.client.upload_media(image, mime_type="image/png", filename="meme.png")
            content = MediaMessageEventContent(
                    msgtype=MessageType.IMAGE,
                    body=f"meme.png",
                    url=ContentURI(f"{mxc_uri}"),
                    info=ImageInfo(
                        mimetype='image/png',
                        size=len(image),
                        thumbnail_url=ContentURI(f"{mxc_uri}"),
                        thumbnail_info=ThumbnailInfo(
                            mimetype="image/png",
                            size=len(image)
                            )
                        )
                    )
            await evt.respond(content)
        else:
            await evt.respond(f"Template '{template}' not found. For a list of available templates, do !meme templates")

    @command.new()
    @command.argument("message", pass_raw=True, required=True)
    async def meme(self, evt: MessageEvent, message: str = "") -> None:
        m = re.search(r'^([^\s]*)\s*(.*)', message)
        if m:
            command = m.group(1)
            parameters = m.group(2)
            if command.lower() == 'help':
                await self.send_help(evt, parameters)
            elif command.lower() == 'templates':
                await self.get_templates(evt)
            else:
                await self.make_meme(evt, command, parameters)
        else:
            await self.send_help(evt)
