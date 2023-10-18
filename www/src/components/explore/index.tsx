import { chakra, Box, Flex } from '@chakra-ui/react'
import Container from '@/layout/container'
import { Button } from './button'
import { Section } from './Section'

const Explore = () => {
  return (
    <Section>
      <Container p={7}>
        <Flex align="center" direction="column" textAlign="center" mb="10">
          <Box maxW="32rem">
            <chakra.h1
              mb={3}
              color={'white'}
              fontWeight={'bold'}
              fontSize={{ base: '4xl', sm: '5xl' }}
            >
              Explore more Books
            </chakra.h1>
            <Button />
          </Box>
        </Flex>
      </Container>
    </Section>
  )
}

export default Explore
