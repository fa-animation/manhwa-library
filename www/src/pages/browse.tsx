import type { GetStaticProps } from 'next'
import Link from 'next/link'
import Head from 'next/head'
import { chakra, Flex, Stack, Heading, Text, useBreakpointValue, Button, Image, Container } from '@chakra-ui/react'
import api from '@/api'
import { MangaProps, MangaT } from '@/types'
import { SwipperSlider } from '@/components/swipper'

interface Random {
  data: MangaProps
}

interface BrowseProps {
  topManga: MangaT
  random: Random
  lastHomeManga: MangaT
}

export const getStaticProps: GetStaticProps = async () => {
  try {
    const { data: topManga } = await api.get('/v1/trending/manga/')
    const { data: random } = await api.get('/v1/manga/random')
    const { data: lastHomeManga } = await api.get('/v1/manga/?order_by=created_at&limit=12')
    return {
      props: {
        topManga,
        random,
        lastHomeManga
      },
      revalidate: 60000
    }
  } catch (error) {
    return {
      notFound: true
    }
  }
}

export default function PageBrowse({ topManga, random, lastHomeManga }: BrowseProps) {
  return (
    <>
      <Head>
        <title>Manga Library - Browse</title>
      </Head>
      <Container maxW={'6xl'}>
        <Stack pt={{ base: 27, md: 24 }} minH={'70vh'} direction={{ base: 'column-reverse', md: 'row' }} justifyContent={'space-between'}>
          <Flex align={'center'} justify={'center'}>
            <Stack spacing={6} w={'full'} maxW={'lg'}>
              <Heading
                fontSize={{ base: '3xl', md: '4xl', lg: '5xl' }}
                mt={useBreakpointValue({ base: '4px', md: '6px' })}
                noOfLines={2}
              >
                {random.data.title}
              </Heading>
              <Text color="brand.600" fontSize={{ base: 'lg', lg: 'xl' }} opacity={0.7}>
                <chakra.span bg={'purple.600'} rounded={'base'} color={'white'} p={1}>
                  {random.data.type_book}
                </chakra.span>
              </Text>
              <Text
                fontSize={{ base: 'md', lg: 'lg' }}
                color={'gray.400'}
                noOfLines={3}
                textAlign="justify"
              >
                {random.data.description}
              </Text>
              <Stack
                mt={2}
                direction={{ base: 'column', sm: 'row' }}
                mb={{ base: 4, md: 8 }}
                spacing={2}
                w="100%"
                justifyContent="flex-start"
              >
                <Button
                  as={Link}
                  display="inline-flex"
                  alignItems="center"
                  justifyContent="center"
                  w={'full'}
                  mb={{ base: 2, sm: 0 }}
                  size="lg"
                  cursor="pointer"
                  bg="gray.500"
                  href={`/manga/${random.data.slug}`}
                >
                  Details
                </Button>
              </Stack>
            </Stack>
          </Flex>
          <Flex align={'center'} justify={'center'}>
            <Image rounded={'base'} src={random.data.image} alt={random.data.title}  maxW={'350px'} maxH={'500px'}/>
          </Flex>
        </Stack>
      </Container>
      <Flex direction={'column'}>
        <SwipperSlider title="Top 10 manga" section={topManga?.data} />
        <SwipperSlider title="Latest manga" section={lastHomeManga?.data} />
      </Flex>
    </>
  )
}
