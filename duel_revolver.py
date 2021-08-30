import Init
import duel

       if choice.content.lower() == 'bastard sword':
            embed_bastard_sword = discord.Embed(colour=discord.Colour.gold())
            embed_bastard_sword.set_author(name='Bastard Sword')
            embed_bastard_sword.set_image(url='https://www.theswordshop.co.uk/media/catalog/product/cache/4/image/650x/bc7d84fa039c363fb93c180fb5d13b79/s/h/sh2250.jpg')
            await ctx.send(embed=embed_bastard_sword)

        if choice.content.lower() == 'revolver':
            embed_revolver = discord.Embed(colour=discord.Colour.light_grey())
            embed_revolver.set_author(name='Old West Revolver')
            embed_revolver.set_image(url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/1858_Remington_Revolver_Replica.jpg/1024px-1858_Remington_Revolver_Replica.jpg')
            await ctx.send(embed=embed_revolver)
            await ctx.send("Cráááá! Is this really your choice?")
            try:
                confirm = await client.wait_for('message', timeout=20, check = confirmation)
            except asyncio.TimeoutError:
                return await ctx.send("Crááááá! Are you gonna choose or not? Maybe you are too scared to duel afterall. Call me again when you're determined to fight!")
            else:
                if confirm.content.lower() in ('no', 'i guess not', 'maybe', 'perhaps'):
                    await ctx.send("Crááááá! Then call me when you make up your mind. Don't waste my time! Crááááa!")
                if confirm.content.lower() in ('yes', 'i guess so', 'of course', 'sure'):
                    await ctx.send("Cráááááá! Very well, then. Now, it's " + str(ctx.author.mention) + "'s turn to choose!")
                    await options()
                    def check3(message3):
                        return message3.author == ctx.author and message3.content.lower() in ('gladius', 'revolver')
                    choice2 = await client.wait_for('message', check = check3)
                    if choice2.content.lower() == 'revolver':
                        await ctx.send(embed=embed_revolver)
                        await ctx.send('Cráááá! Is this really your choice?')
                        try:
                            confirm2 = await client.wait_for('message', timeout=20, check = confirmation2)
                        except asyncio.TimeoutError:
                            return await ctx.send("Crááááá! Are you gonna choose or not? Maybe you are too scared to duel afterall. Call me again when you're determined to fight!")
                        else:
                            if confirm2.content.lower() in ('no', 'i guess not', 'maybe', 'perhaps'):
                                await ctx.send('https://media3.giphy.com/media/YOkVtQYKrP900bWdoC/giphy.gif')
                                await ctx.send("You called me, challenged him to a duel, and now you can't even make up your mind?")
                                time.sleep(5)
                                await ctx.send("Call me when you make up your mind. Don't waste my time!")
                            if confirm2.content.lower() in ('yes', 'i guess so', 'of course', 'sure'):
                                await ctx.send("Cráááááá! Then... **KIIIIIIILL!** CRÁÁÁÁÁÁÁÁÁÁÁÁ!")
                                await ctx.send("https://media0.giphy.com/media/fKwpeyXg2rBPa/giphy.gif")
                                time.sleep(4)
                                await ctx.send(random.choice(start_pistol))
                                time.sleep(6)
                                await ctx.send("Ok, so we'll make things a bit different from the other weapons: I'll make a countdown and, when that countdown comes to an end, I'll post <:gunparrot:769189863890485289>")
                                await ctx.send("Whoever reacts to that emoji first shoots first and wins the duel")
                                time.sleep(10)
                                await ctx.send("Now, now. Are you ready? Crááááá!")
                                timer = await ctx.send(":clock1:")
                                time.sleep(1)
                                await timer.edit(content=':clock2:')
                                time.sleep(1)
                                await timer.edit(content=':clock3:')
                                time.sleep(1)
                                await timer.edit(content=':clock4:')
                                time.sleep(1)
                                await timer.edit(content=':clock5:')
                                time.sleep(1)
                                await timer.edit(content=':clock6:')
                                time.sleep(1)
                                await timer.edit(content=':clock7:')
                                time.sleep(1)
                                await timer.edit(content=':clock8:')
                                time.sleep(1)
                                await timer.edit(content=':clock9:')
                                time.sleep(1)
                                await timer.edit(content=':clock10:')
                                time.sleep(1)
                                await timer.edit(content=':clock11:')
                                time.sleep(1)
                                await timer.edit(content=':clock12:')
                                time.sleep(1)
                                await timer.add_reaction(':gunparrot:769189863890485289')
                                def players(reaction, player):
                                    return player == ctx.author and str(reaction.emoji) == '<:gunparrot:769189863890485289>' or player == opponent and str(reaction.emoji) == '<:gunparrot:769189863890485289>'
                                try:
                                    reaction, player = await client.wait_for('reaction_add', check=players)
                                except:
                                    pass
                                else:
                                    await ctx.send(str(player.mention) + " shoots first!")
                                    await ctx.send(random.choice(pistol))
                                    time.sleep(7)
                                    await ctx.send(str(player.mention) + ", you see your opponent fall on the ground. Probably with a few more minutes of life, but not enough life to shoot you back.")
                                    await ctx.send("You holster your gun, take out some paper and tobacco and make yourself a cigar, then smoke it")
                                    await ctx.send(random.choice(pistol_ending))
                                    time.sleep(8)
                                    await ctx.send("Then you start coughing unbridledly and spits out the cigar. Maybe it wasn't such a good idea. Crááááá!")
                                    time.sleep(3)
                                    await ctx.send("Well, it doesn't matter, anyway. Victory is yours! This ~~town~~ guild is yours! Crááááá!")
                    if choice2.content.lower() == 'gladius':
                        embed_gladius = discord.Embed(colour=discord.Colour.gold())
                        embed_gladius.set_author(name='Gladius(and scutum)')
                        embed_gladius.set_image(url='https://i.pinimg.com/originals/8d/00/ed/8d00ed984e8d8f3a92726d3345b7ec8c.jpg')
                        embed_gladius.add_field(name='Gladius', value="Sword used specially for thrusting. The scutum allows you to block attacks effectively, protecting your whole body", inline=False)
                        await ctx.send(embed=embed_gladius)
                        await ctx.send('Cráááá! Is this really your choice?')
                        try:
                            confirm2 = await client.wait_for('message', timeout=20, check = confirmation2)
                        except asyncio.TimeoutError:
                            return await ctx.send("Crááááá! Are you gonna choose or not? Maybe you are too scared to duel afterall. Call me again when you're determined to fight!")
                        else:
                            if confirm2.content.lower() in ('no', 'i guess not', 'maybe', 'perhaps'):
                                await ctx.send('https://media3.giphy.com/media/YOkVtQYKrP900bWdoC/giphy.gif')
                                await ctx.send("You called me, challenged him to a duel, and now you can't even make up your mind?")
                                time.sleep(5)
                                await ctx.send("Call me when you make up your mind. Don't waste my time!")
                            if confirm2.content.lower() in ('yes', 'i guess so', 'of course', 'sure'):
                                await ctx.send("Cráááááá! Then... **KIIIIIIILL!** CRÁÁÁÁÁÁÁÁÁÁÁÁ!")
                                await ctx.send("https://media0.giphy.com/media/fKwpeyXg2rBPa/giphy.gif")
                                time.sleep(4)
                                await ctx.send("As the duel begins, " + opponent.mention + " draws the chosen revolver and shoots at " + str(ctx.author.mention) + "!")
                                await ctx.send("https://media1.tenor.com/images/dd3e82521578de0eb6644525b5d09874/tenor.gif?itemid=5701823")
                                time.sleep(7)
                                await ctx.send("Cráááááá! " + str(ctx.author.mention) + ", you shouldn't bring a knife to a gun fight, dumbass! Crááááá! Perhaps you thought that the scutum was bulletproof? Cráááá!")
                                await ctx.send("Cráááá! Come on! Did you really think that the romans, in 24 A.D. would think about a shield that was effective against firearms from 19th Century? Not even the heavy armor from Medieval Ages could stand up for that! Cráááá! Stupid! Stupid! Cráááá!")
                                time.sleep(4)
                                await ctx.send("Congratulations, " + opponent.mention + "! You've won the duel, thanks to " + str(ctx.author.mention) + " stupidity(or innocence, I don't care)! Cráááááá!")
