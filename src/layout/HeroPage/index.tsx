import { Box, Button, chakra, Container, Flex, Image, Stack, Text } from '@chakra-ui/react'
import { BsBookHalf } from 'react-icons/bs'
import { Typewriter } from 'react-simple-typewriter'

const HeroPage = () => {
  return (
    <Box as="section" bg={'teal.700'} color={'white'}>
      <Container maxW="6xl" p={{ base: 8, sm: 14 }}>
        <Stack direction="column" pt={{ base: 17, md: 24 }} spacing={6} h="full">
          <Flex direction={'column'} alignItems={'center'} textAlign={'center'}>
            <chakra.h1
              fontSize={{ base: '4xl', sm: '5xl' }}
              fontWeight="bold"
              textAlign="center"
              maxW="700px"
            >
              Korean&#39;s Best Comics Library
            </chakra.h1>
            <Text maxW="550px" fontSize={{ base: '2xl', sm: '3xl' }} textAlign="center" color="gray.200">
              Find Your Dream book{' '}
              <chakra.span 
                position={'relative'}
                _after={{
                  content: '\'\'',
                  width: 'full',
                  height: '10%',
                  position: 'absolute',
                  bottom: 1,
                  left: 0,
                  bg: 'orange.400',
                  zIndex: 1000
                }}
              >
                <Typewriter
                  words={['Here', 'Now', 'easy', '!']}
                  loop
                  cursor
                  cursorStyle="|"
                />
              </chakra.span>
            </Text>
            <Stack w={{ base: '100%', sm: 'auto' }} justify={'center'} mt={4}>
              <Button
                leftIcon={<BsBookHalf />}
                maxW={'500px'}
                w={'257px'}
                bg={'purple.700'}
                rounded="md"
                size="lg"
                height="3.5rem"
                _hover={{
                  bg: 'purple.600'
                }}
                fontSize="1.2rem"
                color={'white'}
              >
                Browse Manhwa
              </Button>
          </Stack>
          </Flex>
          <Flex align={'center'} justify={'center'}>
            <Image
              alt={'Hero Image'}
              objectFit={'cover'}
              maxW={'250px'}
              loading="lazy"
              src={
                '/svg/book.svg'
              }
            />
          </Flex>
        </Stack>
      </Container>
    </Box>
  )
}

export default HeroPage
