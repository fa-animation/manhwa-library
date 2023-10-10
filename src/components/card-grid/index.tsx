import { Box, Container, SimpleGrid, chakra } from '@chakra-ui/react'

const CardGrid = () => {
  return (
    <Box as="section" bg="teal.600" mt={5} borderTopLeftRadius={'3xl'} borderTopRightRadius={'3xl'}>
      <Container py="50px" maxW="1280px" pt="0">
        <Box maxW="760px" mx="auto" textAlign="center" mb={5}>
          <chakra.h1
            fontWeight={'bold'}
            color="white"
            textStyle="heading"
            fontSize={{ base: '2rem', md: '2.5rem' }}
          >
            Why choose Library
          </chakra.h1>
          <chakra.h2 fontSize={{ base: '1rem', md: '1.4rem' }}>
            Library has books in your Favourite categories
          </chakra.h2>
        </Box>
        <SimpleGrid columns={[1, 1, 3]} spacing={10}>
          <Box bg="tomato" height="80px"></Box>
          <Box bg="tomato" height="80px"></Box>
          <Box bg="tomato" height="80px"></Box>
        </SimpleGrid>
      </Container>
    </Box>
  )
}

export default CardGrid
