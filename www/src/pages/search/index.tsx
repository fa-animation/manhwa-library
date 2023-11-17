import type { GetStaticProps } from 'next'
import { useState } from 'react'
import Head from 'next/head'
import {
  Box,
  Center,
  Flex,
  Heading,
  Image,
  Input,
  InputGroup,
  InputLeftElement,
  SimpleGrid,
  Text,
  chakra
} from '@chakra-ui/react'
import { AiOutlineSearch } from 'react-icons/ai'
import { MangaProps, MangaT } from '@/types'
import api from '@/api'
import { Card } from '@/components/card-manga'
import Container from '@/layout/container'

interface SearchProps {
  randomRecommed: MangaT
}

export const getStaticProps: GetStaticProps = async () => {
  try {
    const { data: randomRecommed } = await api.get('/v1/recommend/random?&limit=12')
    return {
      props: {
        randomRecommed
      },
      revalidate: 20
    }
  } catch (error) {
    return {
      notFound: true
    }
  }
}

let timeOutSearch: any

interface GridProps {
  children: React.ReactNode
  title?: string
}

const ContainerGrid = ({ title, children }: GridProps) => (
  <Box
    maxW="7xl"
    mx="auto"
    px={{ base: '4', md: '8', lg: '12' }}
    py={{ base: '6', md: '8', lg: '12' }}
  >
    <Heading mb={5}>{title}</Heading>
    <SimpleGrid
      columns={[2, 4, 6]}
      columnGap={{ base: '4', md: '6' }}
      rowGap={{ base: '8', md: '10' }}
    >
      {children}
    </SimpleGrid>
  </Box>
)

export default function Search({ randomRecommed }: SearchProps) {
  const [termSearch, setTermSearch] = useState<string | undefined>('')
  const [loading, setLoading] = useState<boolean>(false)
  const [results, setResults] = useState<MangaT>()
  function handleTermSearch() {
    setLoading(true)
    clearTimeout(timeOutSearch)
    timeOutSearch = setTimeout(async () => {
      const { data } = await api.get(`/v1/search/?name=${termSearch}`)
      setResults({ ...data })
      setLoading(false)
    }, 700)
  }
  return (
    <>
      <Head>
        <title>Manga Library - search</title>
      </Head>
      <Container>
        <Box
          bg="gray.700"
          p={10}
          mt={{ base: 27, md: 24 }}
          rounded={'base'}
          px={{ base: '4', md: '8', lg: '12' }}
          py={{ base: '6', md: '8', lg: '12' }}
        >
          <Box textAlign={'center'} mb={5}>
            <Heading>Find the perfect manga for you</Heading>
          </Box>
          <Box>
            <InputGroup size="lg" color="gray.300">
              <InputLeftElement pointerEvents="none" children={<AiOutlineSearch color="white" />} />
              <Input
                onKeyUp={() => handleTermSearch()}
                onChange={({ target }) => setTermSearch(target.value)}
                type="text"
                placeholder="Search manga..."
              />
            </InputGroup>
          </Box>
        </Box>
      </Container>
      {loading ? (
        <Flex minH={'50vh'} justify={'center'} align={'center'} textAlign={'center'}>
          <Image
            w={250}
            h={250}
            alt="banana dance"
            src="https://i.pinimg.com/originals/f3/0e/21/f30e21da146bd3501555eec943a8898e.gif"
          />
        </Flex>
      ) : results ? (
        <>
          {results.data.length ? (
            <ContainerGrid title={`Resultados (${results.data.length})`}>
              {results.data.map((data: MangaProps) => (
                <Card
                  key={data.id}
                  image={data.image}
                  ratting={data.ratting}
                  slug={data.slug}
                  title={data.title}
                  type_book={data.type_book}
                />
              ))}
            </ContainerGrid>
          ) : (
            <Flex minH={'50vh'} justify={'center'} align={'center'}>
              <Box p={4} textAlign={'center'}>
                <Center>
                  <Image
                    w="full"
                    rounded="lg"
                    maxW="600px"
                    loading="lazy"
                    src="https://media.tenor.com/XaDOC9Gvu6UAAAAi/ui-shigure-shigure-ui.gif"
                    alt="Nenhum resultado"
                  />
                </Center>
                <Text fontSize={{ base: '2xl', sm: '3xl' }}>
                  Nenhum resultado para &quot;
                  <chakra.span
                    position={'relative'}
                    _after={{
                      content: "''",
                      width: 'full',
                      height: '10%',
                      position: 'absolute',
                      bottom: 1,
                      left: 0,
                      bg: 'orange.400',
                      zIndex: 1000
                    }}
                  >
                    {termSearch}
                  </chakra.span>
                  &quot;
                </Text>
              </Box>
            </Flex>
          )}
        </>
      ) : (
        <ContainerGrid title="Also read">
          {randomRecommed.data.map((data: MangaProps) => (
            <Card
              key={data.id}
              image={data.image}
              ratting={data.ratting}
              slug={data.slug}
              title={data.title}
              type_book={data.type_book}
            />
          ))}
        </ContainerGrid>
      )}
    </>
  )
}
