import { Box, chakra, useColorModeValue } from '@chakra-ui/react'

interface Props {
  children: React.ReactNode
}

const LastCard = ({ children }: Props) => {
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
        {children}
      </Box>
    </Box>
  )
}

export default LastCard
