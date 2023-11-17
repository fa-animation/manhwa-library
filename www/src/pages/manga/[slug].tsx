import { GetStaticPaths, GetStaticProps } from 'next'
import Head from 'next/head'
import {
  Box,
  Container,
  Heading,
  Image,
  SimpleGrid,
  Text,
  AspectRatio,
  Tabs,
  TabList,
  Tab,
  TabPanels,
  TabPanel,
  Flex
} from '@chakra-ui/react'
import api from '@/api/'
import { MangaProps, MangaT } from '@/types'
import { Text as ChakraText } from '@/components/choose-Library/typography'
import { SwipperSlider } from '@/components/swipper'

interface MangaAxios {
  data: MangaProps
}
interface MangaData {
  mangaDetails: MangaProps
  rand: MangaT
}

export const getStaticPaths: GetStaticPaths = async () => {
  return {
    paths: [],
    fallback: 'blocking'
  }
}

export const getStaticProps: GetStaticProps = async (context: any) => {
  const { slug } = context.params
  try {
    // const { data } = await api.get<MangaAxios>()
    const [{ data }, { data: rand }] = await Promise.all([
      api.get(`/v1/manga/${slug}/detail/`),
      api.get('/v1/recommend/random?&limit=12')
    ])
    const mangaDetails = {
      id: data.data.id,
      title: data.data.title,
      description: data.data.description,
      image: data.data.image,
      status_progress: data.data.status_progress
    }
    return {
      props: {
        mangaDetails,
        rand
      },
      revalidate: 20
    }
  } catch (error) {
    return {
      notFound: true
    }
  }
}

export default function MangaDetail({ mangaDetails, rand }: MangaData) {
  return (
    <>
      <Head>
        <title>{`${mangaDetails.title}`}</title>
      </Head>
      <Container maxW="6xl">
        <SimpleGrid
          columns={{ base: 1, md: 2 }}
          paddingX={{ base: 2, md: 5, xl: 100 }}
          pt={{ base: 27, md: 24 }}
          mt={10}
        >
          <Box maxW="20rem">
            <AspectRatio
              ratio={4 / 3}
              _before={{
                content: "''",
                display: 'block',
                height: '0px',
                paddingBottom: '133.333%'
              }}
            >
              <Image
                borderRadius={10}
                src={mangaDetails.image}
                width={{ base: '90%' }}
                objectFit={'cover'}
                alt={mangaDetails.title}
              />
            </AspectRatio>
          </Box>
          <Box marginY={{ base: 5 }}>
            <Heading as="h1">{mangaDetails.title}</Heading>

            <Box>
              <Heading as={'h3'} fontSize={'4xl'} marginY={2}>
                Overview
              </Heading>
              <Tabs variant="enclosed">
                <TabList>
                  <Tab>Description</Tab>
                  <Tab>More info</Tab>
                </TabList>
                <TabPanels>
                  <TabPanel>
                    <Text fontSize="md" textAlign={'justify'}>
                      {mangaDetails.description}
                    </Text>
                  </TabPanel>
                  <TabPanel>
                    <Box>
                      <Text fontSize="md">{mangaDetails.status_progress}</Text>
                    </Box>
                  </TabPanel>
                </TabPanels>
              </Tabs>
            </Box>
          </Box>
        </SimpleGrid>

        <Flex flexDirection="column" width="full" align="center" justifyContent="center">
          <Flex
            justify={'center'}
            width="94%"
            maxWidth="900px"
            borderRadius="sm"
            textAlign="center"
            mt={10}
          >
            <Image
              w="full"
              rounded="lg"
              maxW="300px"
              loading="lazy"
              src="https://epice-app.vercel.app/img/svg/undraw_warning_cyit.svg"
              alt="s"
            />
          </Flex>
          <ChakraText mt={10}>Under construction</ChakraText>
        </Flex>

        <SwipperSlider title="Explore more" section={rand?.data} />
      </Container>
    </>
  )
}
