import Init

@client.command()
async def anime(ctx):
    weeb = ['https://i.redd.it/aetat70iewg21.jpg', 'https://soumo.eu/wp-content/uploads/2018/03/29654/a060ef2c1f8d446835f0c61a3c843b63.jpg',
            'https://pbs.twimg.com/media/EQtDUe5U0AADKVZ.jpg',
            'https://pbs.twimg.com/media/EQw82i2WAAAtH2-.jpg', 'https://en.1jux.net/scale_images/531630_b.jpg',
            'https://images7.memedroid.com/images/UPLOADED827/5d4c714d24b52.jpeg', 'https://i.kym-cdn.com/photos/images/original/001/478/697/8fb.jpg',
            'https://img.memecdn.com/fucking-weeb_o_7257621.jpg', 'https://pics.awwmemes.com/you-filthy-weeb-68917777.png', 'https://i.redd.it/a554u1fjt0w21.jpg']
    await ctx.send(random.choice(weeb))

@client.command()
async def birb(ctx):
    birddie = ['https://i.makeagif.com/media/10-01-2015/GvvVpE.gif', 'https://i.imgur.com/DPL2b0x.gif', 'https://imgflip.com/gif/26y0vr',
               'https://media1.tenor.com/images/c97bc08b3be4f4a759887c17c2c2a6a9/tenor.gif?itemid=14420649',
               'https://i.pinimg.com/564x/fe/11/2d/fe112d3cb79ed4eae022f883896148b3.jpg',
               'https://i.pinimg.com/originals/cb/c9/de/cbc9de7ca1b11006f795902cd6eb9f70.gif',
               'https://media1.tenor.com/images/7691902de8c681704f919ce135d6a37d/tenor.gif',
               'https://i.gifer.com/ShnJ.gif', 'https://media1.tenor.com/images/9af40235e80225d68eaac592aeb74b77/tenor.gif?itemid=3521999',
               'https://media.tenor.com/images/ece9f2862eb4a6ad3db987921f20495a/tenor.gif',
               'https://33.media.tumblr.com/df2bb295c3130b6701bda356e6000786/tumblr_najgugzKzp1r3p42ko3_500.gif', 'https://media1.tenor.com/images/73f61ca3bcfa22a5d0715abfa5e5217c/tenor.gif?itemid=15053628',
               'https://64.media.tumblr.com/9acc969bdaccc0d9e7dc570a0976a19b/tumblr_inline_osok184KPD1rtwwto_540.jpg', 'https://64.media.tumblr.com/b0e9f94be8324b41cb93801cde169b03/tumblr_inline_osok2vDyCb1rtwwto_540.jpg',
               'https://ih1.redbubble.net/image.862136152.9198/flat,750x,075,f-pad,750x1000,f8f8f8.u7.jpg']
    await ctx.send(random.choice(birddie))
    

@client.command()
async def die(ctx):
    ded = ['https://i.pinimg.com/originals/f6/11/65/f61165e9dc871c601b8b63497f842a3b.gif', 'https://i.pinimg.com/originals/94/a6/fd/94a6fd771308741ef5d5a8bffdc56715.gif',
           'https://thumbs.gfycat.com/DecisiveLividJavalina-size_restricted.gif', 'https://media.tenor.com/images/4d200ccf5664bf44d64036224d52a3a1/tenor.gif']
    await ctx.send(random.choice(ded))

