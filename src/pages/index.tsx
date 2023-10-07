import { Heading, Flex, Box, useColorModeValue, Text } from '@chakra-ui/react'
import Head from 'next/head'
import NavHero from '@/layout/header'

export default function Home() {
  return (
    <>
      <Head>
        <title>Template simples</title>
      </Head>
      <NavHero />
      <Flex minHeight={'100vh'} justify={'center'} align={'center'}>
        <Box
          bg={useColorModeValue('gray.300', 'gray.700')}
          p={10}
          rounded={'base'}
          textAlign={'center'}
        >
          <Heading>Simples Template</Heading>
          <Text>Template Nextjs with Chakra and Typescript</Text>
        </Box>
      </Flex>
    </>
  )
}
