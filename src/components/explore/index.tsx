import { chakra, Box, Button, Flex } from '@chakra-ui/react'
import Container from '@/layout/container'

const Explore = () => {
  return (
    <Box bg={'purple.600'}>
      <Container p={7}>
        <Flex direction="column" align="center" justify="space-between">
          <Box maxW="32rem">
            <chakra.h1
              mb={4}
              fontWeight={'bold'}
              textStyle="heading"
              fontSize={{ base: '2rem', md: '2.5rem' }}
            >
              Explore more Books
            </chakra.h1>
            <Button
              width="100%"
              mt={{ base: '6', md: 0 }}
              color="gray.800"
              justifyContent="center"
              display="inline-flex"
              alignItems="center"
              fontWeight="bold"
              shadow="md"
              bg="white"
              px="24px"
              h="56px"
              rounded="lg"
              fontSize="md"
              boxShadow="rgba(0, 0, 0.3)"
            >
              Browse Manhwa
            </Button>
          </Box>
          {/* <Image src="https://manhwa-library.netlify.app/asset/undraw_reading_time_re_phf7.svg" alt="teste" /> */}
        </Flex>
      </Container>
    </Box>
  )
}

export default Explore
