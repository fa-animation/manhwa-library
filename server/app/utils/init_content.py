import uuid

CONTENT = [
    {
      "title": "Solo leveling",
      "slug": None,
      "description": "Solo Leveling, também traduzido alternativamente como Only I Level Up, é uma web novel sul-coreana escrita por Chugong.",
      "status_progress": "Ongoing",
      "ratting": 4.5,
      "image": "https://m.media-amazon.com/images/I/71gnuYUWeTL._AC_UF1000,1000_QL80_.jpg",
      "view_count": 100,
      "year_published": "2022",
      "author": "Chugong",
      "artist": "DUBU",
      "type_book": "manhwa"
      # "created_at": "2023-10-21T18:08:47"
    },
    {
      "title": "School Back",
      "slug": None,
      "description": "Fushimi é a zeladora de uma escola secundária. Ela é alta. Ela trabalha duro. Ela gosta de café enlatado. E ela fala com a gente na distância certa. No momento estou sofrendo com pessoas que se acham adultas. Estou me perguntando que tipo de adulto eu deveria ser agora. Se você se sente assim, por favor, venha ver a Fushimi. Talvez você se sinta aliviado ou tenha um insight.",
      "status_progress": "Ongoing",
      "ratting": 4.5,
      "image": "https://img.mangaschan.com/uploads/manga-images/s/school-back/thumbnail.webp",
      "view_count": 100,
      "year_published": "2023",
      "author": "Onodera Kokoro",
      "artist": "Onodera Kokoro",
      "type_book": "manga"
      # "created_at": "2023-10-21T19:04:49"
    },
    {
      "title": "Assassin’s Creed IV: The Forgotten Temple",
      "slug": None,
      "description": "Edward Kenway recebe uma pista sobre a lenda do templo perdido. Desta vez, não como um pirata, mas como um assassino, rumo ao mar novamente. “Eu sou Edward Kenway? O que está acontecendo…?” Noah Kim, que segue as memórias de seu ancestral distante, Edward Kenway, através do Animus. A sequência de começa no palco do Mar da China Meridional, no sudeste da Ásia, no século XVIII!",
      "status_progress": "Ongoing",
      "ratting": 4.5,
      "image": "https://img.mangaschan.com/uploads/manga-images/a/assassins-creed-iv-the-forgotten-temple/thumbnail.webp",
      "view_count": 100,
      "year_published": "2023",
      "author": "Arc, Shyatan e Ubisoft",
      "artist": "Tabii",
      "type_book": "manhwa"
      # "created_at": "2023-10-21T19:17:06"
    },
    {
      "title": "Silly Little Abella",
      "slug": None,
      "description": "Seokyung Kang é a professora de matemática mais requisitada na cidade de maior prestígio do país. Um dia, ela é atropelada por um caminhão e acorda como Abella, uma linda, mas intelectualmente desafiada filha do arquiduque. Antes que ela pudesse entender o que está acontecendo, ela tem que se casar com o “monstro”, um príncipe imperial corcunda que tem queimaduras por todo o corpo! Mas o chamado “monstro” acaba por ser um bonitão e um menino bonito!",
      "status_progress": "Ongoing",
      "ratting": 8.5,
      "image": "https://img.mangaschan.com/uploads/manga-images/s/silly-little-abella/thumbnail.jpg",
      "view_count": 900,
      "year_published": "2023",
      "author": "Park Seung-Ah",
      "artist": "Park Seung-Ah",
      "type_book": "manhwa"
      # "created_at": "2023-10-21T19:24:48"
    },
     {
      "title": "The Beginning After The End",
      "slug": None,
      "description": "Rei Grey conquistou força, riquezas e prestígio sem iguais em um mundo governado pela habilidade marcial. Entretanto, a solidão acompanha de perto aqueles de grande poder. Por detrás da máscara de um glorioso e poderoso rei, reside a casca vazia de um homem destituído de propósito e vontade. Renascido em um novo mundo repleto de magia e monstros, o Rei Grey terá a chance de refazer sua vida.",
      "status_progress": "Ongoing",
      "ratting": 8.8,
      "image": "https://d30womf5coomej.cloudfront.net/sa/3c/3f10a4c3-686f-4aa1-af71-22bfc021ccd0_z.jpg",
      "view_count": 2000,
      "year_published": "2018",
      "author": "TurtleMe",
      "artist": "Fuyuki23",
      "type_book": "manhwa"
    },
     {
      "title": "Swordmaster’s Youngest Son",
      "slug": None,
      "description": "Jin Runcandel era o filho mais novo do melhor clã de espadachins do continente, e a criança menos talentosa em toda a história do clã. Depois de ter sido expulso de forma patética, tendo seu fim como um inútil, obteve outra chance. “Como quer usar este poder?” “Eu quero usar este poder para mim mesmo.”",
      "status_progress": "Ongoing",
      "ratting": 7.25,
      "image": "https://img.mangaschan.com/uploads/manga-images/s/swordmasters-youngest-son/thumbnail.jpg",
      "view_count": 1000,
      "year_published": "2022",
      "author": "Azi",
      "artist": "Lee Je-Woo",
      "type_book": "manhwa"
    },
    {
      "title": "Berserk",
      "slug": None,
      "description": "Guts, um ex-mercenário agora conhecido como o “Espadachim Negro”, está em busca de vingança. Depois de uma infância tumultuada, ele finalmente encontra alguém que respeita e acredita que pode confiar, apenas para ver tudo desmoronar quando essa pessoa tira tudo que é importante para Guts com o propósito de realizar seus próprios desejos.",
      "status_progress": "Ongoing",
      "ratting": 9,
      "image": "https://i2.wp.com/mangaschan.net/wp-content/uploads/Berserk-Mangaschan.jpg",
      "view_count": 1500,
      "year_published": "1989",
      "author": "MIURA Kentaro",
      "artist": "MIURA Kentaro, Studio Gaga",
      "type_book": "manga"
    },
    {
      "title": "One Punch Man",
      "slug": None,
      "description": "Depois de treinar rigorosamente por três anos, o Saitama comum ganhou uma força imensa que lhe permite derrubar qualquer pessoa e qualquer coisa com apenas um soco. Ele decide colocar sua nova habilidade em bom uso, tornando-se um herói. No entanto, ele rapidamente fica entediado com a facilidade de derrotar monstros e quer que alguém lhe dê um desafio para trazer de volta a centelha de ser um herói.",
      "status_progress": "Ongoing",
      "ratting": 9.1,
      "image": "https://mangaschan.net/wp-content/uploads/One-Punch-Man-Mangaschan.webp",
      "view_count": 2500,
      "year_published": "2012",
      "author": "ONE",
      "artist": "MURATA Yuusuke",
      "type_book": "manga"
    }
  ]

# Para adicioanar tem que comentar os mangas antigos