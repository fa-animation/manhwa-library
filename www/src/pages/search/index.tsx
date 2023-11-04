import type { GetStaticProps } from 'next'
import { useState } from 'react'
import Head from 'next/head'
import {
  Box,
  Center,
  Heading,
  Image,
  Input,
  InputGroup,
  InputLeftElement,
  SimpleGrid
} from '@chakra-ui/react'
import { AiOutlineSearch } from 'react-icons/ai'
import { MangaProps, MangaT } from '@/types'
import api from '@/api'
import { Card } from '@/components/card-manga'
import Container from '@/layout/container'
import { title } from 'process'

interface SearchProps {
  topManga: MangaT
}

export const getStaticProps: GetStaticProps = async () => {
  try {
    const { data: topManga } = await api.get('/v1/trending/manga/')
    return {
      props: {
        topManga
      },
      revalidate: 60000
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

export default function Search({ topManga }: SearchProps) {
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
        <h3>Buscando...</h3>
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
            <Box minH={'100vh'} textAlign={'center'}>
              <strong>Nenhum resultado para {termSearch}</strong>
            </Box>
          )}
        </>
      ) : (
        <ContainerGrid title="Top manga">
          {topManga.data.map((data: MangaProps) => (
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
