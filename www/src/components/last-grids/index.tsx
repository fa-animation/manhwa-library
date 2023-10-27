import { Box, chakra, useColorModeValue } from '@chakra-ui/react'
import { ArrayDataProps, MangaProps } from '@/pages'
import { ContainerGrid } from './grid-card'
import { Card } from './card'

const LastCard = ({ lastHomeManga }: ArrayDataProps) => {
  return (
    <Box>
      <Box
        maxW="7xl"
        mx="auto"
        px={{ base: '4', md: '8', lg: '12' }}
        py={{ base: '6', md: '8', lg: '12' }}
      >
        <chakra.h2
          mb={3}
          fontWeight={'bold'}
          fontSize={{ base: '4xl', sm: '5xl' }}
          textAlign={'center'}
        >
          Latest{' '}
          <chakra.span color={useColorModeValue('orange.500', 'orange.300')}>Books</chakra.span>
        </chakra.h2>
        <ContainerGrid>
          {lastHomeManga?.data.map((data: MangaProps) => (
            <Card
              key={data.id}
              title={data.title}
              type_book={data.type_book}
              image={data.image}
              ratting={data.ratting}
            />
          ))}
        </ContainerGrid>
      </Box>
    </Box>
  )
}

export default LastCard
