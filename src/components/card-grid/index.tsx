import { Box, SimpleGrid, chakra } from '@chakra-ui/react'
import Container from '@/layout/container'
import { CardItem } from './card-item'

const CardGrid = () => {
  return (
    <Box as="section" bg="teal.600" mt={5}>
      <Container py={19}>
        <Box maxW="760px" mx="auto" textAlign="center" mb={8} color="white">
          <chakra.h1
            fontWeight={'bold'}
            textStyle="heading"
            fontSize={{ base: '2rem', md: '2.5rem' }}
          >
            Why choose Library
          </chakra.h1>
          <chakra.h2 fontSize={{ base: '1rem', md: '1.4rem' }}>
            Library has books in your Favourite categories
          </chakra.h2>
        </Box>
        <SimpleGrid columns={{ base: 1, sm: 1, md: 3 }} spacing={10} mb={4}>
          <CardItem key={1} />
          <CardItem key={2} />
          <CardItem key={3} />
        </SimpleGrid>
      </Container>
    </Box>
  )
}

export default CardGrid
