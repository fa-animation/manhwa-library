import {
  Box,
  Button,
  chakra,
  Container,
  Flex,
  Image,
  Stack,
  Text,
  useColorModeValue
} from '@chakra-ui/react'
import { BsBookHalf } from 'react-icons/bs'
import { Typewriter } from 'react-simple-typewriter'

const HeroPage = () => {
  return (
    <Box as="section">
      <Container maxW="6xl" p={{ base: 8, sm: 14 }}>
        <Stack
          direction={{ base: 'column', lg: 'row' }}
          pt={{ base: 28, md: 24 }}
          spacing={6}
          h="full"
        >
          <Stack flex={1} direction={'column'} mb={3}>
            <Box maxW="32rem">
              <chakra.h1 fontSize={{ base: '4xl', sm: '5xl' }} fontWeight="bold" maxW="700px">
                Korean&#39;s Best Comics Library
              </chakra.h1>
              <Text
                maxW="550px"
                fontSize={{ base: '2xl', sm: '3xl' }}
                color={useColorModeValue('gray.700', 'gray.200')}
                mb={3}
              >
                Find Your Dream book{' '}
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
                  <Typewriter words={['Here', 'Now', 'easy', '!']} loop cursor cursorStyle="|" />
                </chakra.span>
              </Text>
              <Stack w={{ base: '100%', sm: 'auto' }}>
                <Button
                  leftIcon={<BsBookHalf />}
                  w={'full'}
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
                  Browse Now Manhwa
                </Button>
              </Stack>
            </Box>
          </Stack>
          <Flex align={'center'} justify={'center'}>
            <Image
              alt={'Hero Image'}
              objectFit={'cover'}
              maxW={'250px'}
              loading="lazy"
              src={'/svg/book.svg'}
            />
          </Flex>
        </Stack>
      </Container>
    </Box>
  )
}

export default HeroPage
