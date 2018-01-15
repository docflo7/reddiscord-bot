from discord.ext import commands
import discord
import math
import urllib.request as web
import json
from collections import namedtuple
import tools
import auth


class Osu():
    def __init__(self, client):
        self.client = client

    async def getBeatmap(self, ctx, url):
        """This function will get infos on a beatmap from its url, using the api.
        The informations are returned as an oject containing the beatmap's properties"""
        osu_domain = "osu.ppy.sh/"
        start = url.find(osu_domain) + len(osu_domain)
        type = url[start:start + 2]
        bmid = None
        if type == "s/":
            bmid = url[start + 2:]
        elif type == "b/":
            end = url.find("&m")
            if end == -1:
                bmid = url[start + 2:]
            else:
                bmid = url[start + 2:end]
        elif type == "p/":
            start = url.find("?b")
            end = url.find("&m")
            bmid = url[start + 3:end]

        print(bmid)
        req = web.Request("https://osu.ppy.sh/api/get_beatmaps?m=2&a=1&k=" + auth.osu_api_token + "&b=" + bmid)
        res = web.urlopen(req).read()[1:-1]
        try:
            asobject = json.loads(res, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            return asobject
        except:
            return None

    def computeCtbPp(self, map, p_acc=None, p_combo=None, p_miss=None):
        """This function calculates the pp value for a given ctb map.
        The default calculated value is for SS, but play datas can be set"""
        # These are the map settings
        sr = float(map.difficultyrating)
        ar = float(map.diff_approach)
        maxCombo = float(map.max_combo)

        # These are the play settings
        acc = p_acc if p_acc is not None else 100
        misses = p_miss if p_miss is not None else 0
        playerCombo = p_combo if p_combo is not None else maxCombo

        # Check that the user values are correct
        if acc < 0 or acc > 100:
            return None
        if playerCombo < 0 or playerCombo > maxCombo:
            return None
        if misses < 0:
            return None

        # This formula is from https://pakachan.github.io/osustuff/ppcalculator.html
        # and from https://github.com/ppy/osu-performance
        final = (((5 * sr / 0.0049) - 4) ** 2) / 100000
        lenparam1 = 1 if maxCombo > 3000 else maxCombo / 3000
        lenparam2 = 0 if maxCombo < 3000 else math.log10(maxCombo / 3000) * 0.5
        lengthbonus = (0.95 + 0.4 * lenparam1 + lenparam2)
        final *= lengthbonus
        final *= (0.97 ** misses)
        final *= ((playerCombo / maxCombo) ** 0.8)
        if ar > 9:
            final *= (1 + 0.1 * (ar - 9.0))
        if ar < 8:
            final *= (1 + 0.025 * (8.0 - ar))
        final *= (acc / 100) ** 5.5
        pp = round((100 * final) / 100, 2)

        return pp

    @commands.command(pass_context=True)
    async def ctbpp(self, ctx, url, *play_infos):
        """Find out how much pp your last CtB choke was worth

        ctbpp <url> <acc> <combo> <misses>
        If you don't specify any play infos, standard values will be given.
        You can either give full specifications (acc, combo, misses) or acc only.
        """
        map = await self.getBeatmap(self, url)
        if map is None:
            await self.client.say("Something went wrong.")
            return
        mes_title = map.artist + " - " + map.title + " [" + map.version + "]"
        mes_descr1 = f"AR{map.diff_approach} CS{map.diff_size} OD{map.diff_overall} HP{map.diff_drain}\n"
        mes_descr2 = f"Difficulty : {str(round(float(map.difficultyrating), 2))}★ | BPM : {map.bpm}\n"
        length = str(int(int(map.hit_length) / 60)) + ":" + str(int(map.hit_length) % 60)
        mes_descr3 = f"Length : {length} | Max Combo : {map.max_combo}\n"
        message = discord.Embed(title=mes_title, colour=0xdc98a4, description=mes_descr1 + mes_descr2 + mes_descr3)
        message.set_footer(text="powered by docflo7")
        message.set_thumbnail(url="https://b.ppy.sh/thumb/" + map.beatmapset_id + ".jpg")
        len_infos = len(play_infos)
        if len_infos == 0:
            # no args : basic values
            pp95 = self.computeCtbPp(map, 95)
            pp98 = self.computeCtbPp(map, 98)
            pp99 = self.computeCtbPp( map, 99)
            pp100 = self.computeCtbPp(map)
            message.add_field(name="95%", value=str(pp95) + "pp")
            message.add_field(name="98%", value=str(pp98) + "pp")
            message.add_field(name="99%", value=str(pp99) + "pp")
            message.add_field(name="100%", value=str(pp100) + "pp")
        elif len_infos == 1:
            # acc only
            try:
                acc = float(play_infos[0])
                pp = self.computeCtbPp(map, acc)
                message.add_field(name=str(acc) + "%", value=str(pp) + "pp")
            except ValueError:
                await self.client.say("...")
                return
        elif len_infos == 2:
            # wrong arg count
            await self.client.say("There's nothing I can do with that number of arguments.")
            return
        else:
            # 3 args (more ignored)
            try:
                acc = float(play_infos[0])
                combo = float(play_infos[1])
                miss = float(play_infos[2])
                pp = self.computeCtbPp(map, acc, combo, miss)
                message.add_field(name=str(acc) + "% " + str(combo) + "x " + str(miss) + "miss", value=str(pp) + "pp")
            except ValueError:
                await self.client.say("...")
                return
        await self.client.send_message(ctx.message.channel, content=None, embed=message)


def setup(client):
    client.add_cog(Osu(client))
