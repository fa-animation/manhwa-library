import { Heading, Flex, Box, useColorModeValue, Text } from '@chakra-ui/react'
import Head from 'next/head'
import NavHero from '@/layout/header'
import HeroPage from '@/layout/HeroPage'

export default function Home() {
  return (
    <>
      <Head>
        <title>Manhwa Library</title>
      </Head>
      <NavHero />
      <HeroPage />
      <Flex minHeight={'100vh'} justify={'center'} align={'center'}>
        <Box
          bg={useColorModeValue('gray.300', 'gray.700')}
          p={10}
          rounded={'base'}
          textAlign={'center'}
        >
          <Heading>Manhwa Library</Heading>
          <Text>List manhwa alls</Text>
        </Box>
      </Flex>
    </>
  )
}
