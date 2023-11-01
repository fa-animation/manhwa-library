import { Box, SimpleGrid, chakra } from '@chakra-ui/react'
import { IoIosBook } from 'react-icons/io'
import { AiFillHeart, AiTwotoneThunderbolt } from 'react-icons/ai'
import { IconType } from 'react-icons'
import Container from '@/layout/container'
import { CardItem } from './card-item'

export interface BoosChoose {
  name: string
  description: string
  icon: IconType
}

const dataChoose: BoosChoose[] = [
  {
    name: 'Easy and Quick',
    description: 'Get access to the book You Purchase Online Instantly',
    icon: AiTwotoneThunderbolt
  },
  {
    name: 'Place to Relax and Read',
    description: 'Enjoy a quiet and comfortable place to relax and read, or to work or study',
    icon: IoIosBook
  },
  {
    name: 'Wide Selection of Resources',
    description: 'Access a vast library of books, articles, and other resources, all in one place',
    icon: AiFillHeart
  }
]

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
          {dataChoose.map((data: BoosChoose, i) => (
            <CardItem key={i} name={data.name} icon={data.icon} description={data.description} />
          ))}
        </SimpleGrid>
      </Container>
    </Box>
  )
}

export default CardGrid
